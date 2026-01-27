import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

MUSIC_DIR = "music_mp3s"

musicList = []

for filename in os.listdir(MUSIC_DIR):
    if not filename.lower().endswith(".mp3"):
        continue

    path = os.path.join(MUSIC_DIR, filename)

    audio = MP3(path, ID3=EasyID3)
    length = int(audio.info.length)

    minutes = length // 60
    seconds = length % 60
    duration = f"{minutes}:{seconds:02d}"

    title = audio.get("title", [os.path.splitext(filename)[0]])[0]
    artist = audio.get("artist", ["Unknown Artist"])[0]
    album = audio.get("album", ["Unknown Album"])[0]

    musicList.append({
        "title": title,
        "artist": artist,
        "album": album,
        "file": filename,
        "duration": duration
    })

# Print in JS-friendly format
print("const musicList = [")
for song in musicList:
    print(f"""  {{
    title: "{song['title']}",
    artist: "{song['artist']}",
    album: "{song['album']}",
    file: "{song['file']}",
    duration: "{song['duration']}"
  }},""")
print("];")
