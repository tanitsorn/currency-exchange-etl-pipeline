from python.extract.extract_data import (
    fetch_exchange_rates,
    save_raw_json
)

def main():
    print("========== Currency Exchange ETL ==========\n")

    print("Step 1 : Extract\n")

    print("Fetching exchange rates...")

    data = fetch_exchange_rates()

    file_path = save_raw_json(data)

    print(f"✓ Raw data saved to: {file_path}\n")

    print("ETL pipeline finished!")

if __name__== "__main__":
    main()