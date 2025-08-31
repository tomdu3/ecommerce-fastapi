from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 5,
                    "name": "airpods",
                    "description": "wireless earphones",
                    "price": 100,
                    "quantity": 1,
                }
            ]
        }
    }
