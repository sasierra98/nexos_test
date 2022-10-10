from json import loads

from django.shortcuts import get_object_or_404
from ninja import Router

from apps.inventory.schema import InventoryOut
from apps.inventory.models import Inventory
from base_model.models import User, Branch, Product

router = Router()


class InventoryAPI:
    @staticmethod
    @router.get("/", response=list[InventoryOut])
    def get(request) -> list[InventoryOut]:
        return Inventory.objects.all()

    @staticmethod
    @router.post('/create')
    def create(request, branch: InventoryOut) -> dict:
        branch_dict = branch.dict()
        branch_dict['user_id'] = branch_dict.pop('user')
        branch_dict['branch_id'] = branch_dict.pop('branch')
        branch_dict['product_id'] = branch_dict.pop('product')
        Inventory.objects.create(**branch_dict)
        return branch_dict

    @staticmethod
    @router.get('/{int:inventory_id}', response=InventoryOut)
    def get_inventory(request, inventory_id: int) -> Inventory:
        return get_object_or_404(Inventory, pk=inventory_id)

    @staticmethod
    @router.put('/{int:inventory_id}', response=dict)
    def update_put_inventory(request, inventory_id: int, payload: InventoryOut) -> dict:
        inventory = get_object_or_404(Inventory, pk=inventory_id)

        for attr, value in payload.dict().items():
            setattr(inventory, attr, value)

        inventory.save()

        return {"success": True}

    @staticmethod
    @router.patch('/{int:inventory_id}', response=dict)
    def update_patch_inventory(request, inventory_id: int, payload: InventoryOut) -> dict:
        inventory = get_object_or_404(Inventory, pk=inventory_id)
        keys = [x for x in loads(request.body).keys()]

        for attr, value in payload.dict().items():
            if attr in keys:
                setattr(inventory, attr, value)
        inventory.save()

        return {"success": True}

    @staticmethod
    @router.delete('/{int:inventory_id}', response=dict)
    def delete_inventory(request, inventory_id: int):
        get_object_or_404(Inventory, pk=inventory_id).delete()
        return {"success": True}
