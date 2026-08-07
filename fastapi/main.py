from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, model_validator, field_validator, computed_field
from typing import List, Dict, Optional, Annotated, Literal
from fastapi.responses import JSONResponse
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(description="The unique identifier for the patient")]
    name: Annotated[str, Field(description="The name of the patient")]
    city: Annotated[str, Field(description="The city where the patient resides")]
    age: Annotated[int, Field(description="The age of the patient")]
    gender: Annotated[str, Field(description="The gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="The height of the patient in meters")]
    weight: Annotated[float, Field(..., gt=0, description="The weight of the patient in kilograms")]


    # bmi
    @computed_field
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    # verdict
    @computed_field
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal weight"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        
    

def load_patients_data():
    with open ("patients.json", "r") as file:
        data = json.load(file)

    return data

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def get_items():
    return {"items": ["item1", "item2", "item3"]}

@app.get("/patients")
def get_patients():
    patients_data = load_patients_data()
    return {"patients": patients_data}

@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve")):
    patients_data = load_patients_data()

    if patient_id in patients_data:
        return {"patient data": patients_data[patient_id]}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="The field to sort patients by (e.g., 'name', 'age')"), order: str = Query("asc", description="The order to sort patients (asc or desc)")):
    patients_data = load_patients_data()

    if sort_by not in ["name", "age"]:
        raise HTTPException(status_code=400, detail="Invalid sort field. Use 'name' or 'age'.")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order. Use 'asc' or 'desc'.")
    
    sorted_order = False if order == "asc" else True
    
    sorted_patients = sorted(patients_data.values(), key=lambda x: x[sort_by], reverse=sorted_order)
    return {"sorted_patients": sorted_patients}

