from django.db import models

# Create your models here.
class Ingredient(models.Model):
    # represents an ingredient used for a menu item.
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    unit_price = models.FloatField(default=0)

class MenuItem(models.Model):
    # represents an item on the django delights menu
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

class RecipeRequirement(models.Model):
    # represents what recipe is required for each menu item.
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

class Purchase(models.Model):
    # represents a purchase made by a customer
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

