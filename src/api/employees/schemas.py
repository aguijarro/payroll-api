from pydantic import BaseModel, PositiveInt
from pydantic.types import StrictStr, StrictFloat
from typing import Optional, List


class EmployeeMessage(BaseModel):
    id: PositiveInt
    name: StrictStr
    contractTypeName: StrictStr
    roleId: PositiveInt
    roleName: StrictStr
    roleDescription: Optional[StrictStr]
    hourlySalary: StrictFloat
    monthlySalary: StrictFloat


class EmployeeMessages(BaseModel):
    employees_messages: List[EmployeeMessage]


class EmployeeInDBMessage(EmployeeMessage):
    id: Optional[PositiveInt]
