from operator import itemgetter


class OS:
    def __init__(self, id, name, bit, interface, computer_id):
        self.id = id
        self.name = name
        self.bit = bit
        self.interface = interface
        self.computer_id = computer_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class OSComputer:
    def __init__(self, computer_id, os_id):
        self.computer_id = computer_id
        self.os_id = os_id


computers = [
    Computer(1, 'Vasya1'),
    Computer(2, 'Anton-385-WH'),
    Computer(3, 'VladVlad123'),
    Computer(4, 'MoiComputer'),
    Computer(5, 'Netac3405'),
    Computer(6, 'JORDAN404-404')
]

OSs = [
    OS(1, 'Windows10', 64, 'Graphic', 2),
    OS(2, 'MacOS', 32, 'Graphic', 2),
    OS(3, 'Linux', 64, 'Graphic', 4),
    OS(4, 'DOS', 16, 'Text', 4),
    OS(5, 'WindowsXP', 32, 'Graphic', 5),
    OS(6, 'UNIX', 64, 'CMD', 4),
    OS(7, 'Windows7', 64, 'Graphic', 6),

]

OSs_computers = [
    OSComputer(2, 1),
    OSComputer(2, 2),
    OSComputer(4, 3),
    OSComputer(4, 4),
    OSComputer(5, 5),
    OSComputer(4, 6),
    OSComputer(6, 7),

    OSComputer(3, 1),
    OSComputer(3, 2),
    OSComputer(3, 3),
    OSComputer(1, 4),
    OSComputer(1, 5),
    OSComputer(1, 6),
    OSComputer(1, 7)
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(o.name, o.bit, o.interface, c.name)
                   for c in computers
                   for o in OSs
                   if o.computer_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, osc.computer_id, osc.os_id)
                         for c in computers
                         for osc in OSs_computers
                         if c.id == osc.computer_id]

    many_to_many = [(o.name, o.bit, o.interface, c_name)
                    for c_name, c_id, os_id in many_to_many_temp
                    for o in OSs if o.id == os_id]

    print('Задание №1')
    print(
        "Выведите список всех связанных операционных систем и компьютеров, отсортированный по операционным системам, сортировка по компьютерам произвольная.")
    first_task = sorted(one_to_many, key=itemgetter(0))
    print(first_task)

    print('\nЗадание №2')
    print(
        "Выведите список компьютеров с количеством установленных операционных систем на каждом компьютере, отсортированный по количеству операционных систем.")
    second_task = []

    for c in computers:
        c_data = {}
        c_oss = list(filter(lambda i: i[3] == c.name, one_to_many))
        c_data["Name"] = c.name
        c_data["Number of OSs"] = len(c_oss)
        second_task.append(c_data)

    second_task = sorted(second_task, key=itemgetter("Number of OSs"), reverse=True)
    for i in second_task:
        print(i)

    print('\nЗадание №3')
    print("Выведите список всех 32-битных операционных систем, и названия компьютеров, на которых они установлены.")
    third_task = []

    for o in OSs:
        o_data = {}
        if o.bit == 32:
            o_data["Name"] = o.name
            os_comp = [mtmt[0] for mtmt in many_to_many_temp if mtmt[1] == o.computer_id]
            o_data["Computer"] = list(set(os_comp))
            o_data["bit"] = 32
            third_task.append(o_data)

    for i in third_task:
        print(i, end="\n")


if __name__ == '__main__':
    main()