#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: FFmpeg Concatenate Script
Author: K4YT3X
Date Created: June 13, 2019
Last Modified: July 5, 2019

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2019 K4YT3X
"""
import argparse
import os
import subprocess

VERSION = '1.1.0'


def process_arguments():
    """Processes CLI arguments

    This function parses all arguments
    This allows users to customize options
    for the output video.
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # video options
    file_options = parser.add_argument_group('File Options')
    file_options.add_argument('-i', '--input', help='Source video file/directory', action='append', required=True)
    file_options.add_argument('-o', '--output', help='Output video file', action='store', required=True)

    # parse arguments
    return parser.parse_args()


# process arguments
args = process_arguments()

# verify input files
if not os.path.isdir(args.input[0]):
    for path in args.input:
        assert os.path.isfile(path), f'File not found: {path}'
else:
    # sorted([os.path.join(args.input[0], f) for f in os.listdir(args.input[0]) if os.path.isfile(os.path.join(args.input[0], f))])
    videos = []
    for f in os.listdir(args.input[0]):
        if os.path.isfile(os.path.join(args.input[0], f)):
            videos.append(os.path.join(args.input[0], f))
    args.input = sorted(videos)

# use an incremental label for each ts file
temp_label = 0
for input_file in args.input:
    execute = [
        'ffmpeg',
        '-i',
        input_file,
        '-c',
        'copy',
        '-bsf:v',
        'h264_mp4toannexb',
        '-f',
        'mpegts',
        f'temp{temp_label}.ts',
        '-y'
    ]
    subprocess.run(execute, check=True)
    temp_label += 1

# generate FFmpeg concatentate string
temp_files = 'concat:'
for label_number in range(temp_label - 1):
    temp_files += f'temp{label_number}.ts|'
temp_files += f'temp{temp_label - 1}.ts'

# generate execution list for concatenating ts files
execute = [
    'ffmpeg',
    '-i',
    f'{temp_files}',
    '-c',
    'copy',
    '-bsf:a',
    'aac_adtstoasc',
    args.output,
    '-y'
]

subprocess.run(execute, check=True)

# delete ts files
for index in range(temp_label):
    os.remove(f'temp{index}.ts')
