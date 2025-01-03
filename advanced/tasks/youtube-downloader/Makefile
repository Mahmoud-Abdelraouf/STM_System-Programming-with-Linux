# Makefile for YouTube Downloader Project

# Variables
VENV_DIR = venv
PYTHON = python3
PIP = $(VENV_DIR)/bin/pip
PYTHON_BIN = $(VENV_DIR)/bin/python
REQUIREMENTS = requirements.txt
APP = app.py

# Declare phony targets
.PHONY: all venv install check_ffmpeg run clean help

# Default target
all: run

# Create a virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV_DIR)

# Install Python dependencies
install: venv
	@echo "Installing Python dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r $(REQUIREMENTS)

# Check and install ffmpeg
check_ffmpeg:
	@echo "Checking if ffmpeg is installed..."
	@which ffmpeg > /dev/null 2>&1 || { \
	    echo "ffmpeg not found. Please install ffmpeg before proceeding."; \
	    exit 1; \
	}
	@echo "ffmpeg is installed."

# Run the application
run: install check_ffmpeg
	@echo "Running the application..."
	$(PYTHON_BIN) $(APP)

# Clean the project
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_DIR)

# Help message
help:
	@echo "Available targets:"
	@echo "  venv         - Create a virtual environment"
	@echo "  install      - Install Python dependencies"
	@echo "  check_ffmpeg - Check if ffmpeg is installed"
	@echo "  run          - Run the application"
	@echo "  clean        - Remove the virtual environment"
	@echo "  help         - Show this help message"
