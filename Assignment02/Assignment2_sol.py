import os
import csv
from collections import namedtuple

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
            elif (self.make > other.make) or (self.model > other.model) or\
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

    def __init__(self):
        self.data = []
        self._load_data()

    
    def __iter__(self):
        return iter(self.data)
    

    def _load_data(self):
        """
        Loads data from a clean data file and loads each observation into the
        data attribute
        """
        #Create clean data file is it doesn't exist:
        if not os.path.exists("auto-mpg.clean.txt"):
            self._clean_data()

        #Create namedtuple for storing records
        record_tuple = namedtuple("Record", ["mpg", "cylinders", "displacement",\
            "horsepower", "weigt", "acceleration", "year", "origin", "name"])
        
        #Load data from clean data file
        with open("auto-mpg.clean.txt", "r") as rf:
            contents = csv.reader(rf, delimiter=" ")
            for line in contents:
                #Create Record tuple:
                line_record = record_tuple(*line)

                #Extract make, model, year, mpg from Record
                try: make, model = line_record.name.split(maxsplit=1)
                except ValueError: continue
                year = int("19" + line_record.year)
                mpg = float(line_record.mpg)

                self.data.append(AutoMPG(make, model, year, mpg))


    def _clean_data(self):
        """
        Reads in dirty data, expands tabs and standardizes data rows
        """
        with open("auto-mpg.clean.txt", "w+") as wf:
            with open("auto-mpg.data.txt", "r") as rf:
                contents = csv.reader(rf)
                for line in contents:
                    wf.writelines(" ".join(line[0].split(maxsplit=8)) + "\n")


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


if __name__=="__main__":
    main()
        







