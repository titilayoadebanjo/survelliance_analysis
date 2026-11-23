import pandas as pd


def create_reporting_delay(df):

    df["SampleDate"] = pd.to_datetime(
        df["SampleDate"],
        dayfirst=True,
        errors="coerce"
    )

    df["ReportDate"] = pd.to_datetime(
        df["ReportDate"],
        dayfirst=True,
        errors="coerce"
    )

    df["ReportingDelay"] = (
        df["ReportDate"]
        -
        df["SampleDate"]
    ).dt.days

    return df


def create_flags(df):

    df["AgeIssue"] = (
        (df["Age"] > 120)
        |
        (df["Age"] < 0)
    )

    df["DelayIssue"] = (
        df["ReportingDelay"] > 14
    )

    return df