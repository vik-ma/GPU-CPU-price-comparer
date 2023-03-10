import React from "react";
import { gql } from "@apollo/client";
import client from "../../../apollo-client";
import {
  ProductListingsProps,
  CompletedFetchProps,
  FetchPageProps,
} from "@/typings";
import CpuListingsTable from "./CpuListingsTable";
import GpuListingsTable from "./GpuListingsTable";
import { notFound } from "next/navigation";

export const dynamic = "auto",
  dynamicParams = true,
  revalidate = 60,
  fetchCache = "auto",
  runtime = "nodejs";

type PageProps = {
  params: {
    fetchId: string;
  };
};

const getProductListings = async (fetchId: string) => {
  const { data } = await client.query({
    query: gql`
      {
        productListings(timestampId:"${fetchId}") {
            productCategory
            storeName
            price
            productLink
            productName
            pricePerformanceRatio
            benchmarkValue
        }
      }
    `,
  });

  return data.productListings as ProductListingsProps[];
};

const getCompletedFetch = async (fetchId: string) => {
  const { data } = await client.query({
    query: gql`
      {
        completedFetchById(timestampId:"${fetchId}") {
          productList
          benchmarkType
          timestamp
          timestampId
        }
      }
    `,
  });

  return data.completedFetchById[0] as CompletedFetchProps;
};

export default async function FetchPage({ params: { fetchId } }: PageProps) {
  const gqlProductListingData = await getProductListings(fetchId);
  const gqlCompletedFetchData = await getCompletedFetch(fetchId);

  if (gqlCompletedFetchData === undefined) return notFound();

  const timestamp = fetchId;
  const year = timestamp.substring(0, 4);
  const month = timestamp.substring(4, 6);
  const day = timestamp.substring(6, 8);
  const hour = timestamp.substring(8, 10);
  const minute = timestamp.substring(10, 12);
  const second = timestamp.substring(12, 14);

  const formattedTimestamp = `${year}-${month}-${day} ${hour}:${minute}:${second}`;

  return (
    <>
      <title>
        {`${gqlCompletedFetchData.benchmarkType} - ${formattedTimestamp}`}
      </title>
      <div className="fetch-content">
        <h1>{gqlCompletedFetchData.benchmarkType}</h1>
        <h2>{gqlCompletedFetchData.productList}</h2>
        <h3>{formattedTimestamp}</h3>
        {gqlCompletedFetchData.benchmarkType === "GPU" ? (
          <GpuListingsTable
            params={{
              fetchInfo: gqlCompletedFetchData,
              productListings: gqlProductListingData,
            }}
          />
        ) : (
          <CpuListingsTable
            params={{
              fetchInfo: gqlCompletedFetchData,
              productListings: gqlProductListingData,
            }}
          />
        )}
      </div>
    </>
  );
}

export async function generateStaticParams() {
  const { data } = await client.query({
    query: gql`
      {
        allCompletedFetches {
          productList
          benchmarkType
          timestamp
          timestampId
        }
      }
    `,
  });

  const fetches: CompletedFetchProps[] = await data.allCompletedFetches;

  return fetches.map((fetch) => ({
    fetchId: fetch.timestampId,
  }));
}
