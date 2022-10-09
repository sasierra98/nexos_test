from ninja import ModelSchema

from base_model.models import User


class UserOut(ModelSchema):
    class Config:
        model = User
        model_exclude = ['groups', 'user_permissions']
