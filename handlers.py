from models import BookRequest, BookResponse, LookupRequest, LookupResponse


def lookup_area_code_handler(payload: LookupRequest) -> LookupResponse:
    return ...


def book_appointment_handler(payload: BookRequest) -> BookResponse:
    return ...
