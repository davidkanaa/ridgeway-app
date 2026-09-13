from fastapi import APIRouter, HTTPException, status

from exceptions import AreaCodeNotServicedException, InvalidSlotIdException
from models import BookRequest, BookResponse, LookupRequest, LookupResponse
from handlers import lookup_area_code_handler, book_appointment_handler

router = APIRouter()


@router.post(
    "/lookup_avail_area_codes_serviced",
    status_code=status.HTTP_200_OK,
    response_model=LookupResponse,
)
def lookup_area_code(payload: LookupRequest) -> LookupResponse:
    return lookup_area_code_handler(payload)


@router.post(
    "/book_appointment",
    status_code=status.HTTP_201_CREATED,
    response_model=BookResponse,
)
def book_appointment_handler(payload: BookRequest) -> BookResponse:
    try:
        return book_appointment_handler(payload)
    except (AreaCodeNotServicedException, InvalidSlotIdException) as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
