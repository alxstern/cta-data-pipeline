import duckdb


def init_db(path: str = "data/cta.db") -> duckdb.DuckDBPyConnection:
    """Open (or create) the DuckDB database and ensure all tables exist."""
    conn = duckdb.connect(path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS train_positions (
            run_number          VARCHAR,
            line                VARCHAR,
            direction           VARCHAR,
            destination         VARCHAR,
            next_station_id     VARCHAR,
            next_station_name   VARCHAR,
            next_stop_id        VARCHAR,
            predicted_time      TIMESTAMP,
            arrival_time        TIMESTAMP,
            is_approaching      INTEGER,
            is_delayed          INTEGER,
            latitude            DOUBLE,
            longitude           DOUBLE,
            heading             INTEGER,
            polled_at           TIMESTAMP
        )
    """)
    return conn
