import winsound

def playAudio(fileName):
    return winsound.PlaySound(fileName,winsound.SND_FILENAME)
