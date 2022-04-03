import pandas as pd

from facilyst.mocks import MockBase
from facilyst.mocks.mock_types.utils import mock_features_dtypes


class Features(MockBase):

    name = "Features"

    def __init__(
        self,
        num_rows=100,
        library="pandas",
        ints=True,
        rand_ints=True,
        floats=True,
        rand_floats=True,
        booleans=False,
        categoricals=False,
        dates=False,
        texts=False,
        ints_nullable=False,
        floats_nullable=False,
        booleans_nullable=False,
        all_dtypes=False,
    ):
        """Class to manage mock data creation of features.

        :param num_rows: The number of observations in the final dataset. Defaults to 100.
        :type num_rows: int, optional
        :param library: The library of which the final dataset should be, options are 'pandas' and 'numpy'. Defaults to 'pandas'.
        :type library: str, optional
        :param ints: Flag that includes column with monotonically increasing incremental set of negative and positive integers. Defaults to True.
        :type ints: bool, optional
        :param rand_ints: Flag that includes column with randomly selected integers between -5 and 5. Defaults to True.
        :type rand_ints: bool, optional
        :param floats: Flag that includes column which is the float version of the 'ints' column. Defaults to True.
        :type floats: bool, optional
        :param rand_floats: Flag that includes column with randomly selected floats between -5 and 5. Defaults to True.
        :type rand_floats: bool, optional
        :param booleans: Flag that includes column with randomly selected boolean values. Defaults to False.
        :type booleans: bool, optional
        :param categoricals: Flag that includes column with four categoriesL 'First', 'Second', 'Third', and 'Fourth'. Defaults to False.
        :type categoricals: bool, optional
        :param dates: Flag that includes column with monotonically increasing dates from 01/01/2001 with a daily frequency. Defaults to False.
        :type dates: bool, optional
        :param texts: Flag that includes column with different text on each line. Defaults to False.
        :type texts: bool, optional
        :param ints_nullable: Flag that includes column which is the same as the 'ints' column with pd.NA included. Defaults to False.
        :type ints_nullable: bool, optional
        :param floats_nullable: Flag that includes column which is the same as the 'floats' column with pd.NA included. Defaults to False.
        :type floats_nullable: bool, optional
        :param booleans_nullable: Flag that includes column which is a randomly selected column with boolean values and pd.NA included. Defaults to False.
        :type booleans_nullable: bool, optional
        :param all_dtypes: Flag that includes all columns. Defaults to False.
        :type all_dtypes: bool, optional
        :return: Mock features data.
        :rtype: pd.DataFrame by default, can also return np.ndarray
        """
        kw_args = locals()

        if all_dtypes:
            parameters = {
                k: True
                for k, v in kw_args.items()
                if k not in ["self", "library", "num_rows", "__class__"]
            }
        else:
            parameters = {
                k: v
                for k, v in kw_args.items()
                if k not in ["self", "library", "num_rows", "__class__"] and v
            }
            if not any(
                parameters.values()
            ):  # All False flags results in all dtypes being included
                parameters = {k: True for k, v in kw_args.items()}

        super().__init__(library, num_rows, parameters)

    def create_data(self):
        data, dtypes_to_keep = self.get_data_from_dict()
        data = self.handle_library(data, dtypes_to_keep)
        return data

    def get_data_from_dict(self):
        """
        Returns the data based on the dtypes specified during class instantiation.

        :return: The final data created from the appropriate library as a pd.DataFrame or ndarray.
        """
        dtypes_to_keep = list(self.parameters.keys())
        mocked = Features._refine_dtypes(dtypes_to_keep, self.num_rows)

        mocked_df = pd.DataFrame.from_dict(mocked)
        return mocked_df, dtypes_to_keep

    def handle_library(self, data, dtypes_to_keep):
        """
        Handles the library that was selected to determine the format in which the data will be returned.

        :return: The final data created from the appropriate library as a pd.DataFrame or ndarray.
        """
        if self.library == "numpy":
            return data.to_numpy()
        else:
            if "ints_nullable" in dtypes_to_keep:
                data["ints_nullable"] = data["ints_nullable"].astype("Int64")
            if "floats_nullable" in dtypes_to_keep:
                data["floats_nullable"] = data["floats_nullable"].astype("Float64")
            data.ww.init()
            return data

    @staticmethod
    def _refine_dtypes(dtypes, num_rows=100):
        """
        Internal function that selects the dtypes to be kept from the full dataset.

        :param dtypes: All data format options from the class initialization. Defaults to returning the full dataset.
        :param num_rows : The number of observations in the final dataset. Defaults to 100.
        :return: A refined form of the full set of columns available.
        """
        full_mock = mock_features_dtypes(num_rows)
        return {k: v for k, v in full_mock.items() if k in dtypes}
