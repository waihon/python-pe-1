en_fr_animals = {"dog": "chien", "cat": "chat", "horse": "cheval"}

for key in en_fr_animals.keys():
    print(key, "->", en_fr_animals[key])

print("-" * 15)

for key in sorted(en_fr_animals.keys()):
    print(key, "->", en_fr_animals[key])

"""
dog -> chien
cat -> chat
horse -> cheval
---------------
cat -> chat
dog -> chien
horse -> cheval
"""
