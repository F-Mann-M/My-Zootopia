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
        output += "<li class=\"cards__item\">\n"
        if name:
            output += (f"<div class=\"card__title\">{name}</div>\n<p class=\"card__text\">")
        if diet:
            output += f"<strong>Diet</strong>: {diet}</br>\n"
        if location:
            output += f"<strong>Location:</strong> {location}</br>\n"
        if animal_type:
            output += f"<strong>Type:</strong> {animal_type}</br>\n"
        output += "</p></li>\n\n" # end of list

    return output


def replace_string(old_string):
    """
    Loads an HTML page, gets data from json, replaces a specific string (old_string)
    with the data from json (new_string) and returns a new HTML.
    :param old_string:
    :return new_html:
    """
    new_string = get_data()
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

write_html("__REPLACE_ANIMALS_INFO__")