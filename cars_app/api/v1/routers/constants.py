# Cargo
CARGO_PREFIX = '/api/v1/cargos'

CARGO_LIST = CARGO_CREATE = ''
CARGO_DETAIL = CARGO_UPDATE = CARGO_DELETE = '/{cargo_id}'

CARGO_LIST_FULL = CARGO_PREFIX + CARGO_LIST
CARGO_DETAIL_FULL = CARGO_PREFIX + CARGO_DETAIL
CARGO_CREATE_FULL = CARGO_PREFIX + CARGO_CREATE
CARGO_UPDATE_FULL = CARGO_PREFIX + CARGO_UPDATE
CARGO_DELETE_FULL = CARGO_PREFIX + CARGO_DELETE

# Car
CAR_PREFIX = '/api/v1/cars'

CAR_LIST = ''
CAR_DETAIL = CAR_UPDATE = CAR_DELETE = '/{car_id}'

CAR_LIST_FULL = CAR_PREFIX + CAR_LIST
CAR_DETAIL_FULL = CAR_PREFIX + CAR_DETAIL
CAR_UPDATE_FULL = CAR_PREFIX + CAR_UPDATE
CAR_DELETE_FULL = CAR_PREFIX + CAR_DELETE

# Messages
