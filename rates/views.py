import pandas as pd 
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Min
from .models import RoomRate, OverriddenRoomRate, Discount, DiscountRoomRate
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import (
    RoomRateSerializer, OverriddenRoomRateSerializer,
    DiscountSerializer, DiscountRoomRateSerializer
)

class RoomRateListCreateView(generics.ListCreateAPIView):
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer

    @swagger_auto_schema(operation_description="Retrieve list of room rates or create a new room rate")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new room rate")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class RoomRateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomRate.objects.all()
    serializer_class = RoomRateSerializer

    @swagger_auto_schema(operation_description="Retrieve a room rate")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a room rate")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a room rate")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class OverriddenRoomRateListCreateView(generics.ListCreateAPIView):
    queryset = OverriddenRoomRate.objects.all()
    serializer_class = OverriddenRoomRateSerializer

    @swagger_auto_schema(operation_description="Retrieve a list of overridden room rates or create a new overridden room rate"    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new overridden room rate")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class OverriddenRoomRateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OverriddenRoomRate.objects.all()
    serializer_class = OverriddenRoomRateSerializer

    @swagger_auto_schema(operation_description="Retrieve an overridden room rate")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update an overridden room rate")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete an overridden room rate")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    @swagger_auto_schema(operation_description="Retrieve a list of discount rates")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create new discount")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class DiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    @swagger_auto_schema(operation_description="Retrieve an discount rate by id")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update an existing discount")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete an existing discount")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class DiscountRoomRateListCreateView(generics.ListCreateAPIView):
    queryset = DiscountRoomRate.objects.all()
    serializer_class = DiscountRoomRateSerializer

    @swagger_auto_schema(operation_description="Retrieve list of discounts mapped to each room - room_rate_id, discount_id ")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new discount relationship for room")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class DiscountRoomRateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiscountRoomRate.objects.all()
    serializer_class = DiscountRoomRateSerializer

    @swagger_auto_schema(operation_description="Retrieve discount relationship using id")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update an existing discount relation")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete an existing discount relation")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

@swagger_auto_schema(
    method='get',
    operation_description="Retrieve the lowest rates for a given room within a date range",
    manual_parameters=[
        openapi.Parameter('room_id', openapi.IN_QUERY, description="ID of the room", type=openapi.TYPE_INTEGER, required=True),
        openapi.Parameter('start_date', openapi.IN_QUERY, description="Start date for the rate search", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, required=True),
        openapi.Parameter('end_date', openapi.IN_QUERY, description="End date for the rate search", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, required=True),
    ],
    responses={
        200: openapi.Response(description="A list of dates with their respective lowest rates"),
        400: openapi.Response(description="Bad Request - Missing or invalid parameters"),
        404: openapi.Response(description="Not Found - Room not found"),
    }
)

@api_view(['GET'])
def lowest_rates(request):
    room_id = request.query_params.get('room_id')
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')
    
    if not (room_id and start_date and end_date):
        return Response({"error": "Please provide room_id, start_date, and end_date"}, status=400)
    
    try:
        room_rate = RoomRate.objects.get(room_id=room_id)
    except RoomRate.DoesNotExist:
        return Response({"error": "Room not found"}, status=404)
    
    rates = []
    for date in pd.date_range(start_date, end_date):
        try:
            overridden_rate = OverriddenRoomRate.objects.get(room_rate=room_rate, stay_date=date).overridden_rate
        except OverriddenRoomRate.DoesNotExist:
            overridden_rate = room_rate.default_rate

        applicable_discounts = DiscountRoomRate.objects.filter(room_rate=room_rate).values_list('discount__discount_value', flat=True)
        if applicable_discounts:
            highest_discount = max(applicable_discounts)
        else:
            highest_discount = 0
        
        final_rate = overridden_rate - highest_discount
        rates.append({'date': date, 'rate': final_rate})
    
    return Response(rates)
