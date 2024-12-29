SELECT 
    m.medicine_id, 
    m.medicine_name, 
    m.quantity, 
    m.warehouse_date, 
    m.warehouse_release_date,
    p.production_place, 
    p.production_date
FROM 
    medicines_table m
JOIN 
    production_info_table p ON m.medicine_id = p.medicine_id
WHERE 
    YEAR(m.warehouse_date) = YEAR(CURDATE()) 
    AND m.warehouse_release_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 6 MONTH);

/* Querry 2: Linear-regression */
SELECT 
    medicine_id,
    price,
    quantity,
    -- Manually calculate slope and intercept for price prediction
    (AVG(price) - (SUM(quantity * price) / SUM(quantity))) 
    / (AVG(quantity) - (SUM(quantity * quantity) / SUM(quantity))) * quantity 
    + (SUM(quantity * price) / SUM(quantity)) 
    AS price_predicted
FROM 
    sales_data
WHERE 
    sale_date >= CURRENT_DATE - INTERVAL 3 MONTH
GROUP BY 
    medicine_id, quantity
ORDER BY 
    sale_date;