#!/bin/bash

# Usage: to_macos.sh video.mp4 or to_macos.sh /path/to/a/video/folder
# The script can be used to convert individual video files or entire directories of video files to MOV format.
# The converted files are saved in a new 'mov' folder within the source directory.
# Description: This script converts MP4, MOV, AVI, and MKV video files to MOV format using ffmpeg.
# The converted files are saved in a new 'mov' folder within the source directory.
# If a single video file is provided, it will be converted to MOV format.
# If a directory containing video files is provided, all video files in the directory will be converted to MOV format.
# The script uses the libx265 video codec and aac audio codec for conversion, which is exactly what IPhone uses on Apple Photos
# The script also preserves the metadata of the original video files during conversion.
# The script checks for the existence of MP4 files in the provided directory and exits if none are found.
# The script displays success or failure messages for each video file processed.
# The script is designed to be run on macOS, but can be modified for other platforms as well.
# The script requires ffmpeg to be installed on the system.

# Check if an argument is passed (file or directory)
if [ -z "$1" ]; then
  echo "Please provide a video file or a folder containing videos."
  exit 1
fi

# Check if the argument is a directory
if [ -d "$1" ]; then
  # If it's a directory, use the provided folder as the source
  SOURCE_DIR="$1"
  OUTPUT_DIR="$SOURCE_DIR/mov"
  mkdir -p "$OUTPUT_DIR"
  echo "Converting all video files in $SOURCE_DIR to MOV format..."

  # Loop through all MP4 files in the provided directory
  for file in "$SOURCE_DIR"/*.{mp4,MP4,mov,MOV,avi,AVI,mkv,MKV}; do
    if [ ! -e "$file" ]; then
      echo "No MP4 files found in $SOURCE_DIR."
      exit 1
    fi

    # Extract the file name without extension
    filename=$(basename -- "$file")
    output_file="$OUTPUT_DIR/${filename%.*}.mov"

    # Convert the MP4 file to MOV format using ffmpeg
    ffmpeg -y -i "$file" -c:v libx265 -tag:v hvc1 -c:a aac -map_metadata 0 "$output_file"

    if [ $? -eq 0 ]; then
      echo "Converted $file to $output_file"
    else
      echo "Failed to convert $file"
    fi
  done
elif [ -f "$1" ]; then
  # If it's a file, process that single video file
  file="$1"
  OUTPUT_DIR="./mov"
  mkdir -p "$OUTPUT_DIR"
  echo "Converting video file $file to MOV format..."

  # Extract the file name without extension
  filename=$(basename -- "$file")
  output_file="$OUTPUT_DIR/${filename%.*}.mov"

  # Convert the MP4 file to MOV format using ffmpeg
  ffmpeg -y -i "$file" -c:v libx265 -tag:v hvc1 -c:a aac -map_metadata 0 "$output_file"

  if [ $? -eq 0 ]; then
    echo "Converted $file to $output_file"
  else
    echo "Failed to convert $file"
  fi
else
  echo "The provided argument is neither a valid file nor a directory."
  exit 1
fi

echo "All videos have been processed. Check $OUTPUT_DIR for results."

