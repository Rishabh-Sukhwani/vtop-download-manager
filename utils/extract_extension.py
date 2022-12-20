import re

def extract_extension(string):
    extension_start_index = string.rfind('.')
    extension = string[extension_start_index: ]
    return extension
