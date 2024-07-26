import sqlite3

groceries = [
	"bananas",
	"apples",
	"clemintines",
	"eggs",
	"dill",
	"flour",
	"honey",
	"granola",
	"ice cream",
	"ketchup",
	"juice",
	"lemon",
	"onion",
	"margarine",
	"potatoes",
	"salt",
	"rosmary",
	"thyme",
	"watermelon",
	"vinegar",
	"pears",
	"garlic",
	"cucumbers",
	"carrots",
	"eggplants",
	"pastries",
	"milk",
	"tea",
	"coffee",
	"rice",
	"lentils",
	"noodles",
	"sweet potatoes",
	"cranberries",
	"strawberries",
	"mangos",
	"zuccinis",
	"pappers",
	"lime",
	"mushrooms",
	"broth",
	"chicken",
	"pork",
	"beef",
	"fish",
	"paprika",
	"cream",
	"tumeric",
	"pumpkin",
	"cinamon",
	"basil",
	"bread",
	"tomatoes",
	"cake",
	"gum",
	"chocolate",
	"pinapple",
	"lettuce",
	"oranges",
	"cheese",
	"cilantro"
]

groceries = sorted(groceries)

connection = sqlite3.connect("grocery_list.db")
cursor = connection.cursor()

cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(groceries)):
	cursor.execute("insert into groceries (name) values (?)",[groceries[i]])
	print("added ", groceries[i])

connection.commit()
connection.close()