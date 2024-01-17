-- Script That Lists The Number Of Records With The Same Score In The Table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;