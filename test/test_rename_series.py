import unittest
from unittest.mock import patch
from src.rename_series import rename_files


class TestSeriesRename(unittest.TestCase):

    def test_rename_files(self):
        name = 'name'
        season = 1
        new_name = [name, season]
        mocked_files = ['test1.mp4', 'test2.mp4', 'test3.mp4']
        renamed_files = ['name - S01 - E01.mp4', 'name - S01 - E02.mp4', 'name - S01 - E03.mp4']

        with patch('src.rename_series.os') as mocked_os:
            mocked_os.listdir.return_value = mocked_files
            mocked_os.path.isdir.return_value = False
            mocked_os.path.splitext.return_value = None, '.mp4'

            returned_files = rename_files(mocked_files, new_name)

            assert renamed_files == returned_files


if __name__ == '__main__':
    unittest.main()
