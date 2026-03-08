from django.db import models
from common.models.base_model import BaseModel

from decimal import Decimal

class Recipe(BaseModel):
  name: str = models.CharField(max_length=240)
  description: str = models.CharField(max_length=240)

  @property
  def total_cost(self) -> Decimal:
    total = Decimal('0.00')
    for item in self.items.recipe_items.select_related('ingredient').all():
      total += item.total_cost

    return total


