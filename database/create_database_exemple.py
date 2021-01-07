import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_segments = """
CREATE TABLE IF NOT EXISTS segments (
    id          INTEGER      PRIMARY KEY,
    name        VARCHAR(50)  NOT NULL    UNIQUE,
    description VARCHAR(100) NOT NULL
);
"""
cursor.execute(create_segments)

create_companies = """
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
"""
cursor.execute(create_companies)

create_skills = """
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
"""
cursor.execute(create_skills)

create_graduations = """
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
"""
cursor.execute(create_graduations)

create_certificates = """
CREATE TABLE IF NOT EXISTS certifications (
    id           INTEGER      PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    organization VARCHAR(100) NOT NULL,
    issued_at    DATE         NOT NULL,
    expires_at   DATE,
    segment_id   INTEGER      NOT NULL DEFAULT 1,
    FOREIGN KEY (segment_id) REFERENCES segments (id),
    UNIQUE (name, organization, issued_at)
);
"""
cursor.execute(create_certificates)

create_resumes = """
CREATE TABLE IF NOT EXISTS resumes (
    id          INTEGER       PRIMARY KEY,
    description VARCHAR(1000) NOT NULL,
    created_at  DATE          NOT NULL DEFAULT CURRENT_DATE,
    segment_id  INTEGER       NOT NULL DEFAULT 1,
    FOREIGN KEY (segment_id) REFERENCES segments (id)
);
"""
cursor.execute(create_resumes)

create_products = """
CREATE TABLE IF NOT EXISTS products (
    id          INTEGER       PRIMARY KEY,
    name        VARCHAR(100)  NOT NULL,
    description VARCHAR(1000) NOT NULL ,
    created_at  DATE          NOT NULL,
    url         VARCHAR(250),
    segment_id  INTEGER       NOT NULL DEFAULT 1 REFERENCES segments (id),
    company_id  INTEGER REFERENCES companies (id)
);
"""
cursor.execute(create_products)

create_presentations = """
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
"""
cursor.execute(create_presentations)

create_users = """
CREATE TABLE IF NOT EXISTS users (
    id         INTEGER PRIMARY KEY,
    username   VARCHAR(100) NOT NULL UNIQUE,
    password   VARCHAR(250) NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    updated_at DATE
);
"""
cursor.execute(create_users)
connection.commit()
connection.close()