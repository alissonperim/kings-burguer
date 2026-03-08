from django.test import TestCase
from django.urls import reverse

from .models.ingredient import Ingredient


class CreateIngredientRouteTests(TestCase):
    def test_should_create_ingredient(self):
        payload = {
            "name": "Queijo Mucarela",
            "purchase_price": "18.5",
            "purchase_unity": "UNITY",
            "usage_quantity": "1.0",
            "purchase_quantity": 10,
            "code": "ING-001",
            "barcode": "7890000000001",
            "stock": 5,
        }

        response = self.client.post(
            reverse("create_ingredient"),
            data=payload,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Ingredient.objects.count(), 1)
        self.assertEqual(Ingredient.objects.first().code, "ING-001")
