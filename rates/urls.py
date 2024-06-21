from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    RoomRateListCreateView, RoomRateDetailView,
    OverriddenRoomRateListCreateView, OverriddenRoomRateDetailView,
    DiscountListCreateView, DiscountDetailView,
    DiscountRoomRateListCreateView, DiscountRoomRateDetailView,
    lowest_rates
)

schema_view = get_schema_view(
    openapi.Info(
        title="Room Rate Discount API",
        default_version='v1',
        description="API documentation for Room Rate and Discount mappings",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@example.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('room-rates/', RoomRateListCreateView.as_view(), name='room-rate-list-create'),
    path('room-rates/<int:pk>/', RoomRateDetailView.as_view(), name='room-rate-detail'),
    path('overridden-room-rates/', OverriddenRoomRateListCreateView.as_view(), name='overridden-room-rate-list-create'),
    path('overridden-room-rates/<int:pk>/', OverriddenRoomRateDetailView.as_view(), name='overridden-room-rate-detail'),
    path('discounts/', DiscountListCreateView.as_view(), name='discount-list-create'),
    path('discounts/<int:pk>/', DiscountDetailView.as_view(), name='discount-detail'),
    path('discount-room-rates/', DiscountRoomRateListCreateView.as_view(), name='discount-room-rate-list-create'),
    path('discount-room-rates/<int:pk>/', DiscountRoomRateDetailView.as_view(), name='discount-room-rate-detail'),
    path('lowest-rates/', lowest_rates, name='lowest-rates')
]
