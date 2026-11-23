def validate_missing_values(df):

    issues = []

    for column, missing_count in df.isnull().sum().items():

        if missing_count > 0:

            issues.append(
                f"{column}: {missing_count} missing values"
            )

    return issues


def validate_duplicates(df):

    issues = []

    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:

        issues.append(
            f"{duplicate_count} duplicate records found"
        )

    return issues


def validate_age(df):

    issues = []

    invalid_ages = len(
        df[
            (df["Age"] > 120)
            | (df["Age"] < 0)
        ]
    )

    if invalid_ages > 0:

        issues.append(
            f"{invalid_ages} invalid age records"
        )

    return issues


def validate_dates(df):

    issues = []

    date_issues = len(
        df[
            df["SampleDate"]
            > df["ReportDate"]
        ]
    )

    if date_issues > 0:

        issues.append(
            f"{date_issues} date anomalies detected"
        )

    return issues