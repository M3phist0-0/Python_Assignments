from contents.babynames import BabyNames
import matplotlib.pyplot as plt


def main():
    """
    creates an instances of BabyNames class and
    performs operations to visualize the data

    """
    bn = BabyNames()

    print('First row of sorted DataFrame:')
    print(bn.names_df.head())

    print('\nGenerating Male vs Female Names Plot...')
    bn.m_f_names()
    plt.show()

    print('\nGenerating Most Popular names Over Time Plot...')
    bn.most_popular_ever()
    plt.show()

    print('\nGenerating Unisex Name Bar Plot...')
    bn.unisex()
    plt.show()

    print('\nTracking Unisex Names Over Time...')
    bn.unisex_evolution()
    plt.show()

if __name__ == '__main__':
    main()


# ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⢠⣶⣄⣀⣀⣤⣄
# ⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠟⠁
# ⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⢀⣠⣴⣦⠻⠿⣿⣿⡇⠀⠀
# ⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣩⣴⣾⡿⠟⠋⠁⠀⠀⠈⠉⠀⠀⠀
# ⠀⢀⣠⡶⠘⣿⣿⣿⣿⠿⠟⣋⣩⣴⣾⡿⠟⣋⣥⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⢴⠟⠉⠀⠀⠛⣋⣭⣴⣶⣿⠿⠛⣋⣥⣶⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⢲⣶⣶⡾⠿⠿⠛⣛⣩⣤⣶⣾⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣿⣿⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