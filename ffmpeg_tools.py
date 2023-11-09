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
        execute(f"ffmpeg -y -i {self.input_file} -codec:v {self.codec} -qscale:v 31 {self.output_file}")

    def change_resolution(self, scale):
        execute(f"ffmpeg -y -i {self.input_file} -filter:v scale={scale} -c:a copy {self.output_file}")

    def chroma_subsample(self, format):
        execute(f"ffmpeg -y -i {self.input_file} -c:v libx264 -vf format={format} {self.output_file}")

    def print_key_values(self, keys):
        print("\n\nprint values")
        print(f"{keys}: ", end="")
        execute(f"ffprobe -v error -select_streams v:0 -show_entries "
                f"stream={keys} -of csv=p=0:s=x {self.input_file}")


# Instance of our class to convert to mpg

tools_mpg = FfmpegTools("BBB.mp4", "BBB_out.mpg", "mp4", 2)
tools_mpg.convert_to_ffmpeg2()

# Call the call to change resolution

tools_resize = FfmpegTools("BBB.mp4", "BBB_out_resized.mp4", "mp4", 2)
tools_resize.change_resolution("480:320")

# call the function to chrom subsample

tools_chroma_subsample = FfmpegTools("BBB.mp4", "BBB_out_subsampled.mp4", "mp4", 2)
tools_chroma_subsample.chroma_subsample("yuv420p")

# call the function to print some interesting values
tools_key_values = FfmpegTools("BBB.mp4", "BBB_out_resized.mp4", "mp4", 2)
tools_key_values.print_key_values("width,height,r_frame_rate,bit_rate,codec_name,duration")
