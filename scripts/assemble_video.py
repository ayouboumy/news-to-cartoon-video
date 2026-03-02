import os

os.system("""
ffmpeg -y \
-i assets/animations/scene1.mp4 \
-i assets/animations/scene2.mp4 \
-i assets/animations/scene3.mp4 \
-i assets/audio/narration.wav \
-filter_complex "[0:v][1:v][2:v]concat=n=3:v=1:a=0[v]" \
-map "[v]" -map 3:a \
-shortest final_video.mp4
""")

print("🎬 Final video ready")
