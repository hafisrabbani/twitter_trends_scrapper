from validator import validate
import json
from models.trends import TwitterTrends
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

def format_number(number):
    number = number.replace(",", "")
    if "K" in number:
        return int(float(number.replace("K", "")) * 1000)
    elif "M" in number:
        return int(float(number.replace("M", "")) * 1000_000)
    elif "B" in number:
        return int(float(number.replace("B", "")) * 1000_000_000)
    else:
        return int(number)


def save_trends(trends):
    try:
        TwitterTrends().save_trends(trends)
        return True
    except Exception as e:
        return f"Error: {e}"


def store_db_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            save_trends(data)
        return True
    except Exception as e:
        return f"Error: {e}"
