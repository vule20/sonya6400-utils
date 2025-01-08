# Sony A6400 Video Metadata Insertion and Image Conversion Tool

This repository provides a set of utilities for managing metadata and converting image and video files, specifically designed for users of the Sony A6400 camera. The tools allow for efficient handling of video metadata and image format conversions, making it easier to organize and store media for use with Apple’s Photos app.

### Intended Use

This tool is designed for users who want to streamline their media collection, particularly those using the Sony A6400 camera and Apple’s Photos app. It enables efficient storage and management of media while preserving the original metadata and ensuring compatibility with Apple devices.

## Features

### Metadata Injection for Sony A6400 Videos:

- Collects and embeds metadata generated during video recording with the Sony A6400 camera.
- Automatically inserts the corresponding metadata into video files (e.g., location, timestamps) and converts the video to HEVC format for optimized storage, compatible with Apple devices.

### Image Format Conversion:

- Converts JPEG and other common image formats to HEIC (High Efficiency Image Coding), ensuring high-quality images with reduced file sizes. This is ideal for storage efficiency and easy integration with the Apple Photos app.

### Benefits

- Seamlessly integrates Sony A6400 videos and images into Apple’s ecosystem, maintaining high quality while optimizing storage.
- Automatically converts files into formats (HEVC for videos, HEIC for images) that are widely supported across Apple devices.
- Efficient metadata handling, making it easy to organize and find your media

## Tools

- **Video Metadata Insertion for Sony A6400**: Automatically inserts camera metadata, including GPS information, into videos recorded with the Sony A6400. This ensures that the corresponding video files are compatible with Apple Photos, allowing you to efficiently manage and view GPS information.

- **Sony A6400 to Apple**: Automatically inserts camera metadata, including GPS information, into videos recorded with the Sony A6400 and converts recorded videos to HEVC format, which is widely used in Apple devices like the Iphone, Ipad, Macbook, for efficient storage (takes much less storage compared to the H264 format). This ensures that the corresponding video files are compatible with Apple Photos, allowing you to efficiently manage and view GPS information.

- **Image Conversion to HEIC**: The `Images2Apple` script converts all `.JPEG`, `.PNG`, and `.JPG` images in the current folder to the Apple-compressed HEIC format. By default, it takes all photos in the folder where the script is located and converts to HEIC and saves in `heic` folder. This significantly reduces image file sizes without sacrificing quality, making it ideal for use on macOS devices.

- **Video conversion to Apple HEVC format**: The script uses the **libx265** video codec and **AAC** audio codec, which are compatible with Apple Photos (iPhone format). It also preserves the metadata of the original video files during conversion.

## Usage

### Sony A6400 to Apple

- The tool inserts relevant metadata into your video files recorded with the Sony A6400, including GPS coordinates, camera model, and other essential information. This metadata helps integrate the videos smoothly into Apple Photos for better management and viewing. It also encodes input videos into the HEVC format, used by Apple devices for efficient storage.

```bash
python3 sony2apple.py --directory /path/to/the/folder/containing/both/xml/and/mp4/files
```

The metadata inserted videos will be placed under `mov`

### Video Metadata Insertion for Sony A6400

- The tool inserts relevant metadata into your video files recorded with the Sony A6400, including GPS coordinates, camera model, and other essential information. This metadata helps integrate the videos smoothly into Apple Photos for better management and viewing.

```bash
python3 sony_metadata2mp4.py --directory /path/to/the/folder/containing/both/xml/and/mp4/files
```

The metadata inserted videos will be placed under `inserted_metadata_videos`

### Image Conversion (Images2Apple.sh Script)

- The `Images2Apple.sh` script to automatically convert all supported image formats (.JPEG, .PNG, .JPG) to the HEIC format. This will reduce the file sizes, allowing for more efficient storage and easier sharing across Apple devices. The output images will be placed under the `heic` folder.

```bash
./Images2Apple.sh /input/image/file/or/input/image/folder
```

### Video conversion to Apple HEVC format

The `Video2HEVCApple.sh` script is designed to convert **MP4**, **MOV**, **AVI**, and **MKV** video files to **MOV** format, encoded with HEVC (H265) using `ffmpeg`. The converted files are saved in a newly created `mov` folder within the source directory.

The script uses the **libx265** video codec and **AAC** audio codec, which are compatible with Apple Photos (iPhone format). It also preserves the metadata of the original video files during conversion.

```bash
./Video2HEVCApple /path/to/video.mp4/or/path/to/video/folder
```

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/vule20/sonya6400-utils.git
cd sonya6400-utils
./install.sh
```

## Limitations

Windows not yet supported. Only supports MacOS and Linux
