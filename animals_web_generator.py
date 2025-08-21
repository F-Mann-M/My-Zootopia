import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_html(file_path):
    """loads a html file"""
    with open(file_path, "r") as file:
        return file.read()

def get_data():
    """
    loads a jason and returns a string with name, diet, type and location of an Animal
    """
    output = ""

    animals_data = load_data('animals_data.json')
    for animal in animals_data:

        # get data from dictionary
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        animal_type = animal.get("characteristics", {}).get("type")
        location = ", ".join(animal.get("locations")) #join location list to string with commas

        # if variable not empty print
        if name:
            output += f"<p>Name: {name}<br>\n"
        if diet:
            output += f"Diet: {diet}<br>\n"
        if animal_type:
            output += f"Type: {animal_type}<br>\n"
        if location:
            output += f"Location: {location}<br></p>\n\n"
    return output


def replace_string(old_string):
    new_string = get_data()
    html_temp = load_html("animals_template.html")
    new_html = html_temp.replace(old_string, new_string)
    return new_html


def write_html(old_string):
    new_html = replace_string(old_string)
    with open("animals.html", "w") as file:
        file.write(new_html)

write_html("__REPLACE_ANIMALS_INFO__")