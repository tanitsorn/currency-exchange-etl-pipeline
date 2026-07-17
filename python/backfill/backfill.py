from datetime import date, timedelta
from python.pipeline import run_pipeline

def get_backfill_dates(days=7):
    """
    Return a list of dates from oldest -> newest.
    """

    today = date.today()
    dates = []

    for i in range(days):
        target_date = today - timedelta(days=i + 1)
        dates.append(target_date.strftime("%Y-%m-%d"))
    dates.reverse()
    return dates

if __name__ == "__main__":
    dates = get_backfill_dates(7)
    for d in dates:
        print(f"\n========== Backfill: {d} ==========\n")
        run_pipeline(d)