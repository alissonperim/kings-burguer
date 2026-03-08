from ..types.purchase_unity_enum import PurchaseUnityEnum
from common.models.base_model import BaseModel
from decimal import Decimal
from django.db import models

class Ingredient(BaseModel):
  name: str = models.CharField(max_length=240)
  package_cost: Decimal = models.DecimalField(max_digits=8, decimal_places=2)
  purchase_unity: PurchaseUnityEnum = models.CharField(choices=PurchaseUnityEnum, default=PurchaseUnityEnum.GRAM)
  purchase_quantity: Decimal = models.DecimalField(max_digits=8, decimal_places=2)
  code: str = models.CharField(unique=True, max_length=120)
  barcode: str = models.CharField(unique=True, max_length=120)
  stock: Decimal = models.DecimalField(max_digits=8, decimal_places=2)
  margin_seller: Decimal = models.DecimalField(max_digits=5, decimal_places=3, default=None)

  @property
  def unit_cost(self) -> Decimal:
    return self.package_cost / self.package_quantity
