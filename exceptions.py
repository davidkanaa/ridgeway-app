class AreaCodeNotServicedException(Exception):
    def __init__(self, areaCode: int):
        self.areaCode = areaCode
        self.message = f"Area code {self.areaCode} is not serviced."
        super().__init__(self.message)

class InvalidSlotIdException(Exception):
    def __init__(self, slotId: int):
        self.slotId = slotId
        self.message = f"Invalid slot Id : {self.slotId}."
        super().__init__(self.message)

