SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";
ALTER DATABASE CHARACTER SET "utf8";


CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fb_id VARBINARY(100) NOT NULL UNIQUE
);
CREATE TABLE user_playlist (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user INT NOT NULL REFERENCES(user),
    listname VARBINARY(200) NOT NULL,
    permissions ENUM('private','shared','public') NOT NULL,
    UNIQUE KEY(user,listname)
);
CREATE TABLE user_video (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user INT NOT NULL REFERENCES(user),
    playlist INT NOT NULL REFERENCES(playlist),
    url VARBINARY(500) NOT NULL,
    title VARBINARY(500),
    episode INT,
    part INT,
    KEY(user,user_playlist)
);
CREATE TABLE user_subscription( 
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user INT NOT NULL REFERENCES(user)
    interest INT NOT NULL,
    playlist INT NOT NULL REFERENCES(user_playlist)
);

CREATE TABLE history (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user INT NOT NULL REFERENCES(user),
    ts TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    action VARBINARY(2000) NOT NULL,
    KEY(user,ts)
);
