def fusionner_dictionnaire(dict1, dict2, func):
    return { k: func(dict1[k], dict2[k]) if k in dict1 and k in dict2 else dict1.get(k, dict2.get(k)) for k in dict1.keys() | dict2.keys() }