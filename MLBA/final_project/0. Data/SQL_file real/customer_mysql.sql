
        USE final_project;
        DROP TABLE IF EXISTS customer;
        CREATE TABLE customer (
            customer_id INT PRIMARY KEY,
            home_store INT,
            customer_first_name VARCHAR(255),
            customer_email VARCHAR(255),
            customer_since DATE,
            loyalty_card_number VARCHAR(255),
            birthdate DATE,
            gender CHAR(1),
            birth_year INT
        );
    