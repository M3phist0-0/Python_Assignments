import collections
import os
import csv
from collections import namedtuple

class AutoMpg:
    """"
    Attributes:
   -------------------------------------
        make(str): the make car object ie: Ford, Chevy, Dodge etc.
        model(str): the model of the car object ie: Focus, Civic, Camry etc.
        year(int): the year the car object was made
        mpg(float): the mpg of the car object

    Methods:
  ---------------------------------------
        init: holds and defines the attributes of the AutoMpg class
        repr: returns the string of attributes in specific repr format
        str: calls the repr method
        lt: compares two objects with less than operator
        eq: compares two objects with the equal operator
        hash: returns a hash value for the car object
    """
#ATTRIBUTES
    def __init__(self, make="", model="", year=0000, mpg=0.0):
        """
        Init holds the attributes of the AutoMpg class
        Args:
        make(str): the make of the car object ie: Ford, Chevy, Dodge etc.
        model(str): the model of the car object ie: Focus, Civic, Camry etc.
        year(int):the year the car object was made
        mpg(float):the mpg of the car object
        Return:
            None
        """
        self.make = make
        self.model = model
        self.year = (int(1900)+int(year))
        self.mpg = mpg

#METHODS
    def __repr__(self):
        """
        the repr method returns the data in repr format
        Return:
            returns the data in format defined below
        """
        return f"AutoMPG('{self.make}', '{self.model}', {self.year}, {self.mpg})"

    def __str__(self):
        """
        calls the repr method
        """
        return self.__repr__()

    def __lt__(self, other):
        """
        lt uses the less than operator to compare two objects
        Args:
            other: a second AutoMpg object
        Return:
            returns a bool (True) if the self object is considered
            less than the other object
        """
        if self.make != other.make:
            return self.make < other.make
        elif self.model != other.model:
            return self.model < other.model
        elif self.year != other.year:
            return self.year < other.year
        return self.mpg < other.mpg


    def __eq__(self, other):
        """
        compare two AutoMPG objects using the equal op
        Args:
            other: a second AutoMpg object
        Return:
        (bool): returns true if all self attributes and other
        objects are equal false if otherwise
        """
        if isinstance(other, AutoMpg):
            return ((self.make, self.model, self.year, self.mpg) ==
                (other.make, other.model, other.year, other.mpg))
        return False


    def __hash__(self):
        """
        returns hash value of AutoMpg objects
        Return:
        (int): returns a hash value of an object of the class
        """
        return hash((self.make, self.model, self.year, self.mpg))


class AutoMPGData:
    """"
     Attributes:
    -------------------------------------
         auto-mpg data: the data list of objects for AutoMpg

     Methods:
   ---------------------------------------
        init: the init method checks if the cleaned data file exists then initializes the data from
        the clean file.
         iter: iterates over the list of objects in the data set
         load data: loads the cleaned data from the auto-mpg.clean
         file and creates the objects using named tuple to identify the
         objects as attributes from AutoMpg
         clean data: cleans the raw data from auto-mpg.data file
         and writes it to auto-mpg.clean
     """

    def __init__(self):
        """
        Checks if the cleaned data file exists then initializes the data from
        the clean file.
        """
        self.data = []
        self._load_data()

#METHODS

    def __iter__(self):
        """

        Return:
        (iter): iterates over the data list
        """
        return iter(self.data)

    @staticmethod
    def _clean_data():
        """
        Cleans the raw data and then saves it to auto-mpg.clean
        (had trouble with this method not sure why, but it kept
        giving me a 'this method may be static' warning. I got annoyed
        and use the @staticmethod to get rid of the warning)
        """

        with open('auto-mpg.data', 'r') as input_file:
            with open('auto-mpg.clean', 'w') as output_file:
                for line in input_file:
                    cleaned_line = line.expandtabs()
                    cleaned_line = " ".join(cleaned_line.split())
                    if cleaned_line.split():
                        output_file.write(cleaned_line+"\n")


    def _load_data(self):
        """
        Loads the clean data from auto-mpg.clean and then
        creates objects from that data
        """

        if not os.path.exists('auto-mpg.clean'):
            self._clean_data()


        with open('auto-mpg.clean', 'r') as file:
            reader = csv.reader(file, delimiter=" ", skipinitialspace=True)
            Record = namedtuple('Record', ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name'])


            for row in reader:
                if len(row) < 9:
                    continue
                mpg = float(row[0])
                year = int(row[6])
                car_name = row[8]

                if " " in car_name:
                    make, model = car_name.split(" ",1)
                else:
                    make = car_name
                    model = ""

                auto_obj = AutoMpg(make, model, year, mpg)
                self.data.append(auto_obj)



def main():
    """
    Initializes the data set, iterates over all AutoMpg objects
    then prints each object.
    """
    auto_please = AutoMPGData()
    for a in auto_please:
        print(a)

if __name__== "__main__":
    main()




