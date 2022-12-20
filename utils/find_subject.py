import re

#to find subject to create directory and store filess in
def find_subject(string):
  pattern = r"B[A-Z]{3}[0-9]{3}[LPJE]"
  match = re.search(pattern, string)
  if match:
    return match.group()