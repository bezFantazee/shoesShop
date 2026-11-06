from python.database.connection import get_session
from python.database.models.PickupPoint import PickupPoint
from sqlalchemy import func

class PickupPointController:
    def __init__(self):
        self.session = get_session()
    def get_id_by_address(self, address: str):
        full_address_column = func.concat(
            PickupPoint.town, " ",
            PickupPoint.street, " ",
            PickupPoint.house
        )

        pickup_point =  (
            self.session.query(PickupPoint)
            .filter(full_address_column == address)
            .first()
        )
        if pickup_point:
            return pickup_point.id
        else:
            return None

    def get_pickup_point_by_id(self, id):
        return self.session.query(PickupPoint).filter(PickupPoint.id == id).first()