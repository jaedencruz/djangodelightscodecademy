from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemForm(forms.ModelForm):
    class Meta:
        models = Ingredient
        fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        models = RecipeRequirement
        fields = "__all__"