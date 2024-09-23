import pandas as pd


def load_and_clean_data():
    # Load the dataset
    df = pd.read_csv('data/michelin_by_Jerry_Ng.csv')

    # Inspect the data
    print(df.head())

    # Drop rows with missing latitude or longitude values (important for mapping)
    df = df.dropna(subset=['Latitude', 'Longitude'])

    # Filter relevant columns for simplicity
    df = df[['Name', 'Location', 'Price', 'Cuisine', 'Longitude', 'Latitude', 'Award', 'GreenStar', 'Description']]

    return df