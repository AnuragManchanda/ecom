import time
def migrate(db):
    count = 0
    while(True):
        try:
            print("running migration")
            db.engine.execute("drop table if exists product_variant_images;")
            db.engine.execute("drop table if exists product_images;")
            db.engine.execute("drop table if exists product_variants;")
            db.engine.execute("drop table if exists products;")
            db.engine.execute("drop table if exists images;")

            db.engine.execute(
                """CREATE TABLE IF NOT EXISTS images (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    url TEXT);
                """
            )

            db.engine.execute(
                """CREATE TABLE IF NOT EXISTS products (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(255),
                    logo_id INT,
                    description TEXT,
                    created_at DATETIME,
                    updated_at DATETIME,
                    FOREIGN KEY (logo_id) REFERENCES images(id)
                    );
                """
            )

            db.engine.execute(
                """CREATE TABLE IF NOT EXISTS product_variants (
                    id INT PRIMARY KEY AUTO_INCREMENT,
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

            db.engine.execute(
                """CREATE TABLE IF NOT EXISTS product_images (
                    product_id INT,
                    image_id INT,
                    FOREIGN KEY (image_id) REFERENCES images(id),
                    FOREIGN KEY (product_id) REFERENCES products(id));
                """
            )

            db.engine.execute(
                """CREATE TABLE IF NOT EXISTS product_variant_images (
                    product_variant_id INT,
                    image_id INT,
                    FOREIGN KEY (image_id) REFERENCES images(id),
                    FOREIGN KEY (product_variant_id) REFERENCES product_variants(id));
                """
            )

            ##### images
            db.engine.execute("insert into images values(1,'/image/iphone_11_red.jpeg');")
            db.engine.execute("insert into images values(2,'/image/iphone_11_blue.jpeg');")
            db.engine.execute("insert into images values(3,'/image/iphone_12_red.jpeg');")
            db.engine.execute("insert into images values(4,'/image/iphone_12_blue.jpeg');")

            ##### product iphone 11

            db.engine.execute(
            "insert into products(name, logo_id, description, created_at, updated_at) values('iphone11', 1, 'iphone description for iphone 11', now(), now());")

            ##### product iphone 11 images
            db.engine.execute(
                "insert into product_images(product_id, image_id) values(1,1);")
            db.engine.execute(
                "insert into product_images(product_id, image_id) values(1,2);")

            ##### product iphone 11 variant
            db.engine.execute(
                "insert into product_variants(product_id, name, color, size, description, created_at, updated_at) values(1,'iphone11','red','64','iphone description for 64 gb', now(), now());")

            ##### product iphone 11 variant images
            db.engine.execute(
                "insert into product_variant_images(product_variant_id, image_id) values(1,1);")

            ##### product iphone 11 variant
            db.engine.execute(
                "insert into product_variants(product_id, name, color, size, description, created_at, updated_at) values(1,'iphone11','blue','128','iphone description for 128 gb', now(), now());")

            ##### product iphone 11 variant images
            db.engine.execute(
                "insert into product_variant_images(product_variant_id, image_id) values(2,2);")

            ##### product iphone 12

            db.engine.execute(
                "insert into products(name, logo_id, description, created_at, updated_at) values('iphone12', 3, 'iphone description for iphone 12', now(), now());")

            ##### product iphone 12 images
            db.engine.execute(
                "insert into product_images(product_id, image_id) values(2,3);")
            db.engine.execute(
                "insert into product_images(product_id, image_id) values(2,4);")

            ##### product iphone 12 variant
            db.engine.execute(
                "insert into product_variants(product_id, name, color, size, description, created_at, updated_at) values(2,'iphone12','red','64','iphone description for 64 gb', now(), now());")

            ##### product iphone 12 variant images
            db.engine.execute(
                "insert into product_variant_images(product_variant_id, image_id) values(3,3);")

            ##### product iphone 12 variant
            db.engine.execute(
                "insert into product_variants(product_id, name, color, size, description, created_at, updated_at) values(2,'iphone12','blue','128','iphone description for 128 gb', now(), now());")

            ##### product iphone 12 variant images
            db.engine.execute(
                "insert into product_variant_images(product_variant_id, image_id) values(4,4);")

            break
        except Exception as e:
            print(e)
            count += 1
            print("retry count :", count)
            time.sleep(5)
