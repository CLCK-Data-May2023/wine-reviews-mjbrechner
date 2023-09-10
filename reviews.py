import pandas as pd
reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

#Get count totals
rar = reviews.country.value_counts()
size = len(rar)

#List each country
unique_countries = reviews.country.unique()

#Get country point averages
country_avg = {}

for x in unique_countries:
        country_avg[x] = reviews.points.loc[reviews.country == x].mean()
country_avg

#Get the final data frame
final = []

for z in rar.index:
    final.append(
    {'Country': z,
    'Count': rar[z],
    'Points': round(country_avg[z], 1)
    }
    )
final
final_df = pd.DataFrame(final)

final_df.to_csv('./data/reviews-per-country.csv', index=False)