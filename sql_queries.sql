-- Total sales by product category
SELECT Category, SUM(Sales) as Total_Sales
FROM sales_cleaned
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Top 10 customers by revenue
SELECT CustomerID, SUM(Sales) as Total_Sales
FROM sales_cleaned
GROUP BY CustomerID
ORDER BY Total_Sales DESC
LIMIT 10;
