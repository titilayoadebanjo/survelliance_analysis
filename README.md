# Surveillance RAP

## Purpose

This project demonstrates a Reproducible Analytical Pipeline (RAP) for analysing surveillance case data.

The pipeline:

- Extracts surveillance data
- Performs validation checks
- Assesses data quality
- Generates outbreak summaries
- Produces reporting outputs

## RAP Components

- extract.py
- validate.py
- transform.py
- analysis.py
- reporting.py

## Outputs

- output/validation_report.txt
- output/disease_summary.csv
- output/regional_summary.csv
- output/outbreak_summary.csv

## Execution

```bash
python src/main.py
```

## Orchestration

A sample Airflow DAG is provided in:

```text
dags/surveillance_case_dag.py
```

## Deployment

The solution can be:

- Containerised using Docker
- Scheduled using Airflow
- Deployed into OpenShift

## Testing

```bash
pytest
```