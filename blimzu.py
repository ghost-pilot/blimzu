import blimzu_utils as utils
import xml.sax.handler
import os
import getpass
import shutil
import time
import sys
from stat import *

################################################################################
# Globals
################################################################################
__author__ = 'ghost_pilot'
root_dir = os.path.abspath(os.path.dirname(__file__))
user = getpass.getuser()
dup_dir = os.path.join(root_dir, 'duplicates/')
itunes_dir = os.path.join('/Users/', user, 'Music/iTunes/')
xml_name = 'iTunes Music Library.xml'
itunes_xml = itunes_dir + xml_name
formats = ['mp3', 'aif', 'wav', 'sd2', 'm4a']


################################################################################
# Routines
################################################################################
def setup_handler():
    parser = xml.sax.make_parser()
    handler = utils.ITunesHandler()
    parser.setContentHandler(handler)
    parser.parse(itunes_xml)
    return handler


def get_music_dict(music_dir):
    """Walks through iTunes Music directory on hard disk and returns a dict where
    Key='full/path/to/song/file' and value={'filename':x, 'file_dir':y, 'file_size':z}"""
    music_dict = {}
    song_dict = {}
    for (dirpath, dirnames, filenames) in os.walk(music_dir):
        for filename in filenames:
            if filename.split('.')[-1] in formats:
                try:
                    song_dict['filename'] = filename
                    song_dict['file_dir'] = dirpath
                    song_dict['file_size'] = os.stat(os.path.join(dirpath, filename))[ST_SIZE]
                    music_dict[os.path.join(dirpath, filename)] = song_dict
                    song_dict = {}
                except OSError, e:
                    print "Error:", e
    return music_dict


def make_dup_dir():
    """Creates Users/user/iTunes/duplicates if the folder does not already exist"""
    if not os.path.exists(dup_dir):
        print "Creating:", dup_dir, "\n"
        os.makedirs(dup_dir)
    elif os.path.exists(dup_dir):
        pass
    else:
        print "Error: Could not create:", dup_dir, "\n"
    return os.path.exists(dup_dir)


def remove_basic_dup_files(dup_files, music_dict):
    """Parses dup_files list and moves each dup_file to Users/user/iTunes/duplicates.
    If a duplicate item exists in the list, shutil.move will throw IOError and it
    will pass on that item"""
    total_dupes = 0
    total_mbs = 0
    yes_answers = ['y', 'ye', 'yes', 'Y', 'YE', 'YES']
    for dup_file_pair in dup_files:
        orig_file = dup_file_pair[0]
        dup_file = dup_file_pair[1]
        dest_file = os.path.join(dup_dir, dup_file.split(os.sep)[-1])
        try:
            print "\n----BASIC DUPLICATE FILE FOUND----"
            print "Original File  :", orig_file
            print "Duplicate File :", dup_file
            print "Will Move To   :", dest_file, "\n"
            if 'test_blimzu.py' in sys.argv:
                prompt = 'y'
            else:
                prompt = raw_input("*WARNING* Are you sure you want to move this file? (Y/N) : ")
            if prompt in yes_answers:
                try:
                    shutil.move(dup_file, dest_file)
                    print music_dict[dup_file]['filename'], "moved to:", dup_dir
                    total_dupes += 1
                    total_mbs += music_dict[dup_file]['file_size']/1000000
                except IOError, e:
                    print "Error moving to:", dest_file, e
            else:
                print music_dict[dup_file]['filename'], "NOT moved..."
        except IOError, e:
            print "Error moving :", dup_file
            print e
    return total_dupes, total_mbs


def find_basic_dup_files(music_dict):
    """Parses music_dict to locate files that have identical size, if the size matches,
    and file 1's name is in file 2's name or vise versa, the pair of files are added to
    a list where each item is [orig_file, dup_file]. Finally that list is returned"""
    dup_files = []
    for key, value in music_dict.iteritems():
        for key2, value2 in music_dict.iteritems():
            if value['file_size'] == value2['file_size']:
                if not key == key2:
                    file_name_1 = music_dict[key]['filename'].rsplit('.', 1)[0]
                    file_name_2 = music_dict[key2]['filename'].rsplit('.', 1)[0]
                    if file_name_1 in file_name_2 or file_name_2 in file_name_1:
                        orig_file = max(key, key2)
                        dup_file = min(key, key2)
                        dup_files.append([orig_file, dup_file])
    return list(set(tuple(i) for i in dup_files))


def print_summary(q_basic_dups_removed, total_mbs):
    total_mbs = ''.join(['[', total_mbs, ' MBs', ']'])
    print "\n-------------SUMMARY--------------"
    print "Basic duplicate files moved:", q_basic_dups_removed, total_mbs
    print "----------------------------------\n"


################################################################################
# Main
################################################################################
def main():
    basic_dups_removed = 0
    total_basic_mbs = 0
    final_basic_dups_removed = 0
    final_basic_total_mbs =0

    if len(sys.argv) > 1:
        print "Begin..."
        start_time = time.time()
        search_dirs = sys.argv[1:]
        for search_dir in search_dirs:
            if os.path.exists(search_dir):
                print "Searching:", search_dir, "..."
                if make_dup_dir():
                    music_dict = get_music_dict(search_dir)
                    dup_files = find_basic_dup_files(music_dict)
                    basic_dups_removed, total_basic_mbs = remove_basic_dup_files(dup_files, music_dict)
            else:
                print('%s is not a valid path, please verify' % search_dir)
            final_basic_dups_removed += basic_dups_removed
            final_basic_total_mbs += total_basic_mbs
        print_summary(str(final_basic_dups_removed), str(final_basic_total_mbs))
        print "...Done,", "operation took:", str(time.time() - start_time), "seconds\n"
    else:
        print('Usage: python blimzu.py dir -or- python blimzu.py dir1 dir2 dir3 ...')


if __name__ == '__main__':
    main()
