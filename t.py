array = [4, [5, 6], [3, [6]], 5]

def transformer_imprequee(array, cle):
    new_list = []
    for element in array:
        if isinstance(element, list):
            new_list.append( transformer_imprequee(element, cle))
        else:
            new_list.append(cle(element))
    return new_list