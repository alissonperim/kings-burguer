from ...ingredients.models.ingredient import Ingredient
from ...common.models.base_model import BaseModel
from decimal import Decimal
from django.db import models

class Product(BaseModel):
  barcode: str = models.CharField(max_length=13, unique=True)
  code: str = models.CharField(max_length=30)
  cost_price: Decimal = models.DecimalField(max_digits=8, decimal_places=2, default=None)
  sale_price: Decimal = models.DecimalField(max_digits=8, decimal_places=2, default=None)
  ingredients: list[Ingredient] = models.ForeignKey(Ingredient)
  ingredient_usage_quantity: Decimal = models.DecimalField(max_digits=8, decimal_places=2)
  margin_seller: Decimal = models.DecimalField(max_digits=5, decimal_places=3, default=None)
  description: str = models.CharField(max_length=240)

  def set_sale_price(self) -> None:
    sum_of_ingredients: float = sum(x['purchase_price'] for x in self.ingredients)

    self.sale_price = sum_of_ingredients

    return None
