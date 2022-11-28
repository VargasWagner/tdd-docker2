# project/app/models/pydantic.py


from pydantic import BaseModel, AnyHttpUrl


class SummaryPayloadSchema(BaseModel):
    url: str

class SummaryResponseSchema(SummaryPayloadSchema):
    id: int

class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str