# wav_I2S - play a wav file using I2S
# The MIT License (MIT)
# Copyright (c) 2022 Mike Teachman
# https://opensource.org/licenses/MIT

# Purpose:  Play a WAV audio file out of a speaker or headphones
#
# - read audio samples from a WAV file stored on internal flash memory
# - write audio samples to an I2S amplifier or DAC module
# - the WAV file will play continuously in a loop until
#   a keyboard interrupt is detected or the board is reset
#
# Blocking version
# - the write() method blocks until the entire sample buffer is written to I2S
#


from machine import I2S
from machine import Pin
import time
import sys


# ======= I2S CONFIGURATION =======
SCK_PIN = 14
WS_PIN = 15
SD_PIN = 13
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 5000

# ======= AUDIO CONFIGURATION =======
WAV_FILE = "wav/Suspense.wav"
WAV_SAMPLE_SIZE_IN_BITS = 16
FORMAT = I2S.STEREO
SAMPLE_RATE_IN_HZ = 16000
# ======= AUDIO CONFIGURATION =======


def play():
    time.sleep(2)
    print("Play a single wav file directly with I2S, Ctrl-C to stop")
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

    while True:
        print(f"Playing {WAV_FILE}")
        wav = open(WAV_FILE, "rb")
        _ = wav.seek(4096)  # goto first byte of Data section in WAV file

        # allocate sample array
        # memoryview used to reduce heap allocation
        wav_samples = bytearray(1000)
        wav_samples_mv = memoryview(wav_samples)

        # continuously read audio samples from the WAV file
        # and write them to an I2S DAC
        try:
            while True:
                num_read = wav.readinto(wav_samples_mv)
                # end of WAV file?
                if num_read == 0:
                    # end-of-file, advance to first byte of Data section
                    _ = wav.seek(44)
                else:
                    _ = audio_out.write(wav_samples_mv[:num_read])

                # cleanup
                wav.close()

        except (KeyboardInterrupt, Exception) as e:
            print("caught exception {} {}".format(type(e).__name__, e))
            sys.print_exception(e)
            audio_out.deinit()

            print("Exiting")
            sys.exit()


if __name__ == '__main__':
    play()
