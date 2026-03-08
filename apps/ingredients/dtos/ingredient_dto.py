from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from ..models.ingredient import Ingredient


@dataclass
class IngredientDTO:
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

    @classmethod
    def from_model(self, ingredient: Ingredient) -> "IngredientDTO":
        return self(
            id=ingredient.id,
            name=ingredient.name,
            package_cost=ingredient.package_cost,
            purchase_unity=ingredient.purchase_unity,
            code=ingredient.code,
            barcode=ingredient.barcode,
            stock=ingredient.stock,
            margin_seller=ingredient.margin_seller,
            purchase_quantity=ingredient.purchase_quantity,
            created_at=ingredient.created_at,
            updated_at=ingredient.updated_at,
            deleted_at=ingredient.deleted_at
        )

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "purchase_price": str(self.purchase_price),
            "purchase_unity": self.purchase_unity,
            "usage_quantity": str(self.usage_quantity),
            "code": self.code,
            "barcode": self.barcode,
            "stock": self.stock,
            "purchase_quantity": self.purchase_quantity,
            "sale_price": str(self.sale_price),
        }
