import os
import subprocess

directory = os.getcwd()

print(f"current directory is{directory}")

result = subprocess.run(["ffmpeg -i mactonight.png -vf scale=320:-2 output_320.png"], shell=True, capture_output=True, text=True)




print(result.stdout)
