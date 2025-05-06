MP3 Key and BPM Tagger


This Python script analyzes MP3 files in a specified folder to detect the musical key and beats per minute (BPM) of each song. It then tags the MP3 files with this information and renames them in the format:

text
<key> - <bpm> - <original filename>.mp3
Features
Reads all MP3 files in a folder.

Estimates BPM and musical key using audio analysis.

Writes BPM and key into ID3 tags (bpm and initialkey).

Renames files to include key and BPM.

Skips files too short for reliable analysis.

Handles MP3s without existing ID3 tags.

Suppresses common warnings for cleaner output.

Displays progress and completion messages.

Requirements
Python 3.7 or higher

librosa (for audio analysis)

mutagen (for MP3 tag editing)

numpy (librosa dependency)

Installation
Install the required Python packages via pip:

bash
pip install librosa mutagen numpy
Usage
Place your MP3 files in a folder.

Update the folder variable in the script to point to your MP3 folder path. For example:

python
folder = "D:/Music/MyMP3s"
Run the script:

bash
python mp3bpmkey.py
The script will process each MP3 file, tag it with key and BPM, rename it, and print progress messages.

When finished, it will print:

text
mp3 rename complete
Notes
Files shorter than ~1024 audio samples are skipped because they are too short for accurate analysis.

The script registers a custom ID3 tag initialkey to store the musical key.

If MP3 files do not have ID3 tags, the script will add them automatically.

The renaming format is:
Key - BPM - OriginalFilename.mp3
Example: C# - 128 - my_song.mp3

Troubleshooting
If you see warnings about n_fft being too large, it means the audio file is very short; those files are skipped.

Ensure your MP3 files are not corrupted and have readable audio data.

For large collections, the script may take some time depending on file length and CPU speed.

License
This script is provided as-is under the MIT License. Feel free to modify and use it for your personal projects.

Contact
For questions or improvements, please open an issue or contact the author.

Feel free to customize it further if you want!
