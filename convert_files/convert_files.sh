#!/bin/bash

# Update these paths for your setup
DITA_OT_PATH="/Users/johnbruno/Desktop/dita-ot-4.0.2"  # Update with your actual DITA OT path
INPUT_PATH="/Users/johnbruno/Desktop/Convert"
OUTPUT_PATH="/Users/johnbruno/Desktop/Converted"

# Ensure the main output directory exists
mkdir -p "$OUTPUT_PATH"

# Function to convert files while maintaining folder structure
convert_files() {
  local input_folder="$1"
  local output_folder="$2"

  # Find all folders in the input directory
  find "$input_folder" -type d | while read -r folder; do
    # Compute the corresponding output directory
    local output_subfolder="${folder/$input_folder/$output_folder}"

    # Ensure the output subfolder exists
    mkdir -p "$output_subfolder"

    # Convert each file in the current folder
    find "$folder" -maxdepth 1 -type f \( -name "*.dita" -o -name "*.xml" -o -name "*.ditamap" \) | while read -r file; do
      local filename=$(basename -- "$file")
      local output_file="$output_subfolder/${filename%.*}.md"
      echo "Converting $file to $output_file"
      "$DITA_OT_PATH/bin/dita" --input="$file" --format=markdown --output="$output_subfolder"
    done
  done
}

# Call the convert_files function with the specified input and output paths
convert_files "$INPUT_PATH" "$OUTPUT_PATH"



