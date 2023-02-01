en_fr_animals = {"cat": "chat",
                 "dog": "chien",
                 "horse": "cheval"}

print(en_fr_animals)

en_fr_animals["cat"] = "chatte" # assign a new value
en_fr_animals["swan"] = "cygne" # add a new key-value pair
en_fr_animals.update({"horse": "jument"}) # assign a new value
en_fr_animals.update({"duck": "canard"}) # add a new key-value pair
del en_fr_animals["dog"] # remove a key-value pair

print(en_fr_animals)
"""
{'cat': 'chat', 'dog': 'chien', 'horse': 'cheval'}
{'cat': 'chatte', 'horse': 'jument', 'swan': 'cygne', 'duck': 'canard}
"""
