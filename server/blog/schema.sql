DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS list;

CREATE TABLE user
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT        NOT NULL
);

CREATE TABLE post
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    author      TEXT      NOT NULL,
    created     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title       TEXT      NOT NULL,
    description TEXT      NOT NULL
);

CREATE TABLE comment
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id    INTEGER   NOT NULL,
    post_title TEXT      NOT NULL,
    author     TEXT      NOT NULL,
    mail       TEXT      NOT NULL,
    created    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content    TEXT      NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post (id)
);

CREATE TABLE list
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    type      TEXT    NOT NULL,
    remote_id INTEGER NOT NULL
);



INSERT INTO user (id, username, password)
VALUES (1, 'CHROMIUM00',
        'scrypt:32768:8:1$UrJMQZ033hhhrcvp$18c59d2a1eb6c1b0853b9c508edbca43e31efdf8fde666cf87c7b9a80d60388c878890d1a2e6c3f1773d7c1cfb145c828bc5c932a19050c042aef3fb4da15638');
