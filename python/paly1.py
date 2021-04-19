import json

user = json.loads('{"id": 100, "name":"홍길동"}')

print('username is' + user['name'])
print(f'username is {user["name"]}')

def userinfo(u):
  """[summary]

  Args:
      u ([type]): [description]

  Returns:
      [type]: [description]
  """
  id = u["id"]
  name = u["name"]
  return f'ID is {id}, Name is {name}'


print(userinfo(user))