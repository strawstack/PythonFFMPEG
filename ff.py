import ffmpeg

stream = ffmpeg.input('in.mkv')

# Process video only?
video_only = False
if video_only:
    stream  = stream.video

# Trim / Split
fps       = 60
start_sec = 20
end_sec   = 74
stream = ffmpeg.trim(stream, start_frame=start_sec * fps, end_frame=end_sec * fps)

# Crop
x      = 98
y      = 135
width  = 1082
height = 612
stream = ffmpeg.crop(stream, x, y, width, height)

stream = ffmpeg.output(stream, 'out.mkv')

ffmpeg.run(stream)