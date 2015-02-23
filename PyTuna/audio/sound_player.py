from winsound import PlaySound
import winsound
import os
from os import path


class SoundPlayer(object):

    def play_sound(self, filePath):
        #if path.exists(""):
            p = path.realpath(r"resources\Guitar_A.wav") 
            r = path.relpath(r"resources\Guitar_A")
            winsound.PlaySound('%s.wav' % r"resources\Guitar_A.wav", winsound.SND_FILENAME)
            PlaySound(p, 1)
        



