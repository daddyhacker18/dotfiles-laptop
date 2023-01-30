#!/bin/bash
sudo cat /usr/bin/audio-speakers
/usr/bin/hda-verb /dev/snd/hwC0D0 0x20 0x500 0xf
/usr/bin/hda-verb /dev/snd/hwC0D0 0x20 0x400 0x7774
/usr/bin/hda-verb /dev/snd/hwC0D0 0x20 0x500 0x45
/usr/bin/hda-verb /dev/snd/hwC0D0 0x20 0x400 0x5289
