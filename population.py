import pandas as pd

def get_population(District , Area):
    df = pd.read_csv("datas/population.csv")
    return df.loc[df['Area'] == f"{District} - {Area}", 'Total'].iloc[0]
    # print(df.query(f'Area=="{District} - {Area}"')['Total'])

# dis = input("District : ")
# area = input("Area : ")

# print(get_population(dis , area))