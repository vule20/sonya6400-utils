#!/bin/bash

# Function to install ffmpeg on Ubuntu (Debian-based)
install_ffmpeg_ubuntu() {
    echo "Ubuntu system detected. Installing ffmpeg..."
    sudo apt update
    sudo apt install -y ffmpeg
}

# Function to install ffmpeg on Linux (RHEL/CentOS/Fedora)
install_ffmpeg_linux() {
    echo "Linux system detected. Installing ffmpeg..."
    if command -v yum &> /dev/null; then
        sudo yum install -y ffmpeg
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y ffmpeg
    else
        echo "No compatible package manager found. Please install ffmpeg manually."
        exit 1
    fi
}

# Check if ffmpeg is already installed
if ! command -v ffmpeg &> /dev/null; then
    echo "ffmpeg is not installed."

    # Check if the system is Ubuntu/Debian-based
    if [ -f /etc/lsb-release ] || [ -f /etc/debian_version ]; then
        install_ffmpeg_ubuntu
    # Check if the system is Linux (RHEL/CentOS/Fedora-based)
    elif [ -f /etc/redhat-release ]; then
        install_ffmpeg_linux
    else
        echo "Unsupported Linux distribution. Please install ffmpeg manually."
        exit 1
    fi
else
    echo "ffmpeg is already installed."
fi
