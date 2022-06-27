import requests
import gzip


def get_value(name, status, download):
    url = f'https://rickandmortyapi.com/api/character/?name={name}&status={status}'
    response = requests.get(url)
    data = response.json()
    if download:
        download_file(str(data))
    print()


def filter_character():
    name = str(input('enter name: '))
    status = str(input('enter status: '))
    download = bool(input('download ? : '))
    get_value(name, status, download)


def download_file(data):
    encoded = data.encode('utf-8')
    compressed = gzip.compress(encoded)
    print(compressed)
    f = open("response.zip", "wb")
    f.write(compressed)
    f.close()


if __name__ == '__main__':
    filter_character()
