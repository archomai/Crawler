# melon
import requests


def save():

    response = requests.get('https://www.melon.com/chart/index.htm')
    source = response.text

    f = open('melon.html', 'wt')
    f.write(source)
    f.close()

if __name__ == "__main__":
    save()

