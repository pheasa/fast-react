from pytest import Session

from app.crud.base import CRUDBase
from app.models.sample import Sample
from app.schemas.sample import SampleCreate, SampleUpdate
from app.schemas.user import User

class CRUDSample(CRUDBase[Sample, SampleCreate, SampleUpdate]):
    def __init__(self, db: Session, user: User):
        super().__init__(db, user, Sample)