/* Query 1: Get active flights with departure dates after 2022-01-01 */
SELECT flight_id, departure_dt, class_id, status_ FROM flight_table
WHERE (status_ = 'A') AND (departure_dt > '2022-01-01');

/* Query 2: Count the difference between total and distinct cities in the airport table */
SELECT COUNT(*) - COUNT(DISTINCT(city)) FROM airport_table;

/* Querry 3: Query the list of city names from airport that do not end with vowels */
SELECT DISTINCT(city) 
FROM airport_table WHERE (      
        city NOT LIKE '%a' AND 
        city NOT LIKE '%o' AND 
        city NOT LIKE '%e' AND 
        city NOT LIKE '%u' AND 
        city NOT LIKE '%i'
    )
