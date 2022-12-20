import re

def find_date(string):
    pattern = r'[0-3][0-9]-[0-1][0-9]-20[0-9][0-9]'
    match = re.search(pattern, string)
    if match:
        return match.group()