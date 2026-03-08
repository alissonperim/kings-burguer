from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

class Ingredient:
    id: UUID
    name: str
    purchase_price: Decimal
    purchase_unity: str
    usage_quantity: Decimal
    code: str
    barcode: str
    stock: float
    purchase_quantity: float
    sale_price: Decimal
