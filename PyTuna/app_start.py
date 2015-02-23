from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from audio import notes
from gui import console
from audio import sound_player


def main():
    #cons = console.Console()
    sound = sound_player.SoundPlayer()
    sound.play_sound(None)

if __name__ == "__main__":
    main()