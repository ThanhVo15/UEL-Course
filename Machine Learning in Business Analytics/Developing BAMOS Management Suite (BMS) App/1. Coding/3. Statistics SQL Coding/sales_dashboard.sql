-- Monthly Recurring Revenue (MRR)
SELECT SUM(line_item_amount) AS total_sales FROM sales;


-- Number of Sales
SELECT SUM(order_id) AS number_of_sales FROM sales;

-- Number of  Sales by Date
SELECT d.Dates_ID, SUM(s.line_item_amount) AS total_line_item_amount
FROM sales s
JOIN dates d ON s.transaction_date = d.transaction_date
GROUP BY d.Dates_ID
ORDER BY d.Dates_ID;
    
-- Sales Growth Rate by Week
WITH weekly_sales AS (
    SELECT 
        d.Week_ID AS week,
        SUM(s.line_item_amount) AS total_line_item_amount
    FROM 
        sales s
    JOIN 
        dates d ON s.transaction_date = d.transaction_date
    WHERE
        d.Week_ID NOT IN (18)  -- Exclude week 18
    GROUP BY 
        d.Week_ID
)
SELECT 
    week,
    total_line_item_amount,
    COALESCE(
        (total_line_item_amount - LAG(total_line_item_amount) OVER (ORDER BY week)) / LAG(total_line_item_amount) OVER (ORDER BY week) * 100,
        0
    ) AS sales_growth_rate
FROM 
    weekly_sales
ORDER BY 
    week;

-- Sales Growth Rate by Part of The Days
SELECT 
    s.transaction_date,
    t.part_of_day,
    SUM(s.line_item_amount) AS total_line_item_amount
FROM 
    sales s
JOIN 
    transaction_times t ON t.transaction_time = s.transaction_time
GROUP BY 
    s.transaction_date,
    t.part_of_day
ORDER BY 
    s.transaction_date,
    FIELD(t.part_of_day, 'Morning', 'Afternoon', 'Evening', 'Night', 'Late Night');
-- DRINK HERE OR GO?
SELECT 
    s.sales_outlet_id, 
    SUM(s.line_item_amount) AS total_amount,
    SUM(s.quantity) AS total_quantity,
    s.instore_yn
FROM 
    sales s
JOIN 
    dates d ON d.transaction_date = s.transaction_date
GROUP BY 
    s.sales_outlet_id,
    s.instore_yn,
    d.Dates_ID
ORDER BY
    d.Dates_ID;


-- FROM WHICH STORE
SELECT 
    s.sales_outlet_id,
    SUM(s.line_item_amount) AS total_amount,
    SUM(s.quantity) as total_quantity
FROM 
    sales s
GROUP BY 
    s.sales_outlet_id
ORDER BY 
    FIELD(s.sales_outlet_id, '3', '5', '8');



select * from sales