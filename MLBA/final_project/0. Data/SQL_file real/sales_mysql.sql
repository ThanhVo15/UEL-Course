
        USE final_project;
        DROP TABLE IF EXISTS sales;
        CREATE TABLE sales (
            transaction_id INT PRIMARY KEY,
            transaction_date DATE,
            transaction_time TIME,
            sales_outlet_id INT,
            staff_id INT,
            customer_id INT,
            instore_yn CHAR(1),
            order_id INT,
            line_item_id INT,
            product_id INT,
            quantity INT,
            line_item_amount FLOAT,
            unit_price FLOAT,
            promo_item_yn CHAR(1),
            FOREIGN KEY (sales_outlet_id) REFERENCES sales_outlet(sales_outlet_id),
            FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
            FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
            FOREIGN KEY (product_id) REFERENCES product(product_id)
        );
    