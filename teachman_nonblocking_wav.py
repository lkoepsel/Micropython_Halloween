# The MIT License (MIT)
# Copyright (c) 2022 Mike Teachman
# https://opensource.org/licenses/MIT

# Purpose:  Play a WAV audio file out of a speaker or headphones
#
# - read audio samples from a WAV file on SD Card
# - write audio samples to an I2S amplifier or DAC module
# - the WAV file will play continuously in a loop until
#   a keyboard interrupt is detected or the board is reset
#
# non-blocking version
# - the write() method is non-blocking.
# - a callback function called when all sample data has been
# written to the I2S interface
# - a callback() method sets the callback function

import time
import micropython
from machine import I2S
from machine import Pin


# ======= I2S CONFIGURATION =======
SCK_PIN = 14
WS_PIN = 15
SD_PIN = 13
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 40000
# ======= I2S CONFIGURATION =======

# ======= AUDIO CONFIGURATION =======
WAV_FILE = "Loons_short.wav"
WAV_SAMPLE_SIZE_IN_BITS = 16
FORMAT = I2S.MONO
SAMPLE_RATE_IN_HZ = 16000
# ======= AUDIO CONFIGURATION =======

PLAY = 0
PAUSE = 1
RESUME = 2
STOP = 3


def eof_callback(arg):
    global state
    print("end of audio file")
    # state = STOP  # uncomment to stop looping playback


def i2s_callback(arg):
    global state
    if state == PLAY:
        num_read = wav.readinto(wav_samples_mv)
        # end of WAV file?
        if num_read == 0:
            # end-of-file, advance to first byte of Data section
            _ = wav.seek(44)
            _ = audio_out.write(silence)
            micropython.schedule(eof_callback, None)
        else:
            _ = audio_out.write(wav_samples_mv[:num_read])
    elif state == RESUME:
        state = PLAY
        _ = audio_out.write(silence)
    elif state == PAUSE:
        _ = audio_out.write(silence)
    elif state == STOP:
        # cleanup
        wav.close()
        audio_out.deinit()
        print("Done")
    else:
        print("Not a valid state.  State ignored")


audio_out = I2S(
    I2S_ID,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mode=I2S.TX,
    bits=WAV_SAMPLE_SIZE_IN_BITS,
    format=FORMAT,
    rate=SAMPLE_RATE_IN_HZ,
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

audio_out.irq(i2s_callback)
state = PAUSE

wav = open(WAV_FILE, "rb")
_ = wav.seek(44)  # advance to first byte of Data section in WAV file

# allocate a small array of blank samples
silence = bytearray(1000)

# allocate sample array buffer
wav_samples = bytearray(10000)
wav_samples_mv = memoryview(wav_samples)

_ = audio_out.write(silence)

# add runtime code here ....
# changing 'state' will affect playback of audio file
start_time = 4
play_time = 6
pause_time = 4
resume_time = 8

time.sleep(start_time)
print(f"starting playback of {WAV_FILE} for {play_time}s")
state = PLAY
time.sleep(play_time)
print(f"pausing playback for {pause_time}s")
state = PAUSE
time.sleep(pause_time)
print(f"resuming playback for {resume_time}")
state = RESUME
time.sleep(resume_time)
print(f"stopping playback")
state = STOP
