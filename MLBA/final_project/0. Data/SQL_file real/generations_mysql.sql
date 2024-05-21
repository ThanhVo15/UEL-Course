
        USE final_project;
        DROP TABLE IF EXISTS generations;
        CREATE TABLE generations (
            birth_year INT PRIMARY KEY,
            generation VARCHAR(255)
        );
    