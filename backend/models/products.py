from  backend import db

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
