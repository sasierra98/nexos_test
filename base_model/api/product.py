from django.shortcuts import get_object_or_404
from ninja import Router

from json import loads

from base_model.models import Product
from base_model.schemas.product import ProductOut

router = Router()


class ProductAPI:
    @staticmethod
    @router.get('/', response=list[ProductOut])
    def get(request) -> list[ProductOut]:
        return Product.objects.all()

    @staticmethod
    @router.post('/create')
    def create(request, product: ProductOut) -> dict:
        Product.objects.create(**product.dict())
        return product.dict()

    @staticmethod
    @router.get('/{int:product_id}', response=ProductOut)
    def get_user(request, product_id: int) -> Product:
        return get_object_or_404(Product, pk=product_id)

    @staticmethod
    @router.put('/{int:product_id}', response=dict)
    def update_put_product(request, product_id: int, payload: ProductOut) -> dict:
        product = get_object_or_404(Product, pk=product_id)

        for attr, value in payload.dict().items():
            setattr(product, attr, value)

        product.save()

        return {"success": True}

    @staticmethod
    @router.patch('/{int:product_id}', response=dict)
    def update_patch_product(request, product_id: int, payload: ProductOut) -> dict:
        product = get_object_or_404(Product, pk=product_id)
        keys = [x for x in loads(request.body).keys()]

        for attr, value in payload.dict().items():
            if attr in keys:
                setattr(product, attr, value)
        product.save()

        return {"success": True}

    @staticmethod
    @router.delete('/{int:product_id}', response=dict)
    def delete_product(request, product_id: int):
        get_object_or_404(Product, pk=product_id).delete()
        return {"success": True}
