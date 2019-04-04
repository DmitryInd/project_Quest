import os
import json_worker
from graph import ListGraph
import calculator
import codecs


def get_str_inventory(inventory):
    """For output inventory"""
    s = ""
    for i in inventory['Visible'].items():
        if i[1] != 0:
            s += '\n' + str(i[0]) + ' - ' + str(int(i[1])) +\
                 ("%.2g" % (i[1] - int(i[1])))[1:]

    return s


def changer_names(expression, inventory):
    """Replaces names with numbers"""
    i = 0
    s = ""
    while i < len(expression):
        if (expression[i] == "\"" and s == "") or (s != ""
                                                   and expression[i] != "\""):
            s += expression[i]
        elif expression[i] == "\"" and s != "":
            s = s[1:]
            k = inventory["Visible"].get(s, None)
            obj = inventory["Visible"]
            if k is None:
                k = inventory["Not visible"].get(s, None)
                obj = inventory["Not visible"]
                if k is None:
                    k = inventory["Always visible"].get(s, None)
                    obj = inventory["Always visible"]
                    if k is None:
                        raise Exception(s + 'does not exist')
            obj = obj[s]
            expression = expression[: i - len(s) - 1] + str(obj) + \
                expression[i + 1:]
            i -= len(s) + 1
            s = ""
        i += 1
    return expression


def perform_condition(condition, inventory):
    """Processing of condition"""
    condition = str(condition)
    if condition == 'True':
        return True
    try:
        while True:
            a = condition.index('{')
            b = condition.index('}')
            part = changer_names(condition[a + 1: b], inventory)
            part = calculator.calculate(part)
            condition = condition[: a] + part + condition[b + 1:]
    except Exception:
        return calculator.truth(condition)


def take_gifts(to, gifts, inventory_name, inventory):
    """For calculate collected objects"""
    for i in gifts.items():
        k = inventory["Visible"].get(i[0], None)
        case = inventory["Visible"]
        if k is None:
            k = inventory["Not visible"].get(i[0], None)
            case = inventory["Not visible"]
            if k is None:
                k = inventory["Always visible"].get(i[0], None)
                case = inventory["Always visible"]
                if k is None:
                    raise Exception(i[0] + 'does not exist')
        if str(type(i[1])) == "<class 'str'>":
            right_copy = changer_names(i[1], inventory)
            case[i[0]] = calculator.polka(right_copy)
        else:
            case[i[0]] += i[1]
    json_worker.transfer(to, inventory_name, inventory)


def launch_story(story_graph, inventory_name, inventory):
    """Launch game with selected plot"""
    while True:
        print(''.join(['+' for i in range(80)]))
        place = inventory['Not visible']['Now']
        inf = story_graph.get_information(place)
        if inf["name"][:5] == '@end@':
            print(inf['name'][5:] + '\n')
            print(inf['text'])
            os.remove(inventory_name)
            break
        print(inf['name'] + '\n')
        print(inf['text'])
        choices = story_graph.get_next_vertices(place)
        k = 0
        i = 0
        while i < len(choices):
            if perform_condition(choices[i]['term'], inventory):
                k += 1
                print(str(k) + ') ' + choices[i]['text'])
                i += 1
            else:
                choices.pop(i)

        s = ""
        for i in inventory['Always visible'].items():
            s += str(i[0]) + ' - ' + str(int(i[1])) +\
                 ("%.2g" % (i[1] - int(i[1])))[1:] + " "
        s += "(Открыть весь инвентарь - inventory)"
        print(s)
        answer = input()
        ex = False
        while True:
            if answer.isdigit():
                if (int(answer) <= len(choices)) and (int(answer) > 0):
                    break
            if answer.lower() == 'inventory':
                print("Инвентарь:" + get_str_inventory(inventory))
            elif answer.lower() == 'exit':
                ex = True
                break
            else:
                print("Некорректный ввод")
            answer = input()
        if ex:
            break
        answer = int(answer) - 1
        take_gifts(choices[answer]["to"], choices[answer]["gifts"],
                   inventory_name, inventory)

    print(''.join(['+' for i in range(80)]))
    print("Игровая сессия закончена")


def selected_story(name_story):
    """Load selected plot"""
    fairy = codecs.open(name_story, 'r', 'utf-8')
    n = int(fairy.readline())
    my_graph = ListGraph(n)
    json_worker.set_up(my_graph, fairy)
    try:
        i = 0
        while True:
            json_worker.fill_up(i, fairy, my_graph)
            i += 1
    except EOFError as e:
        if str(e) != '':
            Exception('File is corrupted\n' + str(e))
    fairy.close()
    inventory_info = json_worker.open_inventory(name_story)
    print("Сюжет загрузился")
    launch_story(my_graph, inventory_info[0], inventory_info[1])


def my_story():
    """This window tries to open your story"""
    print("Введите путь до файла:")
    answer = ""
    while True:
        if answer != "":
            if answer == "exit":
                print(''.join(['+' for i in range(80)]))
                return
            print("(Выход - exit)")
            try:
                selected_story(answer)
                return
            except IOError:
                print("Файл с сюжетом или с инвентарём не существует")
        answer = input()


if __name__ == '__main__':
    try:
        while True:
            print("Главный экран")
            print("Выберите сюжет (выйти - exit):")
            folder = os.listdir('Information')
            variants = []
            h = 0
            while h < len(folder):
                m_inventory_name = folder[h][: -4] + '_Inventory.json'
                try:
                    m = folder.index(m_inventory_name)
                    variants.append(folder[h])
                    if m > h:
                        folder.pop(h)
                        folder.pop(m - 1)
                    else:
                        folder.pop(m)
                        folder.pop(h - 1)
                except Exception:
                    h += 1

            h = 0
            for h in range(len(variants)):
                print(str(h + 1) + ') ' + variants[h][: -4])
            print(str(h + 2) + ') ' + 'Свой')

            f_answer = input()
            while True:
                if f_answer.isdigit():
                    if (int(f_answer) <= (len(variants) + 1))\
                            and (int(f_answer) > 0):
                        break
                if f_answer.lower() == "exit":
                    raise(Exception("Выход"))
                else:
                    print("Некорректный ввод")
                f_answer = input()
            if int(f_answer) <= len(variants):
                x = os.path.join('Information', variants[int(f_answer) - 1])
                selected_story(x)
            else:
                my_story()
    except Exception as f:
        if str(f) != "Выход":
            raise f
