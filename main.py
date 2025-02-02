import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import requests

# Function to download a song from FMA
def download_fma_song(url, output_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded: {output_path}")
    else:
        print(f"Failed to download: {url}")

# Function to plot and save spectrogram
def save_spectrogram(file_path, genre, output_image_path):
    y, sr = librosa.load(file_path, duration=300)  # Load first 30 seconds of the song
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.title(f'Spectrogram of {genre} Song')
    plt.colorbar(format="%+2.0f dB")
    plt.savefig(output_image_path)  # Save the spectrogram as an image
    plt.close()  # Close the figure to free up memory

# List of FMA song URLs and their genres
songs = [
    {"url": "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/WFMU/Broke_For_Free/Directionless_EP/Broke_For_Free_-_01_-_Night_Owl.mp3", "genre": "Electronic"},
    {"url": "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Tours/Enthusiast/Tours_-_01_-_Enthusiast.mp3", "genre": "Rock"},
    {"url": "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/ccCommunity/Chad_Crouch/Arps/Chad_Crouch_-_Shipping_Lanes.mp3", "genre": "Ambient"},
    {"url": "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/WFMU/Broke_For_Free/Directionless_EP/Broke_For_Free_-_01_-_Night_Owl.mp3", "genre": "Pop"}
    ]

# Output directories
output_dir = "downloaded_songs"
spectrogram_dir = "spectrograms"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(spectrogram_dir, exist_ok=True)

# Download songs and save spectrograms
for i, song in enumerate(songs):
    print(f"Downloading {song['genre']} song...")
    song_path = os.path.join(output_dir, f"{song['genre']}_song.mp3")
    download_fma_song(song["url"], song_path)
    
    # Save spectrogram
    spectrogram_path = os.path.join(spectrogram_dir, f"{song['genre']}_spectrogram.png")
    save_spectrogram(song_path, song["genre"], spectrogram_path)
    print(f"Spectrogram saved: {spectrogram_path}")