import json

friend1 = {"Jeevan":[23,"Kathmandu",72026],"Jyoti":[23,"Naikap",72027],"Dipesh":[23,"Jarankhu",72023]}
friend2 = {"Suju":[23,"Pepsicola",72053],"Kailash":[23,"Banasthali",72028]}
friends = (friend1,friend2)

with open('friends.json','w') as f:
    json.dump(friends,f,indent=4)

json_string = json.dumps(friends,indent=4)
print(json_string)
