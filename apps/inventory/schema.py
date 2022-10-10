from ninja import ModelSchema

from apps.inventory.models import Inventory


class InventoryOut(ModelSchema):
    class Config:
        model = Inventory
        model_exclude = ['created_at', 'updated_at']
