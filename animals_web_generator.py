import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')
for animal in animals_data:
    animal_data_dict = dict()

    # get data from dictionary
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    animal_type = animal.get("characteristics", {}).get("type")
    location = ", ".join(animal.get("locations")) #join location list to string with commas

    # if variable not empty print
    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if animal_type:
        print(f"Type: {animal_type}")
    if location:
        print(f"Location: {location} \n")

