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
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return {"product": product}
    return {"message": "product not found"}


@app.post("/products")
def add_one_product(product: Product):
    """
    add a product to the list of products
    Parameters:
    - product: a product object:
        - name: a string
        - description: a string
        - price: a float
        - quantity: an integer
    Returns:
    - a dictionary with the message and status

    """
    products.append(product)
    return {"message": "product added", "status": "success"}
