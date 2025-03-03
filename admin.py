from app import app, db
from flask_admin import Admin

from models import Product, Category
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app)

class ProductView(ModelView):
  can_view_details = True
  can_export = True
  column_searchable_list = ['name', 'description']
  column_filters = ['name', 'price']

admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Category, db.session))
