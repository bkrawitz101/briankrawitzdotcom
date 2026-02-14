#!/bin/bash

# Script to batch process images with ImageMagick
#
# Usage: ./process_images.sh <directory>
#
# This script will create 'resized' and 'thumbnails' directories
# within the specified directory and process all JPG images.

# --- Configuration ---
RESIZED_WIDTH=1200
THUMBNAIL_WIDTH=400
# ---------------------

# Check if a directory is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

TARGET_DIR=$1

# Check if the provided argument is a directory
if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: '$TARGET_DIR' is not a directory."
  exit 1
fi

RESIZED_DIR="$TARGET_DIR/resized"
THUMBNAIL_DIR="$TARGET_DIR/thumbnails"

# Create output directories if they don't exist
mkdir -p "$RESIZED_DIR"
mkdir -p "$THUMBNAIL_DIR"

# Process all JPG and JPEG files in the target directory
find "$TARGET_DIR" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) | while read -r a; do
  FILENAME=$(basename -- "$a")
  echo "Processing $FILENAME..."

  # Create resized image
  convert "$a" -resize "${RESIZED_WIDTH}x>" "$RESIZED_DIR/$FILENAME"

  # Create thumbnail
  convert "$a" -resize "${THUMBNAIL_WIDTH}x>" "$THUMBNAIL_DIR/$FILENAME"
done

echo "Image processing complete."
