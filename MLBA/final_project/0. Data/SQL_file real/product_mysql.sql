
        USE final_project;
        DROP TABLE IF EXISTS product;
        CREATE TABLE product (
            product_id INT PRIMARY KEY,
            product_group VARCHAR(255),
            product_category VARCHAR(255),
            product_type VARCHAR(255),
            product VARCHAR(255),
            product_description TEXT,
            unit_of_measure VARCHAR(255),
            current_wholesale_price FLOAT,
            current_retail_price FLOAT,
            tax_exempt_yn CHAR(1),
            promo_yn CHAR(1),
            new_product_yn CHAR(1)
        );
    