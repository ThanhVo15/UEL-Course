
        USE final_project;
        DROP TABLE IF EXISTS dates;
        CREATE TABLE dates (
            transaction_date DATE,
            Date_ID INT PRIMARY KEY,
            Week_ID INT,
            Week_Desc VARCHAR(255),
            Month_ID INT,
            Month_Name VARCHAR(255),
            Quarter_ID INT,
            Quarter_Name VARCHAR(255),
            Year_ID INT
        );
    