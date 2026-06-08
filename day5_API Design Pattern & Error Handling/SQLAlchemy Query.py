from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


def get_products(
    session: Session,
    category: str = None,
    min_price: float = None,
    max_price: float = None,
    search: str = None,
    skip: int = 0,
    limit: int = 10,
):
    query = select(Product)

    # Filter by category
    if category:
        query = query.where(
            Product.category == category
        )

    # Filter by minimum price
    if min_price is not None:
        query = query.where(
            Product.price >= min_price
        )

    # Filter by maximum price
    if max_price is not None:
        query = query.where(
            Product.price <= max_price
        )

    # Search by product name
    if search:
        query = query.where(
            Product.name.ilike(f"%{search}%")
        )

    # Sort by price
    query = query.order_by(Product.price)

    products = session.execute(
        query.offset(skip).limit(limit)
    ).scalars().all()

    return products