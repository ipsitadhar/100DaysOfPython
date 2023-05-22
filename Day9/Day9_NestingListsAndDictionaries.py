#nesting
capital={
    "Germany":"Berlin",
    "France":"Paris",

}

#Nesting a list in the dictionary
travel_log={
    "France":["Paris","Nice"],
    "Germany":["Berlin","Stuttgart"],
              
}

#Nesting a dictionary in a dictionary
travel_log={
    "France":{"cities_visited":["Paris","Nice"],"Cities_pending":"Dijon"},
    "Germany":["Berlin","Stuttgart"],
              
}

#Nesting a dictionary inside a list
travel_log=[
    {
        "country":"France",
        "cities_visited":["Paris","Nice"],
        "Cities_pending":"Dijon",
        "visits":1,
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Stuttgart"],
        "Cities_pending":"Frankfurt",
        "visits":2,
    },
]

#print(travel_log[0]["country"])
for n in travel_log:
    print(n["country"])