from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=50, title="Name of patient", description="Patient name should" \
    "maximum of 50 chars", examples=["Pankaj"])]
    email: EmailStr
    age:int = Field(gt = 10, lt=60)
    weight: float = Field(gt=0)
    married: bool = False
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]
    address: Address

    @field_validator('email')
    @classmethod
    def email_validator(cls, email):
        valid_domains = ['hdfc.com', 'icici.com']
        domain = email.split('@')[1]

        if domain not in valid_domains:
            raise ValueError('Not a valid domain')
        return email

    @model_validator(mode='after') #after=mode made this is instance method not class method 
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi




def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.age)

address_info = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address = Address(**address_info)


patient_info = {"name":"Pankaj", "age":12, "weight": 70.5, "married":False,
                "email":"abch@hdfc.com",
                "address":address,
                "allergies":["pollen", "dust"], "contact_details":{
                    "phone":"9825257221",
                }}

patient = Patient(**patient_info)

insert_patient(patient)