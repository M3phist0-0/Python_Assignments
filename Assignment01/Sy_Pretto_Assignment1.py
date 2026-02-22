
#Question 1:

from itertools import zip_longest

def paired_list():
    """"
    Description:
        The function paired_list takes in two lists types one of
        strings and the other of ints. Within the while loop, zip_longest
        is used to determine the longest list and add the designated
        placeholder if they are uneven(zip is used if they are).
    Args:
        None.
    Return:
        Each statement within the while loop is returning a zipped tuple
        list meeting conditions for certain cases.

            I. Checks if there are more ints than names. Returns list with
            placeholder 'FNU'.
            II. Checks if there are more names that ints. Returns list with
            placeholder that sums the values of int_list and rounds them.
            III. Checks if the lists are even. Returns zipped list with each
            name and int matched.

     """
    namelist = ['Sylus',"Zayne","Xavier","Rafayel"]
    int_list = [28,27,30,24]
    sum_int = sum(int_list) // 3
# compensation for different cases

    while True:
        if len(int_list) > len(namelist):
            uneven_list1 = list(zip_longest(namelist,int_list, fillvalue='FNU'))
            return uneven_list1

        elif len(namelist) > len(int_list):
            uneven_list2 = list(zip_longest(namelist,int_list, fillvalue=sum_int))
            return uneven_list2

        elif len(int_list) == len(namelist):
            join_even = zip(namelist,int_list)
            joined_list = list(join_even)
            return joined_list

#print joined list
print(paired_list())

#Question 2:

def even_odd_pairs(org_list, boo_val=True):
    """"
       Description:
           The function even_odd_pairs takes the set boolean value
           boo_val and filters the list produced in paired_lists by
           checking the second value in the tuple and determining whether that
            number is even or odd (x % 2 == 0 or x % != 0). It then takes the
            filtered tuples and appends them into a new list, fil_list.
       Args:
           Arg 1(list): org_list represents the list created in paired_list
           Arg 2(boolean): boo_val is the default boolean value that filters
           the tuples based on if its even True or odd False
       Return:
           This functions returns a new list fil_list that contains the
           even or odd tuples depending on the boolean value

        """
#empty list for filtered tuples
    fil_list = []

#filtering the tuple pairs

    for pair in org_list:
       if pair[1] % 2 == 0 and boo_val or pair[1] % 2 != 0 and not boo_val:
           fil_list.append(pair)
    return fil_list

#pass in original list
print(even_odd_pairs(paired_list()))


#Question 3

class Tent:
    """"
    Attributes:
    ----------------------------------------
        num_occupants (int): number of occupants that fit in tents
        material (str): material the tent is made of
        setup_time (int): time it takes to set up the tent
        sqft (float): square footage of the tent
        vestibule (bool): indicating if the tent has a vestibule or not
        weight (float): weight of tent
        structure_poles (bool): if the tent haas structure poles or not
        seasons (int): the type of environment the tent has the ability to withstand
    ...
    Methods:
    ----------------------------------------
        __str__: represents the attributes of the tents in__str__ that
        returns each attribute with a label followed with the value
        __repr__: represents the attributes of the tents in __repr__
        that returns each attribute without the label just the values.
        __lt__: compares the tents number of occupants and square foot where
        if the num_occupants and the square foot is less than it returns true.
        is_better: compares which tent is better based on the tents weight,
        setup time and its season rating.

    ...
"""
#ATTRIBUTES
    def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, structure_poles, seasons):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.vestibule = vestibule
        self.weight = weight
        self.structure_poles = structure_poles
        self.seasons = seasons

#METHODS

    def __str__(self):
        """
            Args:
                self
            Return:
                (String): __str__ returns a string of the attributes of a tent with label and value
        """
        return f"Tent(num_occupants={self.num_occupants}, material={self.material}, setup_time={self.setup_time}, sqft={self.sqft}, vestibule={self.vestibule}, weight={self.weight}, structure_poles={self.structure_poles}, seasons={self.seasons})"

    def __repr__(self):
        """
        Args:
            self

        Return:
            (String): __repr__ returns a string of a tent value attributes only
        """
        return f"({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, {self.vestibule}, {self.weight}, {self.structure_poles}, {self.seasons})"

    def __lt__(self, other):
        """
        Args:
            other: represents another tent object

        Return:
            (Bool): returns a bool True if the first tents attributes
            are less than the seconds false if not.
        """
        if self.num_occupants < other.num_occupants and self.sqft < other.sqft:
            return True

        else:
            return False

    def is_better(self, other):
        """
        Args:
            other: represents a second tent object
        Return:
            (Bool): is_better returns True whether the weight of
            one tent is less that the second, the setup time is
            less that the second, and if the season is rated greater
            than or equal to the other. False if otherwise.
        """

        #weight
        if self.weight > other.weight:
            return False

        elif self.weight < other.weight:
            return True

        elif self.weight == other.weight:
            return False

        #setup_time
        if self.setup_time > other.setup_time:
            return False

        elif self.setup_time < other.setup_time:
            return True

        elif self.setup_time == other.setup_time:
            return False

        #season
        if self.seasons >= other.seasons:
            return True
        else:
            return False


