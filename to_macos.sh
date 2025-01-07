#!/bin/bash

mkdir -p heic_images # Create a folder named 'heic_files' for the converted images

echo "Convert all images to HEIC format..."
for img in *.{jpg,png,bmp,jpeg,JPEG,JPG,PNG}; do
    if [ -f "$img" ]; then
        # Convert the image to HEIC format
        sips -s format heic "$img" --out "heic_images/${img%.*}.heic"
    fi
done

# Create an output folder for MOV files
OUTPUT_DIR="./mov_videos"
mkdir -p "$OUTPUT_DIR"

echo "Converting all MP4 files to MOV format..."

# Loop through all MP4 files in the current directory
for file in *.{MP4,mp4}; do
  # Skip if no MP4 files are found
  if [ ! -e "$file" ]; then
    echo "No MP4 files found in the current directory."
    exit 1
  fi

  # Extract the file name without extension
  filename=$(basename -- "$file")
  output_file="$OUTPUT_DIR/${filename%.*}.mov"

  # Convert the MP4 file to MOV format using ffmpeg
  ffmpeg -i "$file" -c:v libx264 -preset slow -crf 23 -c:a aac -b:a 128k -map_metadata 0 -map_chapters 0 "$output_file"

  if [ $? -eq 0 ]; then
    echo "Converted $file to $output_file"
  else
    echo "Failed to convert $file"
  fi
done

echo "All videos have been processed. Check $OUTPUT_DIR for results."
