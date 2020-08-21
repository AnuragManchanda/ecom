# Ecom Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api
from flask import Flask, jsonify
from flaskext.mysql import MySQL

# Instantiate the app
app = Flask(__name__)
api = Api(app)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'ecom'
app.config['MYSQL_DATABASE_HOST'] = 'mysqldb'

mysql.init_app(app)

def migration():
    cursor = mysql.connect().cursor()

    # cursor.execute("drop table if exists product_variant_images;")
    # cursor.execute("drop table if exists product_images;")
    # cursor.execute("drop table if exists product_variants;")
    # cursor.execute("drop table if exists products;")
    # cursor.execute("drop table if exists images;")

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS images (
            id INT PRIMARY KEY,
            url TEXT);
        """
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS products (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            logo_id INT,
            description TEXT,
            created_at DATETIME,
            updated_at DATETIME,
            FOREIGN KEY (logo_id) REFERENCES images(id)
            );
        """
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS product_variants (
            id INT PRIMARY KEY,
            product_id INT,
            name VARCHAR(255),
            size VARCHAR(255),
            color VARCHAR(255),
            description TEXT,
            created_at DATETIME,
            updated_at DATETIME,
            FOREIGN KEY (product_id) REFERENCES products(id)
            );
        """
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS product_images (
            product_id INT,
            image_id INT,
            FOREIGN KEY (image_id) REFERENCES images(id),
            FOREIGN KEY (product_id) REFERENCES products(id));
        """
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS product_variant_images (
            product_variant_id INT,
            image_id INT,
            FOREIGN KEY (image_id) REFERENCES images(id),
            FOREIGN KEY (product_variant_id) REFERENCES product_variants(id));
        """
    )

class Product(Resource):
    def get(self):
        migration()
        cursor = mysql.connect().cursor()
        cursor.execute('select * from products')
        data = cursor.fetchall()
        return jsonify({'myCollection': data})
        # return {
        #     'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs']
        # }

# Create routes
api.add_resource(Product, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
