from ninja import ModelSchema

from base_model.models import Branch


class BranchOut(ModelSchema):
    class Config:
        model = Branch
        model_fields = '__all__'

