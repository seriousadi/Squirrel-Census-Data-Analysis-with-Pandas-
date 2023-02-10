import pandas
#Cinnamon
#Gray
#White
data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].tolist()
gray = data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].tolist()
black = data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].tolist()
parks_squirrel = {
    "Numbers": [len(cinnamon), len(gray), len(black)],
    "Fur Color": ["Cinnamon","Gray","White"]
}
file = pandas.DataFrame(parks_squirrel)
file.to_csv("New fur color")