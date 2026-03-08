import uuid

from ..models.ingredient import Ingredient

class IngredientsRepository:
    def create(self, data: dict) -> Ingredient:
        return Ingredient.objects.create(id=uuid.uuid4(), **data)
