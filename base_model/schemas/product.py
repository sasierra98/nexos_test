from ninja import ModelSchema

from base_model.models.product import Product


class ProductOut(ModelSchema):
    class Config:
        model = Product
        model_fields = '__all__'
