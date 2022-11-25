import json

data = open('data.json').read()
users = json.loads(data)



def oldest_user(users: list[dict]) -> dict:
    '''returns the oldest user in the list 'users' given as an argument. (you may use max, labmda)
    
    Args:
        users (list): list of users
        
    Returns:
        dict: the oldest user
    '''


def youngest_user(users: list[dict]) -> dict:
    '''returns the youngest user in the list 'users' given as an argument. (you may use min, labmda)
    
    Args:
        users (list): list of users
        
    Returns:
        dict: the youngest user
    '''
