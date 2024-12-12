import requests


def random_number_api(digits):
    url = f'https://www.random.org/integers/?num={
        digits}&min=0&max=9&col=1&base=10&format=plain&rnd=new'

    response = requests.get(url)

    random_number = "".join(response.text.split())
    return random_number
