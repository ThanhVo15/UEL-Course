
        USE final_project;
        DROP TABLE IF EXISTS sales_targets;
        CREATE TABLE sales_targets (
            sales_outlet_id INT,
            beans_goal INT,
            beverage_goal INT,
            food_goal INT,
            merchandise_goal INT,
            total_goal INT,
            Date_ID INT,
            Year_ID INT,
            FOREIGN KEY (sales_outlet_id) REFERENCES sales_outlet(sales_outlet_id),
            FOREIGN KEY (Date_ID) REFERENCES dates(Date_ID)
        );
    