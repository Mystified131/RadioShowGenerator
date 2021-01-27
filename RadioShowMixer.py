#This code imports the necessary modules.

import random
import os
from pydub import AudioSegment
import datetime

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

outfile = open('AutoPlayListBeats.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\RadioShowGenerator'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "newsamplebeat" in str(filepath) :
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()

outfile = open('AutoPlayListDrones.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\RadioShowGenerator'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "newsampledrone" in str(filepath):
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()


outfile = open('AutoPlayListPepper.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\RadioShowGenerator'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "newsamplepepper" in str(filepath):
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()


outfile = open('AutoPlayListGit.m3u', "w")

for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\RadioShowGenerator'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg")) and "guitar" in str(filepath)  and "newsound" not in str(filepath):
            cline = str(os.sep + file)
            bline = cline[1:]
            outfile.write(bline + '\n')

outfile.close()

infile = open("AutoPlayListBeats.m3u", "r")

contentbeats = []

plist = infile.readline()
while plist:
    contentbeats.append(plist)
    plist = infile.readline()
infile.close()

infile = open("AutoPlayListDrones.m3u", "r")

contentdrones = []

plist = infile.readline()
while plist:
    contentdrones.append(plist)
    plist = infile.readline()
infile.close()

infile = open("AutoPlayListPepper.m3u", "r")

contentpepper = []

plist = infile.readline()
while plist:
    contentpepper.append(plist)
    plist = infile.readline()
infile.close()

infile = open("AutoPlayListGit.m3u", "r")

contentgit = []

plist = infile.readline()
while plist:
    contentgit.append(plist)
    plist = infile.readline()
infile.close()

trtot = 18

suctot = 0

plst = []

tlst = []

for ctr in range(700):

    try:

        atracknum1 = random.randrange(0,len(contentbeats))
        atrack1 = contentbeats[atracknum1].strip()
        atracknum2 = random.randrange(0,len(contentgit))
        atrack2 = contentgit[atracknum2].strip()
        atracknum3 = random.randrange(0,len(contentdrones))
        atrack3 = contentdrones[atracknum3].strip()
        atracknum4 = random.randrange(0,len(contentdrones))
        atrack4 = contentdrones[atracknum4].strip()
        atracknum5 = random.randrange(0,len(contentdrones))
        atrack5 = contentdrones[atracknum5].strip()
        atracknum6 = random.randrange(0,len(contentdrones))
        atrack6 = contentdrones[atracknum6].strip()
        atracknum7 = random.randrange(0,len(contentdrones))
        atrack7 = contentdrones[atracknum7].strip()
        atracknum8 = random.randrange(0,len(contentpepper))
        atrack8 = contentpepper[atracknum8].strip()
        atracknum9 = random.randrange(0,len(contentpepper))
        atrack9 = contentpepper[atracknum9].strip()
        atracknum10 = random.randrange(0,len(contentpepper))
        atrack10 = contentpepper[atracknum10].strip()
        atracknum11 = random.randrange(0,len(contentpepper))
        atrack11 = contentpepper[atracknum11].strip()
        atracknum12 = random.randrange(0,len(contentpepper))
        atrack12 = contentpepper[atracknum12].strip()
        atracknum13 = random.randrange(0,len(contentpepper))
        atrack13 = contentpepper[atracknum13].strip()
        atracknum14 = random.randrange(0,len(contentpepper))
        atrack14 = contentpepper[atracknum14].strip()
        atracknum15 = random.randrange(0,len(contentpepper))
        atrack15 = contentpepper[atracknum15].strip()
        atracknum16 = random.randrange(0,len(contentpepper))

        print("")

        print("Layering tracks for track: ", (suctot + 1))


        newAudio1 = AudioSegment.from_wav(atrack2)       
        totlen = len(newAudio1)

        newAudio2 = AudioSegment.from_wav(atrack3) 
        l2 = len(newAudio2)
        rep = int(totlen / l2)

        newAudiox = newAudio2*rep

        newAudiow2 = newAudio1.overlay(newAudiox)

        newAudio3 = AudioSegment.from_wav(atrack4) 
        l2 = len(newAudio3)
        rep = int(totlen / l2)

        newAudiox = newAudio3*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio4 = AudioSegment.from_wav(atrack5) 
        l2 = len(newAudio4)
        rep = int(totlen / l2)

        newAudiox = newAudio4*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio5 = AudioSegment.from_wav(atrack6) 
        l2 = len(newAudio5)
        rep = int(totlen / l2)

        newAudiox = newAudio5*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio6 = AudioSegment.from_wav(atrack7) 
        l2 = len(newAudio6)
        rep = int(totlen / l2)

        newAudiox = newAudio6*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio7 = AudioSegment.from_wav(atrack8) 
        l2 = len(newAudio7)
        rep = int(totlen / l2)

        newAudiox = newAudio7*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio8 = AudioSegment.from_wav(atrack9) 
        l2 = len(newAudio8)
        rep = int(totlen / l2)

        newAudiox = newAudio8*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio9 = AudioSegment.from_wav(atrack10) 
        l2 = len(newAudio9)
        rep = int(totlen / l2)

        newAudiox = newAudio9*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio10 = AudioSegment.from_wav(atrack11) 
        l2 = len(newAudio10)
        rep = int(totlen / l2)

        newAudiox = newAudio10*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio11 = AudioSegment.from_wav(atrack12) 
        l2 = len(newAudio11)
        rep = int(totlen / l2)

        newAudiox = newAudio11*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudio12 = AudioSegment.from_wav(atrack13) 
        l2 = len(newAudio12)
        rep = int(totlen / l2)

        newAudiox = newAudio12*rep

        newAudiow3 = newAudiow2.overlay(newAudiox)

        newAudio13 = AudioSegment.from_wav(atrack14) 
        l2 = len(newAudio13)
        rep = int(totlen / l2)

        newAudiox = newAudio13*rep

        newAudiow1 = newAudiow3.overlay(newAudiox)

        newAudio14 = AudioSegment.from_wav(atrack15) 
        l2 = len(newAudio14)
        rep = int(totlen / l2)

        newAudiox = newAudio14*rep

        newAudiow2 = newAudiow1.overlay(newAudiox)

        newAudioamb1 = newAudiow2.fade_in(200)
        newAudioamb2 = newAudioamb1.fade_out(200)

        newAudioamb2 = newAudioamb2 * 8

        newAudiobeat = AudioSegment.from_wav(atrack1) 

        if len(newAudiobeat) >= len(newAudioamb2):

            newAudionear = newAudioamb2.overlay(newAudiobeat)
        
        if len(newAudiobeat) < len(newAudioamb2):

            newAudionear = newAudiobeat.overlay(newAudioamb2)

        newAudionear = newAudionear.fade_in(5000)
        newAudionear = newAudionear.fade_out(15000)

        oufil = "C:\\Users\\mysti\\Desktop\\AutoProd\\Radio\\Track" + tim + "." + str(suctot) + ".wav"
        newAudionear.export(oufil, format="wav")

        plst.append(oufil)

        trnm = "Track" + tim + "." + str(suctot)
        tlst.append(trnm)

        suctot += 1

        if suctot == trtot:
            break

    except:

        print("")

        print("Error during render. File not created.")

ounam = "C:\\Users\\mysti\\Desktop\\AutoProd\\Radio\\RadioShowPlaylist_" + tim + ".m3u"

outfile = open(ounam, "w")

for elem in plst:
     outfile.write(elem + '\n')

outfile.close()

ounm = "C:\\Users\\mysti\\Desktop\\AutoProd\\Radio\\RadioShowTracklist_" + tim + ".txt"

onm = "RadioShowTracklist_" + tim

outfile = open(ounm, "w")

outfile.write(onm + '\n')

outfile.write('\n')

for elem in tlst:
     outfile.write(elem + '\n')

outfile.close()

print("")

print("Show, playlist and tracklist in remote folder: C:\\Users\\mysti\\Desktop\\AutoProd\\Radio\\")

print("")

## THE GHOST OF THE SHADOW ##
