# Comprehensive Guide to FFmpeg

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
   - [Installing on Debian/Ubuntu](#installing-on-debianubuntu)
   - [Installing on Fedora](#installing-on-fedora)
   - [Installing on Arch Linux](#installing-on-arch-linux)
3. [Basic Usage](#basic-usage)
   - [Transcoding a Video](#transcoding-a-video)
   - [Extracting Audio from a Video](#extracting-audio-from-a-video)
   - [Converting Audio Formats](#converting-audio-formats)
4. [Video Compression](#video-compression)
   - [Understanding CRF and Preset](#understanding-crf-and-preset)
   - [Compressing a Video with H.265](#compressing-a-video-with-h265)
   - [Optimizing for Quality](#optimizing-for-quality)
   - [Best Quality Settings](#best-quality-settings)
5. [Checking Video Metadata](#checking-video-metadata)
   - [Understanding Video and Audio Codecs](#understanding-video-and-audio-codecs)
   - [Determining Appropriate Compression](#determining-appropriate-compression)
6. [Reducing Video Size](#reducing-video-size)
   - [Reducing Video Resolution](#reducing-video-resolution)
   - [Lowering Bitrate](#lowering-bitrate)
   - [Choosing the Right Codec](#choosing-the-right-codec)
7. [Audio Processing](#audio-processing)
   - [Changing Audio Bitrate](#changing-audio-bitrate)
   - [Extracting Specific Audio Streams](#extracting-specific-audio-streams)
   - [Normalizing Audio Volume](#normalizing-audio-volume)
8. [Advanced Video Processing](#advanced-video-processing)
   - [Trimming and Cutting Video](#trimming-and-cutting-video)
   - [Merging Videos](#merging-videos)
   - [Adding Watermarks](#adding-watermarks)
   - [Adding Subtitles](#adding-subtitles)
   - [Changing Video Speed](#changing-video-speed)
9. [Batch Processing](#batch-processing)
   - [Batch Convert Videos](#batch-convert-videos)
   - [Batch Resize Images](#batch-resize-images)
   - [Using Scripts for Automation](#using-scripts-for-automation)
10. [Video Streaming](#video-streaming)
    - [Live Streaming to YouTube](#live-streaming-to-youtube)
    - [Creating HLS Streams](#creating-hls-streams)
11. [Optimizing for Web](#optimizing-for-web)
    - [Creating Web-Friendly MP4](#creating-web-friendly-mp4)
    - [Generating Thumbnails](#generating-thumbnails)
12. [Miscellaneous Features](#miscellaneous-features)
    - [Converting Image Sequences to Video](#converting-image-sequences-to-video)
    - [Extracting Frames from Video](#extracting-frames-from-video)
    - [Creating GIFs from Videos](#creating-gifs-from-videos)
13. [Troubleshooting](#troubleshooting)
    - [Common Issues and Solutions](#common-issues-and-solutions)
    - [Optimizing Performance](#optimizing-performance)
14. [More Useful FFmpeg Commands](#more-useful-ffmpeg-commands)
    - [Creating a Video Slideshow from Images](#creating-a-video-slideshow-from-images)
    - [Recording Screen with FFmpeg](#recording-screen-with-ffmpeg)
    - [Adding Metadata to Video](#adding-metadata-to-video)
    - [Extracting Audio Metadata](#extracting-audio-metadata)
15. [Conclusion](#conclusion)

---

## 1. Introduction

### What is FFmpeg?

**FFmpeg** is a comprehensive, cross-platform solution to record, convert, and stream audio and video. It includes `libavcodec`, the leading audio/video codec library, and `libavformat`, an audio/video container mux and demux library. FFmpeg can decode, encode, transcode, mux, demux, stream, filter, and play almost anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge. No matter if they were designed by some standards committee, the community, or a corporation.

### Key Features:

- **Convert between Formats:** Convert media files from one format to another.
- **Compress Videos:** Reduce the size of video files while maintaining quality.
- **Extract Audio:** Separate audio tracks from video files.
- **Stream Media:** Stream media files over a network.
- **Advanced Filtering:** Apply filters, effects, and complex manipulations to audio and video streams.

### Basic Syntax:

```bash
ffmpeg [input options] -i [input file] [output options] [output file]
```

- **`-i`**: Specifies the input file.
- **Input Options**: Various flags and settings that modify how FFmpeg handles the input file.
- **Output Options**: Flags and settings that affect the output file, such as codec settings, bitrate, resolution, etc.

---

## 2. Installation

### Installing on Debian/Ubuntu

To install FFmpeg on Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

### Installing on Fedora

To install FFmpeg on Fedora:

```bash
sudo dnf install ffmpeg
```

### Installing on Arch Linux

To install FFmpeg on Arch Linux:

```bash
sudo pacman -S ffmpeg
```

---

## 3. Basic Usage

### Transcoding a Video

**Transcoding** is the process of converting a video file from one format to another. This can be useful for compatibility with different devices or reducing file size.

**Example Command:**

```bash
ffmpeg -i input_video.avi output_video.mp4
```

**Explanation:**

- **`-i input_video.avi`**: Specifies the input file (in this case, an AVI file).
- **`output_video.mp4`**: Specifies the output file and format (MP4 in this case). FFmpeg automatically selects appropriate codecs for MP4.

### Extracting Audio from a Video

Extracting audio from a video allows you to save just the audio track of a video file.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -q:a 0 -map a output_audio.mp3
```

**Explanation:**

- **`-i input_video.mp4`**: Specifies the input video file.
- **`-q:a 0`**: Sets the audio quality. `0` is the best possible quality.
- **`-map a`**: Maps only the audio stream to the output, discarding the video.
- **`output_audio.mp3`**: Specifies the output audio file format (MP3).

### Converting Audio Formats

You can convert an audio file from one format to another using FFmpeg.

**Example Command:**

```bash
ffmpeg -i input_audio.wav output_audio.mp3
```

**Explanation:**

- **`-i input_audio.wav`**: Specifies the input audio file in WAV format.
- **`output_audio.mp3`**: Converts the file to MP3 format.

---

## 4. Video Compression

### Understanding CRF and Preset

- **CRF (Constant Rate Factor):** Controls video quality. Lower CRF values result in better quality and larger file sizes. CRF ranges from 0 (lossless) to 51 (worst quality).
- **Preset:** Determines the encoding speed and compression efficiency. Slower presets result in better compression but take longer to encode.

### Compressing a Video with H.265

H.265 (also known as HEVC) provides better compression than H.264.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -vcodec libx265 -crf 28 -preset slow output_video.mp4
```

**Explanation:**

- **`-vcodec libx265`**: Specifies the video codec as H.265 (libx265).
- **`-crf 28`**: Sets the CRF to 28. This is a good balance between quality and file size.
- **`-preset slow`**: Uses the "slow" preset to achieve better compression at the cost of encoding speed.
- **`output_video.mp4`**: Specifies the output file.

### Optimizing for Quality

For higher quality compression, use a lower CRF value:

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -vcodec libx265 -crf 20 -preset slow output_video.mp4
```

**Explanation:**

- **`-crf 20`**: A lower CRF value for higher quality, resulting in a larger file size.

### Best Quality Settings

To achieve the best possible quality, use the following settings:

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -c:v libx264 -crf 18 -preset veryslow -c:a copy output_best_quality.mp4
```

**Explanation:**

- **`-c:v libx264`**: Uses the H.264 codec, which is widely compatible and offers excellent quality.
- **`-crf 18`**: A CRF of 18 is considered visually lossless, meaning most people can't tell the difference between the original and the compressed video.

- **`-preset veryslow`**: The "veryslow" preset provides the best compression, resulting in the smallest file size with the highest quality.
- **`-c:a copy`**: Copies the audio stream without re-encoding, preserving the original audio quality.

---

## 5. Checking Video Metadata

Before deciding on the compression or conversion settings, it's important to check the metadata of the video file. This includes information about the codecs, resolution, frame rate, and bitrate.

### Example Command:

```bash
ffmpeg -i input_video.mp4
```

**Explanation:**

- This command displays all metadata for the specified video file, including video and audio codec, resolution, frame rate, and duration.

### Understanding Video and Audio Codecs

- **Video Codec**: Look for `Video: h264` or `Video: hevc`, which indicates the compression format of the video stream.
- **Audio Codec**: Check if the audio stream is encoded with AAC, MP3, Vorbis, etc.

### Determining Appropriate Compression

- **If the video is already using a highly compressed codec like H.265 (HEVC)**, re-encoding may not significantly reduce file size and could potentially increase it.
- **If the resolution is higher than necessary for your use**, consider reducing it to save space.

---

## 6. Reducing Video Size

To minimize the video file size while maintaining an acceptable quality level, consider the following methods:

### Reducing Video Resolution

Lowering the resolution of the video is one of the most effective ways to reduce file size.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -vf scale=1280:720 -c:v libx265 -crf 28 -preset slow output_video_720p.mp4
```

**Explanation:**

- **`-vf scale=1280:720`**: Resizes the video to 720p resolution.
- **`-c:v libx265`**: Encodes the video with H.265 codec.
- **`-crf 28`**: Balances quality and file size.

### Lowering Bitrate

Reducing the bitrate directly affects the size of the video.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -b:v 1000k -c:a copy output_video_lower_bitrate.mp4
```

**Explanation:**

- **`-b:v 1000k`**: Sets the video bitrate to 1000 kbps.

### Choosing the Right Codec

H.265 (HEVC) and VP9 are known for their high compression efficiency, making them ideal choices for reducing file size.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -c:v libvpx-vp9 -b:v 0 -crf 30 -c:a libopus output_video_vp9.webm
```

**Explanation:**

- **`-c:v libvpx-vp9`**: Uses the VP9 codec for video compression.
- **`-b:v 0 -crf 30`**: CRF-based compression for best quality.
- **`-c:a libopus`**: Uses Opus codec for audio, known for high compression efficiency.

---

## 7. Audio Processing

### Changing Audio Bitrate

You can change the bitrate of an audio file to reduce its size or improve its quality.

**Example Command:**

```bash
ffmpeg -i input_audio.mp3 -b:a 128k output_audio.mp3
```

**Explanation:**

- **`-b:a 128k`**: Sets the audio bitrate to 128 kbps, which balances quality and file size.

### Extracting Specific Audio Streams

If a video has multiple audio streams, you can extract a specific one.

**Example Command:**

```bash
ffmpeg -i input_video.mkv -map 0:a:0 -c copy output_audio.aac
```

**Explanation:**

- **`-map 0:a:0`**: Maps the first audio stream from the input file.
- **`-c copy`**: Copies the audio stream without re-encoding it.

### Normalizing Audio Volume

Normalizing audio adjusts the volume to a standard level across the entire file.

**Example Command:**

```bash
ffmpeg -i input_audio.mp3 -filter:a loudnorm output_normalized_audio.mp3
```

**Explanation:**

- **`-filter:a loudnorm`**: Applies the `loudnorm` filter to normalize audio loudness.

---

## 8. Advanced Video Processing

### Trimming and Cutting Video

You can trim or cut a section from a video.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -ss 00:00:30 -to 00:01:00 -c copy output_cut.mp4
```

**Explanation:**

- **`-ss 00:00:30`**: Starts the cut at 30 seconds.
- **`-to 00:01:00`**: Ends the cut at 1 minute.
- **`-c copy`**: Copies the original video and audio without re-encoding.

### Merging Videos

To concatenate multiple videos into one file:

**Example Command:**

```bash
ffmpeg -f concat -safe 0 -i file_list.txt -c copy output_merged.mp4
```

**Explanation:**

- **`-f concat`**: Specifies that files should be concatenated.
- **`-safe 0`**: Allows usage of unsafe file paths.
- **`-i file_list.txt`**: Specifies the input file list.

### Adding Watermarks

You can overlay a watermark image onto a video.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -i watermark.png -filter_complex "overlay=10:10" output_video.mp4
```

**Explanation:**

- **`-filter_complex "overlay=10:10"`**: Places the watermark at the position (10, 10) on the video.

### Adding Subtitles

You can add subtitles to a video using FFmpeg.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -i subtitles.srt -c copy -c:s mov_text output_video_with_subs.mp4
```

**Explanation:**

- **`-i subtitles.srt`**: Specifies the subtitle file.
- **`-c:s mov_text`**: Uses the `mov_text` codec to encode the subtitles for MP4.

### Changing Video Speed

You can change the speed of a video (either speed it up or slow it down).

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -filter:v "setpts=0.5*PTS" output_fast_video.mp4
```

**Explanation:**

- **`-filter:v "setpts=0.5*PTS"`**: Speeds up the video by a factor of 2. Use a value greater than 1 to slow it down (e.g., `2.0*PTS`).

---

## 9. Batch Processing

### Batch Convert Videos

Automate the conversion of multiple files in a directory.

**Example Command:**

```bash
for f in *.avi; do
  ffmpeg -i "$f" "${f%.avi}.mp4"
done
```

**Explanation:**

- **`for f in *.avi`**: Loops over all `.avi` files in the directory.
- **`${f%.avi}.mp4`**: Converts the filename to `.mp4`.

### Batch Resize Images

Resize multiple images in a directory.

**Example Command:**

```bash
for img in *.jpg; do
  ffmpeg -i "$img" -vf scale=800:600 "${img%.jpg}_resized.jpg"
done
```

**Explanation:**

- **`-vf scale=800:600`**: Resizes the image to 800x600 pixels.

### Using Scripts for Automation

You can use shell scripts to automate repetitive tasks.

**Example Script:**

```bash
#!/bin/bash
for f in *.mp4; do
  ffmpeg -i "$f" -vcodec libx265 -crf 28 -preset slow "compressed_$f"
done
```

**Explanation:**

- This script compresses all `.mp4` files in a directory using H.265.

---

## 10. Video Streaming

### Live Streaming to YouTube

You can stream live video content to YouTube using FFmpeg.

**Example Command:**

```bash
ffmpeg -re -i input_video.mp4 -f flv rtmp://a.rtmp.youtube.com/live2/your_stream_key
```

**Explanation:**

- **`-re`**: Reads input in real-time mode.
- **`-f flv`**: Specifies the FLV format, which is required for YouTube live streaming.
- **`rtmp://a.rtmp.youtube.com/live2/your_stream_key`**: RTMP server URL with your stream key.

### Creating HLS Streams

HTTP Live Streaming (HLS) is a popular streaming format used for web streaming.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -codec: copy -start_number 0 -hls_time 10 -hls_list_size 0 -f hls output.m3u8
```

**Explanation:**

- **`-start_number 0`**: Starts segment numbering from 0.
- **`-hls_time 10`**: Splits video into 10-second segments.
- \*\*`-hls

\_list_size 0`\*\*: Stores all segments in the playlist.

---

## 11. Optimizing for Web

### Creating Web-Friendly MP4

Optimize MP4 files for fast start on web streaming platforms.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -vcodec libx264 -acodec aac -strict -2 -movflags +faststart output_web.mp4
```

**Explanation:**

- **`-movflags +faststart`**: Moves metadata to the beginning of the file, making it web-optimized.

### Generating Thumbnails

Create a thumbnail image from a video file.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -vf "thumbnail,scale=320:240" -frames:v 1 thumbnail.png
```

**Explanation:**

- **`-vf "thumbnail,scale=320:240"`**: Selects a thumbnail frame and resizes it to 320x240 pixels.
- **`-frames:v 1`**: Outputs only one frame.

---

## 12. Miscellaneous Features

### Converting Image Sequences to Video

Combine a sequence of images into a video.

**Example Command:**

```bash
ffmpeg -framerate 24 -i img%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p output_video.mp4
```

**Explanation:**

- **`-framerate 24`**: Specifies the input frame rate.
- **`img%03d.png`**: Input files named img001.png, img002.png, etc.
- **`-r 30`**: Sets the output frame rate.

### Extracting Frames from Video

Extract frames from a video at a specified rate.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -vf "fps=1" img%03d.png
```

**Explanation:**

- **`-vf "fps=1"`**: Extracts one frame per second.

### Creating GIFs from Videos

Convert a video segment into a GIF.

**Example Command:**

```bash
ffmpeg -i input_video.mp4 -vf "fps=10,scale=320:-1:flags=lanczos" -ss 00:00:05 -t 10 output.gif
```

**Explanation:**

- **`fps=10`**: Captures 10 frames per second for the GIF.
- **`scale=320:-1`**: Scales the video to 320 pixels wide, keeping the aspect ratio.
- **`-ss 00:00:05`**: Starts at the 5-second mark.
- **`-t 10`**: Captures 10 seconds of video.

---

## 13. Troubleshooting

### Common Issues and Solutions

- **Issue:** FFmpeg fails with "unknown encoder."

  - **Solution:** Install the necessary codec or use a supported one.

- **Issue:** Video output is too large.
  - **Solution:** Increase the CRF value or use a slower preset.

### Optimizing Performance

- **Use Hardware Acceleration:** Enable hardware acceleration (if supported by your GPU) to speed up encoding/decoding.

```bash
ffmpeg -hwaccel cuda -i input.mp4 -c:v h264_nvenc output.mp4
```

**Explanation:**

- **`-hwaccel cuda`**: Enables CUDA hardware acceleration (requires an NVIDIA GPU).
- **`-c:v h264_nvenc`**: Uses the NVIDIA encoder for H.264.

- **Parallel Processing:** Utilize multiple CPU threads to improve performance.

```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -threads 4 output.mp4
```

**Explanation:**

- **`-threads 4`**: Uses 4 CPU threads for encoding.

---

## 14. More Useful FFmpeg Commands

### Creating a Video Slideshow from Images

Create a video slideshow from a series of images.

**Example Command:**

```bash
ffmpeg -framerate 1/5 -i img%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p slideshow.mp4
```

**Explanation:**

- **`-framerate 1/5`**: Displays each image for 5 seconds.
- **`-r 30`**: Sets the output frame rate to 30 fps.

### Recording Screen with FFmpeg

Capture your screen and save it as a video file.

**Example Command:**

```bash
ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0+0,0 output_screen.mp4
```

**Explanation:**

- **`-video_size 1920x1080`**: Captures a screen area of 1920x1080 pixels.
- **`-framerate 25`**: Sets the capture frame rate to 25 fps.
- **`-f x11grab`**: Grabs the screen in an X11 environment.

### Adding Metadata to Video

You can add or edit metadata in video files.

**Example Command:**

```bash
ffmpeg -i input.mp4 -metadata title="My Video" -metadata author="John Doe" output.mp4
```

**Explanation:**

- **`-metadata title="My Video"`**: Sets the title metadata.
- **`-metadata author="John Doe"`**: Sets the author metadata.

### Extracting Audio Metadata

Extract metadata from an audio file.

**Example Command:**

```bash
ffmpeg -i input.mp3 -f ffmetadata metadata.txt
```

**Explanation:**

- **`-f ffmetadata`**: Specifies the output format as FFmpeg metadata.
- **`metadata.txt`**: Saves the metadata in a text file.

---

## 15. Conclusion

FFmpeg is an incredibly powerful tool that can handle a wide range of multimedia processing tasks. Whether you're compressing videos, converting formats, streaming, or editing, FFmpeg's versatility and command-line accessibility make it an essential tool for professionals and enthusiasts alike. With the right scripts and optimizations, you can streamline your workflow and handle even the most complex media tasks efficiently.

This README provides a comprehensive overview of FFmpeg, explaining not just the commands but also the purpose and effect of each option, ensuring you understand how to make the most of this powerful tool.
