#   MP3 Key and BPM Tagger
#
#   Created by Patrick Elliott
#


import os
import warnings
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, ID3NoHeaderError
import librosa

# Suppress specific librosa warnings
warnings.filterwarnings("ignore", message="n_fft=1024 is too large*", category=UserWarning)

# Register 'initialkey' as a valid EasyID3 key
EasyID3.RegisterTextKey('initialkey', 'TKEY')

folder = "your_mp3_folder"  # Change this to your folder path

mp3_files = [f for f in os.listdir(folder) if f.lower().endswith(".mp3")]

for idx, filename in enumerate(mp3_files, 1):
    path = os.path.join(folder, filename)
    try:
        y, sr = librosa.load(path, sr=None)
        if len(y) < 1024:
            print(f"File too short for analysis: {filename}")
            continue

        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key_idx = chroma.sum(axis=1).argmax()
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        key = note_names[key_idx]

        try:
            audio = EasyID3(path)
        except ID3NoHeaderError:
            audiofile = ID3()
            audiofile.save(path)
            audio = EasyID3(path)

        audio['bpm'] = str(int(float(tempo)))
        audio['initialkey'] = key
        audio.save()

        new_name = f"{key} - {int(float(tempo))} - {filename}"
        new_path = os.path.join(folder, new_name)
        os.rename(path, new_path)

        print(f"Processed and renamed: {new_name}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

if mp3_files:
    print("mp3 (key-bpm) rename complete")
