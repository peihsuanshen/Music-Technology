#   python code
#   script_name: Music Technology Project B
#
#   author: Pei-Hsuan Shen
#   description: 8 tracks, 1 min 23 sec long. Sep 2016. 
#

from earsketch import *
from random import *

init()
setTempo(120)

beatTracks = [1, 2, 3]
introTrack = 4
bassTrack = 5
mainTrack = [6, 7]
transTrack = 8

#------------#
# Intro      #
#------------#
fitMedia(Y17_WHOOSH_1, introTrack, 1, 4)

#------------#
# Transition #
#------------#
fitMedia(YG_NEW_HIP_HOP_FX_4, transTrack, 4, 6)
fitMedia(DUBSTEP_DRUMLOOP_PART_017, transTrack, 8, 9)
fitMedia(RD_ROCK_POPRHYTHM_FILL_4, transTrack, 16, 17)
fitMedia(RD_ROCK_POPRHYTHM_FILL_6, transTrack, 20, 21)
fitMedia(YG_NEW_HIP_HOP_FX_4, transTrack, 26, 27)
fitMedia(YG_FUNK_WAH_GUITAR_1, transTrack, 27, 28)

#------------#
# Bass       #
#------------#
fitMedia(YG_FUNK_BASS_5, bassTrack, 4, 8)
fitMedia(RD_ROCK_POPELECTRICBASS_12, bassTrack, 9, 17)
fitMedia(YG_GOSPEL_BASS_5, bassTrack, 33.75, 34)
fitMedia(YG_FUNK_BASS_5, bassTrack, 34, 42)

#------------#
# Beat       #
#------------#
beatSounds  = [RD_ROCK_POPRHYTHM_MAINDRUMS_17,OS_SNARE01,OS_CLOSEDHAT02,OS_CLAP01,YG_FUNK_SNARE_1] 
cHatPattern  = "0---0---0---0---"
kickPattern  = "0---0---0---0---"
snarePattern = "----0--0----0--0"
clapPattern  = "----0-------0---"
beatStartMeasure = 9
clapStartMeasure = 17
for i in range(8):
  makeBeat(beatSounds[2], beatTracks[0], beatStartMeasure + i, cHatPattern)
  makeBeat(beatSounds[1], beatTracks[2], beatStartMeasure + i, snarePattern)
for j in range(7):
  makeBeat(beatSounds[3], beatTracks[2], clapStartMeasure + j, clapPattern)
fitMedia(beatSounds[0],beatTracks[1],17,20)
fitMedia(beatSounds[0],beatTracks[1],21,24)
makeBeat(beatSounds[randint(0,4)], beatTracks[1], 24, kickPattern)
kickPattern2 = "0-0-0-0-0-0-0---"
makeBeat(beatSounds[randint(0,4)], beatTracks[1], 25, kickPattern2)
fitMedia(beatSounds[4],beatTracks[1],34,42)

#------------#
# Main       #
#------------#
fitMedia(RD_ROCK_POPLEADSTRUM_GUITAR_10, mainTrack[0], 13, 17)
fitMedia(RD_ROCK_POPRHYTHM_GUITAR_11, mainTrack[0], 17, 24)
fitMedia(YG_GOSPEL_PIANO_4, mainTrack[0], 28, 34)
fitMedia(YG_FUNK_BRASS_1, mainTrack[1], 32, 32.5)
fitMedia(YG_FUNK_FUNK_GUITAR_1, mainTrack[1], 34, 42)

#------------#
# Effect     #
#------------#
setEffect(mainTrack[1],VOLUME,GAIN,4,34,4,38)
setEffect(mainTrack[1],VOLUME,GAIN,0,38,-60,42)
setEffect(mainTrack[0],VOLUME,GAIN,0,1,0,13)
setEffect(mainTrack[0],VOLUME,GAIN,-5,13,-5,17)
setEffect(mainTrack[0],VOLUME,GAIN,-5,17,-5,24)
setEffect(mainTrack[0],VOLUME,GAIN,8,28,8,34)
setEffect(beatTracks[1],VOLUME,GAIN,0,1,0,17)
setEffect(transTrack,VOLUME,GAIN,0,1,0,20)
setEffect(transTrack,VOLUME,GAIN,-5,20,-5,21)
setEffect(transTrack,VOLUME,GAIN,5,26,5,28)
setEffect(beatTracks[1],VOLUME,GAIN,-5,17,-5,24)
setEffect(beatTracks[1],VOLUME,GAIN,0,24,0,34)
setEffect(beatTracks[1],VOLUME,GAIN,4,34,4,38)
setEffect(beatTracks[1],VOLUME,GAIN,0,38,-20,42)
setEffect(bassTrack,VOLUME,GAIN,0,38,-60,42)
setEffect(bassTrack,VOLUME,GAIN,12,4,12,8)
setEffect(bassTrack,VOLUME,GAIN,0,9,0,34)
setEffect(bassTrack,VOLUME,GAIN,4,34,4,38)

finish()

