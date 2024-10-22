# Directory to check (change this to the target directory)
TARGET_DIR="preprocessing"

# Iterate over each file in the directory
for file in "$TARGET_DIR"/*; do
  # Check if it is a regular file (not a directory)
  if [[ -f "$file" ]]; then
    # Get the file extension
    extension="${file##*.}"
    
    # If the file extension is not "ipynb" or "py", delete the file
    if [[ "$extension" != "ipynb" && "$extension" != "py" ]]; then
      echo "Deleting: $file"
      rm "$file"
    fi
  fi
done