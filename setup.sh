#!/bin/bash

# Install cantools using pip
echo "Installing cantools..."
python3 -m pip install cantools

# Check if .config already exists
if [ ! -f "../../.config" ]; then
    echo ".config does not exist, copying .config.example..."
    cp .config.example ../../.config
else
    echo ".config already exists, skipping copy."
fi

echo "Done."
