CREATE TABLE IF NOT EXISTS segments (
    id          INTEGER      PRIMARY KEY AUTOINCREMENT,
    name        VARCHAR(50)  NOT NULL    UNIQUE,
    description VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS companies (
    id          INTEGER       PRIMARY KEY,
    name        VARCHAR(100)  NOT NULL,
    position    VARCHAR(100)  NOT NULL,
    assignments VARCHAR(1000) NOT NULL,
    started_at  DATE          NOT NULL,
    ended_at    DATE,
    segment_id  INTEGER       NOT NULL DEFAULT 1,
    FOREIGN KEY (segment_id) REFERENCES segments (id)
);

CREATE TABLE IF NOT EXISTS skills (
    id          INTEGER       PRIMARY KEY,
    name        VARCHAR(50)   NOT NULL,
    description VARCHAR(1000) NOT NULL,
    level       INTEGER       NOT NULL,
    created_at  DATE          NOT NULL DEFAULT CURRENT_DATE,
    segment_id  INTEGER       NOT NULL DEFAULT 1,
    FOREIGN KEY (segment_id) REFERENCES segments (id),
    UNIQUE (name, created_at)
);

CREATE TABLE IF NOT EXISTS graduations (
    id          INTEGER      PRIMARY KEY,
    course      VARCHAR(50)  NOT NULL,
    institution VARCHAR(100) NOT NULL,
    started_at  DATE         NOT NULL,
    ended_at    DATE,
    segment_id  INTEGER      NOT NULL DEFAULT 1,
    FOREIGN KEY (segment_id) REFERENCES segments (id),
    UNIQUE (course, institution, started_at)
);

CREATE TABLE IF NOT EXISTS certifications (
    id           INTEGER      PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    organization VARCHAR(100) NOT NULL,certificates
    issued_at    DATE         NOT NULL,
    expires_at   DATE,
    segment_id   INTEGER      NOT NULL DEFAULT 1,
    FOREIGN KEY (segment_id) REFERENCES segments (id),
    UNIQUE (name, organization, issued_at)
);

CREATE TABLE IF NOT EXISTS resumes (
    id          INTEGER       PRIMARY KEY,
    description VARCHAR(1000) NOT NULL,
    created_at  DATE          NOT NULL DEFAULT CURRENT_DATE,
    segment_id  INTEGER       NOT NULL DEFAULT 1,
    FOREIGN KEY (segment_id) REFERENCES segments (id)
);

CREATE TABLE IF NOT EXISTS products (
    id          SMALLINT      PRIMARY KEY,
    name        VARCHAR(100)  NOT NULL,
    description VARCHAR(1000) NOT NULL ,
    created_at  DATE          NOT NULL,
    url         VARCHAR(250),
    segment_id  INTEGER       NOT NULL DEFAULT 1 REFERENCES segments (id),
    company_id  INTEGER REFERENCES companies (id)
);

CREATE TABLE IF NOT EXISTS presentations (
    id           INTEGER      PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    performed_at DATE         NOT NULL,
    city         VARCHAR(250) NOT NULL,
    state        VARCHAR(250),
    country      VARCHAR(250) NOT NULL,
    segment_id   INTEGER      NOT NULL DEFAULT 1 REFERENCES segments (id),
    company_id   INTEGER REFERENCES companies (id)
);

CREATE TABLE IF NOT EXISTS users (
    id         INTEGER PRIMARY KEY,
    username   VARCHAR(100) NOT NULL UNIQUE,
    password   VARCHAR(250) NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    updated_at DATE
);