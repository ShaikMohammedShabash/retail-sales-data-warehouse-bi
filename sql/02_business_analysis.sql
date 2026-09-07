SELECT substr(order_date,1,7) month,SUM(net_sales) revenue,SUM(profit) profit FROM fact_sales WHERE order_status='Completed' GROUP BY month;
SELECT c.region,SUM(f.net_sales) revenue,SUM(f.profit) profit FROM fact_sales f JOIN dim_customer c ON f.customer_id=c.customer_id GROUP BY c.region ORDER BY revenue DESC;
SELECT p.product_name,SUM(f.net_sales) revenue,SUM(f.quantity) units FROM fact_sales f JOIN dim_product p ON f.product_id=p.product_id GROUP BY p.product_name ORDER BY revenue DESC LIMIT 10;
