-- KEYS = [postgres psql create user readonly]

CREATE USER username WITH PASSWORD 'your_password';
GRANT CONNECT ON DATABASE database_name TO username;
GRANT USAGE ON SCHEMA schema_name TO username;

-- grant select on specific table
GRANT SELECT ON table_name TO username;

-- grant select on all tables
GRANT SELECT ON ALL TABLES IN SCHEMA schema_name TO username;

-- grant select on future created tables
ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name
GRANT SELECT ON TABLES TO username;