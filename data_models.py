from pydantic import BaseModel

class Emp(BaseModel):
    name: str
    age: int
    position: str