create database ecommerce_db;
use ecommerce_db;

 
create table basket_details(
 customer_id int,
 product_id int,
 basket_date DATE,
 basket_count int);
 
 create table customer_details (
  customer_id int primary key,
  sex varchar(10),
  customer_age int,
  tenure int);
  
  SELECT * FROM basket_details LIMIT 10;
  SELECT * from customer_details LIMIT 10;
  DESCRIBE customer_details;
  DESCRIBE basket_details;
  
  -- Customer Loyality:
  -- Identifying Top 5 High-Volume Buyers 
SELECT c.sex, SUM(b.basket_count) as total_items
FROM basket_details b
JOIN customer_details c ON b.customer_id = c.customer_id
GROUP BY c.sex;


-- Top 5 Customers by Purchase Volume  
SELECT customer_id, SUM(basket_count) as total_bought
FROM basket_details
GROUP BY customer_id
ORDER BY total_bought DESC
LIMIT 5;


-- Market Segmentation:
-- Analyzing Sales Performance by Age group
SELECT 
    CASE 
        WHEN customer_age < 30 
THEN 'Young'
        WHEN customer_age BETWEEN 30 AND 50
THEN 'Middle-Aged'
        ELSE 'Senior'
    END as age_category,
    SUM(basket_count) as total_items
FROM customer_details c
JOIN basket_details b ON c.customer_id = b.customer_id
GROUP BY age_category;

--  Age Wise Shopping Behavior 
SELECT customer_age, SUM(basket_count) as total_items
FROM basket_details b
JOIN customer_details c ON b.customer_id = c.customer_id
GROUP BY customer_age
ORDER BY total_items DESC
LIMIT 10;


-- Average Relationship Duration of All customers
Select avg(tenure) as overall_avg_tenure from customer_details where sex in ('Male','Female');


-- Demographic Analysis
-- ===== Comparing Tenurebetween  Male & Female Customers =====
select sex,avg(Tenure) 
from customer_details where sex in ('Male','Female') 
group by sex;

-- Peak Shopping Days Analysis
select dayname(basket_date) as day_name, sum(basket_count) as total_items 
from basket_details
 group by dayname(basket_date)
 order by total_items DESC;
 
 -- Monthly Shoppping Trends Analysis
 select monthname(basket_date) as month_name,
 sum(basket_count) as total_items
 from basket_details 
 group by monthname(basket_date)
 order by total_items DESC;
 
 
-- Identifying Outliers
-- ==== Customers with unrealistics age (>100) ==== 
SELECT * FROM customer_details WHERE customer_age > 100;
SELECT COUNT(*) FROM customers_details WHERE customer_age > 100;
SELECT AVG(customer_age) FROM customer_details WHERE customer_age <= 100;
DESCRIBE customer_details;


-- Temporarily disbling 
-- ==== SQL_SAFE_UPDATES to allow data Modification ====  
SET SQL_SAFE_UPDATES = 0;

-- Data Cleaning:
-- === Updating anomalous age values to the mean age (32) ===
UPDATE customer_details 
SET customer_age = 32 
WHERE customer_age > 100;

-- Data Validtion:
-- === Verifying that all age outliers have been corrected === 
SELECT COUNT(*) FROM customer_details WHERE customer_age > 100;

-- Re_enabling SQL_SAFE_UPDATES for database security ===
SET SQL_SAFE_UPDATES = 1;

