from pydantic import BaseModel
from typing import Optional

class Emp(BaseModel):
    name: str
    age: int
    position: str
    
class UpdateEmp(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    position: Optional[str] = None    