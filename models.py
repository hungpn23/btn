from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app import app, db
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    name = Column(String(20), nullable=False)
    products = relationship('Product', back_populates='category')
 

class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    
    category_id = Column(Integer, ForeignKey('category.id'), default=1)
    category = relationship('Category', back_populates='products')
    # (category_name = Column(String(50), nullable=False))

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(Category(name='Dien thoai'))
        db.session.add(Category(name='May tinh bang'))

        products = [{
          "name": "iPhone 7 Plus",
          "description": "Apple, 32GB, RAM: 3GB, iOS13",
          "price": 17000000,
          "image": "images/image1.jpeg",
          "category_id": 1
        }, {
          "name": "iPad Pro 2020",
          "description": "Apple, 128GB, RAM: 6GB",
          "price": 37000000,
          "image": "images/image2.jpeg",
          "category_id": 2
        }, {
          "name": "Galaxy Note 10 Plus",
          "description": "Samsung, 64GB, RAML: 6GB",
          "price": 24000000,
          "image": "images/image3.jpeg",
          "category_id": 1
        },{
          "name": "iPhone XS Max",
          "description": "Apple, 64GB, RAM: 8GB, iOS13",
          "price": 20000000,
          "image": "images/image1.jpeg",
          "category_id": 1
        }, {
          "name": "Tablet Pro 2025",
          "description": "Android, 512GB, RAM: 12GB",
          "price": 50000000,
          "image": "images/image2.jpeg",
          "category_id": 2
        }, {
          "name": "Tablet A6",
          "description": "Samsung, 64GB, RAML: 6GB",
          "price": 6000000,
          "image": "images/image3.jpeg",
          "category_id": 2
        }]

        for product in products:
            p = Product(name=product['name'], description=product['description'], price=product['price'], image=product['image'], category_id=product['category_id'])
            db.session.add(p)

        db.session.commit()