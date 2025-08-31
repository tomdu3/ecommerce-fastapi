from fastapi import FastAPI
from models import Product

app = FastAPI()


@app.get("/")
def greet():
    return {"message": "Api is up and running", "status": "success", "version": "1.0.0"}


products = [
    Product(id=1, name="phone", description="a budget phone",
            price=20, quantity=99),
    Product(
        id=2, name="laptop", description="a gaming laptop", price=2500, quantity=100
    ),
    Product(id=3, name="tv", description="a smart tv", price=300, quantity=50),
    Product(
        id=4,
        name="computer",
        description="mini personal computer",
        price=400,
        quantity=100,
    ),
]


@app.get("/products")
def get_all_products():
    return {"products": products}


@app.get("/products/{id}")
def get_product_by_id(product_id: int):
    return {"product": products[product_id - 1]}
