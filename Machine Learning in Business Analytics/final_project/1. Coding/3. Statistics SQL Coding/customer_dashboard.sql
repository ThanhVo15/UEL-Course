-- Number of New Customer
SELECT 
    COUNT(DISTINCT c.customer_id) AS new_customers 
FROM 
    customer c
JOIN 
    sales s ON c.customer_since = s.transaction_date;

-- Calculate churn rate for April 2019
SELECT 
    (inactive_data.inactive_customers / total_data.total_customers) * 100 AS churn_rate
FROM 
    (SELECT 
        COUNT(DISTINCT c.customer_id) AS inactive_customers 
    FROM 
        customer c
    LEFT JOIN 
        sales s ON c.customer_id = s.customer_id 
        AND s.transaction_date BETWEEN '2019-04-01' AND '2019-04-30'
    WHERE 
        s.customer_id IS NULL 
        AND c.customer_since <= '2019-03-31'
    ) AS inactive_data,
    (SELECT 
        COUNT(*) AS total_customers 
    FROM 
        customer 
    WHERE 
        customer_since <= '2019-03-31'
    ) AS total_data;

-- purchase by gender
SELECT 
    c.gender,
    COUNT(DISTINCT s.customer_id) AS purchase_count
FROM 
    customer c
JOIN 
    sales s ON c.customer_id = s.customer_id
GROUP BY 
    c.gender;

-- purchase amount by age
SELECT 
    CASE 
        WHEN YEAR(s.transaction_date) - c.birth_year < 20 THEN '<20'
        WHEN YEAR(s.transaction_date) - c.birth_year BETWEEN 20 AND 29 THEN '20-29'
        WHEN YEAR(s.transaction_date) - c.birth_year BETWEEN 30 AND 39 THEN '30-39'
        WHEN YEAR(s.transaction_date) - c.birth_year BETWEEN 40 AND 49 THEN '40-49'
        ELSE '50+'
    END AS age_group,
    SUM(s.line_item_amount) AS total_revenue
FROM 
    customer c
JOIN 
    sales s ON c.customer_id = s.customer_id
GROUP BY 
    age_group;

-- Purchase by gender and by product category
SELECT 
    c.gender,
    p.product_category,
    COUNT(s.line_item_amount) AS purchase_count
FROM 
    customer c
JOIN 
    sales s ON c.customer_id = s.customer_id
JOIN 
    product p ON s.product_id = p.product_id
GROUP BY 
    c.gender, p.product_category;

-- RFM
WITH rfm AS (
    SELECT 
        c.customer_id,
        MAX(s.transaction_date) AS last_purchase_date,
        COUNT(s.line_item_id) AS frequency,
        SUM(s.line_item_amount) AS monetary_value,
        DATEDIFF('2019-05-01', MAX(s.transaction_date)) AS recency,
        c.gender
    FROM 
        customer c
    JOIN 
        sales s ON c.customer_id = s.customer_id
    GROUP BY 
        c.customer_id
)
SELECT 
    customer_id,
    recency,
    frequency,
    monetary_value,
    gender
FROM 
    rfm;









SELECT * FROM final_project.customer;