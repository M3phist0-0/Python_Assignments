import pandas as pd #was having issues importing pandas on my machine not sure what was up
import os

#click here for a laugh: https://www.youtube.com/watch?v=n6ryB5wz_Fw&ab_channel=aquat33n

class RealEstate2:
    """
        class for loading, processing, and analyzing real estate data from a CSV file
        Attributes:
            file_name(str): name of the csv file (realtor-data.csv)
            location(str): the state to filter the dataset by
            properties_df(DataFrame): a pandas DataFrame storing real estate data
        Methods:
            __init__: initializes the class and loads the data
            load_data: loads and processes the data from csv file
            col_2_numeric: converts columns to numeric format
            filter_by_location: filters the dataset by specified location column
            check_type: returns the data types of all columns
            helper_guy_not_col: helper function
            num_nulls: returns the number of null values in column
            get_unique_vals: retrieves unique values from column
            filth_be_gone: removes rows with a specific value in a column
            col_val_count: returns value counts for a specified column
            helper_sum_stat: helper function that calculates percentage of values
            above the median for a numeric column
            summary_table: generates a summary column for numeric columns

        """

    def __init__(self, file_name, location=None):
        """
        initializes the class and loads the real estate data
        Args:
            file_name(str): name of the CSV file to load
            location(str): specific state to filter the data by
        Returns:
            None

               """

        self.file_name = file_name
        self.location = location
        self.properties_df = pd.DataFrame()
        self.load_data(file_name, location)



    def load_data(self, file_name, location):
        """
        loads and processes the real estate data from a CSV file
        Args:
            file_name(str): name of the CSV file to load
            location(str): specific state to filter the data by
        Returns:
            None
               """

        file_path = os.path.join('data', file_name)

        if not os.path.exists(file_path):
            print(f'File not {file_name} found')
            return

        try:
            self.properties_df = pd.read_csv(file_path, low_memory = False)
            print(f'ଘ(੭ˊᵕˋ)੭*✩‧˚Data Loaded from {file_name}!')
            self._col_2_numeric()
            self.properties_df.drop_duplicates(inplace=True)

            if location:
                self.properties_df['state'] = self.properties_df['state'].astype(str)
                self.properties_df = self.properties_df[self.properties_df['state'].str.lower() == location.lower()]


        except FileNotFoundError:
            print('File not found')
        except Exception as e:
            print(f'Error loading data: {e}')



    def _col_2_numeric(self):
        """
        converts columns to numeric format
        Returns:
            None
            """

        for col in self.properties_df.columns:
            if self.properties_df[col].dtype != 'object':
                self.properties_df[col] = pd.to_numeric(self.properties_df[col], errors='coerce')
        return

    def filter_by_location(self, location_col, location_val):
        """
        filters the dataset by a specified location column
         Args:
             location_col(str): the column to filter by
             location_val(str): the value to filter for
        Returns:
            DataFrame if data is found, else None
                """
        if location_col not in self.properties_df.columns:
            print(f'{location_col} does not exist')
            return None

        filter_df = self.properties_df[self.properties_df[location_col] == location_val]

        if filter_df.empty:
            print(f'No data for {location_val} in {location_col}')

        return filter_df

    def check_type(self):
        """
        returns the data types of all columns
        Returns:
            series: data types of all columns
             """

        return self.properties_df.dtypes


    def helper_guy_not_col(self, col_name):
        """
        checks if a column exists
        Args:
            col_name(str): column name
        Returns:
            str: column name if it exists, otherwise False
               """

        if col_name in self.properties_df.columns:
            return col_name
        else:
            return False


    def num_nulls(self, col_name):
        """
        returns the number of null values in a given column.
        Args:
            col_name(str): column name
        Returns:
            int: number of null values, or None if column doesn't exist
                """
        if self.helper_guy_not_col(col_name):
            return self.properties_df[col_name].isnull().sum()
        else:
            return print(f'(⌐■_■){col_name} does not exist ')


    def get_unique_vals(self, col_name):
        """
        retrieves unique values from a column
        Args:
            col_name(str): column name
        Returns:
            tuple: (count of unique values, unique values) or None if column doesn't exist
                """

        if self.helper_guy_not_col(col_name):
            unique_vals = self.properties_df[col_name].dropna().unique()
            return len(unique_vals), unique_vals

        else:
            return print(f'(⌐■_■){col_name} does not exist ')


    def filth_be_gone(self, col_name, value):
        """
         removes rows with a specific value in a column
         Args:
             col_name(str): column name
             value: value to remove from the column
         Returns:
             None
         """
        if self.helper_guy_not_col(col_name):
            init_count = len(self.properties_df)
            self.properties_df = self.properties_df[self.properties_df[col_name] != value]
            fin_count = len(self.properties_df)
            rows = init_count - fin_count
            return print(f'( ﾉ･o･ )ﾉGot rid of {rows} filth where {col_name} == {value}.')
        else:
            return print(f'(⌐■_■){col_name} does not exist ')


    def col_val_count(self, col_name):
        """
        returns value counts for specified column
        Args:
            col_name(str): column name
        Returns:
            series: value counts, or None if column doesn't exist
                """

        if self.helper_guy_not_col(col_name):
            return self.properties_df[col_name].value_counts()
        else:
            return print(f'(⌐■_■){col_name} does not exist ')


    def helper_sum_stat(self, col_name):
        """
        Calculates the percentage of values above the median for a numeric column.
        Args:
            col_name(str): column name
        Returns:
            float: percentage of values above the median, or None if the column is not numeric
                """

        if self.properties_df[col_name].dtype not in ['float64', 'int64']:
            return print(f'(⌐■_■){col_name} is not a numeric column for aggregation.')

        median_val = self.properties_df[col_name].median()
        above_median = self.properties_df[self.properties_df[col_name] > median_val]
        above_median_percentage =(above_median.shape[0]/self.properties_df.shape[0]) * 100
        return above_median_percentage

    def summary_table(self, col_name):
        """
        generates a summary table for numeric columns
        Args:
            col_name(str): column name
        Returns:
            DataFrame: summary statistics including mean, min, max, count, and percentage above the median.
                """
        valid_col = self.helper_guy_not_col(col_name)

        if not valid_col:
            return print(f'(⌐■_■){col_name} does not exist ')

        if self.properties_df[valid_col].dtype not in ['float64', 'int64']:
            self.properties_df[valid_col] = pd.to_numeric(self.properties_df[valid_col], errors='coerce')

        summary = self.properties_df.groupby(['state', 'city']).agg({valid_col: ['mean','min','max','count']}).round(2)
        summary = summary.reset_index()
        summary.columns = ['state','city',f'{valid_col}_mean', f'{valid_col}_min', f'{valid_col}_max', f'{valid_col}_count']

        above_median_percentage = self.helper_sum_stat(valid_col)
        summary[f'{valid_col}_top_half%'] = above_median_percentage
        return summary

def main():
    file_name = 'realtor-data.csv'
    location = 'New York'

    real_estate = RealEstate2(file_name, location)

    filtered_data = real_estate.filter_by_location('state', f'{location}')
    if filtered_data is not None:
        print(f'Data filtered for state: {location}')
        print(filtered_data.head())

    col_name = 'price'
    print(f'\nSummary table for {col_name}: ')
    summary = real_estate.summary_table(col_name)
    if summary is not None:
        print(summary)


if __name__ == '__main__':
    main()





