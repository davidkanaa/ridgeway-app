import re
from pydantic import BaseModel, field_validator

# Lookup endpoint models
class LookupRequest(BaseModel):
    areaCode: str

    @field_validator("areaCode")
    def validate_area_code(cls, v: str) -> str:
        if not re.fullmatch(r"\d{3}", v):
            raise ValueError("Area code must be exactly 3 digits")
        return v

class Slot(BaseModel):
    id: str
    label: str


class LookupResponse(BaseModel):
    ok: bool
    serviced: bool
    areaCode: str
    region: str | None = None
    slots: list[Slot] = []


# Booking endpoint models
class BookRequest(BaseModel):
    areaCode: str
    slotId: str
    name: str
    phone: str
    symptom: str

    @field_validator("areaCode")
    def validate_area_code(cls, v: str) -> str:
        if not re.fullmatch(r"\d{3}", v):
            raise ValueError("Area code must be exactly 3 digits")
        return v

    @field_validator("phone")
    def validate_phone(cls, v: str) -> str:
        if not re.fullmatch(r"\d{10}", v):
            raise ValueError("Phone number must be 10 digits without country code")
        return v

class AppointmentDetails(BaseModel):
    confirmation: str
    areaCode: str
    slotId: str
    label: str


class BookResponse(BaseModel):
    ok: bool
    appointment: AppointmentDetails
