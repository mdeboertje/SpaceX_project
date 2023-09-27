import requests


connection = requests.get('https://api.spacexdata.com/v3/launches')
def spacex_connection():

    return connection.json()
