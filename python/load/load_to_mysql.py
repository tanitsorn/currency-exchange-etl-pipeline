from pathlib import Path
from sqlalchemy import create_engine
from python.utils.config import (DB_USER,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME,)
import pandas as pd
from sqlalchemy import text

def get_engine():
    """Create SQLAlchemy engine."""

    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return engine

def execute_schema(engine):
    """Execute schema.sql"""

    schema_path = Path("sql/schema.sql")

    with open(schema_path, "r") as file:
        sql_script = file.read()

    with engine.connect() as connection:

        for statement in sql_script.split(";"):

            statement = statement.strip()

            if statement:
                connection.exec_driver_sql(statement)

        connection.commit()

    print("✓ Database schema created")


def rate_exists(engine, rate_date):
    """
    Check whether exchange rates for a given date
    already exist in the database.
    """

    query = text("""
        SELECT COUNT(*)
        FROM exchange_rates
        WHERE rate_date = :rate_date
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"rate_date": rate_date},
        )

        count = result.scalar()

    return count > 0

def load_csv_to_mysql(engine, csv_path, target_date=None):
    """Load cleaned CSV into MySQL."""

    df = pd.read_csv(csv_path)
    rate_date = df["rate_date"].iloc[0]

    # Check whether data for this date already exists
    if rate_exists(engine, rate_date):
        if target_date is None:
            print(f"✓ Exchange rates for {rate_date} already exist.")
        else:
            print(
                f"✓ Requested {target_date} "
                f"resolved to {rate_date}, "
                "which already exists."
            )
        print("Skipping load.")

        return
    
    # Load new records into MySQL
    df.to_sql(
        name="exchange_rates",
        con=engine,
        if_exists="append",
        index=False,
    )
    print( 
        f"✓ Loaded {len(df)} exchange rates "
        f"for {rate_date}"
    )