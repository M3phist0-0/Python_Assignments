import os
import csv
from collections import namedtuple
import logging
from program.custom_logger import my_logger


class AutoMPG:
    """
    This class defines an AutoMPG (car) object

    Attributes:
    -----------------------------------------------
        make (str): manufacturer of the car
        model (str): car model
        year (int): model year
        mpg (float): miles per gallon

    Methods:
    -----------------------------------------------
        __init__: constructor of the AutoMPG class
        __repr__: calls __str__ method
        __str__: returns string representation of an instance
        with the form AutoMPG(make, model, year, mpg)
        __eq__: compares make, model, year and mpg for equality
        __lt__: checks that all 4 attributes are less than all 4
        attributes of an object of the same class
        __hash__: creates unique hashing value using a tuple of
        all 4 attributes
    """

    def __init__(self, make: str, model: str, year: int, mpg: float) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg

    def __repr__(self):
        return self.__str__()

    def __str__(self) -> str:
        return f"AutoMPG({self.make}, {self.model}, {self.year}, {self.mpg})"

    def __eq__(self, other) -> bool:
        if type(self) == type(other):
            return (self.make, self.model, self.year, self.mpg) == \
                (other.make, other.model, other.year, other.mpg)
        else:
            return NotImplemented

    def __lt__(self, other):
        if type(self) == type(other):
            if (self.make, self.model, self.year, self.mpg) == \
                    (other.make, other.model, other.year, other.mpg):
                return False
            elif (self.make > other.make) or (self.model > other.model) or \
                    (self.year > other.year) or (self.mpg > other.mpg):
                return False
            else:
                return True
        else:
            return NotImplemented

    def __hash__(self) -> int:
        return hash((self.make, self.model, self.year, self.mpg))


class AutoMPGData:
    """
    This class will read in a data file, clean it, and generate a list
    of AutoMPG objects.
    Attributes:
    -----------------------------------------------
        data (list[AutoMPG]): list of AutoMPG objects

    Methods:
    -----------------------------------------------
        __init__: constructor of the AutoMPGData class. Loads data file
        __iter__: creates an iterator over the data attribute
        _load_data: reads in clean data file, if the file doesn't exist
        calls _clean_data to generate clean data file. When loading clean
        data, it creates a namedtuple 'Record' for each row and extracts
        values needed to instantiate a series of AutoMPG objects which are
        loaded into the list attribute data.
        _clean_data: loads in original data file, expands tabs, removes
        unnecessary characters and creates auto-mpg.clean.txt file.
    """

    def __init__(self, sort_year=False, sort_mpg=False):
        self.sort_year = sort_year
        self.sort_mpg = sort_mpg
        self.logger = my_logger('logs')
        self.logger.debug('Initializing AutoMPGData class.')
        self.data = []
        self._load_data()
        self.logger.debug('Data Loaded')

    def __iter__(self):
        return iter(self.data)


    def _load_data(self):
        """
        Loads data from a clean data file and loads each observation into the
        data attribute
        """
        # Create clean data file is it doesn't exist:
        if not os.path.exists("program/data/auto-mpg.clean.txt"):
            self._clean_data()

        # Create namedtuple for storing records
        record_tuple = namedtuple("Record", ["mpg", "cylinders", "displacement",
                                             "horsepower", "weight", "acceleration", "year", "origin", "name"])

        # Load data from clean data file
        with open("program/data/auto-mpg.clean.txt", "r") as rf:
            contents = csv.reader(rf, delimiter=" ")
            for line in contents:
                # Create Record tuple:
                line_record = record_tuple(*line)

                # Extract make, model, year, mpg from Record
                try:
                    make, model = line_record.name.split(maxsplit=1)
                except ValueError:
                    continue
                year = int("19" + line_record.year)
                mpg = float(line_record.mpg)

                self.data.append(AutoMPG(make, model, year, mpg))


    def _clean_data(self):
        """
        Reads in dirty data, expands tabs and standardizes data rows
        """
        with open("program/data/auto-mpg.clean.txt", "w+") as wf:
            with open("program/data/auto-mpg.data.txt", "r") as rf:
                contents = csv.reader(rf)
                for line in contents:
                    wf.writelines(" ".join(line[0].split(maxsplit=8)) + "\n")

    def sort_data(self):
        """
        Sorts the AutoMpg data list based on year, mpg, or both
        """
        if self.sort_year and self.sort_mpg:
            self.data.sort(key=lambda x: (x.year, x.mpg))
            sort_type = 'year.mpg'
        elif self.sort_year:
            self.data.sort(key=lambda x: x.year)
        elif self.sort_mpg:
            self.data.sort(key=lambda x: x.mpg)
            sort_type = 'mpg'
        else:
            sort_type = 'not sorted'

            self.logger.debug(f'Data sorted b {sort_type}')

    def save_data(self, file_path):
        """
        Saves the AutoMpg data list toa text file in specified directory
        """
        sort_type = 'year.mpg' if (self.sort_year and self.sort_mpg) else 'year' if self.sort_year else 'mpg' if self.sort_mpg else ""
        file_name = f'auto.data.{sort_type}.txt' if sort_type else 'auto.data.txt'
        save_path = os.path.join(file_path, file_name)

        os.makedirs(file_path, exist_ok=True)

        with open(save_path, 'w') as wf:
            for entry in self.data:
                wf.write(f'{entry.make}{entry.model}{entry.year}{entry.mpg}\n')
        log_message = f'(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧Data saved, sorted by {sort_type}' if sort_type else "Data saved, not sorted.!!!"
        self.logger.debug(log_message)
        print(log_message)


def main():
    """
    Instantiates an AutoMPGData object and iterates over the data
    list attribute

    Args:
        None

    Returns:
        None
    """
    auto_list = AutoMPGData()

    for car in auto_list:
        print(car)


if __name__ == "__main__":
    main()






