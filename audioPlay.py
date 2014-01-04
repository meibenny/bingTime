***
    audioPlay.py  Python script to play .mp3 files in Windows.
    
    Copyright (C) 2012  Joseph Grillo & Benny Mei
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    LICENSE: This is open-source software released under the terms of the
    GPL (http://www.gnu.org/licenses/gpl.html).
    
***

import winsound

def playAudio(fileName):
    return winsound.PlaySound(fileName,winsound.SND_FILENAME)
