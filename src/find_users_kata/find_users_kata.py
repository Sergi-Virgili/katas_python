# Escribe una función que reciba una lista de usuarios y un id y devuelva el usuario con ese id HAPPY
# Si no encuentra el usuario, devuelve una excepción con el mensaje "User with id: {id} not found"
# TDD - Test Driven Development

def find_user_by_id(users, id):
    for user in users:
        if user['id'] == id:
            return user