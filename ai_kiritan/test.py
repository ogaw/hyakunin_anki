import os
from mutagen.oggvorbis import OggVorbis

def get_ogg_duration_ms(file_path):
    try:
        audio = OggVorbis(file_path)
        # audio.info.length は「秒（浮動小数点）」で返ってくる
        duration_ms = int(audio.info.length * 1000)
        return duration_ms
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# 処理したいディレクトリ
target_dir = "."

# ファイル一覧を取得してソート（連番対応）
files = sorted([f for f in os.listdir(target_dir) if f.endswith('.ogg')])

print(f"{'Filename':<20} | {'Duration (ms)':<15}")
print("-" * 40)

for filename in files:
    path = os.path.join(target_dir, filename)
    ms = get_ogg_duration_ms(path)
    
    if ms is not None:
        print(f"{filename:<20} | {ms:>10} ms")
