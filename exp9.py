Lion = {
    "name" : "Lion",
    "type" : "mammal",
    "habitat" : "Green Land",
    "diet" : "Carnivore"
}
Monkey = {
    "name" : "Monkey",
    "type" : "mammal",
    "habitat" : "Forest",
    "diet" : "Omnivore"
}
Penguin = {
    "name" : "Penguin",
    "type" : "bird",
    "habitat" : "Antartica",
    "diet" : "Carnivore"
}
print("name: ", Lion['name'])
print("habitat: ",Lion['habitat'])

cat = {
    "name" : "cat",
    "superclass" : "Lion",
    "habitat" : "Domestic",
    "diet" : "Carnivore",
    "has_fur" : True,
    "can_climb" : True
}
print(cat['superclass'])