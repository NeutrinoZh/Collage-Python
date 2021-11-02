import os
import simple_db
import pytest

def setup():
     simple_db.create_database()
 
def teardown():
    os.remove("mydatabase.db")

def test_updating_artist():
    simple_db.update_artist('Red', 'Redder')
    actual = simple_db.select_all_albums('Redder')
    expected = [('Until We Have Faces', 'Redder',
                '2/1/2011', 'Essential Records', 'CD')]
    assert expected == actual

def test_artist_does_not_exist():
    result = simple_db.select_all_albums('Redder')
    assert result == []