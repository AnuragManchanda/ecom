import os
from werkzeug.utils import secure_filename

from models.schema import Product, ProductSchema
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
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return url_for('uploaded_file',
                            filename=filename)


@app.route('/image/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/products')
def product_index():
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify({'products': product_schema.dump(products)})

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
def product_create():
    import code
    code.interact(local=dict(globals(), **locals()))
    product = Product(
    name=request.json['name'],
    description=request.json['description'],
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(ProductSchema().dump(product))
    # product_schema = ProductSchema(many=True)
    # output = product_schema.dump(products)
    # if 'logo' in request.files:
    #     import code
    #     code.interact(local=dict(globals(), **locals()))
    #     file = request.files['logo']
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # product.logo = filename

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
