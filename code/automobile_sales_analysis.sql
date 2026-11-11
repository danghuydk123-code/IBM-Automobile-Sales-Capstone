-- IBM Automobile Sales Capstone SQL analysis
-- Import historical_automobile_sales.csv as automobile_sales first.

SELECT Recession, COUNT(*) AS records,
       ROUND(AVG(Automobile_Sales), 2) AS avg_sales
FROM automobile_sales GROUP BY Recession ORDER BY Recession;

SELECT Vehicle_Type, Recession,
       ROUND(AVG(Automobile_Sales), 2) AS avg_sales,
       COUNT(*) AS records
FROM automobile_sales
GROUP BY Vehicle_Type, Recession
ORDER BY Vehicle_Type, Recession;

SELECT Year,
       ROUND(AVG(Automobile_Sales), 2) AS avg_sales,
       SUM(CASE WHEN Recession = 1 THEN 1 ELSE 0 END) AS recession_records
FROM automobile_sales GROUP BY Year ORDER BY Year;

SELECT Recession,
       ROUND(AVG(GDP), 2) AS avg_gdp,
       ROUND(AVG(unemployment_rate), 2) AS avg_unemployment,
       ROUND(AVG(Consumer_Confidence), 2) AS avg_consumer_confidence,
       ROUND(AVG(Price), 2) AS avg_price
FROM automobile_sales GROUP BY Recession;

SELECT Month, ROUND(AVG(Automobile_Sales), 2) AS avg_sales
FROM automobile_sales GROUP BY Month ORDER BY Month;

SELECT Vehicle_Type, Recession,
       ROUND(AVG(Advertising_Expenditure), 2) AS avg_ad_spend
FROM automobile_sales
GROUP BY Vehicle_Type, Recession
ORDER BY Vehicle_Type, Recession;
