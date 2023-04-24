import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

###################################GET##########################################

    def get_api_key(self, email, password):
        headers = {
            "email": email,
            "password": password
        }
        resp = requests.get(self.base_url+"api/key", headers=headers)
        status = resp.status_code
        try:
            result = resp.json()
        except:
            result = resp.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {"auth_key": auth_key["key"]}
        filter = {"filter": filter}

        resp = requests.get(self.base_url+"api/pets", headers=headers, params=filter)
        status = resp.status_code
        try:
            result = resp.json()
        except:
            result = resp.text
        return status, result

###################################POST##########################################

    def add_simple_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

###################################DELETE##########################################

    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

###################################UPDATE##########################################

    def update_pet_info(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: int) -> json:
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

###################################NEGATIVE##########################################
###################################POST##########################################
    def add_new_pet_ico(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/ico')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

###################################NEGATIVE##########################################
###################################DELETE############################################
