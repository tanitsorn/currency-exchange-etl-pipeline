import sys
from python.utils.logger import logger

def run_step(step_name, func, *args, **kwargs):
    """
    Execute one ETL step with common error handling.
    """

    try:
        return func(*args, **kwargs)

    except Exception as e:

        print(f"\n✗ {step_name} failed\n")
        print(e)

        logger.exception(f"{step_name} failed")

        sys.exit(1)