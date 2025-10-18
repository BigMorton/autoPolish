import os
import pandas as pd
import requests
import torch
from TTS.api import TTS
from moviepy import (TextClip, ImageClip, AudioFileClip, 
                            CompositeVideoClip, concatenate_videoclips, ColorClip)
from moviepy.video.fx import all as vfx


backgroundClip = ImageClip("resources\autoPolish_BG.png").subclipped(0, 60)       # Create background video from background image (60 seconds)
backgroundClip.preview()

