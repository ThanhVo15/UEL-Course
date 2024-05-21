
        USE final_project;
        DROP TABLE IF EXISTS staff;
        CREATE TABLE staff (
            staff_id INT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            position VARCHAR(255),
            start_date DATE,
            location VARCHAR(255)
        );
    