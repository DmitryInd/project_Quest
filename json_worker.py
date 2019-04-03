"""
Working with json
"""


import os
import shutil
import json
import codecs


def get_json(file):
    """Take sting in format of json from txt-file"""
    a = file.readline()
    if a == '':
        raise EOFError
    try:
        k = a.index('{')
        a = a[k:]
    except Exception:
        raise EOFError("There is not open parenthesis in {}".format(a))

    s = ""
    i = 1
    while i > 0:
        s += a
        a = file.readline()
        try:
            k = a.index('}')
            i -= 1
        except Exception:
            i = i
        try:
            a.index('{')
            i += 1
        except Exception:
            i = i

    a = a[: k + 1]
    s += a
    return s


def set_up(my_graph, file):
    """Reading edges of graph"""
    s = get_json(file)
    edges = json.loads(s)['Edges']
    for i in edges:
        my_graph.add_choice(i[0], i[1])


def fill_up(num, file, my_graph):
    """Fill up graph by conditions and texts"""
    s = get_json(file)
    context = json.loads(s)

    my_graph.add_information(num, context["name"], context["image"],
                             context["text"])
    for i in range(len(context["choices"])):
        a = context["choices"][i]["condition"]
        b = context["choices"][i]["text"]
        c = context["choices"][i]["gifts"]
        my_graph.add_content(num, i, a, b, c)


def transfer(to, inventory_name, inventory):
    """Update file with inventory"""
    inventory["Not visible"]["Now"] = to
    file_inv = codecs.open(inventory_name, 'w', 'utf-8')
    json.dump(inventory, file_inv, indent="\t", ensure_ascii=False)
    file_inv.close()


def open_inventory(name_story):
    """Load inventory in dictionary"""
    index = 0
    for index in range(len(name_story) - 1, -1, -1):
        if name_story[index] == '\\':
            break
    file = os.listdir(name_story[: index])
    inventory_name = name_story[: -4] + '_Inventory_save.json'
    try:
        file.index(name_story[index + 1: -4] + '_Inventory_save.json')
    except Exception:
        shutil.copyfile(name_story[: -4] + '_Inventory.json', inventory_name)
    inventory = codecs.open(inventory_name, 'r', 'utf-8')
    inv_arr = json.load(inventory)
    inventory.close()
    return [inventory_name, inv_arr]
