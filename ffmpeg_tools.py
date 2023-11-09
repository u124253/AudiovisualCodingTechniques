import os
import subprocess
import sys


def execute(command):
    subprocess.check_call(command, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)


class FfmpegTools:
    input_file = "BBB.mp4"
    output_file = "BBB.mpg"

    def __init__(self, input_, output_):
        """
        Constructor for FfmpegTools class
        :param input file name:
        :param output file name :
        """
        self.input_file = input_
        self.output_file = output_

    def convert_to_codec(self):
        """Function that converts a video into a codec """
        execute(f"ffmpeg -y -i {self.input_file}  -qscale:v 31 {self.output_file}")

    def change_resolution(self, scale):
        execute(f"ffmpeg -y -i {self.input_file} -filter:v scale={scale} -c:a copy {self.output_file}")

    def chroma_subsample(self, format):
        execute(f"ffmpeg -y -i {self.input_file} -c:v libx264 -vf format={format} {self.output_file}")

    def print_key_values(self, keys):
        print("\n\nprint values")
        print(f"{keys}: ", end="")
        execute(f"ffprobe -v error -select_streams v:0 -show_entries "
                f"stream={keys} -of csv=p=0:s=x {self.input_file}")


class Slicer(FfmpegTools):
    def __init__(self, input_, output_):
        super().__init__(input_, output_)

    def display_motion_vector(self, start, duration):
        #start = 00 duration = 9
        execute(f"ffmpeg -y -flags2 +export_mvs -ss {start} -t {duration} -i {self.input_file} -vf codecview=mv=pf+bf+bb {self.output_file}")
        pass

    def container(self):
        execute(f"ffmpeg -y -i {self.input_file} -ac 1 mp3_mono.mp3")
        #96kbps
        execute(f"ffmpeg -i {self.input_file} -map 0:a:0 -b:a 96k mp3_stereo_96.mp3")
        #flacc
        execute("ffmpeg -i audio.xxx -c:a flac flac.flac")

    def tracks_from_container(self):
        pass

    def add_subtitles(self):
        pass
    def yuv_histogram(self):
        pass


# Instance of our class to convert to mpg
tools_mpg = FfmpegTools("BBB.mp4", "BBB_out.mpg")
tools_mpg.convert_to_codec()

# Call the call to change resolution
tools_resize = FfmpegTools("BBB.mp4", "BBB_out_resized.mp4")
tools_resize.change_resolution("480:320")

# Call the function to chrom subsample
tools_chroma_subsample = FfmpegTools("BBB.mp4", "BBB_out_subsampled.mp4")
tools_chroma_subsample.chroma_subsample("yuv420p")

# Call the function to print some interesting values
tools_key_values = FfmpegTools("BBB.mp4", "BBB_out_resized.mp4")
tools_key_values.print_key_values("width,height,r_frame_rate,bit_rate,codec_name,duration")






# We create a instance of the new subclass derived from ffmpegtools
tools_motionvecton = Slicer("BBB.mp4", "BBB_motionvector.mp4")
tools_motionvecton.display_motion_vector("00","9")
