import Kepler.actions as actions
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
            "type_de_language": "famillier"
        }
    }

    actions.bonjour(request)

    