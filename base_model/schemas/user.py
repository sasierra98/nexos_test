from ninja import ModelSchema, Schema

from base_model.models import User


class UserOut(ModelSchema):
    class Config:
        model = User
        model_exclude = ['groups', 'user_permissions']


class UserUpdate(ModelSchema):
    class Config:
        model = User
        model_exclude = ['groups', 'user_permissions', 'username', 'password']
