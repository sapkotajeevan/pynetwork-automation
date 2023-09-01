import json

with open('friends.json','r') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)


json_string = """[
    {
        "Jeevan": [
            23,
            "Kathmandu",
            72026
        ],
        "Jyoti": [
            23,
            "Naikap",
            72027
        ],
        "Dipesh": [
            23,
            "Jarankhu",
            72023
        ]
    },
    {
        "Suju": [
            23,
            "Pepsicola",
            72053
        ],
        "Kailash": [
            23,
            "Banasthali",
            72028
        ]
    }
]"""

obj = json.loads(json_string)
print(type(obj))
print(obj)
