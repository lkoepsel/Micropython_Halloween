# The MIT License (MIT)
# Copyright (c) 2022 Mike Teachman
# https://opensource.org/licenses/MIT
#
# Purpose:  Play a WAV audio file out of a speaker or headphones
#

import time
from machine import Pin

from wavplayer import WavPlayer


# ======= I2S CONFIGURATION =======
SCK_PIN = 7
WS_PIN = 8
SD_PIN = 9
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 40000
# ======= I2S CONFIGURATION =======

WAV_FILES = ["crickets.wav",
             "thunder_clap.wav",
             "loons.wav",
             "door.wav",
             "dark_howl.wav",
             "Suspense.wav",
             "opening.wav",
             "gasp.wav",
             "monsters.wav",
             "Vincent_laugh.wav",
             ]


wp = WavPlayer(
    id=I2S_ID,
    sck_pin=Pin(SCK_PIN),
    ws_pin=Pin(WS_PIN),
    sd_pin=Pin(SD_PIN),
    ibuf=BUFFER_LENGTH_IN_BYTES,
)
time.sleep(3)
print(f"starting playback of .wav files")

for wav_file in WAV_FILES:
    wp.play(wav_file, loop=False)
    # wait until the entire WAV file has been played
    i = 0
    while wp.isplaying():
        i += 1
        if i > 10000:
            print(f"You are hearing {wav_file}")
            i = 0
        pass
