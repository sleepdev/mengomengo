SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";
ALTER DATABASE CHARACTER SET "utf8";


CREATE TABLE user (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fb_id VARBINARY(100) NOT NULL UNIQUE
);
CREATE TABLE permission (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL,
    verb ENUM('read','write','delete') NOT NULL,
    owner BIGINT NOT NULL,
    object ENUM('wallpost','playlist','subscription','video') NOT NULL,
    UNIQUE KEY(user,verb,owner,object)
);

CREATE TABLE wallpost (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL,
    author BIGINT NOT NULL,
    url VARBINARY(500) NOT NULL,
    message VARBINARY(500),
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    KEY(user,ts)
);
CREATE TABLE playlist (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL,
    title VARBINARY(500) NOT NULL,
    permit ENUM('public','shared','private','explicit') NOT NULL,
    KEY(user)
);
CREATE TABLE video (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    playlist BIGINT NOT NULL,
    url VARBINARY(500) NOT NULL,
    title VARBINARY(500),
    episode INT,
    part INT,
    KEY(playlist)
);
CREATE TABLE subscription ( 
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL,
    playlist BIGINT NOT NULL,
    KEY(user)
);

