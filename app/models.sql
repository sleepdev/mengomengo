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

CREATE TABLE wall (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL,
    subject BIGINT NOT NULL,
    verb VARBINARY(100) NOT NULL,
    object BIGINT NOT NULL,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    KEY(user,ts)
);
CREATE TABLE list (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL,
    title VARBINARY(500) NOT NULL,
    permit ENUM('public','shared','private','explicit') NOT NULL DEFAULT 'shared',
    KEY(user)
);
CREATE TABLE video (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    list BIGINT NOT NULL,
    url VARBINARY(500) NOT NULL,
    title VARBINARY(500),
    episode INT,
    part INT,
    KEY(list,episode,part)
);
CREATE TABLE subscription ( 
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user BIGINT NOT NULL,
    list BIGINT NOT NULL,
    KEY(user)
);

