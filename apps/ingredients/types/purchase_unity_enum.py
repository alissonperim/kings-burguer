from enum import Enum
from django.db import models

class PurchaseUnityEnum(models.TextChoices):
  GRAM = 'GRAM'
  UNITY = 'UNITY'
  KILOGRAMA = 'KILOGRAM'
