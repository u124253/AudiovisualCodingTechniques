import os
import subprocess

directory = os.getcwd()

print(f"current directory is{directory}")
#resize the imagen
scale=320
result = subprocess.run([f"ffmpeg -i mactonight.png -vf scale={scale}:-2 output_320.png"], shell=True, capture_output=True, text=True)
print(f"image with resolution: {scale} was created")
