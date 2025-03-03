from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import utils

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@127.0.0.1:33061/btn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

@app.route('/')
def index():
    categories = utils.load_categories()
    return render_template("index.html", categories=categories)


@app.route('/products')
def get_products():
    category_id = request.args.get('category_id')
    kw = request.args.get('kw')
    from_price = request.args.get('from_price')
    to_price = request.args.get('to_price')
    page = request.args.get('page', 1)

    products = utils.load_products(category_id, kw,  from_price, to_price, page)
    return render_template('products.html', products=products)

@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = utils.get_product(product_id)
    return render_template('product_detail.html', product=product)


if __name__ == '__main__':
    from admin import *
    app.run(host='0.0.0.0', port=5001, debug=True)
