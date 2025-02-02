# Spectrogram Analysis of Songs from Free Music Archive (FMA)

This project downloads songs from the Free Music Archive (FMA) and analyzes their spectrograms. It compares the spectrograms of songs from different genres and saves the plots as image files.

## Requirements

- Python 3.8 or higher
- Libraries listed in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
        https://github.com/sm1899/song_analysis.git
        cd spectrogram-analysis
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download FFmpeg (required for librosa):

    - **Linux**:

      ```bash
      sudo apt-get install ffmpeg
      ```

    - **macOS**:

      ```bash
      brew install ffmpeg
      ```

    - **Windows**:

      Download FFmpeg from the official [FFmpeg website](https://ffmpeg.org/download.html) and follow the installation instructions.

## Usage

1. Run the script to download songs from the Free Music Archive and analyze their spectrograms:

    ```bash
    python main.py
    ```

2. The spectrogram plots will be saved in the `output/` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

