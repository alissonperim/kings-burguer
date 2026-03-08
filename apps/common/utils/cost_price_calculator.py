from ingredients.schemas.create_ingredient import CreateIngredientSchema
from decimal import Decimal

def calculate_cost_price(
  package_cost: Decimal,
  purchase_quantity: Decimal,
  usage_quantity: Decimal) -> Decimal:
    return (package_cost / purchase_quantity) * usage_quantity
