from pydantic import BaseModel, Field
from decimal import Decimal
from ..types.purchase_unity_enum import PurchaseUnityEnum

class CreateIngredientSchema(BaseModel):
  name: str = Field(max_length=240, min_length=3)
  purchase_price: Decimal = Field(max_digits=8, decimal_places=2)
  purchase_unity: PurchaseUnityEnum
  margin_seller: Decimal = Field(max_digits=5, decimal_places=3, default=None)
  usage_quantity: Decimal = Field(max_digits=8, decimal_places=2)
  barcode: str = Field(max_length=13, min_length=13)
  stock: Decimal = Field(max_digits=8, decimal_places=2, default=0)
  purchase_quantity: Decimal = Field(max_digits=8, decimal_places=2)
