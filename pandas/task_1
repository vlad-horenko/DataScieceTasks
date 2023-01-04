import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None
import math

def answer_one():
    energy = pd.read_excel('Energy_Indicators.xls')
    energy = pd.DataFrame(energy[17:244])
    energy.reset_index(drop=True, inplace=True)
    energy.columns = ["n1", "n2", "Country", "Energy Supply", "Energy Supply per Capita", "% Renewable"]

    energy.drop(columns=["n1", "n2"], inplace=True)
    replace_value = {"Republic of Korea":"South Korea", "United States of America":"United States",
                     "United Kingdom of Great Britain and Northern Ireland":"United Kingdom",
                     "China, Hong Kong Special Administrative Region":"Hong Kong"}
    for i in range(0, len(energy)):
        for index, element in enumerate(energy.loc[i]):
            if element == "...":
                energy.loc[i][index] = np.nan
        country = ""
        for j in energy.loc[i][0]:
            if not j.isdigit():
                country += j
        energy.loc[i][0] = country
        if energy.loc[i][0] == "Republic of Korea":
            energy.loc[i][0] = "South Korea"
        elif energy.loc[i][0] == "United States of America":
            energy.loc[i][0] = "United States"
        elif energy.loc[i][0] == "United Kingdom of Great Britain and Northern Ireland":
            energy.loc[i][0] = "United Kingdom"
        elif energy.loc[i][0] == "China, Hong Kong Special Administrative Region":
            energy.loc[i][0] = "Hong Kong"
        elif energy.loc[i][0] == "Iran (Islamic Republic of)":
            energy.loc[i][0] = "Iran"
        energy.loc[i][1] = energy.loc[i][1] * 1000000
    # energy.replace({"Country":replace_value}, inplace=True)


    GDP = pd.read_csv("world_bank.csv", sep = ',', skiprows=3, encoding='utf-8')
    GDP.drop(columns=['2016', '2017', '2018', '2019', '2020', '2021', 'Unnamed: 66'], inplace=True)
    replace_value = {"Korea, Rep.":"South Korea", "Iran, Islamic Rep.":"Iran", "Hong Kong SAR, China":"Hong Kong"}
    GDP.replace({"Country Name":replace_value}, inplace=True)
    GDP.rename(columns={"Country Name":"Country"}, inplace=True)
    GDP.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code', '1960',
           '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969',
           '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978',
           '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
           '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996',
           '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005'], inplace=True)
    ScimEn = pd.read_excel("scimagojr country.xlsx")
    ScimEn.drop(columns=["Region"], inplace=True)

    data = ScimEn.merge(energy, how="inner", on=["Country"])
    data = data.merge(GDP, how="inner", on=["Country"])
    index = data["Country"]
    data.drop(columns=["Country"], inplace=True)
    data = pd.DataFrame(data.values, index=index, columns=['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'])
    return data[:15]

def answer_two():
    Top_15 = answer_one()
    list_average = []
    for i, e in enumerate(Top_15.values):
        average = (e[10] + e[11] + e[12] + e[13] + e[14] + e[15] + e[16] + e[17] + e[18] + e[19]) / 10
        list_average.append((average))
    avgGDP = pd.Series(list_average, index=Top_15.index)
    avgGDP.sort_values(ascending=False, inplace=True)
    return avgGDP

def answer_three():
    Top_15 = answer_one()
    list_average = answer_two()
    index = list_average.index[5]
    low = Top_15.loc[index].loc["2006"]
    high = Top_15.loc[index].loc["2015"]
    return abs(high - low)

def answer_four():
    Top_15 = answer_one()
    self_country = []
    total = 0
    for i in range(len(Top_15)):
        total += Top_15.iloc[i].loc["Self-citations"]
    Top_15["Total"] = Top_15["Self-citations"] / total * 100

    result = (Top_15.sort_values(by = "Total", ascending=False).index[0], Top_15.sort_values(by = "Total", ascending=False).iloc[0].loc["Total"])
    return result



# 5 кількість населення
def answer_five():
    Top_15 = answer_one()
    Top_15["Population"] = Top_15["Energy Supply"] / Top_15["Energy Supply per Capita"]
    country = Top_15.sort_values(by="Population").index[2]
    data = Top_15.sort_values(by="Population").iloc[2].loc["Population"]
    return f"{country} : {data}"

# 6
def answer_six():
    Top_15 = answer_one()
    Top_15["Population"] = Top_15["Energy Supply"] / Top_15["Energy Supply per Capita"]
    Top_15["Citable documents per capita"] = Top_15["Citable documents"] / Top_15["Population"]
    return Top_15["Citable documents per capita"].astype('float64').corr(Top_15["Energy Supply per Capita"].astype('float64'))

# 7
def answer_seven():
    Top_15 = answer_one()
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    result_data = pd.DataFrame(columns=['size', 'sum', 'mean', 'std'])
    Top_15['Estimate Population'] = Top_15['Energy Supply'] / Top_15['Energy Supply per Capita']
    groups = Top_15.groupby(ContinentDict)
    for group, frame in groups:
        size = len(frame)
        sum = frame["Estimate Population"].sum()
        mean = frame["Estimate Population"].mean()
        std = frame["Estimate Population"].std()
        result_data.loc[group] = [size, sum, mean, std]
    return result_data

if __name__ == "__main__":
    print("answer two")
    print(answer_two())
    print()
    print("answer three")
    print(answer_three())
    print()
    print('answer four')
    print(answer_four())
    print()
    print("answer five")
    print(answer_five())
    print()
    print("answer six")
    print(answer_six())
    print()
    print("answer seven")
    print(answer_seven())
