-- Quatity Sold ( biểu đồ chồng)
SELECT d.Month_ID, pi.sales_outlet_id,pi.product_id,
    SUM(pi.quantity_sold) AS Total_quantity_sold
FROM 
    pastry_inventory pi
JOIN 
    dates d ON pi.transaction_date = d.transaction_date
GROUP BY
    pi.product_id,
    d.Month_ID,
    pi.sales_outlet_id
ORDER BY 
    d.Month_ID;
    
    
-- Percent Waste 
SELECT pi.sales_outlet_id,pi.product_id,
    SUM(pi.quantity_sold)/COUNT(d.Dates_ID) AS Total_Percen_Waste
FROM 
    pastry_inventory pi
JOIN 
    dates d ON pi.transaction_date = d.transaction_date
GROUP BY
    pi.product_id,
    d.Month_ID,
    pi.sales_outlet_id
ORDER BY 
    d.Month_ID;
    
-- Total Inventory SOLD by day
SELECT
d.Dates_ID,
SUM(pi.quantity_sold) as total_quantity_sold,
pi.sales_outlet_id
FROM pastry_inventory pi
JOIN dates d ON d.transaction_date = pi.transaction_date
group by
d.Dates_ID,
pi.sales_outlet_id
ORDER BY 
d.Dates_ID;

-- TOTAL AMOUNT THAT PURCHASE
SELECT SUM(pi.quantity_sold * p.current_wholesale_price) as total_amount_purchase
FROM pastry_inventory pi
JOIN product p ON p.product_id = pi.product_id;

-- TOTAL AMOUNT THAT SOLD
SELECT SUM(pi.quantity_sold * p.current_retail_price) as total_amount_sale
FROM pastry_inventory pi
JOIN product p ON p.product_id = pi.product_id;

-- Tổng doanh thu thực tế theo tháng so với mục tiêu
SELECT 
    pi.sales_outlet_id,
    st.total_goal,
    SUM(pi.quantity_sold) AS total_quantity_sold,
    (SUM(pi.quantity_sold)/st.total_goal)*100 as percent
FROM 
    pastry_inventory pi
JOIN 
    product pr
ON 
    pi.product_id = pr.product_id
JOIN 
    sales_targets st
ON 
    pi.sales_outlet_id = st.sales_outlet_id
GROUP BY 
    pi.sales_outlet_id, st.total_goal;





SELECT * FROM final_project.pastry_inventory;