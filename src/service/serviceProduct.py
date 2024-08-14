from models.Product import Product
from config.config import engine, session
from sqlalchemy.orm.exc import NoResultFound
import logging
from models.OrderProduct import OrderProduct  # Import the relationship model

db = session

# Configure logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

# Service of the product: add, update, delete products

def addProducts(name, price):
    try:
        newProduct = Product(name=name, price=price)
        db.add(newProduct)
        db.commit()
        db.refresh(newProduct)
        logger.info(f"Product added: {newProduct}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error adding product: {e}")
        raise

def getProducts():
    try:
        products = db.query(Product).all()
        return products
    except Exception as e:
        logger.error(f"Error retrieving products: {e}")
        raise

def updateProduct(product_id, name=None, price=None):
    try:
        product = db.query(Product).filter(Product.id == product_id).one()
        if name:
            product.name = name
        if price:
            product.price = price
        db.commit()
        db.refresh(product)
        logger.info(f"Product updated: {product}")
    except NoResultFound:
        logger.error(f"Product with ID {product_id} not found")
    except Exception as e:
        db.rollback()
        logger.error(f"Error updating product: {e}")
        raise


def deleteProduct(product_id):
    try:
        # First, delete the relationships in OrderProduct
        db.query(OrderProduct).filter(OrderProduct.product_id == product_id).delete()
        
        # Now delete the product
        product = db.query(Product).filter(Product.id == product_id).one()
        db.delete(product)
        db.commit()
        
        logger.info(f"Product deleted: {product}")
    except NoResultFound:
        logger.error(f"Product with ID {product_id} not found")
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting product: {e}")
        raise



def get_product_id_by_name(product_name):
    product = db.query(Product).filter_by(name=product_name).first()
    return product.id if product else None
