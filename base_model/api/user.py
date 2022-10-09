from django.shortcuts import get_object_or_404
from ninja import Router

from json import loads

from base_model.models import User
from base_model.schemas import UserOut, UserUpdate

router = Router()


class UserAPI:
    @staticmethod
    @router.get('/', response=list[UserOut])
    def get(request) -> list[UserOut]:
        return User.objects.all()

    @staticmethod
    @router.post('/create')
    def create(request, user: UserOut) -> dict:
        User.objects.create(**user.dict())
        return user.dict()

    @staticmethod
    @router.get('/{int:user_id}', response=UserOut)
    def get_user(request, user_id: int) -> User:
        return get_object_or_404(User, pk=user_id)

    @staticmethod
    @router.put('/{int:user_id}', response=dict)
    def update_put_employee(request, user_id: int, payload: UserOut) -> dict:
        user = get_object_or_404(User, pk=user_id)
        for attr, value in payload.dict().items():
            setattr(user, attr, value)
        user.save()

        return {"success": True}

    @staticmethod
    @router.patch('/{int:user_id}', response=dict)
    def update_patch_user(request, user_id: int, payload: UserUpdate) -> dict:
        user = get_object_or_404(User, pk=user_id)
        keys = [x for x in loads(request.body).keys()]

        for attr, value in payload.dict().items():
            if attr in keys:
                setattr(user, attr, value)
        user.save()

        return {"success": True}


