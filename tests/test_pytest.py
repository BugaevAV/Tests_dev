import mock
import builtins

from ya_disk import create_folder_in_Ya, is_folder_in_Ya, delete_folder


class TestFunction:

    def test_create_folder_in_Ya(self):
        with mock.patch.object(builtins, 'input', lambda _: 'Тестовая папка'):
            assert create_folder_in_Ya() == 201

    def test_folder_already_in_Ya(self):
        with mock.patch.object(builtins, 'input', lambda _: 'Тестовая папка'):
            assert create_folder_in_Ya() == 409

    def test_is_folder_in_Ya(self):
        with mock.patch.object(builtins, 'input', lambda _: 'Тестовая папка'):
            assert is_folder_in_Ya() == 200

    def test_folder_not_in_Ya(self):
        with mock.patch.object(builtins, 'input', lambda _: 'Тестовая папка'):
            delete_folder()
            with mock.patch.object(builtins, 'input', lambda _: 'Тестовая папка'):
                assert is_folder_in_Ya() == 404

