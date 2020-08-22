from marshmallow_sqlalchemy import ModelSchema
import datetime
import code
import os
from werkzeug.utils import secure_filename

# from models.schema import db, Product, ProductSchema, Image, ImageSchema, ProductVariant, ProductVariantSchema
from flask import Flask, jsonify, request, send_from_directory, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from migration import migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import time
time.sleep(5)
app = Flask(__name__)
CORS(app)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(ROOT_DIR, "uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysqldb/ecom'

db = SQLAlchemy(app)
migrate(db)
ma = Marshmallow(app)

db = SQLAlchemy()

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)


product_images = db.Table('product_images',
                          db.Column('product_id', db.Integer,
                                    db.ForeignKey('products.id')),
                          db.Column('image_id', db.Integer,
                                    db.ForeignKey('images.id'))
                          )

product_variant_images = db.Table('product_variant_images',
                                  db.Column('product_variant_id', db.Integer,
                                            db.ForeignKey('product_variants.id')),
                                  db.Column('image_id', db.Integer,
                                            db.ForeignKey('images.id'))
                                  )


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    logo_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    images = db.relationship('Image', secondary=product_images, lazy='subquery',
                             backref=db.backref('products', lazy=True))


class ProductVariant(db.Model):
    __tablename__ = 'product_variants'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    name = db.Column(db.String(255), nullable=False)

    size = db.Column(db.String)
    color = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    images = db.relationship('Image', secondary=product_variant_images, lazy='subquery',
                             backref=db.backref('product_varaints', lazy=True))

class ProductSchema(ModelSchema):
    class Meta:
        model = Product

class ProductVariantSchema(ModelSchema):
    class Meta:
        model = ProductVariant

class ImageSchema(ModelSchema):
    class Meta:
        model = Image


@app.route('/image', methods=['POST'])
def upload_file():
    file = request.files['image']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    image = Image(url=url_for('uploaded_file',filename=filename))
    db.session.add(image)
    db.session.commit()
    return jsonify({'image': ImageSchema().dump(image)})

@app.route('/image/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/products')
def product_index():
    products = Product.query.all()
    return jsonify({'products': ProductSchema(many=True).dump(products)})

@app.route('/products/<id>')
def product_show(id):
    product = Product.query.get(id)
    return jsonify(ProductSchema().dump(product))

@app.route('/images')
def image_index():
    images = Image.query.all()
    return jsonify({'images': ImageSchema(many=True).dump(images)})

@app.route('/products/<id>', methods = ['PUT'])
def product_update(id):
    product = Product.query.get(id)
    product.name = request.json['name']
    product.description = request.json['description']
    product.logo_id = request.json['logo_id']
    if request.json['images']:
        product.images = []
        for image_id in request.json['images']:
            image = Image.query.get(image_id)
            product.images.append(image)

    db.session.add(product)
    try:
        db.session.commit()
        return jsonify(ProductSchema().dump(product))
    except SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()
        return jsonify({"ERROR": str(e)})

@app.route('/products', methods=['POST'])
def product_create():
    product = Product(
        name=request.json['name'],
        description=request.json['description'],
        logo_id=request.json['logo_id']
    )

    if request.json['images']:
        for image_id in request.json['images']:
            image = Image.query.get(image_id)
            product.images.append(image)

    db.session.add(product)
    try:
        db.session.commit()
        return jsonify(ProductSchema().dump(product))
    except SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()
        return jsonify({"ERROR": str(e)})

@app.route('/product_variants', methods=['POST'])
def product_variant_create():
    product_variant = ProductVariant(
        name=request.json['name'],
        product_id=request.json['product_id'],
        size=request.json['size'],
        color=request.json['color'],
    )
    if request.json['images']:
        for image_id in request.json['images']:
            image = Image.query.get(image_id)
            product_variant.images.append(image)

    db.session.add(product_variant)
    try:
        db.session.commit()
        return jsonify(ProductVariantSchema().dump(product_variant))
    except SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()
        return jsonify({"ERROR": str(e)})

@app.route('/product_variants/<id>/', methods=['PUT'])
def product_variant_update(id):
    product_variant = ProductVariant.query.get(id)
    product_variant.name = request.json['name']
    product_variant.product_id = request.json['product_id']
    product_variant.size = request.json['size']
    product_variant.color = request.json['color']

    if request.json['images']:
        product_variant.images = []
        for image_id in request.json['images']:
            image = Image.query.get(image_id)
            product_variant.images.append(image)

    db.session.add(product_variant)
    try:
        db.session.commit()
        return jsonify(ProductVariantSchema().dump(product_variant))
    except SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()
        return jsonify({"ERROR": str(e)})

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
