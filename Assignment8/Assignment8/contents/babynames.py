import pandas as pd
import matplotlib.pyplot as plt
from contents.helper_functions.hf import retrieve_files, record_loader_gen

# (U・ﻌ・U) added some fun ascii art at the end of this as well as in the __init's__ enjoy!

class BabyNames:
    """
    processes and visualizes baby name data
    Attributes:
        names_df: pd.DataFrame
    Methods:
        __init__: initializes the BabyNames instance
        sort_data: sorts the names_df DataFrame
        m_f_names: generate and displays a line plot show the total # of male and female
        births per year
        most_popular_ever: generates and displays a line plot showing the trends of the
        top 3 most popular names
        unisex: generates and displays a bar plot showing the total # of unisex names per year
        unisex_evolution: tracks the evolution of specific unisex names over time based on user input

    """

    def __init__(self):
        """
        initializes BabyName Instance
        Attrs:
            None
        Returns:
            None
        """
        directory = retrieve_files('.txt')
        print(f'Files Found:{len(directory)}')
        self.names_df = pd.DataFrame(record_loader_gen(directory), columns=['Name', 'Gender', 'Births', 'Year'])
        self.sort_data()


    def sort_data(self):
        """
        sorts the names_df Dataframe by the Year column in ascending order
        Args:
            None
        Returns:
            None

        """
        self.names_df.sort_values(by=['Year'], ascending= True)

    def m_f_names(self, starting_year=1880, ending_year=2022):
        """
        generates and displays a line plot show the total # of male and female
        births per year
        Args:
            starting_year(int): the starting year for analysis
            ending_year(int): the ending year for analysis
        Returns:
            Line plot
        """

        filter_df = self.names_df[(self.names_df['Year'] >= starting_year) & (self.names_df['Year'] <= ending_year)]
        gender_births = filter_df.groupby(['Year', 'Gender'])['Births'].sum().unstack()

        plt.figure(figsize= (10,5))
        gender_births.plot(kind='line', ax=plt.gca())

        plt.xlabel('Year')
        plt.ylabel('Births')
        plt.title('Number of Male and Female Births')
        plt.legend(['Male','Female'])

        plt.show()

    def most_popular_ever(self):
        """
        generates and displays a line plot showing the trends of the
        top 3 most popular names
         Args:
             None
         Returns:
             Line plot
         """

        total_births = self.names_df.groupby('Name')['Births'].sum().sort_values(ascending=False)
        top_3_names = total_births.head(3).index

        plt.figure(figsize=(10, 5))

        for name in top_3_names:
            name_data = self.names_df[self.names_df['Name'] == name]
            yearly_counts = name_data.groupby('Year')['Births'].sum()
            plt.plot(yearly_counts.index, yearly_counts.values, label=name)

        plt.xlabel('Year')
        plt.ylabel('Total Births')
        plt.title('Top 3 Most Popular Names Over Time')
        plt.legend()
        plt.show()

    def unisex(self):
        """
        generates and displays a bar plot showing the total # of unisex names per year
         Args:
             None
         Returns:
             Bar graph
        """

        name_count = self.names_df.groupby(['Year','Name'])['Gender'].nunique().reset_index()
        unisex_names = name_count[name_count['Gender'] == 2]
        unisex_data = self.names_df.merge(unisex_names[['Year', 'Name']], on=['Year', 'Name'])
        unisex_data = unisex_data.groupby('Year')['Births'].sum().reset_index()

        plt.figure(figsize=(10,5))
        plt.bar(unisex_data['Year'], unisex_data['Births'], color='green')
        plt.title('Unisex Names by Year')
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.legend(['Unisex Names'])
        plt.show()

    def unisex_evolution(self):
        """
        tracks the evolution of specific unisex names over time based on user input
         Args:
             None
         Returns:
             Line Graph
        """
        m_names = set(self.names_df[self.names_df['Gender'] == 'M']['Name'])
        f_names = set(self.names_df[self.names_df['Gender'] == 'F']['Name'])
        unisex_names = m_names.intersection(f_names)

        print('Unisex Names:', unisex_names)
        selected_names = set()

        while True:
            name = input('Enter a unisex name to track (or q to quit): ').strip()
            if name == 'q':
                break
            elif name in unisex_names:
                selected_names.add(name)

            else:
                print('Invalid name. Please enter a name from the list.')

        if not selected_names:
            print('No name selected.(⇀‸↼‶)⊃━☆ﾟ.*･｡ﾟ  Exiting')
            return

        plt.figure(figsize=(10,5))

        for name in selected_names:
            unisex_data = self.names_df[self.names_df['Name'] == name]
            yearly_counts = unisex_data.groupby('Year')['Births'].sum()
            plt.plot(yearly_counts.index, yearly_counts.values, label=name)

        plt.xlabel('Year')
        plt.ylabel('Total Births')
        plt.title('Glorious Evolution')
        plt.legend()

