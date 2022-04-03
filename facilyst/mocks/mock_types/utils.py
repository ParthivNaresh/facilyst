import numpy as np
import pandas as pd


def handle_mock_and_library_type(mock_type="features", library="pandas"):
    if mock_type.lower() in ["df", "dataframe", "features", "x"]:
        mock_type_ = "features"
    elif mock_type.lower() in ["dates", "date"]:
        mock_type_ = "dates"
    elif mock_type.lower() in ["waves", "wave", "sine", "sin", "cosine", "cos"]:
        mock_type_ = "wave"
    else:
        mock_type_ = "features"

    if library.lower() in ["pd", "pandas", "df", "dataframe", "series"]:
        library_ = "pandas"
    elif library.lower() in ["np", "numpy", "array", "ndarray"]:
        library_ = "numpy"
    else:
        library_ = "pandas"

    return mock_type_, library_


def mock_features_dtypes(num_rows=100):
    """
    Internal function that returns the default full dataset.

    :param num_rows: The number of observations in the final dataset. Defaults to 100.
    :return: The dataset with all columns included.
    """
    dtypes_dict = {
        "ints": [i for i in range(-num_rows // 2, num_rows // 2)],
        "rand_ints": np.random.choice([i for i in range(-5, 5)], num_rows),
        "floats": [float(i) for i in range(-num_rows // 2, num_rows // 2)],
        "rand_floats": np.random.uniform(low=-5.0, high=5.0, size=num_rows),
        "booleans": np.random.choice([True, False], num_rows),
        "categoricals": np.random.choice(
            ["First", "Second", "Third", "Fourth"], num_rows
        ),
        "dates": pd.date_range("1/1/2001", periods=num_rows),
        "texts": [
            f"My children are miserable failures, all {i} of them!"
            for i in range(num_rows)
        ],
        "ints_nullable": np.random.choice(
            [i for i in range(-10 // 2, 10 // 2)] + [pd.NA], num_rows
        ),
        "floats_nullable": np.random.choice(
            np.append([float(i) for i in range(-5, 5)], pd.NA), num_rows
        ),
        "booleans_nullable": np.random.choice([True, False, None], num_rows),
    }
    return dtypes_dict
