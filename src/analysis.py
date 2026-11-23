def disease_summary(df):

    return (
        df.groupby("Disease")
        .size()
        .reset_index(name="Cases")
        .sort_values(
            by="Cases",
            ascending=False
        )
    )


def regional_summary(df):

    return (
        df.groupby("Region")
        .size()
        .reset_index(name="Cases")
        .sort_values(
            by="Cases",
            ascending=False
        )
    )


def outbreak_summary(df):

    return (
        df.groupby("OutbreakRef")
        .size()
        .reset_index(name="Cases")
        .sort_values(
            by="Cases",
            ascending=False
        )
    )