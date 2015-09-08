import os
import getpass
import xml.sax.handler

################################################################################
# Globals
################################################################################
__author__ = 'mantis'


################################################################################
# Class: ITunesHandler
################################################################################
class ITunesHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.parsing_tag = False
        self.tag = ''
        self.value = ''
        self.tracks = []
        self.track = None

    def startElement(self, name, attributes):
        if name == 'key':
            self.parsing_tag = True

    def characters(self, data):
        if self.parsing_tag:
            self.tag = data
            self.value = ''
        else:
            # could be multiple lines, so append data.
            self.value = self.value + data

    def endElement(self,name):
        if name == 'key':
            self.parsing_tag = False
        else:
            if self.tag == 'Track ID':
                # start of a new track, so a new object
                # is needed.
                self.track = Track()
            elif self.tag == 'Size' and self.track:
                self.track.size = self.value
            elif self.tag == 'Name' and self.track:
                self.track.track = self.value
            elif self.tag == 'Artist' and self.track:
                self.track.artist = self.value
            elif self.tag == 'Album' and self.track:
                self.track.album = self.value
                # assume this is all the data we need
                # so append the track object to our list
                # and reset our track object to None.
                self.tracks.append(self.track)
                self.track = None


################################################################################
# Class: Track
################################################################################
class Track:
    def __init__(self):
        self.track = ''
        self.artist = ''
        self.album = ''
        self.size = ''
    def __str__(self):
        return "Track = %s\nArtist = %s\nAlbum = %s\nSize = %s\n" % (self.track,self.artist, self.album, self.size)


