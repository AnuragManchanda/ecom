from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from migration import migrate
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema

import time
time.sleep(5)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysqldb/ecom'
db = SQLAlchemy(app)
migrate(db)
ma = Marshmallow(app)

product_images = db.Table('product_images',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('image_id', db.Integer, db.ForeignKey('images.id'))
    )

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.Text)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, auto_now_add=True)
    updated_at = db.Column(db.DateTime, auto_now_add=True)
    images = db.relationship('Image', secondary=product_images, lazy='subquery',
                           backref=db.backref('products', lazy=True))

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)

class ProductSchema(ModelSchema):
    class Meta:
        model = Product

# 5. Query products and variants
@app.route('/products')
def product_index():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    output = product_schema.dump(products)
    return jsonify({'products': output})

# 5. Query products and variants
@app.route('/products/<id>/')
def product_show(id):
    product = Product.query.get(id)
    product_schema = ProductSchema()
    output = product_schema.dump(product)
    return jsonify({'product': output})

@app.route('/products/<id>/', methods = ['PUT'])
def product_update(id):
    product = Product.query.get(id)
    product.name = request.json['name']
    product.description = request.json['description']
    db.session.commit()
    return jsonify({'product': ProductSchema().dump(product)})

@app.route('/products', methods=['POST'])
def product_create(id):
    product = Product(
        name=request.json['name'],
        description=request.json['description'],
        logo=request.json['logo'],
    )


#     # as for logo_url
#     logo_url
#     search in images __tablename__
#     add that id to logo_id




# 1. Create/Update a product  -> post put
# 2. Create multiple variants under a product
# 3. Update a variant
# 4. Link Products/Variants to images
# 5. Query products and variants

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
