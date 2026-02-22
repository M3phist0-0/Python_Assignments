from real_estate.helper_functions.calculate_stats import budget_friendly
from real_estate.load_data.load import RealEstate

def main():
    """
    Main function that calls the sorted output of the real estate data
    Return:
    None - results are printed to terminal
    """
    real_estate = RealEstate('realtor-data.csv', 'real_estate/load_data/data')

    for category, states in real_estate.properties_dict.items():
        for state, properties in states.items():
            print(f'\n{state}: {properties[:5]}')


    stats_functions = ['cheapest', 'priciest', 'dirt_cheap', 'best_deal', 'budget_friendly']
    selected_state = 'New York'

    for func in stats_functions:
        try:
            if func == 'best_deal':
                result = real_estate.compute_stats(func, selected_state, bed=float , bath=float)
            elif func == 'budget_friendly':
                result = real_estate.compute_stats(func, bed=float, bath=float , max_budget=float)
            else:
                result = real_estate.compute_stats(func, selected_state)
                print(f'{func}: {result}')
        except Exception as e:
            print(f'Error computing {func}: {e}')

if __name__ == '__main__':
    main()
