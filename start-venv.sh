#!/bin/bash

# Start the virtual environment
source .venv/bin/activate
pip3 install -r ./src/ContentService/requirements.txt
pip3 install -r ./src/ProgressService/requirements.txt
pip3 install -r ./src/QuestionService/requirements.txt
pip3 install -r ./src/RegistryService/requirements.txt