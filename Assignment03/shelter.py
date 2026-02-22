

class Shelter:
    """""
    Attributes:
        num_occupants(int): the number of occupants that fit on the hammock
        material(str): the material the hammock is made of
        setup_time(int): the time it takes to set up the hammock
        weight(float): how much the hammock weighs
        seasons(int): what weather the hammock can withstand

    Methods:
        __str__(string):  returns __repr__
        __repr__(string): __repr__ returns a string of a Shelter value attributes only
        is_better(bool): is_better checks whether the weight and set up time of
            one shelter is less that the second, the setup time is
            less that the second, and if the season is rated higher
            than or equal to the other.

    """


    def __init__(self, num_occupants, material, setup_time, weight, seasons):
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.seasons = seasons


    def is_better(self, other):
        """""
        Args:
            other: represents another shelter object
        Methods:
            is_better(bool): is_better checks whether the weight and set up time of
                one shelter is less that the second, the setup time is
                less that the second, and if the season is rated higher
                than or equal to the other.

        """
        if type(self) == type(other):
            return ((self.weight < other.weight) and (self.setup_time < other.setup_time)
                    and (self.seasons >= other.seasons))
        return NotImplemented

    @staticmethod
    def total_sleep_spots(shelters):
        """""
        Args:
            shelters: represents a shelter object
        Methods:
            total_sleep_spots: adds up the total number of sleeping spots available
             from a non-determined number of Shelters

        """
        return sum(shelter.num_occupants for shelter in shelters)

    def __str__(self):
        """""
        Methods:
            __str__(string): returns __repr__

        """
        return self.__repr__()

    def __repr__(self):
        """""
        Methods:
            __repr__(string): __repr__ returns a string of a hammock value attributes only

        """
        return f"Shelter({self.num_occupants}, '{self.material}', {self.setup_time}, {self.weight}, {self.seasons}"


class Hammock(Shelter):
    """""
    Attributes:
        num_occupants(int): the number of occupants that fit on the hammock
        material(str): the material the hammock is made of
        setup_time(int): the time it takes to set up the hammock
        weight(float): how much the hammock weighs
        length(int): the length of the hammock
        seasons(int): what weather the hammock can withstand

    Methods:
        __str__(string): returns __repr__
        __repr__(string): __repr__ returns a string of a hammock value attributes only
        __lt__: returns NotImplemented

    """
    def __init__(self, num_occupants, material, setup_time, weight, length, seasons=3):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.length = length

    def __lt__(self, other):
        """""
          Args:
            other: represents another hammock object

        Methods:

            __lt__: compares the hammocks weight and setup time returns NotImplemented

        """
        if type(self) == type(other):
            return (self.weight < other.weight) and (self.setup_time < other.setup_time)
        return NotImplemented

    def __str__(self):
        """""
     Methods:
              __str__(string): returns __repr__

          """
        return self.__repr__()

    def __repr__(self):
        """""
          Methods:
              __repr__(string): __repr__ returns a string of a hammock value and inherited atts.

          """
        return f"{super().__repr__()}, {self.length})"




class Tent(Shelter):
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
        __str__: returns __repr__
        __repr__: represents the attributes of the tents in __repr__
        that returns each attribute without the label just the values.
        __lt__: compares the tents number of occupants and square foot where
        if the num_occupants and the square foot is less than it returns NotImplemented

    ...
"""

    def __init__(self, num_occupants, material, setup_time, sqft, vestibule, weight, structure_poles=True, seasons=3 ):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft
        self.vestibule = vestibule
        self.structure_poles = structure_poles


    def __lt__(self, other):
        """
                Args:
                    other: represents another tent object

                Returns:
                    NotImplemented: compares the tents number of occupants and square foot where
        if the num_occupants and the square foot is less than it returns NotImplemented
                """
        if type(self) == type(other):
            return (self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)
        return NotImplemented

    def __str__(self):
        """

    Return:
        (String): returns __repr__
     """
        return self.__repr__()

    def __repr__(self):
        """

               Return:
                   (String): __repr__ returns a parent class attributes and
                   unique atts of a tent object
               """
        return f"{super().__repr__()}, {self.sqft}, {self.vestibule}, {self.structure_poles})"



class Tarp(Shelter):
    """""
         Attributes:
             num_occupants(int): the number of occupants that fit on the hammock
             material(str): the material the hammock is made of
             setup_time(int): the time it takes to set up the hammock
             sqft(float): the square footage of the tarp
             weight(float): how much the hammock weighs
             seasons(int): what weather the hammock can withstand

         Methods:
             __str__(string):  returns __repr__
             __repr__(string): __repr__ returns a string of a tarp value
             attributes and inherited atts.
             __lt__(bool): returns NotImplemented

         """

    def __init__(self, num_occupants, material, setup_time, sqft, weight, seasons=3):
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft

    def __lt__(self, other):
        """
            Args:
                other: represents another tent object

            Returns:
                NotImplemented: compares the tarps number of occupants and square foot where
               if the num_occupants and the square foot is less than it returns NotImplemented
                       """
        if type(self) == type(other):
            return (self.num_occupants < other.num_occupants) and (self.sqft < other.sqft)
        return NotImplemented

    def __str__(self):
        """

         Return:
             (String): returns __repr__
          """
        return self.__repr__()


    def __repr__(self):
        """""

         Methods:
            __str__(string):  returns __repr__
                     __repr__(string): __repr__ returns a string of a tarp value
                     attributes and inherited atts.


        """

        return f"{super().__repr__()}, {self.sqft})"