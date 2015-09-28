import pytest
import os

################################################################################
# Globals
################################################################################
root_dir = os.path.abspath(os.path.dirname(__file__))
__author__ = 'mantis'

ds_store = os.path.join(root_dir, '__test/.DS_Store')
dj_craze_jpg = os.path.join(root_dir, '__test/__test_album2/00-dj_craze-bully_breaks_2-vinyl-front_cover-2003-chr.jpg')
fafsa_rtf = os.path.join(root_dir, '__test/__test_album2/fafsaconfirm09.rtf')
fireball_m4v = os.path.join(root_dir, '__test/__test_album2/06 Fireball (feat. The Cataracs).m4v')
djs_to_peep_rtf = os.path.join(root_dir, "__test/__test_album2/DJ's_to_Peep.rtf")
resume_doc = os.path.join(root_dir, '__test/__test_album2/JD Keisers resume.doc')
neverwinter_pdf = os.path.join(root_dir, '__test/__test_album3/Neverwinter Grimoire v3.0.pdf')
p90_txt = os.path.join(root_dir, '__test/__test_album3/P90X.txt')
photo_1_jpg = os.path.join(root_dir, '__test/__test_album3/photo 1.JPG')
picture_11_png = os.path.join(root_dir, '__test/__test_album3/Picture 11.png')
vmac_prefs = os.path.join(root_dir, '__test/__test_album3/vMac Prefs')

joker_mp3 = os.path.join(root_dir, '__test/__test_album/01 Joker feat. Jessie Ware - The Vision (Breathe In).mp3')
jacobs_ladder_wav = os.path.join(root_dir, '__test/__test_album/Jacobs Ladder.wav')
poison_m4a = os.path.join(root_dir, '__test/__test_album/01 Poison.m4a')
my_friends_aif = os.path.join(root_dir, '__test/__test_album/2 With A Little Help From My Friends.aif')
ride_on_sd2 = os.path.join(root_dir, '__test/__test_album/Ride On mix.sd2')

jacobs_ladder_aif = os.path.join(root_dir, '__test/__test_album4/Jacobs Ladder.aif')
jacobs_ladder_mp3 = os.path.join(root_dir, '__test/__test_album4/Jacobs Ladder.mp3')
my_friends_wav = os.path.join(root_dir, '__test/__test_album4/2 With A Little Help From My Friends.wav')
my_friends_mp3 = os.path.join(root_dir, '__test/__test_album4/2 With A Little Help From My Friends.mp3')

illegal_files = [ds_store, dj_craze_jpg, fafsa_rtf, fireball_m4v, djs_to_peep_rtf, resume_doc,
                 neverwinter_pdf, p90_txt, photo_1_jpg, picture_11_png, vmac_prefs]

legal_files = [joker_mp3, jacobs_ladder_wav, poison_m4a, my_friends_aif, ride_on_sd2]

dup_files = [os.path.join(root_dir, '__test/__test_album/01 Joker feat. Jessie Ware - The Vision (Breathe In) 2.mp3'),
             os.path.join(root_dir, '__test/__test_album/Jacobs Ladder 2.wav'),
             os.path.join(root_dir, '__test/__test_album/01 Poison 2.m4a'),
             os.path.join(root_dir, '__test/__test_album/2 With A Little Help From My Friends 2.aif'),
             os.path.join(root_dir, '__test/__test_album/Ride On mix 2.sd2')]

files_with_sizes = ([joker_mp3, 276], [jacobs_ladder_wav, 376], [poison_m4a, 262], [my_friends_aif, 195])
same_song_diff_types = ([jacobs_ladder_wav, jacobs_ladder_aif], [jacobs_ladder_wav, jacobs_ladder_mp3],
                        [my_friends_aif, my_friends_wav], [my_friends_aif, my_friends_mp3])


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


@pytest.fixture(params=files_with_sizes)
def files_with_size(request):
    return request.param


@pytest.fixture(params=same_song_diff_types)
def same_song_diff_type(request):
    return request.param

