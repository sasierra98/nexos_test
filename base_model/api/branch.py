from django.shortcuts import get_object_or_404
from ninja import Router

from json import loads

from base_model.models import Branch
from base_model.schemas.branch import BranchOut

router = Router()


class BranchAPI:
    @staticmethod
    @router.get('/', response=list[BranchOut])
    def get(request) -> list[BranchOut]:
        return Branch.objects.all()

    @staticmethod
    @router.post('/create')
    def create(request, branch: BranchOut) -> dict:
        Branch.objects.create(**branch.dict())
        return branch.dict()

    @staticmethod
    @router.get('/{int:branch_id}', response=BranchOut)
    def get_branch(request, branch_id: int) -> Branch:
        return get_object_or_404(Branch, pk=branch_id)

    @staticmethod
    @router.put('/{int:branch_id}', response=dict)
    def update_put_branch(request, branch_id: int, payload: BranchOut) -> dict:
        branch = get_object_or_404(Branch, pk=branch_id)

        for attr, value in payload.dict().items():
            setattr(branch, attr, value)

        branch.save()

        return {"success": True}

    @staticmethod
    @router.patch('/{int:branch_id}', response=dict)
    def update_patch_branch(request, branch_id: int, payload: BranchOut) -> dict:
        branch = get_object_or_404(Branch, pk=branch_id)
        keys = [x for x in loads(request.body).keys()]

        for attr, value in payload.dict().items():
            if attr in keys:
                setattr(branch, attr, value)
        branch.save()

        return {"success": True}

    @staticmethod
    @router.delete('/{int:branch_id}', response=dict)
    def delete_user(request, branch_id: int):
        get_object_or_404(Branch, pk=branch_id).delete()
        return {"success": True}
