from collections import namedtuple


#defining Property namedtuple
Property = namedtuple('Property', ['price', 'bed', 'bath', 'house_size', 'state'])

def cheapest(properties_dict, state):
    """
    finds the cheapest property in determined state
    Args:
        properties_dict: a dictionary containing sorted real estate data
        state: the specified state
    Return:
        Property namedtuple : property with the lowest price
    """
    print(f'\nCheapest in {state}:')
    state_properties = properties_dict['US States'].get(state, []) + properties_dict['Territories'].get(state, [])
    state_properties = [prop for prop in state_properties if prop.price.replace('.','', 1).isdigit()]
    if not state_properties:
        return None
    return min(state_properties, key=lambda x : float(x.price))


def priciest(properties_dict, state):
    """
    finds the priciest properties in determined state
    Args:
        properties_dict: a dictionary containing sorted real estate data
        state: the specified state
    Return:
    Property namedtuple: property with the highest price
    """
    print(f'\nPriciest in {state}:')
    state_properties = properties_dict['US States'].get(state, []) + properties_dict['Territories'].get(state, [])
    state_properties = [prop for prop in state_properties if prop.price.replace('.', '',1).isdigit()]
    if not state_properties:
        return None
    return max(state_properties, key=lambda x: float(x.price))


def dirt_cheap(properties_dict, state):
    """
    find the dirt cheap properties in determined states
    Args:
        properties_dict: a dictionary containing sorted real estate data
        state: the specified state
    Return:
    Property namedtuple: property with absolute lowest price
    """
    print(f'\nDirt Cheap in {state}:')
    properties = [prop for state in properties_dict['US States'].values() for prop in state] + \
                 [prop for territory in properties_dict['Territories'].values() for prop in territory]
    properties = [prop for prop in properties if prop.price.replace('.', '', 1).isdigit()]
    if not properties:
        return None
    return min(properties, key=lambda x: float(x.price))


def best_deal(properties_dict, state, *, bed=float, bath=float):
    """
    finds the best deal in determined state
    Args:
        properties_dict: a dictionary containing sorted real estate data
        state: the specified state
        bed: number of bedrooms
        bath: number of bathrooms
    Return:
    Property namedtuple: the best deal property
    """
    print(f'\nBest Deal in {state}:')
    print('(T＿T)')

    state_properties = [prop for prop in properties_dict['US States'].get(state, []) + properties_dict['Territories'].get(state, [])
                        if prop.bed.isdigit() and float(prop.bed) == bed and prop.bath.replace('.', '', 1).isdigit() and
                        float(prop.bath) == bath and prop.price.replace('.', '', 1).isdigit() and prop.house_size.replace('.', '', 1).isdigit()]
    if not state_properties:
        return None
    return min(state_properties, key=lambda x: float(x.price) / float(x.house_size))


def budget_friendly(properties_dict, *, bed=float, bath=float, max_budget=float):
    """
    find the budget friendly option in determined state
    Args:
        properties_dict: a dictionary containing sorted real estate data
        bed: number of bedrooms
        bath: number of bathrooms
        max_budget: maximum budget for property
    Return:
    Property namedtuple: the budget-friendly property
    """
    print(f'\nBudget Friendly:')
    print('(T＿T)')
    properties = [prop for state in properties_dict['US States'].values() for prop in state] + \
                 [prop for territory in properties_dict['Territories'].values() for prop in territory]
    filter_props = [prop for prop in properties if prop.bed.isdigit() and int(prop.bed) == bed and
                    prop.bath.replace('.', '', 1).isdigit() and float(prop.bath) == bath and
                    prop.price.replace('.', '', 1).isdigit() and float(prop.price) <= max_budget and
                    prop.house_size.replace('.','',1).isdigit()]
    if not filter_props:
        return None
    return min(filter_props, key=lambda x: float(x.price) / float(x.house_size))