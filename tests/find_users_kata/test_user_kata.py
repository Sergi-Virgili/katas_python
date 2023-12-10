from find_users_kata.find_users_kata import find_user_by_id

# TDD => Steps: RED, GREEN, REFACTOR

users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Patricia'},
    ]

def test_return_user_if_exist():
    # GIVEN - ESCENARIO
    
    # WHEN - ACCIÓN => SUT (System Under Test) lo que queremos testear
    user = find_user_by_id(users, 2)

    # THEN - ASSERT => OBJETIVO => Comporabacion de el test (que nos devuelva {'id': 2, 'name': 'Bob'})
    assert user == {'id': 2, 'name': 'Bob'}

def test_raise_an_Exeption_if_not_exist():
    try:
        find_user_by_id(users, 4)
        assert False
    except Exception as e:
        assert str(e) == "User with id: 4 not found"
