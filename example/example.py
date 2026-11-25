# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "pydantic>=2.14.4",
# ]
# ///
from pydantic import BaseModel, Field

class Product(BaseModel):
    id: int = Field(..., description="ID of the product")
    name: str = Field(..., description="Name of the product")
    age: int = Field(..., description="Age of the product")

product = Product(id=1, name="Sample Product", age=10)
print(f"Product ID: {product.id}, Name: {product.name}, Age: {product.age}")