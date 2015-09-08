import os
import sys
import pytest
import shutil

root_dir = os.path.abspath(os.path.dirname(__file__))
test_dir = os.path.join(root_dir, '__test/')
sys.path.append(os.path.dirname(root_dir))
import blimzu


################################################################################
# Globals
################################################################################
__author__ = 'mantis'


################################################################################
# Routines
################################################################################
def put_dup_files_back():
    test_dir = os.path.join(root_dir, '__test/__test_album/')
    files = os.listdir(blimzu.dup_dir)
    for f in files:
        if not f.startswith('.'):
            shutil.move(blimzu.dup_dir + f, test_dir + f)


################################################################################
# Tests
################################################################################
def test_get_music_dict_illegal(illegal_file):
    music_dict = blimzu.get_music_dict(test_dir)
    assert illegal_file not in music_dict


def test_get_music_dict_legal(legal_file):
    music_dict = blimzu.get_music_dict(test_dir)
    print music_dict
    assert legal_file in music_dict


def test_find_basic_dup_files_exists(dup_file):
    music_dict = blimzu.get_music_dict(test_dir)
    dup_files = blimzu.find_basic_dup_files(music_dict)
    assert any(e[1] == dup_file for e in dup_files)


def test_find_basic_dup_files_length():
    music_dict = blimzu.get_music_dict(test_dir)
    dup_files = blimzu.find_basic_dup_files(music_dict)
    assert len(dup_files) == 5

def test_remove_basic_dup_files(dup_file):
    music_dict = blimzu.get_music_dict(test_dir)
    dup_files = blimzu.find_basic_dup_files(music_dict)
    blimzu.remove_basic_dup_files(dup_files, music_dict)
    music_dict = blimzu.get_music_dict(test_dir)
    put_dup_files_back()
    assert dup_file not in music_dict


################################################################################
# Main
################################################################################
if __name__ == '__main__':
    pytest.main("-vv")

