# mutagen.easyid3 : 간단한 ID3 태그 정보 읽기 및 처리 라이브러리
# mutagen.id3 : 가사나 이미지 같은 고급 정보 처리 라이브러리
# USLT : 가사 저장 프레임
# APIC : 앨범 이미지 저장 프레임

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, USLT, APIC

def extract_mp3_metadata(file_path):
    # mp3 파일에서 추출할 정보 저장할 딕셔너리
    metadata = {}

    try:
        # 기본 메타데이터 가져오기 (아티스트, 앨범 등)
        audio = EasyID3(file_path)
        metadata['title'] = audio.get('title', ['Unknown Title'])[0]
        metadata['artist'] = audio.get('artist', ['Unknown Artist'])[0]
        metadata['album'] = audio.get('album', ['Unknown Album'])[0]

        # 고급 가사 및 앨범 이미지 가져오기
        audio_tags = ID3(file_path)

        # 가사 (USLT 프레임)
        lyrics = ""
        for tag in audio_tags.values():
            if isinstance(tag, USLT):
                lyrics = tag.text
                break
        metadata['lyrics'] = lyrics

        # 앨범 이미지 (APIC 프레임)
        album_art_path = None
        for tag in audio_tags.values():
            if isinstance(tag, APIC):
                # 파일명 설정
                album_art_path = "album_art.jpg"
                # 이미지 파일로 저장
                with open(album_art_path, "wb") as img_file:
                    img_file.write(tag.data)
                break
        metadata['album_art_path'] = album_art_path

    except Exception as e:
        print(f"Error reading MP3 file: {e}")

    return metadata


# mp3 정보 추출
metadata = extract_mp3_metadata("my_music.mp3")

# 내용 확인
print("Title:", metadata.get('title'))
print("Artist:", metadata.get('artist'))
print("Album:", metadata.get('album'))
print("Lyrics:", metadata.get('lyrics'))
