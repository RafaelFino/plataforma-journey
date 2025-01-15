#!/bin/bash

# Start the virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate

pip3 install -r ./ContentService/requirements.txt
pip3 install -r ./ProgressService/requirements.txt
pip3 install -r ./QuestionService/requirements.txt
pip3 install -r ./RegistryService/requirements.txt