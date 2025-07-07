CREATE TEMP TABLE df_employee AS
SELECT
  TRIM(s.employee_id || '_' || s.date) AS id,
   STRFTIME('%Y-%m', s.date) AS month_year,
   e.employee_code_emp AS employee_id,
   TRIM(e.employee_name_emp) AS employee_name,
  TRIM(e."GEN(M_F)") AS gender,
e.age,
   CAST(TRIM(s.salary) AS REAL) AS salary,
   TRIM(f.function_group) AS function_group,
   TRIM(s.comp_name) AS company_name,
   TRIM(c.company_city) AS company_city,
   TRIM(c.company_state) AS company_state,
   TRIM(c.company_type) AS company_type,
   TRIM(c.const_site_category) AS const_site_category
FROM salaries s
LEFT JOIN employees e ON s.employee_id = e.employee_code_emp
LEFT JOIN companies c ON s.comp_name = c.company_name
LEFT JOIN functions f ON s.func_code = f.function_code;

UPDATE df_employee
SET
   id = TRIM(id),
   employee_name = TRIM(employee_name),
   gender = TRIM(gender),
   function_group = TRIM(function_group),
   company_name = TRIM(company_name),
   company_city = TRIM(company_city),
   company_state = TRIM(company_state),
  company_type = TRIM(company_type),
   const_site_category = TRIM(const_site_category);

SELECT * FROM df_employee
WHERE id IS NULL
   OR employee_id IS NULL
   OR salary IS NULL
   OR salary = '';

DELETE FROM df_employee
WHERE salary IS NULL OR salary = '';

SELECT 
    company_name,
    COUNT(DISTINCT employee_id) AS current_employee_count
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_name
ORDER BY current_employee_count DESC;

WITH city_counts AS (
    SELECT 
        company_city,
        COUNT(DISTINCT employee_id) AS total_employees
    FROM df_employee
    GROUP BY company_city
),
total AS (
    SELECT SUM(total_employees) AS total FROM city_counts
)
SELECT 
    c.company_city,
    c.total_employees,
    ROUND(100.0 * c.total_employees / t.total, 2) AS percentage
FROM city_counts c, total t
ORDER BY c.total_employees DESC;

SELECT 
    month_year,
    COUNT(DISTINCT employee_id) AS total_employees
FROM df_employee
GROUP BY month_year
ORDER BY month_year;

WITH monthly_counts AS (
    SELECT 
        month_year,
        COUNT(DISTINCT employee_id) AS monthly_total
    FROM df_employee
    GROUP BY month_year
)
SELECT ROUND(AVG(monthly_total), 2) AS avg_employees_per_month
FROM monthly_counts;

WITH monthly_counts AS (
    SELECT 
        month_year,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
)
SELECT 
    (SELECT month_year FROM monthly_counts ORDER BY employee_count ASC LIMIT 1) AS month_min,
    (SELECT employee_count FROM monthly_counts ORDER BY employee_count ASC LIMIT 1) AS min_employees,
    (SELECT month_year FROM monthly_counts ORDER BY employee_count DESC LIMIT 1) AS month_max,
    (SELECT employee_count FROM monthly_counts ORDER BY employee_count DESC LIMIT 1) AS max_employees;

SELECT 
    month_year,
    function_group,
    COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year, function_group
ORDER BY month_year, function_group;

WITH year_salary AS (
    SELECT 
        SUBSTR(month_year, 1, 4) AS year,
        CAST(salary AS REAL) AS salary
    FROM df_employee
    WHERE salary IS NOT NULL
)
SELECT 
    year,
    ROUND(AVG(salary), 2) AS avg_annual_salary
FROM year_salary
GROUP BY year
ORDER BY year;