## Off-set Pageination
from sqlalchemy.orm import Session
from fastapi import Depends
from app import products
from app.database import get_db
from app.models import Product
import app
@app.get("/products")
def get_products(
    db: Session = Depends(get_db),
    limit: int = 10,
    offset: int = 0
):
    products = (
        db.query(Product)
        .offset(offset)
        .limit(limit)
        .all()
    )

    return products

## Cursor Pagination
@app.get("/products")
def get_products(
    cursor: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    items = (
        db.query(Product)
        .filter(Product.id > cursor)
        .order_by(Product.id)
        .limit(limit)
        .all()
    )

    next_cursor = None

    if items:
        next_cursor = items[-1].id

    return {
        "items": items,
        "next_cursor": next_cursor
    }