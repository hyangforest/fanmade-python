from mutagen.id3 import ID3, TIT2, TPE1, error

file_path = "test.mp3"

try:
    tags = ID3()
    tags.add(TIT2(encoding=3, text="노래 타이틀"))
    tags.add(TPE1(encoding=3, text="아티스트"))
    tags.save(file_path)
    print("태그 저장 성공!")
except Exception as e:
    print("저장 실패:", e)
