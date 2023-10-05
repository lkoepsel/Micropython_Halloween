# MicroPython and Halloween
This repository uses MicroPython and various sensors and amplifiers to create a scary skeleton soundtrack!
## Links
Links
* [Simple MP3 Audio Playback With Raspberry Pi Pico - Embedded Computing Design](https://embeddedcomputing.com/technology/processing/interface-io/simple-mp3-audio-playback-with-raspberry-pi-pico)
* [I2S Volume Control With Raspberry Pi Pico and CircuitPython - Embedded Computing Design](https://embeddedcomputing.com/technology/open-source/i2s-volume-control-with-raspberry-pi-pico-and-circuitpython)
* [Raspberry Pi Pico Audio Line Out Via PCM5102A I2S Breakout - Embedded Computing Design](https://embeddedcomputing.com/technology/open-source/development-kits/raspberry-pi-pico-audio-line-out-via-pcm5102a-i2s-breakout)
* [PicoAudioPWM](https://github.com/danjperron/PicoAudioPWM#picoaudiopwm)
[Playing Sounds on The RP2040 Chip](https://www.coderdojotc.org/micropython/sound/07-play-audio-file/#playing-sounds-on-the-rp2040-chip)
## Hardware
* [Adafruit Mono 2.5W Class D Audio Amplifier - PAM8302](https://www.adafruit.com/product/2130) Buy
* [Adafruit I2S 3W Class D Amplifier Breakout - MAX98357A](https://www.adafruit.com/product/3006) Buy
* [Adafruit PAM8302 - Mono 2.5W Class D Audio Amplifier](https://learn.adafruit.com/adafruit-pam8302-mono-2-5w-class-d-audio-amplifier) Learn
* [Adafruit MAX98357 I2S Class-D Mono Amp](https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp) Learn
* [Interfacing Ky037 038 Sound Sensor With Raspberry Pi Pico](https://otosection.com/interfacing-ky037-038-sound-sensor-with-raspberry-pi-pico/)
* [GitHub - miketeachman/micropython-i2s-examples: Examples for I2S support on microcontrollers that run MicroPython](https://github.com/miketeachman/micropython-i2s-examples)
* [class I2S – Inter-IC Sound bus protocol — MicroPython v1.20.0 documentation](https://docs.micropython.org/en/v1.20.0/library/machine.I2S.html?highlight=i2s#machine.I2S)
* ([IR Distance Sensor - MicroPython for Kids](https://www.coderdojotc.org/micropython/sensors/08-ir-distance-sensor/)


## Sound Files
Clips need to be formatted correctly for playback, and Audacity is an excellent, free tool for doing so. You’ll need to save your MP3s in the correct format–a bit rate of less than 64kbit/s and sample rate of between 8kHz and 24kHz. Drag your files onto the Pico’s Flash memory, and change the names in the code to match your clips.


