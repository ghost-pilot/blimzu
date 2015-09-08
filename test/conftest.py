import pytest
import os

################################################################################
# Globals
################################################################################
root_dir = os.path.abspath(os.path.dirname(__file__))
__author__ = 'mantis'

illegal_files = [os.path.join(root_dir, '__test/.DS_Store'),
                 os.path.join(root_dir, '__test/__test_album/.DS_Store'),
                 os.path.join(root_dir, '__test/__test_album2/00-dj_craze-bully_breaks_2-vinyl-front_cover-2003-chr.jpg'),
                 os.path.join(root_dir, '__test/__test_album2/fafsaconfirm09.rtf'),
                 os.path.join(root_dir, '__test/__test_album2/06 Fireball (feat. The Cataracs).m4v'),
                 os.path.join(root_dir, "__test/__test_album2/DJ's_to_Peep.rtf"),
                 os.path.join(root_dir, '__test/__test_album2/JD Keisers resume.doc'),
                 os.path.join(root_dir, '__test/__test_album3/Neverwinter Grimoire v3.0.pdf'),
                 os.path.join(root_dir, '__test/__test_album3/P90X.txt'),
                 os.path.join(root_dir, '__test/__test_album3/photo 1.JPG'),
                 os.path.join(root_dir, '__test/__test_album3/Picture 11.png'),
                 os.path.join(root_dir, '__test/__test_album3/vMac Prefs')]

legal_files = [os.path.join(root_dir, '__test/__test_album/01 Joker feat. Jessie Ware - The Vision (Breathe In).mp3'),
               os.path.join(root_dir, '__test/__test_album/Jacobs Ladder.wav'),
               os.path.join(root_dir, '__test/__test_album/01 Poison.m4a'),
               os.path.join(root_dir, '__test/__test_album/2 With A Little Help From My Friends.aif'),
               os.path.join(root_dir, '__test/__test_album/Ride On mix.sd2')]

dup_files = [os.path.join(root_dir, '__test/__test_album/01 Joker feat. Jessie Ware - The Vision (Breathe In) 2.mp3'),
             os.path.join(root_dir, '__test/__test_album/Jacobs Ladder 2.wav'),
             os.path.join(root_dir, '__test/__test_album/01 Poison 2.m4a'),
             os.path.join(root_dir, '__test/__test_album/2 With A Little Help From My Friends 2.aif'),
             os.path.join(root_dir, '__test/__test_album/Ride On mix 2.sd2')]


################################################################################
# Fixtures
################################################################################
@pytest.fixture(params=illegal_files, ids=illegal_files)
def illegal_file(request):
    return request.param

@pytest.fixture(params=legal_files, ids=legal_files)
def legal_file(request):
    return request.param

@pytest.fixture(params=dup_files, ids=dup_files)
def dup_file(request):
    return request.param

