from fastapi import APIRouter, HTTPException
from app.infrastructure.repositories.house_repository import HouseRepository
from app.usecases.predict_price import PredictPriceUseCase

router = APIRouter(prefix="/houses", tags=["House"])
repo = HouseRepository()
predict_use_case = PredictPriceUseCase(repo)


@router.get("/")
def get_houses():
    return repo.get_houses()


@router.get("/{house_id}/predict")
def predict_price(house_id: int):
    try:
        predicted_price = predict_use_case.execute(house_id)
        return {"house_id": house_id, "predicted_price": predicted_price}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
