import pandas

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
black_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])

squirrels_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrels, black_squirrels, cinnamon_squirrels]
}

squirrels_frame = pandas.DataFrame(squirrels_dict)
squirrels_frame.to_csv("squirrel_count.csv")