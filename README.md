# FFmpeg Concatenate Script

## Recent Changes

### 1.1.1 (July 5, 2019)

- Added the ability to specify ffmpeg binary location

### 1.1.0 (July 5, 2019)

- Added the ability to concat all videos in a folder

### 1.0.0 (June 13, 2019)

- Initial commit

## Description

A script to help concatenating video files using FFmpeg.

## Usages

```
usage: ffmpeg_concat.py [-h] -i INPUT -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit

File Options:
  -i INPUT, --input INPUT
                        Source video file/directory (default: None)
  -o OUTPUT, --output OUTPUT
                        Output video file/directory (default: None)
```

## Example

The following example concatenates video1.mp4 and video2.mp4 into output.mp4.

```console
python3 ffmpeg_concat.py -i video1.mp4 -i video2.mp4 -o output.mp4
```