from jinja2 import Environment, FileSystemLoader
from server import list_users

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')
output_from_parsed_template = template.render(users=list_users(),script=False).encode('utf-8')

# print output_from_parsed_template

# to save the results
with open("index.html", "wb") as fh:
    fh.write(output_from_parsed_template)