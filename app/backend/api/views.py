from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .serializers import FetchPropertiesSerializer
# from . import test_module


valid_fetch_types = {"GPU", "CPU-Gaming", "CPU-Normal"}

valid_gpu_set = {
    "GeForce RTX 4090",
    "GeForce RTX 4080",
    "Radeon RX 7900 XTX",
    "GeForce RTX 4070 Ti",
    "Radeon RX 6950 XT",
    "Radeon RX 7900 XT",
    "Radeon RX 6800 XT",
    "GeForce RTX 3070 Ti",
    "GeForce RTX 3070",
    "Radeon RX 6800",
    "Radeon RX 6750 XT",
    "GeForce RTX 3060 Ti",
    "Radeon RX 6700 XT",
    "Radeon RX 6700",
    "Radeon RX 6650 XT",
    "GeForce RTX 3060",
    "Radeon RX 6600 XT",
    "Radeon RX 6600",
    "GeForce RTX 2060",
    "GeForce GTX 1660 Super",
    "GeForce RTX 3050",
    "GeForce GTX 1660 Ti",
    "GeForce GTX 1660",
    "Radeon RX 6500 XT",
    "Radeon RX 6400",
}

valid_cpu_normal_set = {
    "AMD Ryzen 9 5950X",
    "AMD Ryzen 9 5900X",
    "AMD Ryzen 7 5800X",
    "AMD Ryzen 7 5800X3D",
    "AMD Ryzen 7 5700X",
    "AMD Ryzen 5 5600X",
    "AMD Ryzen 5 5600",
    "AMD Ryzen 5 5500",
    "AMD Ryzen 9 7950X",
    "AMD Ryzen 9 7900X",
    "AMD Ryzen 9 7900",
    "AMD Ryzen 7 7700X",
    "AMD Ryzen 7 7700",
    "AMD Ryzen 5 7600X",
    "AMD Ryzen 5 7600",
    "Intel Core i9-13900KS",
    "Intel Core i9-13900K",
    "Intel Core i9-13900KF",
    "Intel Core i9-13900F",
    "Intel Core i9-13900",
    "Intel Core i7-13700K",
    "Intel Core i7-13700KF",
    "Intel Core i9-12900KS",
    "Intel Core i9-12900K",
    "Intel Core i9-12900KF",
    "Intel Core i7-13700",
    "Intel Core i7-13700F",
    "Intel Core i5-13600K",
    "Intel Core i5-13600KF",
    "Intel Core i9-12900F",
    "Intel Core i9-12900",
    "Intel Core i7-12700K",
    "Intel Core i7-12700KF",
    "Intel Core i5-13500",
    "Intel Core i7-12700F",
    "Intel Core i7-12700",
    "Intel Core i5-12600K",
    "Intel Core i5-12600KF",
    "Intel Core i5-13400",
    "Intel Core i5-13400F",
    "Intel Core i5-12600",
    "Intel Core i5-12500",
    "Intel Core i5-12400F",
    "Intel Core i5-12400",
}

valid_cpu_gaming_set = valid_cpu_normal_set.copy()
valid_cpu_gaming_set.remove("Intel Core i9-13900F")
valid_cpu_gaming_set.remove("Intel Core i9-13900")

def validate_fetch_request(serializer_data):
    if serializer_data["fetch_type"] not in valid_fetch_types:
        raise serializers.ValidationError("Not a valid fetch_type")
        
    fetch_type = serializer_data["fetch_type"]

    product_list = serializer_data["product_list"].split(",")
    
    if fetch_type == "GPU":
        valid_product_set = valid_gpu_set
    elif fetch_type == "CPU-Gaming":
        valid_product_set = valid_cpu_gaming_set
    elif fetch_type == "CPU-Normal":
        valid_product_set = valid_cpu_normal_set

    if not set(product_list).issubset(valid_product_set):
        raise serializers.ValidationError(f"Not a valid {fetch_type} product_list")

    return "Success"

@api_view(['POST'])
def test_post(request):
    serializer = FetchPropertiesSerializer(data=request.data)
    if serializer.is_valid():
        # test = test_module.test_function(serializer.data)
        validated_data = validate_fetch_request(serializer.data)
        return Response(validated_data)
    return Response(serializer.errors)