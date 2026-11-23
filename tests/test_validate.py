import pandas as pd

from validate import validate_duplicates


def test_validation_returns_list():

    df = pd.DataFrame(
        {
            "id": [1, 1]
        }
    )

    result = validate_duplicates(df)

    assert isinstance(result, list)