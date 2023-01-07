# Python FFMPEG 

Example code for triming, croping, and transcoding a video file.

# Overview

ffmpeg is a video manipulation lib written in C or something designed for use in the terminal. Python has a wrapper for ffmpeg called `ffmpeg-python` (see Notes below). The code in [ff.py](https://github.com/strawstack/PythonFFMPEG/blob/main/ff.py) takes `in.mkv` as input. The video file is `trimmed` and `cropped` by the script. The output video file is `out.mkv`. `ff_format.py` takes `out.mkv` as input and generates `out.mp4`. Finally, we use `ff_scale.py` to scale `out.mp4` to the output `out_1920.mp4`.

# Determine Crop Ratio

[Figma File](https://www.figma.com/file/iAWUjaWzykgCmwCilOJ7CK/ffmpeg_crop?node-id=0%3A1&t=gz9Lup8XCFjOjlms-1)

# Video Example

View the input video used by [the script](https://github.com/strawstack/PythonFFMPEG/blob/main/ff.py) in this repo, and output video that the script generates.

- [Input Video](https://youtu.be/FrOTCRuQN2M)

- [Output Video (Cropped and Trimmed)](https://youtu.be/sFIhnM7CqlM)

- [Output Video (Format Conversion, Scaled back to 1920p)](https://youtu.be/pmrBEZupeFk)

# Notes

- [ffmpeg Python Docs](https://kkroening.github.io/ffmpeg-python/)

- [Format Conversion](https://askubuntu.com/questions/396883/how-to-simply-convert-video-files-i-e-mkv-to-mp4)

- [Frame By Frame Skip](http://www.inconduit.com/smpte/)

  - [Frame By Frame Code](http://www.inconduit.com/smpte/js/smpte_test_universal.js)
