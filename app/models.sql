SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";


CREATE TABLE playlist (
    owner VARBINARY(100) NOT NULL,
    listname VARBINARY(200) NOT NULL,
    permissions ENUM('private','shared','public') NOT NULL,
    PRIMARY KEY(user,listname)
);

CREATE TABLE video (
    owner VARBINARY(100) NOT NULL,
    listname VARBINARY(200) NOT NULL,
    urlhash VARBINARY(100) NOT NULL,
    url VARBINARY(500) NOT NULL,
    title VARBINARY(500),
    ep INT,
    part INT,
    PRIMARY KEY(user,listname,urlhash)
);

CREATE TABLE history (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user VARBINARY(100) NOT NULL,
    ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    action VARBINARY(2000) NOT NULL,
    KEY(user,ts)
);
