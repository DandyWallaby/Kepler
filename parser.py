import actions
import data_base as database

import random

# Actions -> Décrire quoi en un mot : ACTION

# Parametres -> Détails de l'exécution : QUOI

# Modifiers -> Avec quel particularité l'exécuter : COMMENT

# Reference

def bonjour(tokens):
    request = {
        "parameters" : {
            "demander_comment_sa_va": False
        },
        "modifiers" : {
            "type_de_language": "familier"
        }
    }

    token_amount = 5

    for i in range(token_amount - len(tokens)):
        tokens.append(None)

    cleaned_tokens = tokens.remove('bonjour')
    print(cleaned_tokens)

    match cleaned_tokens:
        case ["comment", "sa", "aller"]:
            request["parameters"]["demander_comment_sa_va"] = True
        case ["kepler", "comment", "sa", "aller"]:
            request["parameters"]["demander_comment_sa_va"] = True
        case ["kepler", "comment", "kepler", "aller"]:
            request["parameters"]["demander_comment_sa_va"] = True
        case ["kepler", "aller", "bien"]:
            request["parameters"]["demander_comment_sa_va"] = True
        case ["comment", "kepler", "aller"]:
            request["parameters"]["demander_comment_sa_va"] = True
        


    actions.bonjour(request)
