SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";
ALTER DATABASE CHARACTER SET "utf8";


CREATE TABLE user (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fb_id VARBINARY(100) NOT NULL UNIQUE
);
CREATE TABLE permission (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL REFERENCES(user),
    verb ENUM('read','write','delete') NOT NULL,
    group_type ENUM('user','playlist') NOT NULL,
    group BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    object ENUM('wallpost','playlist','subscription','video') NOT NULL
);

CREATE TABLE wallpost (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL REFERENCES(user),
    author BIGINT NOT NULL REFERENCES(user),
    link VARBINARY(500) NOT NULL,
    message VARBINARY(500),
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    KEY(user,ts)
);
CREATE TABLE playlist (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL REFERENCES(user),
    title VARBINARY(500) NOT NULL,
    permit ENUM('public','shared','private','explicit') NOT NULL,
    UNIQUE KEY(user,title)
);
CREATE TABLE video (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    playlist BIGINT NOT NULL REFERENCES(playlist),
    url VARBINARY(500) NOT NULL,
    title VARBINARY(500),
    episode INT,
    part INT,
    KEY(playlist)
);
CREATE TABLE subscription ( 
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL REFERENCES(user),
    playlist BIGINT NOT NULL REFERENCES(user_playlist)
);

