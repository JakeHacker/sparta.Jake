import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#순위/곡 제목/가수
#파이썬 내장 함수인 strip()을 연구할 것
for music in musics:
    music_needrename = music.select_one('td.info > a.title.ellipsis')
    music_name = music_needrename.text.strip()
    
    music_needrerank = music.select_one('td.number')
    music_rank = music_needrerank.text.strip()[0]

#   music_rank = music.select_one('td.number')

    music_singer = music.select_one('td.info > a.artist.ellipsis').text
    print (music_rank, music_name, music_singer)
    # print (music_needrerank)