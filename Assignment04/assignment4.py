from collections import defaultdict, Counter, namedtuple
import csv
import sys

class InvalidColumnNames(Exception):
    """
     Exception class raised when invalid column names are encountered.

     Attributes:
         col_names (list):list of invalid column names.
         msg (str):message that describes the invalid columns.
     """

    def __init__(self, column_names):
        """
        Initializes InvalidColumnNames exception.

        Args:
            column_names (list):list of column names that are invalid.
        """
        self.col_names = column_names
        self.msg = f"The names of the columns are invalid. Column names can only be alpha-numeric: {column_names}"
        super().__init__(self.msg)


class NoRecordStatsFound(Exception):
    """
      Exception class raised when statistics for a non-existent column are requested.

      Attributes:
          column_name (str):name of the column for which stats were not found.
          msg (str):message indicating that no stats are available for the column.
      """
    def __init__(self, column_name):
        """
        Initializes NoRecordStatsFound exception.

        Args:
            column_name (str):column name that is missing statistics.
        """
        self.column_name = column_name
        self.msg = f"The column stats you’re trying to access doesn’t exist. You entered {column_name}."
        super().__init__(self.msg)


class Records:
    """"
    Attributes:
   -------------------------------------
        file_name(str): csv file to load data
        file_title(file_title): title of the dataset
        record_dict(defaultdict): nested dictionary to store data
        and statistics of dataset

    Methods:
  ---------------------------------------
        init: initializes a Record object with file name and title loads data from file
        load_data: loads data from csv file and processes it into namedtuples
        _standardize_col_names: standardizes column names by removing non-alphanumeric characters
        _create_container: creates a namedtuple container using standardized column names
        record_stats: takes the file_title, a column name you wish to process and a lambda function, as arguments
        extract_top_n: extracts the top n most common values from the statistics of a specified column.

    """


    def __init__(self, file_name, file_title):
        """
         Initializes a Records object with a file name and title, and loads data from the specified file.

         Args:
             file_name (str): CSV file to load data from.
             file_title (str):title/category for the dataset.
         """

        self.file_name = file_name
        self.file_title = file_title
        self.record_dict = defaultdict(lambda: defaultdict(list), {
            'credit card': defaultdict(list, {
                'data': [],
                'stats_period': Counter()
            }),
            'customer complaints': defaultdict(list, {
                'data': [],
                'stats_product': Counter()
            }),
        })
        if self.file_name and file_title:
            self.load_data()


    def load_data(self):
        """
        Loads data from the CSV file and processes it into namedtuples for each row.
    Returns:

        If data is loaded successfully, a message will be printed confirming the file is loaded.
        Also returns sys.exit() if you quit the program
        """

        while True:

            try:
                with open(self.file_name, 'r') as file:
                    reader = csv.reader(file)
                    header = next(reader)
                    entry_tup = self._create_container(header)

                    data = [entry_tup(*row) for row in reader]

                    self.record_dict[self.file_title]['data'] = data
                    print(f'Loaded data from {self.file_name}')
                    return


            except FileNotFoundError:
                new_file = input('File not found. Please enter a valid file name or q to quit: ')
                if new_file.lower() == 'q':
                    print('Exiting...')
                    return sys.exit()


    @staticmethod
    def _standardize_col_names(col_names):
        """
        Args:
            col_names (list): A list of column names to standardize.

        Returns:
            A list of standardized column names. If any column name contains non-alphanumeric
            characters raises InvalidColumnNames.
        """

        standard_column = [''.join(char for char in col if char.isalnum()).lower() for col in col_names]

        invalid_column = [col for col in standard_column if not col.isalnum()]

        if invalid_column:
            raise InvalidColumnNames(invalid_column)

        return standard_column


    def _create_container(self, header):
        """
        Args:
             header(list): The list of column names.

         Returns:
             A namedtuple class with the standardized column names as attributes.
         """

        standard_column = self._standardize_col_names(header)
        Entry = namedtuple("Entry", standard_column)
        return Entry



    def record_stats(self, file_title, column_name, lambda_func):
        """
         Args:
             file_title(str): The dataset title.
             column_name(str): The column where statistics are calculated.
             lambda_func(function): A lambda function to process the column values.

         Returns:
             A tuple containing the column name and the Counter object with the frequency distribution.
         """

        column_name = column_name.lower()

        data = self.record_dict[file_title]['data']

        if not data or not hasattr(data[0], column_name):
            raise NoRecordStatsFound(f'No data found for {column_name}')

        lambda_func = map(lambda entry: getattr(entry, column_name), data)
        filtered_values = filter(lambda x: x is not None, lambda_func)

        stats = Counter(filtered_values)
        stats_column = f'stats_{column_name}'
        self.record_dict[file_title][stats_column] = stats

        return column_name, stats



    def extract_top_n(self, n, file_title, stats_column_name):
        """
         Args:
            n(int): The number of top values to retrieve.
            file_title(str): The dataset title (either 'credit card' or 'customer complaints').
            stats_column_name(str): The column name for which to extract statistics.

        Returns:
             A list of the top n most common values as tuples (value, count).
        """

        stats_column_name = stats_column_name.lower()
        stats = self.record_dict[file_title].get(f'stats_{stats_column_name}')
        if stats is None:
            raise NoRecordStatsFound(stats_column_name)
        most_common = stats.most_common(n)

        return most_common


def main():
    credit_card = Records('credit_card.csv', 'credit card')
    customer_complaints = Records('customer_complaints.csv', 'customer complaints')

    credit_card.record_stats('credit card','Period', lambda x: x)
    top_n_credit = credit_card.extract_top_n(10,'credit card', 'period')
    print("\n10 most common values in the Period column are:")
    for value, count in top_n_credit:
        print(f'{value}: {count}')

    customer_complaints.record_stats('customer complaints','Product', lambda x: x)
    top_n_complaints = customer_complaints.extract_top_n(10, 'customer complaints','product')
    print("\n10 most common values in the Product column are:")
    for value, count in top_n_complaints:
        print(f'{value}: {count}')
    print('(ﾉ￣□￣)ﾉ ~┻━┻ ')


if __name__ == '__main__':
    main()