import Kepler.data_base as database
import random

def pick(variable:list):
    return random.choice(variable)

def bonjour(request):
    if request["modifiers"]["type_de_language"] == "famillier":
        salutation = pick(database.salutations_famillieres)
    elif request["modifiers"]["type_de_language"] == "normal":
        salutation = pick(database.salutations_normales)
    elif request["modifiers"]["type_de_language"] == "serieux":
        salutation = pick(database.salutations_serieuses)

    if request["parameters"]["demander_comment_sa_va"] == True:
        print(pick([(salutation + " ! Je vais bien et toi ?"), (salutation + " ! Je vais super, toi comment vas-tu ?")]))
    else:
        print(pick([(salutation + " ! Comment puis-je t'aider ?"), (salutation + " ! Sur quoi à-tu besoin d'aide ?")]))