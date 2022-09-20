import unittest
import unittest.mock
from parameterized import parameterized

from main import check_document_existance, get_doc_owner_name, \
    get_all_doc_owners_names, remove_doc_from_shelf, add_new_shelf, \
    append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, \
    show_document_info, show_all_docs_info, add_new_doc, documents


class TestFunction(unittest.TestCase):

    @parameterized.expand(['2207 876234', '11-2', '10006'])
    def test_check_document_existance(self, number):
        result = check_document_existance(number)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main

    def test_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input', return_value='2207 876234'):
            etalon = 'Василий Гупкин'
            result = get_doc_owner_name()
            self.assertEqual(etalon, result)


    def test_get_all_doc_owners_names(self):
        etalon = {'Василий Гупкин', 'Аристарх Павлов', 'Геннадий Покемонов'}
        result = get_all_doc_owners_names()
        self.assertEqual(etalon, result)

    def test_remove_doc_from_shelf(self):
        doc_number = '10006'
        etalon = remove_doc_from_shelf(doc_number)
        self.assertNotIn(doc_number, etalon)

    def test_add_new_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='4'):
            result = add_new_shelf(shelf_number='')
            etalon = '4', True
            self.assertEqual(result, etalon)

    def test_add_new_shelf_2(self):
        with unittest.mock.patch('builtins.input', return_value='3'):
            result = add_new_shelf(shelf_number='')
            etalon = '3', False
            self.assertEqual(result, etalon)

    def test_append_doc_to_shelf(self):
        result = append_doc_to_shelf('11-2', '1')
        doc_number = '11-2'
        self.assertIn(doc_number, result)

    def test_delete_doc(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            result = delete_doc()
            etalon = '11-2', True
            self.assertEqual(result, etalon)

    def test_get_doc_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            result = get_doc_shelf()
            etalon = '1'
            self.assertEqual(result, etalon)

    def test_move_doc_to_shelf(self):
        with unittest.mock.patch('builtins.input',
                                 side_effect=['5455 028765', '3']):
            result = move_doc_to_shelf()
            etalon = '5455 028765', '3'
            self.assertEqual(etalon, result)

    def test_show_document_info(self):
        result = show_document_info(documents[0])
        etalon = "passport", "2207 876234", "Василий Гупкин"
        self.assertEqual(etalon, result)

    def test_show_all_docs_info(self):
        result = show_all_docs_info()
        etalon = [('passport', '2207 876234', 'Василий Гупкин'),
                  ('invoice', '11-2', 'Геннадий Покемонов'),
                  ('insurance', '10006', 'Аристарх Павлов')]
        self.assertEqual(etalon, result)

    def test_add_new_doc(self):
        with unittest.mock.patch('builtins.input',
                                 side_effect=['111-1',
                                              'driver_license',
                                              'Федор Лунтиков', '3']):
            result = add_new_doc()
            etalon = {'type': 'driver_license',
                      'number': '111-1',
                      'name': 'Федор Лунтиков'}, '3'
            self.assertEqual(result, etalon)
