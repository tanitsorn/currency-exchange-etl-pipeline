from python.extract.extract_data import (
    fetch_exchange_rates,
    save_raw_json,
)
from python.transform.transform_exchange_rates import (
    transform_exchange_rates,
)
from python.validation.validation_exchange_rates import (
    validate_exchange_rates,
)
from python.load.load_to_mysql import (
    get_engine,
    execute_schema,
    load_csv_to_mysql,
)
from python.utils.logger import logger
from python.utils.pipeline_helpers import run_step


def run_pipeline(target_date=None):

    print("========== Currency Exchange ETL ==========\n")

    # =========================
    # Step 1 : Extract
    # =========================
    print("Step 1 : Extract\n")

    print("Fetching exchange rates...")
    logger.info("Starting extraction")

    data = run_step(
        "Extract",
        fetch_exchange_rates,
        target_date,
    )

    actual_date = data["date"]

    if target_date is not None:
        print(f"Requested date : {target_date}")
        print(f"API rate date : {actual_date}")

    raw_path = run_step(
        "Save Raw JSON",
        save_raw_json,
        data,
        target_date,
    )

    print(f"✓ Raw data saved to: {raw_path}\n")
    logger.info(f"Extract completed ({raw_path})")

    # =========================
    # Step 2 : Transform
    # =========================
    print("Step 2 : Transform\n")

    df, clean_path = run_step(
        "Transform",
        transform_exchange_rates,
        raw_path,
        target_date,
    )

    print(f"✓ Clean data saved to: {clean_path}\n")
    logger.info(f"Transform completed ({clean_path})")

    # =========================
    # Step 3 : Validation
    # =========================
    print("Step 3 : Validation\n")

    results = run_step(
        "Validation",
        validate_exchange_rates,
        df,
    )

    if results["missing_values"] == 0:
        print("✓ No missing values")
    else:
        print(f"✗ Found {results['missing_values']} missing values")

    if results["duplicate_rows"] == 0:
        print("✓ No duplicate rows")
    else:
        print(f"✗ Found {results['duplicate_rows']} duplicate rows")

    if results["invalid_rates"] == 0:
        print("✓ All exchange rates are valid")
        logger.info("Validation passed")
    else:
        print(f"✗ Found {results['invalid_rates']} invalid exchange rates")

    print()

    # =========================
    # Step 4 : Load
    # =========================
    print("Step 4 : Load\n")

    engine = run_step(
        "Create Engine",
        get_engine,
    )

    run_step(
        "Create Schema",
        execute_schema,
        engine,
    )

    run_step(
        "Load",
        load_csv_to_mysql,
        engine,
        clean_path,
        target_date,
    )

    logger.info("Load completed")

    print("ETL pipeline finished!")
    logger.info("Pipeline finished successfully")