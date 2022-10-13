"""nexos_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from ninja import NinjaAPI

from base_model.api.user import router as user_route
from base_model.api.branch import router as branch_route
from base_model.api.product import router as product_route
from base_model.views import HomeView, Error404
from apps.inventory.api import router as inventory_route


api = NinjaAPI()

api.add_router("/user", user_route, tags=['User'])
api.add_router("/branch", branch_route, tags=['Branch'])
api.add_router("/product", product_route, tags=['Product'])
api.add_router("/inventory", inventory_route, tags=['Inventory'])

urlpatterns = [
    path('', HomeView.as_view()),
    path('api/', api.urls),
    path('blob_storage/', include("apps.blop_storage.urls"))
]

handler404 = Error404.as_view()
