import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')
for animal in animals_data:
    animal_data_dict = dict()

    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    animal_type = animal.get("characteristics", {}).get("type")
    location = animal.get("locations")

    if name:
        animal_data_dict["Name"] = name
    if diet:
        animal_data_dict["Diet"] = diet
    if animal_type:
        animal_data_dict["Type"] = animal_type
    if location:
        animal_data_dict["Location"] = location


    for info, data in animal_data_dict.items():
        if isinstance(data, str):
            print(f"{info}: {data}")
        elif isinstance(data, list):
            print(f"{info}:", end=" ")
            for continent in data:
                print(continent, end=" ")
    print("\n")
