from math import floor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, ImageClip
import moviepy.editor as mp
import random, os
from meme_collecting import MemeMachine
from src.renderer.image import ImageRenderer   


# Generates meme vidoes to be uploaded on TikTok
class VideoGenerator:
    # Constructor
    def __init__(self, output_name, meme_machine):
        self.output_name = output_name
        self.machine     = meme_machine


    # Generates a meme video with a unique background clip and meme
    def gen_meme_video(self):
        meme_file  = self.machine.new_meme()
        ImageRenderer(self.output_name).render(meme_file)
    
