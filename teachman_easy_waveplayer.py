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
SCK_PIN = 14
WS_PIN = 15
SD_PIN = 13
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 40000
# ======= I2S CONFIGURATION =======

WAV_FILES = ["Howl_short_2.wav",
             "Suspense_2.wav",
             "Loons_short_2.wav",
             "Door_Metal_2.wav"]


wp = WavPlayer(
    id=I2S_ID,
    sck_pin=Pin(SCK_PIN),
    ws_pin=Pin(WS_PIN),
    sd_pin=Pin(SD_PIN),
    ibuf=BUFFER_LENGTH_IN_BYTES,
)
time.sleep(3)
print(f"starting playback of {WAV_FILE}")

wp.play(WAV_FILE, loop=False)
# wait until the entire WAV file has been played
while wp.isplaying():
    print(f"You should be hearing {WAV_FILE}")
    pass

wp.play(WAV_FILE, loop=False)
time.sleep(10)  # play for 10 seconds
wp.pause()
print(f"Paused playback of {WAV_FILE}")
time.sleep(5)  # pause playback for 5 seconds
wp.resume()  # continue playing to the end of the WAV file
