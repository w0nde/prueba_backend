import requests

def get_value(name, status):
    url = f'https://rickandmortyapi.com/api/character/?name={name}&status={status}'
    response = requests.get(url)
    print(response.json())


def filter_character():
    name = str(input('enter name: '))
    status = str(input('enter status: '))
    get_value(name, status)


if __name__ == '__main__':
    filter_character()
