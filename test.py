"""
    This file has no meaning and is solely used for testing purposes.
"""

import dbHelper

obj1 = dbHelper.Requirements(requirement_arg="The comments were thoroughly explained.", best_arg="Outstanding",
                             good_arg="Very satisfactory",
                             bad_arg="Satisfactory", worst_arg="Unsatisfactory", written_arg=False,
                             programming_arg=True, math_arg=False, type_arg="Structure")
print(obj1.read_database(db_name="comments"))
print(obj1.read_columns("comments"))
print(obj1.read_columns("requirements"))
print(obj1.read_database(db_name="requirements"))

import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
data = {'text': 'I like books'}
response = requests.get("https://api.amplitude.com/", headers=headers)
print(response)
# response = requests.post("https://api.amplitude.com/", data=data)
# doc = BeautifulSoup(response.text, 'html.parser')
# title_tags = doc.find_all('div')