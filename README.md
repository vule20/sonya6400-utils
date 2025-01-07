# sonya6400-utils

# Metadata Insertion and Image Conversion for Sony A6400

This repository contains tools for managing metadata and converting images in your video and image collection.

## Features

- **Video Metadata Insertion**: Automatically inserts camera metadata, including GPS information, into videos recorded with the Sony A6400. This ensures that the corresponding video files are compatible with Apple Photos, allowing you to efficiently manage and view GPS information.
- **Image Conversion to HEIC**: The `to_macos` script converts all `.JPEG`, `.PNG`, and `.JPG` images in the current folder to the Apple-compressed HEIC format. This significantly reduces image file sizes without sacrificing quality, making it ideal for use on macOS devices.

## Usage

### Video Metadata Insertion

- The tool inserts relevant metadata into your video files recorded with the Sony A6400, including GPS coordinates, camera model, and other essential information. This metadata helps integrate the videos smoothly into Apple Photos for better management and viewing.

```bash
python3 sony_metadata2mp4.py --directory /path/to/the/folder/containing/both/xml/and/mp4/files
```

The metadata inserted videos will be placed under `inserted_metadata_videos`

### Image Conversion (to_macos Script)

- Run the `bash to_macos.sh` script to automatically convert all supported image formats (.JPEG, .PNG, .JPG) in your current folder to the HEIC format. This will reduce the file sizes, allowing for more efficient storage and easier sharing across Apple devices.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/vule20/sonya6400-utils.git
   ```
