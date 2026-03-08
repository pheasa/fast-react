from app.crud.base import CRUDBase
from app.models.sample import Sample
from app.schemas.sample import SampleCreate, SampleUpdate

class CRUDSample(CRUDBase[Sample, SampleCreate, SampleUpdate]):
    pass

sample = CRUDSample(Sample)
