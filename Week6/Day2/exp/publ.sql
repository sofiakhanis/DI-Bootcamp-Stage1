SELECT * FROM items ORDER BY price ASC;

SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;

SELECT name_cust, surname_cust  FROM customers ORDER BY name_cust ASC LIMIT 3;

SELECT surname_cust FROM customers ORDER BY surname_cust DESC;
