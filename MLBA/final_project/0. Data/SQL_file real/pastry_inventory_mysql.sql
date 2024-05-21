
        USE final_project;
        DROP TABLE IF EXISTS pastry_inventory;
        CREATE TABLE pastry_inventory (
            sales_outlet_id INT,
            transaction_date DATE,
            product_id INT,
            start_of_day INT,
            quantity_sold INT,
            waste INT,
            percent_waste FLOAT,
            FOREIGN KEY (sales_outlet_id) REFERENCES sales_outlet(sales_outlet_id),
            FOREIGN KEY (product_id) REFERENCES product(product_id)
        );
    