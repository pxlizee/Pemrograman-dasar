people = {
    "name": "Ikbal",
    "age": 30,
    "is_married": True,
    "children": ["Anna", "Bob"],
    "wives" : ["ara", "riska"],
    "address": [
        {
            "street": "123 Main St",
            "city": "New York",
            "state": "NY"
        },
        {
            "street": "456 Elm St",
            "city": "Los Angeles",
            "state": "CA"
        },
        {
            "street": "789 Oak St",
            "city": "Chicago",
            "state": "IL"
        }
    ]
}

print (people["address"][2]["street"])