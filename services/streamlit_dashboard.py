

import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.express as px

df= pd.read_excel("pogoda_rozszerzona.xlsx")

# Konwersja timrstamp na datetime
df["timestamp_dt"] = pd.to_datetime(df["timestamp"], format = "%H:%M:%S %d-%m-%Y")

#Sortowanie po timestamp
df=df.sort_values("timestamp_dt", ascending=True)

# MATPLOTLIB
# #wykres punktowy: temp vs wilgotnosc
#
# plt.figure()
# plt.scatter(df["temp"], df["humidity"])
# plt.title("Temp. vs. wilgotność")
# plt.xlabel("Temp. w C")
# plt.ylabel("Wilgotność w %")
# plt.xlim([-30,50])
# plt.ylim([0,100])
# #plt.show()
#
# #Histogram rozkładu temperatur
# plt.figure()
# # wyciąganie wartości y, x i informacji o słupkach
# y_values, x_values, patches = plt.hist(df['temp'])
# plt.xlabel("Temperatura")
# plt.ylabel("Liczba obserwacji")
# plt.title("Rozkład temperatur")
# plt.ylim(0,20)
#
# print(y_values, x_values, patches)
# for p in patches:
#     p.set_facecolor((random.random(), random.random(), random.random()))
#
# #plt.show()
#
# #Wykres pudelkowy temperatury wg miasta  (box plot)
# top_cities = df["place"].value_counts().head(5).index
# #Wybór wierszy, ktore maja jedno z 5 miast w wartosciach place
# subset = df[df["place"].isin(top_cities)]
#
# #wypis wszystkich wierszy (:) i tylko kolumny "place
# #print(subset.loc[:, ["place"]])
#
# data_for_box = [
#     subset[subset["place"]==city]["temp"]
#     for city in top_cities
# ]
#
# plt.figure()
# plt.boxplot(data_for_box, labels=top_cities)
# #plt.show()
#
# #Liniowy - temperatura i temeratura odczuwalna w czasie dla jednego miasta
# city ="Lisbon"
# city_df=df[df["place"] == city]
#
#
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df[ "temp"], label="Temperatura")
# plt.plot(city_df["timestamp_dt"], city_df[ "temp_feels_like"], label="Odczuwalna")
#
# plt.legend()
# plt.title(f"Temperatura w czasie - {city}")
# plt.show()
#
# # Średnia temperatura w miastach - słupkowy
# mean_temp = df.groupby("place")["temp"].mean().sort_values()
#
# plt.figure()
# plt.bar(mean_temp.index, mean_temp.values)
# plt.ylim([-20,50])
# plt.show()
#
# #Zadanka
# #1 wykres słupkowy srednia wilgotnosc w miastach
# mean_humidity = df.groupby("place")["humidity"].mean().sort_values()
# plt.figure()
# plt.bar(mean_humidity.index, mean_humidity.values)
# plt.ylim([0,100])
# plt.show()
#
# #2 predkosc wiatru toronto w czasie
# city ="Lisbon"
# city_df=df[df["place"] == city]
#
#
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df[ "wind"], label="Wiatr")
#
# plt.legend()
# plt.title(f"Wiatr w czasie - {city}")
# #plt.show()
#
#
#
# from collections import Counter
# weather_descriptions = df['description'].dropna().tolist()
#
# # --- LICZENIE WYSTĄPIEŃ ---
# counts = df['description'].value_counts()
#
# labels = list(counts.keys())
# sizes = list(counts.values())
#
# # --- WYKRES KOŁOWY ---
# plt.figure(figsize=(6, 6))
# plt.pie(
#     sizes,
#     labels=labels,
#     autopct="%1.1f%%",   # etykiety procentowe
#     startangle=90,       # obrót wykresu (opcjonalnie)
# )
# plt.title("Udział procentowy typów pogody")
# plt.axis("equal")        # sprawia, że koło jest okrągłe
# plt.show()

# Plotly

# wykres kołowy

# fig = px.pie(df,
#              names='description',
#              title='Udział typów pogody')
# fig.show()

#wykres słupkowy
# fig= px.bar(data_frame=df,
#             x="place",
#             title = "Liczba obserwacji w miastach")
#
# fig.show()

#fig_bar ....

fig = px.scatter(df, x="temp", y="humidity", title ="Temp. vs wilgotnosc",
                 labels={"temp":"Temp. C", "humidity":"Wilgotnosc w %"})
fig.show()