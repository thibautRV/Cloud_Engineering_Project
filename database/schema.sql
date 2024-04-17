-- Database: NumericFarm

--DROP DATABASE IF EXISTS "NumericFarm";

--CREATE DATABASE "NumericFarm"
  --  WITH
    --OWNER = postgres
    --ENCODING = 'UTF8'
    --LC_COLLATE = 'fr_FR.UTF-8'
    --LC_CTYPE = 'fr_FR.UTF-8'
    --LOCALE_PROVIDER = 'libc'
    --TABLESPACE = pg_default
    --CONNECTION LIMIT = -1
    --IS_TEMPLATE = False;

-- Use the existing NumericFarm database initialized by Docker
\c NumericFarm;

CREATE TABLE sensors (
    sensor_id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE readings (
    reading_id SERIAL PRIMARY KEY,
    sensor_id INTEGER REFERENCES sensors(sensor_id),
    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
    value FLOAT
);

CREATE TABLE anomalies (
    anomaly_id SERIAL PRIMARY KEY,
    reading_id INTEGER REFERENCES readings(reading_id),
    type VARCHAR(255),
    details TEXT
);


