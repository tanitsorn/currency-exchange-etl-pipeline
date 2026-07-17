# Currency Exchange ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?logo=sqlalchemy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-lightgrey)
![ETL](https://img.shields.io/badge/ETL-Pipeline-success)
![License](https://img.shields.io/badge/License-MIT-green)


A simple **ETL (Extract, Transform, Load) pipeline** that collects daily exchange rates from the Frankfurter API, transforms the data into a structured format, validates data quality, stores the results in MySQL, and performs SQL analytics.

---

## Project Overview

This project demonstrates a complete ETL workflow using Python and MySQL.

The pipeline performs the following tasks:

- Extract daily exchange rates from the Frankfurter API
- Store the raw API response as JSON
- Transform JSON into a clean tabular format (CSV)
- Validate data quality
- Load cleaned data into MySQL
- Prevent duplicate data loading
- Support historical backfill
- Analyze exchange rates using SQL

---

## Features

- Daily exchange rate extraction
- Historical backfill support
- JSON → CSV transformation
- Data validation
    - Missing values
    - Duplicate rows
    - Invalid exchange rates
- MySQL integration
- Duplicate load protection (Idempotent loading)
- SQL analytics queries
- Logging

---

## Architecture Diagram

---

## Tech Stack

### Programming Language

- Python 3.11

### Libraries

- pandas
- requests
- SQLAlchemy
- PyMySQL
- python-dotenv

### Database

- MySQL

### Concepts

- ETL Pipeline
- Data Validation
- Data Cleaning
- Logging
- Window Functions
- SQL Analytics

---

## Project Structure

```text
currency-exchange-etl-pipeline/
│
├── python/
│   ├── extract/
│   ├── transform/
│   ├── validation/
│   ├── load/
│   ├── backfill/
│   └── utils/
│
├── sql/
│   ├── schema.sql
│   ├── analytics/
│   └── validation/
│
├── data/
│   ├── raw/
│   └── clean/
│
├── logs/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ETL Workflow

```text
Frankfurter API
        │
        ▼
     Extract
        │
        ▼
    Raw JSON
        │
        ▼
    Transform
        │
        ▼
    Clean CSV
        │
        ▼
   Validation
        │
        ▼
      MySQL
        │
        ▼
 SQL Analytics
```

---

## SQL Analytics

The project includes several SQL analysis scripts.

| File | Description |
|------|-------------|
| 01_currency_strength.sql | Average, minimum, and maximum exchange rates |
| 02_daily_summary.sql | Daily exchange rate summary |
| 03_rate_changes.sql | Daily exchange rate changes using window functions |
| 04_cross_currency.sql | Cross currency exchange calculations |
| 05_currency_volatility.sql | Exchange rate volatility using STDDEV |
| 06_currency_ranking.sql | Currency ranking using SQL window functions |

---

## Installation

Clone the repository.

```bash
git clone <repository-url>

cd currency-exchange-etl-pipeline
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```text
DB_HOST=localhost
DB_PORT=3306
DB_NAME=currency_exchange
DB_USER=root
DB_PASSWORD=your_password
```

---

## Running the Pipeline

Run today's ETL.

```bash
python -m python.main
```

Run historical backfill.

```bash
python -m python.backfill.backfill --days 7
```

---

## Example Output

```text
========== Currency Exchange ETL ==========

Step 1 : Extract

Fetching exchange rates...

✓ Raw data saved

Step 2 : Transform

✓ Clean data saved

Step 3 : Validation

✓ No missing values
✓ No duplicate rows
✓ All exchange rates are valid

Step 4 : Load

✓ Loaded 8 exchange rates into MySQL

ETL pipeline finished!
```

---

## Future Improvements

- Docker support
- Apache Airflow scheduling
- Unit testing
- CI/CD pipeline
- Power BI / Tableau dashboard
- Data warehouse integration

---

## License

MIT License