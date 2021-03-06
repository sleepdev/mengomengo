SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";
ALTER DATABASE CHARACTER SET "utf8";


CREATE TABLE user (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fb_id VARBINARY(100) NOT NULL UNIQUE
);

CREATE TABLE list (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    owner BIGINT NOT NULL,
    title VARBINARY(500) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY(owner)
);

CREATE TABLE video (
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARBINARY(500),
    list BIGINT NOT NULL,
    type VARBINARY(100) NOT NULL,
    data VARBINARY(100) NOT NULL,
    episode INT,
    part INT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    KEY(list,episode,part,created_at)
);

CREATE TABLE stalking ( 
    id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    stalker BIGINT NOT NULL,
    victim BIGINT NOT NULL,
    KEY(stalker),
    KEY(victim)
);

