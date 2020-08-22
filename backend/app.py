import os
from werkzeug.utils import secure_filename

from models.schema import Product, ProductSchema, Image, ImageSchema
from flask import Flask, jsonify, request, send_from_directory, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
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

@app.route('/products/<id>/')
def product_show(id):
    product = Product.query.get(id)
    return jsonify(ProductSchema().dump(product))

@app.route('/products/<id>/', methods = ['PUT'])
def product_update(id):
    import code
    code.interact(local=dict(globals(), **locals()))

    # product = Product.query.get(id)
    product.name = request.json['name']
    product.description = request.json['description']
    product.logo_id = request.json['logo_id']
    if request.json['images']:
        product.images.delete()
        for image_id in request.json['images']:
            image = Image.query.get(image_id)
            product.images.append(image)

    db.session.commit()
    return jsonify(ProductSchema().dump(product))

@app.route('/images')
def image_index():
    images = Image.query.all()
    return jsonify({'images': ImageSchema(many=True).dump(images)})

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

    db.session.commit()
    return jsonify(ProductSchema().dump(product))

# 1. Create/Update a product  -> post put
# 2. Create multiple variants under a product
# 3. Update a variant
# 4. Link Products/Variants to images
# 5. Query products and variants

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
