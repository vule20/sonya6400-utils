# sony2mov.py
# Created on: 2025-01-03 20:00:33
# Author: VuLe@macbook
# Last updated: 2025-01-08 14:16:17
# Last modified by: VuLe@macbook

import os
import xml.etree.ElementTree as ET
import subprocess
import argparse


def extract_metadata_from_xml(xml_file):
    """Extract all metadata from the XML file."""
    metadata = {}

    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Define namespace for parsing
    ns = {"ns": "urn:schemas-professionalDisc:nonRealTimeMeta:ver.2.00"}

    # Extract general metadata
    creation_date = root.find("ns:CreationDate", ns).get("value", "")
    metadata["creationdate"] = creation_date
    metadata["creation_time"] = creation_date

    device = root.find("ns:Device", ns)

    if device is not None:
        metadata["model"] = (
            device.get("manufacturer", "") + " " + device.get("modelName", "")
        )

    # Extract GPS data
    gps_group = root.find("ns:AcquisitionRecord/ns:Group[@name='ExifGPS']", ns)

    if gps_group is not None:
        latitude = longitude = latitude_ref = longitude_ref = None
        for item in gps_group.findall("ns:Item", ns):
            name = item.get("name", "")
            value = item.get("value", "")
            if name == "Latitude":
                latitude = value
            elif name == "Longitude":
                longitude = value
            elif name == "LatitudeRef":
                latitude_ref = value
            elif name == "LongitudeRef":
                longitude_ref = value

        # Convert latitude and longitude to ISO 6709 format
        if latitude and longitude and latitude_ref and longitude_ref:
            # Parse latitude and longitude
            lat_deg, lat_min, lat_sec = map(float, latitude.split(":"))
            lon_deg, lon_min, lon_sec = map(float, longitude.split(":"))

            # Convert to decimal degrees
            lat_dd = dms_to_dd(lat_deg, lat_min, lat_sec, latitude_ref)
            lon_dd = dms_to_dd(lon_deg, lon_min, lon_sec, longitude_ref)

            metadata["location"] = (
                f"{lat_dd:.6f}{'+' if lon_dd >= 0 else ''}{lon_dd:.6f}"
            )
            metadata["location-eng"] = (
                f"{lat_dd:.6f}{'+' if lon_dd >= 0 else ''}{lon_dd:.6f}"
            )

    print(f"metadata is {metadata}")

    return metadata


def dms_to_dd(degrees, minutes, seconds, direction):
    """
    Converts DMS (Degrees, Minutes, Seconds) to Decimal Degrees (DD).
    :param degrees: Integer degrees.
    :param minutes: Integer minutes.
    :param seconds: Float seconds.
    :param direction: String direction (N, S, E, W).
    :return: Decimal degrees as float.
    """
    dd = degrees + (minutes / 60) + (seconds / 3600)
    if direction in ["S", "W"]:
        dd = -dd
    return dd


def inject_metadata_to_video(video_file, metadata, output_file):
    """Inject metadata into a video file using ffmpeg."""
    # Construct the ffmpeg command with metadata
    cmd = ["ffmpeg", "-y", "-i", video_file, "-map_metadata", "0", "-c", "copy"]

    # Add metadata fields to the ffmpeg command
    for key, value in metadata.items():
        if value:  # Only include non-empty metadata
            cmd.extend(["-metadata", f"{key}={value}"])

    # Specify the output file
    cmd.append(output_file)
    print(cmd)

    # Run the ffmpeg command
    subprocess.run(cmd, check=True)


def insert_metadata_to_video(video_file, xml_file, output_file):
    """Insert metadata into a video file using ffmpeg."""

    # Check if the files exist
    if not os.path.exists(xml_file):
        print(f"Error: XML file '{xml_file}' does not exist.")
        return
    if not os.path.exists(video_file):
        print(f"Error: Video file '{video_file}' does not exist.")
        return

    # Extract metadata from the XML file
    metadata = extract_metadata_from_xml(xml_file)
    print("Extracted Metadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

    # Inject the metadata into the video file
    try:
        inject_metadata_to_video(video_file, metadata, output_file)
        print(f"Metadata successfully added to '{output_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error during ffmpeg processing: {e}")


def main(directory="./"):
    # video and metadata file have this format C0013M01.XML and C0013.MP4
    # Paths to the XML and video files

    xml_files = []

    for file_name in os.listdir(directory):
        full_path = os.path.join(directory, file_name)

        # If the path is a file and ends with ".xml", add it to the list
        if (
            os.path.isfile(full_path)
            and file_name.endswith(".xml")
            or file_name.endswith(".XML")
        ):
            xml_files.append(full_path)

    # copy video files to the output folder.
    os.makedirs("work", exist_ok=True)

    # First, insert metadata to mp4
    for xml_file in xml_files:
        video_file = (
            xml_file.replace("M01.xml", ".MP4")
            if "xml" in xml_file
            else xml_file.replace("M01.XML", ".MP4")
        )
        output_file = os.path.join(directory, "work", os.path.basename(video_file))

        insert_metadata_to_video(video_file, xml_file, output_file)

    # Next, convert mp4 to mov and reinsert metadata. The camera model is not
    # included with the MP4 container, and can be included with the MOV
    # container. Not sure why

    os.makedirs("mov", exist_ok=True)

    for xml_file in xml_files:
        video_file = (
            xml_file.replace("M01.xml", ".MP4")
            if "xml" in xml_file
            else xml_file.replace("M01.XML", ".MP4")
        )
        mp4_video_file = os.path.join(directory, "work", os.path.basename(video_file))
        mov_video_file = mp4_video_file.replace(".MP4", ".mov")
        final_mov_video_file = os.path.join(
            directory, "mov", os.path.basename(mov_video_file)
        )
        mov_cmd = [
            "ffmpeg",
            "-y",
            "-i",
            mp4_video_file,
            "-acodec",
            "copy",
            "-vcodec",
            "copy",
            "-map_metadata",
            "0",
            "-c",
            "copy",
            mov_video_file,
        ]
        # convert to mov
        subprocess.run(mov_cmd, check=True)
        # insert lens and camera model to mov
        insert_metadata_to_video(mov_video_file, xml_file, final_mov_video_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse the current working directory.")
    # Add argument to accept directory path
    parser.add_argument(
        "directory",
        type=str,
        nargs="?",
        default=os.getcwd(),
        help="Directory to parse (default is the current working directory)",
    )
    args = parser.parse_args()

    main(args.directory)

# "ffmpeg -i input_file.mp4 -acodec copy -vcodec copy output_file.mov"
