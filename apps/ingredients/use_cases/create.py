from decimal import Decimal

from ..repositories.ingredients_repository import IngredientsRepository
from ..types.purchase_unity_enum import PurchaseUnityEnum
from ..dtos.ingredient_dto import IngredientDTO
from ..schemas.create_ingredient import CreateIngredientSchema
from ..types.ingredient import Ingredient
from common.utils.internal_code_generator import internal_code_generator

class CreateIngredientUseCase:
    def __init__(self, repository: IngredientsRepository | None = None) -> None:
        self.repository = repository or IngredientsRepository()

    def execute(self, data: CreateIngredientSchema):
        ingredient_body: Ingredient = self.crate_ingredient_body(data)

        response = self.repository.create(ingredient_body)
        dto = IngredientDTO.from_model(response)

        return dto.to_dict()

    def crate_ingredient_body(self, data: CreateIngredientSchema) -> Ingredient:
        purchase_unity = str(data.purchase_unity).upper()
        if purchase_unity not in PurchaseUnityEnum.values:
            raise ValueError(
                f"Invalid purchase_unity. Allowed values: {', '.join(PurchaseUnityEnum.values)}"
            )

        purchase_price = Decimal(str(data.purchase_price))
        usage_quantity = Decimal(str(data.usage_quantity))
        margin_seller = Decimal(str(data.margin_seller)) if data.margin_seller else 0
        stock = Decimal(str(data.stock))
        purchase_quantity = Decimal(str(data.purchase_quantity))

        if purchase_price <= 0:
            raise ValueError("purchase_price must be greater than zero")

        ingredient_data = {
            "name": data.name,
            "purchase_price": purchase_price,
            "purchase_unity": purchase_unity,
            "usage_quantity": usage_quantity,
            "code": internal_code_generator(),
            "barcode": data.barcode,
            "stock": stock,
            "purchase_quantity": purchase_quantity,
            "cost_price": self.calculate_cost_price(data),
            "margin_seller": margin_seller
        }

        return ingredient_data

    def calculate_cost_price(self, data: CreateIngredientSchema) -> None:
        return (data.purchase_price / data.purchase_quantity) * data.usage_quantity
