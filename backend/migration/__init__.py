def migrate(db):
    # print("running migration")
    # db.engine.execute("drop table if exists product_variant_images;")
    # db.engine.execute("drop table if exists product_images;")
    # db.engine.execute("drop table if exists product_variants;")
    # db.engine.execute("drop table if exists products;")
    # db.engine.execute("drop table if exists images;")

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

