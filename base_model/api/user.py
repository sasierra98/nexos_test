from ninja import Router

from base_model.models import User
from base_model.schemas import UserOut

router = Router()


class UserAPI:
    @staticmethod
    @router.get('/user', response=list[UserOut])
    def get(request) -> list[UserOut]:
        return User.objects.all()

    @staticmethod
    @router.post('/create')
    def create(request, user: UserOut) -> dict:
        User.objects.create(**user.dict())
        return user.dict()

