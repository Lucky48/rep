from api import PetFriends
from settings import valid_email, valid_password
from settings import invalid_email, invalid_password
import os


pf = PetFriends()
###################################POSITIVE##########################################
#####################################GET#############################################

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result

def test_get_all_pets_with_valid_key(filter=""):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0

def test_get_all_my_pets_with_valid_key(filter="my_pets"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0

###################################POST##########################################

def test_simple_add_new_pet_with_valid_data(name="Tuzik", animal_type="Cat",age="2"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_simple_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_valid_data(name="Tuzik", animal_type="Cat",age="2", pet_photo="images/image.jpg"):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

###################################DELETE##########################################

def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Tuzik", "Cat", "2", "images/image.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

###################################UPDATE##########################################

def test_successful_update_self_pet_info(name='Tuzik1', animal_type='Cat', age=2):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

###################################NEGATIVE##########################################
#####################################GET#############################################


def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result

def test_get_all_pets_with_invalid_key(filter=""):
    _, auth_key = pf.get_api_key(invalid_email, invalid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0

def test_get_all_my_pets_with_invalid_key(filter="my_pets"):
    _, auth_key = pf.get_api_key(invalid_email, invalid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0

###################################NEGATIVE##########################################
###################################POST##############################################

def test_simple_add_new_pet_with_invalid_data(name="Tuzik", animal_type="Cat",age="a"):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_simple_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_with_ico(name="Tuzik", animal_type="Cat",age="2", pet_photo="images/ico.ico"):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_ico(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

###################################NEGATIVE##########################################
###################################DELETE############################################

def test_successful_delete_foreign_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "")
    pet_id = pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "")
    assert status == 200
    assert pet_id not in my_pets.values()

###################################NEGATIVE##########################################
###################################UPDATE############################################

def test_successful_update_self_pet_info(name='Tuzik1', animal_type='Cat', age=2):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "")
    if len(pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no pets")