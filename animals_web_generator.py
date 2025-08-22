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
    animals_data_dict = {}
    animals_data = load_data('animals_data.json')
    for animal in animals_data:

        # get data from dictionary
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        animal_type = animal.get("characteristics", {}).get("type")
        location = ", ".join(animal.get("locations")) #join location list to a string

        animals_data_dict.setdefault(name, {})
        if diet:
            animals_data_dict[name].setdefault("Diet", diet)
        if location:
            animals_data_dict[name].setdefault("Location", location)
        if animal_type:
            animals_data_dict[name].setdefault("Type", animal_type)
    return animals_data_dict


def serialize_animal(animal_dict):
    """Gets an dictionaries in a dictionary and returns it as html list"""
    output = ""
    for animal, data in animal_dict.items():
        output += "<li class=\"cards__item\">\n"
        output += f"<div class=\"card__title\">{animal}</div>\n<p class=\"card__text\">"
        for info, detail in data.items():
            output += f"<strong>{info}</strong>: {detail}</br>\n"
        output += "</p></li>\n\n"
    return output


def replace_string(old_string):
    """
    Loads an HTML page, gets data from json, replaces a specific string (old_string)
    with the data from json (new_string) and returns a new HTML.
    :param old_string:
    :return new_html:
    """
    new_string = serialize_animal(get_data())
    html_temp = load_html("animals_template.html")
    new_html = html_temp.replace(old_string, new_string)
    return new_html


def write_html(old_string):
    """
    Gets HTML code and writes it to a html file
    :param old_string:
    """
    new_html = replace_string(old_string)
    with open("animals.html", "w") as file:
        file.write(new_html)

# call function an (over)write html
write_html("__REPLACE_ANIMALS_INFO__")
print(serialize_animal(get_data()))