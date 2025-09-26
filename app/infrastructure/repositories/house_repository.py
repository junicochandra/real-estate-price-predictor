from typing import List
from app.domain.entities.house import House
from app.domain.interfaces.house_interface import HouseRepositoryInterface


class HouseRepository(HouseRepositoryInterface):
    def __init__(self):
        self.houses = [
            House(
                id=1,
                address="Jl. Merdeka No.1",
                city="Jakarta",
                state="DKI Jakarta",
                zip_code="10110",
                bedrooms=3,
                bathrooms=2,
                year_built=2010,
                lot_size_m2=120,
                has_garage=True,
                has_pool=False,
                predicted_price=None,
                actual_price=2500000000,
            ),
            House(
                id=2,
                address="Jl. Diponegoro No.5",
                city="Bandung",
                state="Jawa Barat",
                zip_code="40115",
                bedrooms=4,
                bathrooms=3,
                year_built=2015,
                lot_size_m2=200,
                has_garage=True,
                has_pool=True,
                predicted_price=None,
                actual_price=3500000000,
            ),
            House(
                id=3,
                address="Jl. Sudirman No.10",
                city="Surabaya",
                state="Jawa Timur",
                zip_code="60234",
                bedrooms=2,
                bathrooms=1,
                year_built=2005,
                lot_size_m2=80,
                has_garage=False,
                has_pool=False,
                predicted_price=None,
                actual_price=1800000000,
            ),
        ]

    def get_houses(self) -> List[House]:
        return self.houses

    def get_house_by_id(self, house_id: int) -> House:
        return next((h for h in self.houses if h.id == house_id), None)

    def save_prediction(self, house: House) -> None:
        for idx, h in enumerate(self.houses):
            if h.id == house.id:
                self.houses[idx] = house
                break
