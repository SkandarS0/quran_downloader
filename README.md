# Quran Downloader

Welcome to the Quran Downloader project, a simple tool that allows users to download Surahs from the Quran conveniently.

## Description

Quran Downloader is a Python-based application that helps users select and download specific Surahs from the Quran via a menu-driven interface. It retrieves metadata about the Quran from an online source and uses that information to allow you to choose the Surahs you need.

## Installation

To set up and run this project, you need Docker. The presence of a `Dockerfile` in the project allows for easy setup and execution within a Docker environment.

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/quran-downloader.git
   cd quran-downloader
   ```

2. Build the Docker image:
   ```bash
   docker build -t quran-downloader .
   ```

3. Run the Docker container:
   ```bash
   docker run -it quran-downloader
   ```

## Usage

Once the Docker container is running, the `main.py` script will execute, launching an interactive menu for selecting and downloading Surahs.

**Main Features:**

- **Choose Surahs**: Select one or more Surahs by their numbers using the menu.
- **Download Surahs**: Start downloading the selected Surahs.

## Features

- Interactive menu for selecting Surahs to download.
- Downloads can be tailored by selecting individual Surahs or ranges.
- Asynchronous operations for efficient metadata loading and downloading.