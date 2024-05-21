
        USE final_project;
        DROP TABLE IF EXISTS sales_outlet;
        CREATE TABLE sales_outlet (
            sales_outlet_id INT PRIMARY KEY,
            sales_outlet_type VARCHAR(255),
            store_square_feet INT,
            store_address VARCHAR(255),
            store_city VARCHAR(255),
            store_state_province VARCHAR(255),
            store_telephone VARCHAR(255),
            store_postal_code VARCHAR(255),
            store_longitude FLOAT,
            store_latitude FLOAT,
            manager INT,
            Neighborhood VARCHAR(255)
        );
    