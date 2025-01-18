from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, USLT, TPE2, error

def set_mp3_metadata(file_path, title=None, artist=None, album=None, album_artist=None, year=None, lyrics=None, album_art_path=None):
    try:
        # EasyID3 태그 설정(기본)
        audio = EasyID3(file_path)
        if title:
            audio['title'] = title
        if artist:
            audio['artist'] = artist
        if album:
            audio['album'] = album
        if year:
            audio['date'] = year
        audio.save()

        # ID3 태그 설정(앨범 음악가)
        audio_tags = ID3(file_path)
        if album_artist:
            audio_tags.add(TPE2(encoding=3, text=album_artist))  # TPE2 태그 추가
        audio_tags.save()

        # ID3 태그 설정 (가사와 앨범 이미지)
        audio_tags = ID3(file_path)
        if lyrics:
            audio_tags.add(USLT(encoding=3, lang='eng', desc='Lyrics', text=lyrics))
        if album_art_path:
            with open(album_art_path, 'rb') as img_file:
                album_art_data = img_file.read()
                audio_tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=album_art_data))
        audio_tags.save()

        print("mp3 Metadata 업데이트 성공")

    except error as e:
        print(f"update metadata 실패({e})")

# MP3 파일 경로
file_path = "Blueming (KARA).mp3"

# 가사
lyrics_text = '''(승연)'뭐해?'라는 두 글자에
(승연)'네가 보고 싶어' 나의 속마음을 담아 우
(규리)이모티콘 하나하나 속에
(규리)달라지는 내 미묘한 심리를 알까 우

(영지)아니 바쁘지 않아 (영지,승연)nothing no no
(니콜)잠들어 있지 않아 (규리,니콜)insomnia nia nia
(지영)지금 다른 사람과 함께이지 않아
(지영)응, 나도 너를 생각 중

(규리)우리의 (규리,니콜)네모 칸은 bloom
(규리,지영)엄지손가락으로 장미꽃을 피워
(승연,니콜)향기에 취할 것 같아 우
(승연,영지)오직 둘만의 비밀의 정원

(규리,지영)I feel (니콜,승연,영지)bloom 
(규리,지영)I feel (니콜,승연,영지)bloom 
(지영,규리)I feel (니콜,승연,영지)bloom
(지영)너에게 한 송이를 더 보내

(영지)밤샘 작업으로 업데이트
(영지)흥미로운 이 (영지,승연)작품의 지은이 
(영지)that's her 우
(니콜)어쩜 이 관계의 클라이맥스
(니콜)2막으로 넘어(니콜,승연)가기엔 지금이 
(니콜)good timing 우

(승연)같은 맘인 걸 알아 (영지,승연)realize la lize
(규리)말을 고르지 말아 (니콜,규리)just reply la la ly
(지영)조금 장난스러운 나의 은유에
(지영)네 해석이 궁금해

(규리)우리의 (규리,니콜)색은 gray and blue
(규리,지영)엄지손가락으로 말풍선을 띄워
(승연)금세 (승연,니콜)터질 것 같아 우
(승연,영지)호흡이 가빠져 어지러워

(규리,지영)I feel (승연,니콜,영지)blue. 
(규리,지영)I feel (승연,니콜,영지)blue. 
(규리,지영)I feel (승연,니콜,영지)blue. 
(니콜)너에게 가득히 채워

(규리,영지)띄어쓰기없이보낼게사랑인것같애
(규리,영지)백만송이장미꽃을, 나랑피워볼래?
(니콜)꽃잎의 색은 우리 마음 가는 대로 칠해
(니콜)시들 때도 (니콜,규리)예쁘게

(승연)우리의 네모 칸은 bloom
(승연,영지)엄지손가락으로 장미꽃을 피워
(지영,규리,니콜)향기에 취할 것 같아 우
(영지,지영)오직 둘만의 비밀의 정원

(지영,규리)I feel (니콜,승연,영지)bloom 
(규리,지영)I feel (승연,니콜,영지)bloom 
(지영,규리)I feel (니콜,승연,영지)bloom
(규리)너에게 한 송이를 
(all)더 (규리)보내
'''

set_mp3_metadata(
    file_path,
    title="Blueming(cover by KARA)",
    artist="카라(KARA)",
    album="아이유의 팔레트 Ep.16",
    album_artist="카라(KARA)",
    year="2022",
    lyrics=lyrics_text,
    album_art_path="album_art_01.jpg"
)