#
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣵⣿⠿⢟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠈⡀⠀⠀⠀⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⢛⠩⠥⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢀⡠⠖⠉⡠⢶⡄⠀⣀⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⡀⠀⢠⣾⣿⣿⣿⣿⣿⡿⢋⡵⠛⢁⣠⠶⠋⣀⣀⣠⠴⠋⠁⠀⠟⣁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣠⡾⠋⢁⡀⢰⠄⣴⣿⣿⣿⣿⣿⢟⡡⠞⠉⢀⣴⠟⠁⠀⣾⠟⠋⢀⣀⠀⡠⣠⣾⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣜⡟⠁⡴⠟⢀⠆⣼⣿⣿⣿⡿⢟⡤⠊⠀⢀⣴⠟⢁⠀⢀⣆⣠⣾⠀⠟⣡⢞⣵⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⢀⣾⡏⠀⠈⠀⠀⠊⣾⡟⣿⣿⠋⡴⠋⠀⠀⣠⡿⠃⠀⠀⣰⣿⣿⣿⢃⣴⣿⣵⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⢸⡇⣿⣿⠁⠀⠀⠀⣠⣼⠋⠜⠉⡡⠊⠀⢠⢏⣼⠏⡠⢂⠀⢠⣻⣿⠋⠁⣠⣵⠆⠙⠛⠿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⣸⡟⢻⡇⠀⠀⠀⠀⡿⠁⠀⠀⠄⠀⠀⣰⢃⡾⢁⣼⣷⢋⡄⣾⣿⡏⢠⡾⠟⣁⠤⠀⠀⠀⢼⣿⣿⠇⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀
# ⠀⢹⡇⠆⡇⠀⠀⠀⠸⠁⠀⠀⠂⠀⠀⢰⣧⡞⢠⣿⡿⢁⣾⣿⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡟⠀⠀⠀⡼⠁⣴⣷⠀⠀⠀⠀⠀
# ⠀⠸⠃⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⢡⣿⡟⠀⢾⣿⡏⣿⣿⡇⠀⠀⠀⢠⣤⣄⣀⠒⠀⠀⠀⠀⠀⠀⠁⢀⠈⠁⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢰⣿⣁⣾⣿⡇⠈⠙⠛⠇⣿⣿⡇⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⣆⠀⠀⠀⠀⢠⠀⠠⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣆⠀⠀⠀⠈⠀⠀⡠⠃⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⢿⡇⢀⣴⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⣠⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠘⣧⢆⠻⠀⡄⢿⡏⢀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠇⢴⣿⣿⠟⣣⣴⢿⣿⠿⠿⠛⠿⡆⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⡀⠐⠢⠈⠸⣷⡀⢳⠈⠀⢸⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣡⣾⣿⣿⣦⣤⣤⣈⣠⣺⠇⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⠀⠀⠁⠛⠁⣸⡇⠀⢸⠀⠐⣿⠄⠀⠀⠀⠀⠀⡀⠀⢰⣿⣿⣿⣿⣿⣿⠿⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⢻⡷⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣛⣋⠁⢤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠖⢒⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡙⠛⠿⢿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⡁⠰⣶⡄⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠦⠀⠾⠿⠿⠦⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡦⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠸⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣤⣀⣠⣤⣤
# ⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