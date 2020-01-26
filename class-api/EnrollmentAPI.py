import requests
import json


API_ADDRESS = 'localhost:5000'


class EnrollmentAPI:
    basic_url = 'http://' + API_ADDRESS

    def add(self, data):
        raise NotImplementedError

    def update(self, id, data):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def delete(self, data):
        raise NotImplementedError


class FacultyAPI(EnrollmentAPI):
    def __init__(self):
        self.url = '/'.join([self.basic_url, 'faculties'])


    def add(self, data):
        r = requests.post(self.url, json=data)

        return r.json()

    def get_all(self):
        r = requests.get(self.url)

        return r.json()

    def update(self, id, data):
        update_url = '/'.join([self.url, str(id)])

        r = requests.put(update_url, json=data)

        return r.json()

    def delete(self, id):
        delete_url = '/'.join([self.url, str(id)])

        r = requests.delete(delete_url)

        return r.json()

    def get(self, id):
        r = requests.get(self.url)

        json_r = r.json()
        result = ''

        try:
            result = json_r[id-1]
        except IndexError:
            result = f'No faculty (id={id})'

        return result
        

if __name__ == "__main__":
    # API tests :

    faculties = FacultyAPI()

    data = {'title': 'physics'}

    info = faculties.get(1)
    print(info)