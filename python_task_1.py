import pandas as pd



def generate_car_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a DataFrame for id combinations.

    Args:
        df (pandas.DataFrame): Input DataFrame with 'id_1', 'id_2', and 'car' columns.

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values,
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = car_matrix.fillna(0)
    for i in car_matrix.index:
        car_matrix.at[i, i] = 0
    return car_matrix

df = pd.read_csv("dataset-1.csv")
result = generate_car_matrix(df)
print(result)


import pandas as pd

def get_type_count(df) -> dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    
    df['car_type'] = pd.cut(df['car'], bins=[float('-inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    
    type_counts = df['car_type'].value_counts().to_dict()

    
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts


df = pd.read_csv("dataset-1.csv")
result = get_type_count(df)
print(result)



def get_bus_indexes(df):
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    
    bus_mean = df['bus'].mean()

    
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    return sorted(bus_indexes)


df = pd.read_csv("dataset-1.csv")

result = get_bus_indexes(df)

print(result)



import pandas as pd

def filter_routes(df):
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    
    route_avg_truck = df.groupby('route')['truck'].mean()

    
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    return sorted(filtered_routes)


df = pd.read_csv("dataset-1.csv")
result = filter_routes(df)
print(result)




def multiply_matrix(matrix):
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Use the applymap function to modify each element in the DataFrame
    modified_matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix


result = generate_car_matrix(df)
modified_result = multiply_matrix(result)
print(modified_result)



def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
