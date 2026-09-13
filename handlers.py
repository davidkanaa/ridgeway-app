import random

from exceptions import AreaCodeNotServicedException, InvalidSlotIdException
from models import (BookRequest, BookResponse,
                    LookupRequest, LookupResponse,
                    AppointmentDetails, Slot)

SEEDED_REGIONS = {
    "503": {
        "region": "Portland metro",
        "slots": [
            {"id": "SLOT-TUE-AM", "label": "Tue 8:00am–12:00pm"},
            {"id": "SLOT-TUE-PM", "label": "Tue 1:00pm–5:00pm"},
        ],
    },
    "360": {
        "region": "Vancouver WA",
        "slots": [
            {"id": "SLOT-WED-AM", "label": "Wed 8:00am–12:00pm"},
            {"id": "SLOT-WED-PM", "label": "Wed 1:00pm–5:00pm"},
        ],
    },
}

def lookup_area_code_handler(payload: LookupRequest) -> LookupResponse:
    if payload.areaCode in SEEDED_REGIONS:
        info = SEEDED_REGIONS[payload.areaCode]
        return LookupResponse(
            ok=True,
            serviced=True,
            areaCode=payload.areaCode,
            region=info["region"],
            slots=[Slot(**slot) for slot in info["slots"]],
        )

    return LookupResponse(
        ok=True,
        serviced=False,
        areaCode=payload.areaCode,
        region=None,
        slots=[],
    )


def book_appointment_handler(payload: BookRequest) -> BookResponse:
    if payload.areaCode not in SEEDED_REGIONS:
        raise AreaCodeNotServicedException(payload.areaCode)

    valid_slots = SEEDED_REGIONS[payload.areaCode]["slots"]
    matched_slot = next(
        (s for s in valid_slots if s["id"] == payload.slotId), None
    )
    if not matched_slot:
        raise InvalidSlotIdException(payload.slotId)

    confirmation_code = f"AC-{random.randint(10000, 99999)}"
    return BookResponse(
        ok=True,
        appointment=AppointmentDetails(
            confirmation=confirmation_code,
            areaCode=payload.areaCode,
            slotId=payload.slotId,
            label=matched_slot["label"],
        ),
    )
