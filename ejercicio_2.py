palabras = ["perro","gato", "elefante","oso","jirafa"]

animal= lambda x : len(x)>5

animales=list(filter(animal,palabras))
print(animales)