-- KEYS = [postgres psql drop database]

SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid() AND datname = '<db-name>';

DROP DATABASE "<db-name>";