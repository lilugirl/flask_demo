import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()

for user in data['results']:
    print(user['name']['first'])

def greet(greeting,name):
    """Returns a greeting

    Args:
        greeting (string): A greet word
        name (string): A persons name

    Returns:
       string: A greeting with a name
    """
    return f'{greeting} {name}'

print(greet('Hello','World'))
