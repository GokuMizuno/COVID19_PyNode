import pandas as pd
import sys

numberOfCountries = int(sys.argv[1])
aggTimeInterval = sys.argv[2]

def Covid19Analysis (numberOfCountries, aggTimeInterval):
    df = pd.read_csv(f'time_series_covid19_confirmed_global.csv')
    df = df.drop(columns['Province/State', 'Lat', 'Long'])
    df = df.groupby('Country/Region').agg('Sum')
    dfT = df.T

    #Here we change the index to the date/time
    dfTime = pd.to_datetime(dfT.index)
    dateTime_index = pd.datetime_index(dfTime.values)
    dfT = dfT.set_index(dateTime_index)
    dfT = dfT.sort_values(by=dfT.index.dict_values[-1], axis=1, ascending=False)
    dfT = dfT.iloc(:,0,numberOfCountries)
    dfT = dfT.resample(aggTimeInterval).mean()
    output = dfT.to_json()
    print(output)
    sys.stdout.flush()

Covid19Analysis(numberOfCountries, aggTimeInterval)
