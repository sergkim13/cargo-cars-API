from http import HTTPStatus

from fastapi import APIRouter, Depends

from cars_app.api.v1.routers.constants import (
    CARGO_CREATE,
    CARGO_DELETE,
    CARGO_DETAIL,
    CARGO_LIST,
    CARGO_PREFIX,
    CARGO_UPDATE,
)
from cars_app.services.cargo import CargoService, get_cargo_service
from cars_app.validation.schemas import (
    CargoCreate,
    CargoInfo,
    CargoInfoDetail,
    CargoListElement,
    CargoUpdate,
    QueryParams,
)

router = APIRouter(
    prefix=CARGO_PREFIX,
    tags=['cargo'],
)


@router.get(
    path=CARGO_LIST,
    status_code=HTTPStatus.OK,
    response_model=list[CargoListElement],
    summary='Получение списка всех грузов',
)
async def cargo_list(
    query: QueryParams = Depends(),
    cargo_service: CargoService = Depends(get_cargo_service)
) -> list[CargoListElement] | None:
    """Shows cargo's info list."""
    return await cargo_service.get_list(query)


@router.get(
    path=CARGO_DETAIL,
    status_code=HTTPStatus.OK,
    response_model=CargoInfoDetail,
    summary='Получение информации о грузе',
)
async def cargo_detail(
    cargo_id: int,
    cargo_service: CargoService = Depends(get_cargo_service),
) -> CargoInfoDetail:
    return await cargo_service.get_detail(cargo_id)


@router.post(
    path=CARGO_CREATE,
    status_code=HTTPStatus.CREATED,
    response_model=CargoInfo,
    summary='Создание нового груза',
)
async def cargo_create(
    data: CargoCreate,
    cargo_service: CargoService = Depends(get_cargo_service),
) -> CargoInfo:
    """Creates new cargo."""
    return await cargo_service.create(data)


@router.patch(
    path=CARGO_UPDATE,
    status_code=HTTPStatus.OK,
    response_model=CargoInfo,
    summary='Редактирование информации о грузе',
)
async def cargo_update(
    cargo_id: int,
    data: CargoUpdate,
    cargo_service: CargoService = Depends(get_cargo_service),
) -> CargoInfo:
    """Updates specific cargo."""
    return await cargo_service.update(cargo_id, data)


@router.delete(
    path=CARGO_DELETE,
    status_code=HTTPStatus.NO_CONTENT,
    summary='Удаление груза',
)
async def cargo_delete(
    cargo_id: int,
    cargo_service: CargoService = Depends(get_cargo_service),
) -> None:
    """Deletes specific cargo."""
    return await cargo_service.delete(cargo_id)
