-- Script That Creates The Table id_not_null On Your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY(id)
);