from validator import validate
import json
def validate_data(schema, data):
    return validate(schema, data)

def write_to_file(data, filename):
    try:
        filename = f"{filename}.json"
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        return f"Data written to {filename} successfully. \n"
    except Exception as e:
        return f"Error: {e}"

def remove_char(text, char):
    return text.replace(char, "")

def get_first_element_separator(text, separator):
    return text.split(separator)[0]