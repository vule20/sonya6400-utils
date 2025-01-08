#!/bin/bash

mkdir -p heic # Create a folder named 'heic_files' for the converted images

echo "Convert all images in the current folder to HEIC format..."
for img in *.{jpg,png,bmp,jpeg,JPEG,JPG,PNG}; do
    if [ -f "$img" ]; then
        # Convert the image to HEIC format
        sips -s format heic "$img" --out "heic/${img%.*}.heic"
    fi
done
