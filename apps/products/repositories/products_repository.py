import uuid

from ..models.product import Product

class ProductsRepository:
    def create(self, data: dict) -> Product:
        return Product.objects.create(id=uuid.uuid4(), **data)
