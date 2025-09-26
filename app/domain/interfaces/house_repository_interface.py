from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.house import House


class HouseRepositoryInterface(ABC):
    @abstractmethod
    def get_houses(self) -> List[House]:
        pass

    @abstractmethod
    def get_house_by_id(self, house_id: int) -> House:
        pass

    @abstractmethod
    def save_prediction(self, house: House) -> None:
        pass
