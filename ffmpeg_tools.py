import os
import subprocess
import sys


def execute(command):
    subprocess.check_call(command, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)


class FfmpegTools:
    input_file = "BBB.mp4"
    output_file = "BBB.mpg"
    codec = None
    control_quantizer = 2  # from 2 to 31 , highest quality 2

    def __init__(self, input, output, codec, quantizer):
        """
        Constructor for FfmpegTools class
        :param input:
        :param output:
        :param codec:
        :param quantizer:
        """
        self.input_file = input
        self.output_file = output
        self.codec = codec
        self.control_quantizer = quantizer

    def convert_to_ffmpeg2(self):
        """Function that converts a video into a mpg2 file"""
        self.codec = "mpeg2video"
        execute(f"ffmpeg -i {self.input_file} -codec:v {self.codec} -qscale:v 31 {self.output_file}")


# Instance of our class
test = FfmpegTools("BBB.mp4", "BBB_out.mpeg", "mp4", 2)
# Call to the function that convert a video to mpg2
test.convert_to_ffmpeg2()
