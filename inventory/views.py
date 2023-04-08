from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

#home view
class HomeView(TemplateView):
    template_name = 'inventory/home/html'

#IngredientListView
class IngredientList(ListView):
    model = Ingredient
    template_name = 'inventory/ingredients_list.html'

#create ingredient view
class CreateIngredientView(CreateView):
    model = Ingredient
    template_name = 'inventory/create_ingredient.html'
    form_class = IngredientForm

#update ingredient view
class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = 'inventory/update_ingredient.html'
    form_class = IngredientForm

#delete ingredient view
class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = 'inventory/delete_ingredient.html'
    success_url = reverse_lazy('ingredients')

#menu view
class MenuView(ListView):
    model = MenuItem
    template_name = 'inventory/menu_list.html'

#create new menu item
class NewMenuItem(CreateView):
    model = MenuItem
    template_name = 'inventory/create_menu.html'
    form_class = MenuItemForm

#Update a menu item
class UpdateMenuItem(UpdateView):
    model = MenuItem
    template_name = 'inventory/update_menu.html'
    form_class = MenuItemForm

#delete a menu item
class DeleteMenuItem(DeleteView):
    model = MenuItem
    template_name = 'inventory/delete_menu.html'
    success_url = reverse_lazy('menu')

#recipe requirement view
class RecipeRequirementView(ListView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_list.html'

#add new recipe requirement
class NewRecipeRequirement(CreateView):
    model = RecipeRequirement
    template_name = 'inventory/new_recipe_requirement.html'
    form_class = RecipeRequirementForm

# purchases view
class PurchasesView(ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'

# adding a purchase to the purchase list
class NewPurchase(CreateView):
    template_name = 'inventory/add_purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [X for X in MenuItem.objects.all() if X.available()]
        return context

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()

        purchase.save()
        return redirect("/purchases")

#reports view

class ReportView(TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit * \
                    recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context







