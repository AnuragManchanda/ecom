# import datetime
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import ModelSchema
# db = SQLAlchemy()
# class Image(db.Model):
#     __tablename__ = 'images'
#     id = db.Column(db.Integer, primary_key=True)
#     url = db.Column(db.String, unique=True, nullable=False)

# product_images = db.Table('product_images',
#                           db.Column('product_id', db.Integer,
#                                     db.ForeignKey('products.id')),
#                           db.Column('image_id', db.Integer,
#                                     db.ForeignKey('images.id'))
#                           )

# product_variant_images = db.Table('product_variant_images',
#                           db.Column('product_variant_id', db.Integer,
#                                     db.ForeignKey('product_variants.id')),
#                           db.Column('image_id', db.Integer,
#                                     db.ForeignKey('images.id'))
#                           )

# class Product(db.Model):
#     __tablename__ = 'products'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     logo_id = db.Column(db.Integer, db.ForeignKey('images.id'))
#     description = db.Column(db.String)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#     images = db.relationship('Image', secondary=product_images, lazy='subquery',
#                              backref=db.backref('products', lazy=True))

# class ProductVariant(db.Model):
#     __tablename__ = 'product_variants'
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     name = db.Column(db.String(255), nullable=False)

#     size = db.Column(db.String)
#     color = db.Column(db.String)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#     images = db.relationship('Image', secondary=product_variant_images, lazy='subquery',
#                              backref=db.backref('product_varaints', lazy=True))

# class ProductSchema(ModelSchema):
#     class Meta:
#         model = Product

# class ProductVariantSchema(ModelSchema):
#     class Meta:
#         model = ProductVariant

# class ImageSchema(ModelSchema):
#     class Meta:
#         model = Image
