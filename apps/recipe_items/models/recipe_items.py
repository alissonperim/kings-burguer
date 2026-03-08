from decimal import Decimal
from pydantic import ValidationError
from common.models.base_model import BaseModel
from recipes.models.recipe import Recipe
from ingredients.models.ingredient import Ingredient

from django.db import models

class RecipeItems(BaseModel):
  recipe: list[Recipe] = models.ForeignKey(
      Recipe,
      on_delete=models.PROTECT,
      related_name="recipe_items",
  )
  ingredient: list[Ingredient] = models.ForeignKey(
      Ingredient,
      on_delete=models.PROTECT,
      related_name="recipe_ingredients",
  )

  usage_quantity: Decimal = models.DecimalField(max_digits=10, decimal_places=3)

  class Meta:
      db_table = "recipe_items"
      ordering = ["recipe__name", "ingredient__name"]
      constraints = [
          models.UniqueConstraint(
              fields=["recipe", "ingredient"],
              name="unique_ingredient_per_recipe",
          )
      ]

  def __str__(self) -> str:
      return f"{self.recipe.name} - {self.ingredient.name}"

  def clean(self) -> None:
      if self.usage_quantity <= 0:
          raise ValidationError({"usage_quantity": "Usage quantity must be greater than zero."})

  @property
  def total_cost(self) -> Decimal:
      return self.ingredient.unit_cost * self.usage_quantity

