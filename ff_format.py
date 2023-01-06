import ffmpeg

stream = ffmpeg.input('out.mkv')

stream = ffmpeg.output(stream, 'out.mp4', format="mp4")

ffmpeg.run(stream)