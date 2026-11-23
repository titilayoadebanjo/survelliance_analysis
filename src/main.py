"""
HPISD Surveillance RAP

Author: Titilayo Adebanjo

Demonstrates:

- RAP Principles
- Validation
- Data Quality Checks
- Epidemiological Analysis
- Reporting
"""

from pathlib import Path

import logging
import yaml

from extract import load_data

from validate import (
    validate_missing_values,
    validate_duplicates,
    validate_age,
    validate_dates
)

from transform import (
    create_reporting_delay,
    create_flags
)

from analysis import (
    disease_summary,
    regional_summary,
    outbreak_summary
)

from reporting import (
    write_validation_report,
    write_summary_report
)

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_FILE = (
    BASE_DIR
    / "config"
    / "config.yaml"
)

with open(CONFIG_FILE) as f:

    config = yaml.safe_load(f)

DATA_FILE = (
    BASE_DIR
    / config["dataset"]["source"]
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def main():

    logging.info(
        "Pipeline started"
    )

    df = load_data(DATA_FILE)

    logging.info(
        f"{len(df)} records loaded"
    )

    df = create_reporting_delay(df)

    quality_issues = []

    quality_issues.extend(
        validate_missing_values(df)
    )

    quality_issues.extend(
        validate_duplicates(df)
    )

    quality_issues.extend(
        validate_age(df)
    )

    quality_issues.extend(
        validate_dates(df)
    )

    df = create_flags(df)

    disease = disease_summary(df)

    region = regional_summary(df)

    outbreaks = outbreak_summary(df)

    write_validation_report(
        quality_issues
    )

    write_summary_report(
        disease,
        region,
        outbreaks
    )

    logging.info(
        "Pipeline completed successfully"
    )


if __name__ == "__main__":

    main()
