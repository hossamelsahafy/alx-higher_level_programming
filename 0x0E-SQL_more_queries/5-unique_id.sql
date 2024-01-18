--  Script That Creates The Table unique_id On Your MySQL Server.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE(id)
);