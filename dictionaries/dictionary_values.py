# As the dictionary is not able to automatically find a key
# for a given value, the role of the values method is
# rather limited.

en_fr_animals = {"dog": "chien",
                 "cat": "chat",
                 "horse": "cheval"}

for french in en_fr_animals.values():
    print(french)

"""
dog -> chien
cat -> chat
horse -> cheval
"""
