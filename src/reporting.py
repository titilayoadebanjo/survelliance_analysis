def write_validation_report(issues):

    with open(
        "output/validation_report.txt",
        "w"
    ) as report:

        report.write(
            "SURVEILLANCE VALIDATION REPORT\n"
        )

        report.write(
            "=" * 40 + "\n"
        )

        for issue in issues:

            report.write(
                issue + "\n"
            )


def write_summary_report(
    disease,
    region,
    outbreak
):

    disease.to_csv(
        "output/disease_summary.csv",
        index=False
    )

    region.to_csv(
        "output/regional_summary.csv",
        index=False
    )

    outbreak.to_csv(
        "output/outbreak_summary.csv",
        index=False
    )
