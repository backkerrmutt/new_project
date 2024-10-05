import pandas as pd

def Rate_Cal(s_station, e_station):

    data = pd.read_excel('Station_Atago.xlsx',sheet_name='Price')
    selected_data = data.iloc[s_station-1,e_station+1]
    print(selected_data)
