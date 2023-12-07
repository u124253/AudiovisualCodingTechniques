from ffmpeg_tools import execute


def change_resolution(resolution="1280:720"):
    execute(f"ffmpeg - i input.mp4 - vf scale={resolution} output.mp4")


def change_codec(codec="x265"):
    # codec = "libvpx-vp9"
    # codec = "libaom-av1"
    # codec = "libvpx" vp8
    execute(f"ffmpeg -i input.mp4 -c:v {codec} -vtag hvc1 output.mp4")
