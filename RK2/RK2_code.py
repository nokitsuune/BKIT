from operator import itemgetter

class Stud:
    """Студент"""
    def __init__(self, id, fio, scr, grp_id ):
        self.id = id
        self.fio = fio
        self.scr = scr
        self.grp_id = grp_id

class Grp:
    """Группа"""
    def __init__(self, id, name):
            self.id = id
            self.name = name

class StudGrp:
    """ 'Студенты группы' для реализации связи многие-ко-многим"""
    def __init__(self, stud_id, grp_id):
        self.grp_id = grp_id
        self.stud_id = stud_id

# Группы
groups = [
    Grp(1, 'ИУ5-31Б'),
    Grp(2, 'ИУ5-32Б'),
    Grp(3, 'ИУ5-33Б'),
    Grp(4, 'ИУ5-34Б'),
    Grp(5, 'ИУ5-35Б')
]

# Студенты
studs = [
    Stud(1, 'Иванов', 80, 1),
    Stud(2, 'Петрова', 85, 1),
    Stud(3, 'Андреева', 99, 2),
    Stud(4, 'Коваленко', 71, 2),
    Stud(5, 'Бодров', 100, 2),
    Stud(6, 'Степанова', 60, 3),
    Stud(7, 'Платонов', 89, 3),
    Stud(8, 'Сидоров', 90, 3),
    Stud(9, 'Гладких', 67, 3),
    Stud(10, 'Батянов', 100, 4),
    Stud(11, 'Золина', 70, 5)
]

studs_groups = [
    StudGrp(1,1),
    StudGrp(2,1),
    StudGrp(3,2),
    StudGrp(4,2),
    StudGrp(5,2),
    StudGrp(6,3),
    StudGrp(7,3),
    StudGrp(8,3),
    StudGrp(9,3),
    StudGrp(10,4),
    StudGrp(11,5)
]
def b1(one_to_many):

    res1 = sorted(one_to_many, key=itemgetter(0))
    return res1

def b2(one_to_many):
    res2_temp = []
    # Перебираем все группы
    for g in groups:
        # Список студентов группы
        g_studs = list(filter(lambda i: i[2] == g.name, one_to_many))
        if len(g_studs) > 0:
            res2_temp.append((g.name, len(g_studs)))
    # Сортировка по количеству студентов в группе
    res2 = sorted(res2_temp, key=itemgetter(1), reverse=True)
    return res2

def b3(many_to_many):
    res3 = {}
    for s in studs:
        if s.fio.endswith('ов'):
            # Список студентов с фамилией на "ов"
            s_groups = list(filter(lambda i: i[0] == s.fio, many_to_many))
            # Получаем их имена
            s_groups_names = [x[2] for x in s_groups]
            res3[s.fio] = s_groups_names
    return res3

def main():
    # Соединение данных один-ко-многим
    one_to_many = [(s.fio, s.scr, g.name)
        for s in studs
        for g in groups
        if s.grp_id==g.id]
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(g.name, sg.grp_id, sg.stud_id)
        for g in groups
        for sg in studs_groups
        if g.id==sg.grp_id]

    many_to_many = [(s.fio, s.scr, grp_name)
        for grp_name, grp_id, stud_id in many_to_many_temp
        for s in studs if s.id == stud_id]

    print('Задание Б1')
    print(b1(one_to_many))

    print('\nЗадание Б2')

    print(b2(one_to_many))

    print('\nЗадание Б3')

    print(b3(many_to_many))


if __name__ == '__main__':
    main()
