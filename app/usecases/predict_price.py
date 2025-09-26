from app.domain.interfaces.house_interface import HouseRepositoryInterface


class PredictPriceUseCase:
    def __init__(self, repo: HouseRepositoryInterface):
        self.repo = repo

    def execute(self, house_id: int) -> float:
        house = self.repo.get_house_by_id(house_id)
        if not house:
            raise ValueError("House not found")

        base_price = 500000000
        price = base_price
        price += house.bedrooms * 100000000
        price += house.bathrooms * 75000000
        if house.has_garage:
            price += 50000000
        if house.has_pool:
            price += 100000000
        if house.lot_size_m2:
            price += house.lot_size_m2 * 1000000

        house.predicted_price = price
        self.repo.save_prediction(house)
        return house.predicted_price
