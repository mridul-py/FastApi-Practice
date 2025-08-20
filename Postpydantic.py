'''
Model will have following:
name
city
age
gender
height
weight
bmi and verdict we will calculate
'''
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of Patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of Patient", max_length=50)]
    city: Annotated[str, Field(..., description="City Location of Patient")]
    age: Annotated[int, Field(..., description="Age of patient", gt=0, lt=100)]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description="Gender of Patient")]
    height: Annotated[float, Field(..., description="Height of Patient in cm")]
    weight: Annotated[float, Field(..., description="Weight of Patient in kg")]

    @computed_field(return_type=float)
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height / 100) ** 2, 2)

    @computed_field(return_type=str)
    @property
    def verdict(self) -> str:
        bmi = self.bmi
        
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    
    
    
    