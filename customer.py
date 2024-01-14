from typing import List
from pydantic import BaseModel, EmailStr, Field


class Customer(BaseModel):
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    email: EmailStr = Field(..., example="john.doe@example.com")
    street: str = Field(..., example="123 Main St")
    city: str = Field(..., example="Anytown")
    state: str = Field(..., example="Anystate")
    zip_code: str = Field(..., example="12345")
    country: str = Field(..., example="USA")
    email_consent: bool = Field(
        default=False,
        description="Indicates if the customer has consented to receive emails"
    )
    concerns: List[str] = Field(
        default=[],
        description="List of customer concerns"
    )

    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "street": "123 Main St",
                "city": "Anytown",
                "state": "Anystate",
                "zip_code": "12345",
                "country": "USA",
                "email_consent": False,
                "concerns": ["Range", "Maintenance"],
            }
        }
