"""djangodelightscodecademy URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(''. views.HomeView.as_view(), name='home'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients'),
    path('ingredients/new', views.CreateIngredientView.as_view(), name='ingredient_create'),
    path('ingredients/<int:pk>/update', views.UpdateIngredientView.as_view(), name='ingredient_update'),
    path('ingredients/<int:pk>.delete', views.DeleteIngredientView.as_view(), name='ingredient_delete'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/new', views.NewMenuItem.as_view(), name='create_menu_item'),
    path('menu/<int:pk>/update', views.UpdateMenuItem.as_view(), name='menu_update'),
    path('menu/<int:pk>/delete', views.DeleteMenuItem.as_view(), name='menu_delete'),
    path('reciperequirement/', views.RecipeRequirementView.as_view(), name='reciperequirement'),
    path('reciperequirement/new', views.NewRecipeRequirement.as_view(), name='new_recipe_requirement'),
    path('purchases/', views.PurchasesView.as_view(), name='purchases'),
    path('purchases/new', views.NewPurchase.as_view(), name='add_purchase'),
    path('reports', views.ReportView.as_view(), name='reports'),
]
