from models import Category, Product

def load_categories():
    categories = Category.query.all()

    print(categories)
    return categories
def load_products(category_id=None, kw=None, from_price=None, to_price=None, page=1):
    products = Product.query.filter(Product.active == True)

    if category_id:
        products = Product.query.filter(Product.category_id == category_id)

    if kw:
        products = Product.query.filter(Product.name.contains(kw))

    if from_price:
        products = Product.query.filter(Product.price >= from_price)

    if to_price:
        products = Product.query.filter(Product.price <= to_price)

    return products.paginate(page=int(page), per_page=4)

def get_product(product_id):
    return Product.query.get(product_id)