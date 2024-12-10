DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS comment;

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
    body        TEXT      NOT NULL,
    description TEXT      NOT NULL
);

CREATE TABLE comment
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER   NOT NULL,
    author  TEXT      NOT NULL,
    mail    TEXT      NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content TEXT      NOT NULL,
    FOREIGN KEY (post_id) REFERENCES post (id)
)


