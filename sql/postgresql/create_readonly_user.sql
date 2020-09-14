-- KEYS=[postgres sql new user readonly]

CREATE USER username WITH PASSWORD 'your_password';
GRANT CONNECT ON DATABASE database_name TO username;
GRANT USAGE ON SCHEMA schema_name TO username;
GRANT SELECT ON table_name TO username;
-- or
GRANT SELECT ON ALL TABLES IN SCHEMA schema_name TO username;

ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name
GRANT SELECT ON TABLES TO username;
