#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import RPi.GPIO as GPIO
import random
import logging

logging.basicConfig(level=logging.INFO)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)

queue_video = True
player = OMXPlayer(
        '/home/pi/Videos/Always_Sunny/s1/S01E01.mkv',
        dbus_name='org.mpris.MediaPlayer2.omxplayer',
        pause=True,
        args=[
            '--timeout', '30',
            ]
        )

sleep(5)

def load_playlist(tv_show=''):
    videos = [ v for v in Path('/home/pi/Videos/' + tv_show).rglob('*.mkv') ]
    random.shuffle(videos)
    return videos

def queue_video_event(*args):
    global queue_video
    print('queue video event fired')
    print("Arguments: ", *args)
    queue_video = True

player.exitEvent = queue_video_event
GPIO.add_event_detect(26, GPIO.FALLING, callback=queue_video_event, bouncetime=500)

all_videos = load_playlist()

while True:
    if len(all_videos) == 0:
        all_videos = load_playlist()

    if queue_video is True:
        player.load(all_videos.pop())
        sleep(5)
        queue_video = False

    sleep(0.5)
