from django.urls import path, include
from rest_framework import routers
from .views import ProductApiView, CompanyApiView, CategoryApiView, AmortizationApiView

router = routers.DefaultRouter()
router.register("", ProductApiView, "products")
router.register("companies", CompanyApiView, "companies")
router.register("categories", CategoryApiView, "categories")
router.register("amortization", AmortizationApiView, "amortization")


urlpatterns = [
    path('', include(router.urls)),
]