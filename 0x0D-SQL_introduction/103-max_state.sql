-- Script That Displays The Max Temperature Of Each State 
SELECT state, MAX(value) as max_temp FROM temperatures
GROUP BY state ORDER BY state;
