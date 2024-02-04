from validator import validate
import json
import time
def validate_data(schema, data):
    return validate(schema, data)

def write_to_file(data):
    try:
        filename = f"temp/trends_{int(time.time())}.json"
        with open(filename, "w") as file:
            json.dump(data, file)

        print(f"Data has been written to {filename}")
        return filename
    except Exception as e:
        return f"Error: {e}"

def remove_char(text, char):
    return text.replace(char, "")

def get_first_element_separator(text, separator):
    return text.split(separator)[0]