#OBJECTS
tent1 = Tent(num_occupants=4, material="polyester", setup_time=6, sqft=36.0, vestibule=False, weight=12.5, structure_poles=True, seasons=3)
tent2 = Tent(num_occupants=4, material="polyester", setup_time=5, sqft=35.0, vestibule=False, weight=11.5, structure_poles=True, seasons=3)
tent3 = Tent(num_occupants=3, material="polyester", setup_time=4, sqft=35.0, vestibule=False, weight=11.0, structure_poles=True, seasons=4)

#Print Statement
print(str(tent1))
print(repr(tent3))
print(tent3 < tent1)
print(tent1.is_better(tent2))


#Question 4

class Hammock:
    """""
    Attributes:
        num_occupants(int): the number of occupants that fit on the hammock
        material(str): the material the hammock is made of
        setup_time(int): the time it takes to set up the hammock
        weight(float): how much the hammock weighs
        length(int): the length of the hammock
        seasons(int): what weather the hammock can withstand

    Methods:
        __str__(string):  __str__ returns a string of the attributes of a
        hammock with label and value.
        __repr__(string): __repr__ returns a string of a hammock value attributes only
        __lt__(bool): returns a bool True if the first hammocks attributes
            are less than the seconds false if not.
        is_better(bool): is_better returns True whether the weight and set up time of
            one hammock is less that the second, the setup time is
            less that the second, and if the season is rated higher
            than or equal to the other. False if otherwise.

    """


#ATTRIBUTES

    def __init__(self, num_occupants, material, setup_time, weight, length, seasons):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.length = length
        self.seasons = seasons

#METHODS

    def __str__(self):
        """
        Args:
            self
        Return:
            (String): __str__ returns a string of the attributes of a hammock with label and value
        """
        return f"Hammock(Num_Occupants={self.num_occupants}, Material={self.material}, Setup Time={self.setup_time}, Weight={self.weight}, Length={self.length}, Seasons={self.seasons}"

    def __repr__(self):
        """
        Args:
            self

        Return:
            (String): __repr__ returns a string of a hammock value attributes only
        """
        return f"({self.num_occupants}, {self.material}, {self.setup_time}, {self.weight}, {self.length}, {self.seasons})"

    def __lt__(self, other):
        """
        Args:
            other: represents another hammock object

        Return:
            (Bool): returns a bool True if the first hammocks attributes
            are less than the seconds false if not.
        """
        if self.weight < other.weight and self.setup_time < other.setup_time:
            return True
        else:
            return False

    def is_better(self, other):
        """
        Args:
            other: represents a second hammock object
        Return:
            (Bool): is_better returns True whether the weight of
            one hammock is less that the second, the setup time is
            less that the second, and if the season is rated greater
            than or equal to the other. False if otherwise.
        """

        if self.weight > other.weight:
            return False

        elif self.weight < other.weight:
            return True

        elif self.weight == other.weight:
            return False

        #setup_time
        if self.setup_time > other.setup_time:
            return False

        elif self.setup_time < other.setup_time:
            return True

        elif self.setup_time == other.setup_time:
            return False

        #season
        if self.seasons >= other.seasons:
            return True
        else:
            return False

#OBJECTS

hammock1 = Hammock(num_occupants=2, material='nylon', setup_time=3, weight=9.0, length=11, seasons=3)
hammock2 = Hammock(num_occupants=1, material='polyester', setup_time=2, weight=11.0, length=13, seasons=4)
hammock3 = Hammock(num_occupants=2, material='cotton', setup_time=5, weight=8.0, length=11, seasons=4)

#print statements
print(str(hammock3))
print(repr(hammock1))
print(hammock2 < hammock1)
print(hammock3.is_better(hammock1))


#Question 5

