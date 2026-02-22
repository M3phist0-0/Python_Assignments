import sys
from collections import defaultdict, namedtuple
from real_estate.helper_functions.context_manager import ContextManager
from real_estate.helper_functions.calculate_stats import *

class RealEstate:
    """
          initializes attributes for RealEstate creates default dict properties_dict
           Attributes:
              file_name: file to load data
              location: the directory where the file is located
              properties_dict: nested dictionary storing property data
           Methods:
           load_data: reads and cleans data from the csv file
           _create_container: creates a namedtuple for property records
           compute_stats: computes specified statistics on the dataset
           """

    def __init__(self, file_name, location):
        """
        initializes attributes for RealEstate and loads real estate data
         Args:
            file_name: file to load data
            location: the directory where the file is located
         Returns:
             None
         """
        self.file_name = file_name
        self.location = location
        self.properties_dict = defaultdict(lambda: defaultdict(list),
            {
                'Territories': defaultdict(list, {
                    'Puerto Rico': [],
                    'Virgin Islands': []
                }),
                'US States': defaultdict(list, {
                    'Massachusetts': [],
                    'Connecticut': [],
                    'New Hampshire': [],
                    'Vermont': [],
                    'New Jersey': [],
                    'New York': [],
                    'South Carolina': [],
                    'Tennessee': [],
                    'Rhode Island': [],
                    'Virginia': [],
                    'Wyoming': [],
                    'Maine': [],
                    'Georgia': [],
                    'Pennsylvania': [],
                    'West Virginia': [],
                    'Delaware': [],
                    'Louisiana': []
                })
            }
        )
        self.load_data()

    def load_data(self):
        """
            reads and processes real estate data from csv file
         Return:
            None
         """

        while True:
            try:
                with ContextManager(self.file_name, 'r', self.location) as f:
                    headers = next(f).strip().split(',')
                    Property = self._create_container(headers)

                    for line in f:
                        row = [value.strip() for value in line.strip().split(',')]
                        if len(row) == len(headers):
                            property_instance = Property(*row)
                            state = getattr(property_instance,'state', None)

                            if state in self.properties_dict['Territories']:
                                self.properties_dict['Territories'][state].append(property_instance)
                            elif state in self.properties_dict['US States']:
                                self.properties_dict['US States'][state].append(property_instance)
                break
            except FileNotFoundError:
                file_not_found = input(f'{self.file_name} not found. Please enter a valid file name or q to quit: ')
                if file_not_found.lower() == 'q':
                    sys.exit()
                self.file_name = file_not_found

    @staticmethod
    def _create_container(header):
        """
        creates a namedtuple to represent property records based on file headers
        Args:
            header: a list of the column names form the csv file
         Return:
         namedtuple: a namedtuple class for property records
         """
        return namedtuple('Property', header)


    def compute_stats(self, function_name=str, *args, **kwargs):
        """
        real estate statistics based on the specified function
         Args:
            function_name: name of statistical function to execute
            args: additional positional arguments
            kwargs: additional keyword arguments
         Return:
             the result of the requested calculate stats function

         """
        available_func = {'cheapest': cheapest,
                        'priciest': priciest,
                        'dirt_cheap': dirt_cheap,
                        'best_deal': best_deal,
                        'budget_friendly': budget_friendly}
        if function_name in available_func:
            return available_func[function_name](self.properties_dict, *args, **kwargs)
        else:
            raise ValueError(f'{function_name} not found in calculate_stats')








