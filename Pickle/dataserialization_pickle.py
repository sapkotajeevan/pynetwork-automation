import pickle

friend1 = {"Jeevan":[23,"Kathmandu",72026],"Jyoti":[23,"Naikap",72027],"Dipesh":[23,"Jarankhu",72023]}
friend2 = {"Suju":[23,"Pepsicola",72053],"Kailash":[23,"Banasthali",72028]}
friends = (friend1,friend2)

##Serialization : Converting Python object into binary

with open('friends.dat','wb') as f:
    pickle.dump(friends,f)


##Deserialization : Converting binary object back to python object

with open('friends.dat','rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)
