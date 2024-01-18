-- Script That Lists All The Cities Of California That Can Be Found In The Database hbtn_0d_usa.
SELECT cities.id,
    cities.name
FROM cities,
    states
WHERE cities.state_id = states.id
    AND states.name = 'California'
ORDER BY cities.id ASC;