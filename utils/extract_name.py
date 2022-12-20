import re

def extract_name(string):
    pattern = r'[0-3][0-9]-[0-1][0-9]-20[0-9][0-9]'
    match = re.search(pattern, string)
    date_end_index = match.end()
    name_start_index = date_end_index + 1
    name_end_index = string.rfind('.')
    name_string = string[name_start_index: name_end_index]
    name_string = name_string.replace('_', ' ')
    name_string = name_string.replace('-', ' ')
    return name_string