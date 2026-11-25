import sys
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., description="Product Name")
    material: str = Field(default="PLA", description="Filament or material")
    size_mm: int = Field(default=None, description="Size of the product in millimeters")
    description: str = Field(default=None, description="Description of the product")

name = sys.argv[1] if len(sys.argv) > 1 else input("Product name: ")
print(Product(name=name).model_dump_json(indent=2))