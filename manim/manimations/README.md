# Bacherlorarbeit_Presentation
Bacherlorarbeit_Presentation

## manim

https://docs.manim.community/en/stable/installation/uv.html

cd C:\Users\lapto\Documents\Aschaffenburg\BachelorArbeit\Bacherlorarbeit_Presentation\manim

uv init --python 3.13 manimations
cd manimations
uv add manim
uv run manim checkhealth
uv run manim main.py
uv run manim outer_product.py
uv run manim simd.py
uv run manim sisd.py


# MP4 to GIF

cd C:\Users\lapto\Documents\Aschaffenburg\BachelorArbeit\Bacherlorarbeit_Presentation\manim\manimations\media\videos\outer_product\1920p30
ffmpeg -ss 0 -t 14 -i DefaultTemplate.mp4 -vf "fps=30,scale=1024:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
