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

        package_cost = Decimal(str(data.package_cost))
        margin_seller = Decimal(str(data.margin_seller)) if data.margin_seller else 0
        stock = Decimal(str(data.stock))
        purchase_quantity = Decimal(str(data.purchase_quantity))

        if package_cost <= 0:
            raise ValueError("purchase_price must be greater than zero")

        ingredient_data = {
            "name": data.name,
            "package_cost": package_cost,
            "purchase_unity": purchase_unity,
            "code": internal_code_generator(),
            "barcode": data.barcode,
            "stock": stock,
            "purchase_quantity": purchase_quantity,
            "margin_seller": margin_seller
        }

        return ingredient_data
