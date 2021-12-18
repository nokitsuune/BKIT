import unittest
from main import *

class test_cases(unittest.TestCase):
    def test_b1(self):
        one_to_many = [(s.fio, s.scr, g.name)
                       for s in studs
                       for g in groups
                       if s.grp_id == g.id]



        self.assertEqual(b1(one_to_many), [('Андреева', 99, 'ИУ5-32Б'),
                                           ('Батянов', 100, 'ИУ5-34Б'),
                                           ('Бодров', 100, 'ИУ5-32Б'),
                                           ('Гладких', 67, 'ИУ5-33Б'),
                                           ('Золина', 70, 'ИУ5-35Б'),
                                           ('Иванов', 80, 'ИУ5-31Б'),
                                           ('Коваленко', 71, 'ИУ5-32Б'),
                                           ('Петрова', 85, 'ИУ5-31Б'),
                                           ('Платонов', 89, 'ИУ5-33Б'),
                                           ('Сидоров', 90, 'ИУ5-33Б'),
                                           ('Степанова', 60, 'ИУ5-33Б')])
    def test_b2(self):
        one_to_many = [(s.fio, s.scr, g.name)
                       for s in studs
                       for g in groups
                       if s.grp_id == g.id]
        self.assertEqual(b2(one_to_many), [('ИУ5-33Б', 4),
                                           ('ИУ5-32Б', 3),
                                           ('ИУ5-31Б', 2),
                                           ('ИУ5-34Б', 1),
                                           ('ИУ5-35Б', 1)])

    def test_b3(self):
        many_to_many_temp = [(g.name, sg.grp_id, sg.stud_id)
                             for g in groups
                             for sg in studs_groups
                             if g.id == sg.grp_id]

        many_to_many = [(s.fio, s.scr, grp_name)
                        for grp_name, grp_id, stud_id in many_to_many_temp
                        for s in studs if s.id == stud_id]
        self.assertEqual(b3(many_to_many),{'Иванов': ['ИУ5-31Б'],
                                           'Бодров': ['ИУ5-32Б'],
                                           'Платонов': ['ИУ5-33Б'],
                                           'Сидоров': ['ИУ5-33Б'],
                                           'Батянов': ['ИУ5-34Б']})



if __name__ == '__main__':
    unittest.main()
