import fastapi
from fastapi_chameleon import template
from starlette.requests import Request
from viewmodels.home.indexviewmodel import IndexViewModel
from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/")  # type: ignore
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")  # type: ignore
@template()
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
