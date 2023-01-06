import ffmpeg

stream = ffmpeg.input('out.mp4')

width = 1920
stream = ffmpeg.filter(stream, 'scale', width, -1)

stream = ffmpeg.output(stream, 'out_1920.mp4')

ffmpeg.run(stream)
