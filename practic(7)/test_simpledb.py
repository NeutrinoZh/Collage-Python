import os
import simple_db
import sqlite3
import unittest

class TestMusicDatabase(unittest.TestCase):
    """
    Тестування музичної бази даних
    """

    def setUp(self):
        simple_db.create_database()
        
    def tearDown(self):
        """
        Видалити базу даних
        """
        os.remove("mydatabase.db")

    def test_updating_artist(self):
        """
        Tests that we can successfully update an artist's name
        """
        simple_db.update_artist('Red', 'Redder')
        actual = simple_db.select_all_albums('Redder')
        expected = [('Until We Have Faces', 'Redder',
                    '2/1/2011', 'Essential Records', 'CD')]
        self.assertListEqual(expected, actual)

    def test_artist_does_not_exist(self):
        """
        Test that an artist does not exist
        """
        result = simple_db.select_all_albums('Redder')
        self.assertFalse(result)