class Tarp:
    """""
      Attributes:
          num_occupants(int): the number of occupants that fit on the hammock
          material(str): the material the hammock is made of
          setup_time(int): the time it takes to set up the hammock
          sqft(float): the square footage of the tarp
          weight(float): how much the hammock weighs
          seasons(int): what weather the hammock can withstand

      Methods:
          __str__(string):  __str__ returns a string of the attributes of a
          tarp with label and value.
          __repr__(string): __repr__ returns a string of a tarp value attributes only
          __lt__(bool): returns a bool True if the first tarps attributes
              are less than the seconds false if not.
          is_better(bool): is_better returns True whether the weight and set up time of
              one tarp is less that the second, the setup time is
              less that the second, and if the season is rated higher
              than or equal to the other. False if otherwise.

      """

#ATTRIBUTES
    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.weight = weight
        self.seasons = seasons


#METHODS
    def __str__(self):
        """
        Args:
            self
        Return:
            (String): __str__ returns a string of the attributes of a tarp with label and value
        """
        return f"Tarp(Num_Occupants={self.num_occupants}, Material={self.material}, Setup Time={self.setup_time}, Sqft={self.sqft}, Weight={self.weight}, Seasons={self.seasons}"

    def __repr__(self):
        """
        Args:
            self

        Return:
            (String): __repr__ returns a string of a tarps value attributes only
        """
        return f"({self.num_occupants}, {self.material}, {self.setup_time}, {self.sqft}, {self.weight}, {self.seasons})"

    def __lt__(self, other):
        """
        Args:
            other: represents another tarp object

        Return:
            (Bool): returns a bool True if the first tarps attributes
            are less than the seconds false if not.
            """
        if self.num_occupants < other.num_occupants and self.sqft < other.sqft:
            return True
        else:
            return False

    def is_better(self, other):
        """
        Args:
            other: represents a second tarp object
        Return:
            (Bool): is_better returns True whether the weight of
            one tarp is less that the second, the setup time is
            less that the second, and if the season is rated greater
            than or equal to the other. False if otherwise.
        """
        #weight
        if self.weight > other.weight:
            return False

        elif self.weight < other.weight:
            return True

        elif self.weight == other.weight:
            return False

        #setup_time
        if self.setup_time > other.setup_time:
            return False

        elif self.setup_time < other.setup_time:
            return True

        elif self.setup_time == other.setup_time:
            return False

        #season
        if self.seasons >= other.seasons:
            return True
        else:
            return False

#OJECTS
tarp1 = Tarp(num_occupants=3, material='polyethylene', setup_time=2, sqft=50.0, weight=10.0, seasons=3)
tarp2 = Tarp(num_occupants=2, material='canvas', setup_time=3, sqft=61.0, weight=13.0, seasons=3)
tarp3 = Tarp(num_occupants=4, material='nylon', setup_time=4, sqft=75.0, weight=15.0, seasons=4)

#print statements
print(str(tarp3))
print(repr(tarp1))
print(tarp1 < tarp2)
print(hammock1.is_better(tarp3))

class Shelter:

    def __init__(self, num_occupants, material, setup_time, weight, seasons):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.seasons = seasons


    def is_better(self, other):
        if not isinstance(other, Shelter):
            return NotImplemented
        return ((self.weight < other.weight) and
                (self.setup_time < other.setup_time) and
                (self.seasons <= other.seasons))

    @staticmethod
    def total_sleep_spots(shelters):
        return sum(shelter.num_occupants for shelter in shelters)

    def __str__(self):
        return f"({self.num_occupants}, {self.material}, {self.setup_time}, {self.weight}, {self.seasons})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if isinstance(other, Shelter):
            raise NotImplementedError("__lt__ is baased on specific class atts.")
        return NotImplemented

class Hammock(Shelter):

    def __init(self, num_occupants, material, setup_time, weight, length=11, seasons=3):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.length = length

    def __lt__(self, other):
        if isinstance(other, Hammock):
            return (self.weight < other.weight) and (self.setup_time < other.setup_time)
        elif isinstance(other, Shelter):
            return ((self.weight < other.weight) and (self.setup_time < other.setup_time)
                    and (self.num_occupants < self.num_occupants))
        return NotImplemented



class Tent(Shelter):

    def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, structure_poles=True, seasons=3 ):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft
        self.vestibule = vestibule
        self.structure_poles = structure_poles


    def __lt__(self, other):
        if isinstance(other, Tent):
            return(self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)
        elif isinstance(other, Shelter):
            return ((self.num_occupants < other.num_occupants) and (self.setup_time < other.setup_time)
                    and (self.weight < other.weight))

        return NotImplemented



class Tarp(Shelter):

    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft

    def __lt__(self, other):
        if isinstance(other, Tarp):
            return(self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)
        elif isinstance(other, Shelter):
            return ((self.num_occupants < other.num_occupants) and (self.setup_time < other.setup_time)
                    and (self.weight < other.weight))
        return NotImplemented
