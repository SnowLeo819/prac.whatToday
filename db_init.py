from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.what_today

db.qna.drop();
db.ans.drop();
db.like.drop();

# 작성중 내용, 완성본 아님

doc = [
    {'idx': 1, 'quiz': "코로나 시국 종료!<br>제일 먼저 가고 싶은 여행지는?",'ans_01p':'', 'ans_01': "도시의 야경을 감상할 수 있는<br>뉴욕", 'ans_02': "다양한 액티비티가 가능한<br>스위스",
     'ans_03': "우아한 만찬과 낭만의 도시<br>파리", 'ans_04': "바다를 보며 휴식할 수 있는<br>괌"},
    {'idx': 2, 'quiz': "즐거운 여행을 끝마치고<br>집으로 돌아온 나는?", 'ans_01': "여행은 자주 다녀줘야 제 맛,<br>다음엔 어디를 가볼까~", 'ans_02': "친구들에게 여행 썰 풀어줘야지,<br>바로 약속을 잡는다",
     'ans_03': "사온 기념품 먼저 정리하고<br>밀린 집안일 해야지!", 'ans_04': "돌아다니느라 너무 피곤했음,<br>집에서 휴식"},
    {'idx': 3, 'quiz': "갑작스럽게 휴무를 얻게 되었다!<br>오늘의 일정은?", 'ans_01': "다들 모여! 나들이 가자~", 'ans_02': "근손실 못참지!",
     'ans_03': "출출한데 뭐라도 사올까?", 'ans_04': "혼자 뒹굴뒹굴.."},
    {'idx': 4, 'quiz': "서점에 들어간 당신,<br>가장 먼저 집어든 책의 제목은?", 'ans_01': "너와 함께라면 인생도 여행이다", 'ans_02': "백년운동",
     'ans_03': "백종원의 집밥 요리 레시피", 'ans_04': "달러구트 꿈 백화점"},
    {'idx': 5, 'quiz': "책을 구매하고 카페로 들어간<br>당신이 고른 메뉴는?", 'ans_01': "역시 커피는 얼죽아!<br>아이스 아메리카노", 'ans_02': "내 취향이 어때서!<br>민트초코라떼",
     'ans_03': "알콜은 나의 힘!<br>와인에이드", 'ans_04': "따뜻한게 제일이지!<br>핫초코"},
    {'idx': 6, 'quiz': "음료를 다 마시고 카페를 나온 당신<br>오늘의 날씨는?", 'ans_01': "나들이 가고 싶다<br>맑은 날", 'ans_02': "밖으로 나가면 안되는<br>폭염", 'ans_03': "파전에 막걸리가 땡기는<br>소나기",
     'ans_04': "간판 날아갈 거 같은<br>태풍"},
]

ansDoc = [
    {'idx': 1, 'type': 'A',
     'cover': 'https://blog.kakaocdn.net/dn/mSsTK/btreY4uZSGY/JG4YUDQ2LmLFdUlR4liXFK/img.png',
     'suggest': '“산책으로 바깥공기 만끽하기!”', },

    {'idx': 2, 'type': 'B',
     'cover': 'https://blog.kakaocdn.net/dn/csFn7r/btreZ15RV1F/FXSyNFkjUXXhGnPO1yO761/img.png',
     'suggest': '“근손실 방지! 홈트하자~”',
     'img-link1': 'https://i.ytimg.com/vi/myNjmnvI6x0/hqdefault.jpg',
     'title1': 'NO 층간소음 올인원 운동 - 40분 유산소운동 홈트 - 관절에 무리없이 체지방 태우기',
     'genre1': 'NO 층간소음 NO 스쿼트 - 40분 유산소운동 홈트 - 관절에 무리없이 체지방 태우기] - 땀 많이 나고 숨이 많이 차는 올인원 운동입니다. NO 층간소음 30동작 유산소 ...',
     'info1': '2021-01-22',
     'director1': '빅씨스',
     'link1': 'https://www.youtube.com/watch?v=myNjmnvI6x0',
     'img-link2': 'https://i.ytimg.com/vi/gMaB-fG4u4g/hqdefault.jpg',
     'title2': '전신 다이어트 최고의 운동 [칼소폭 찐 핵핵매운맛]',
     'genre2': '이번 영상은 정말! 정말! 맵습니다. 사실 운동 영상을 준비할 때 강도를 높이는 것은 그리 어려운 작업이 아닙니다. (스쿼트, 런지, 점핑잭, 버피등 반복..) 그래서 ...',
     'info2': '2021-05-24',
     'director2': 'Thankyou BUBU',
     'link2': 'https://www.youtube.com/watch?v=gMaB-fG4u4g',
     'img-link3': 'https://i.ytimg.com/vi/sqQpL1wKW6M/hqdefault.jpg',
     'title3': '12분 서서하는 복근운동 홈트레이닝 - 체지방 태우기는 보너스',
     'genre3': '서서하는 복근운동 홈트레이닝 - 복근운동을 제대로 하면서 체지방까지 태우는 루틴입니다. 서서하는 복근운동 은 누워서 할때보다 자극을 주기가 어렵기 때문에 루틴 ...',
     'info3': '2021-05-24',
     'director3': '빅씨스',
     'link3': 'https://www.youtube.com/watch?v=sqQpL1wKW6M'},

    {'idx': 3, 'type': 'C',
     'cover': 'https://blog.kakaocdn.net/dn/o2vyi/btre5PbYRGa/PE818HoBW7CUY55zOX2h3k/img.png',
     'suggest': '“맛있는건 언제나 옳다! 요리!”',
     'img-link1': 'https://i.ytimg.com/vi/tPf-KfZ6W84/hqdefault.jpg',
     'title1': '도톰한 감자튀김과 치즈소스 :: 바삭한 감자튀김 만들기 :: 감자요리 :: Fried Potatoes and cheese sauce :: French Fries',
     'genre1': '예상되는 질문들 하단에 TIP 으로 적어두었으니 참고하세요. 겉은 바삭 속은 촉촉한 감자튀김 만들었어요. 저처럼 두껍게 자르면 웨지감자 처럼 겉은 바삭, 속은 촉촉 ...',
     'info1': '2021-02-03',
     'director1': '매일맛나 delicious day',
     'link1': 'https://www.youtube.com/watch?v=tPf-KfZ6W84',
     'img-link2': 'https://i.ytimg.com/vi/LrTljxRQm4c/hqdefault.jpg',
     'title2': '요리먹방 :) 구독자 200만명 너무 감사합니다.🙏🏻 짜장 해물찜(랍스터테일, 전복, 주꾸미, 새우, 가리비, 오징어, 팽이버섯, 표고버섯, 새송이버섯) MUKBANG',
     'genre2': '여러분 덕분에 구독자가 200만명이 되었습니다. 너무 감사합니다. 기념으로 짜장소스 해물찜을 준비해봤어요~ 해물 : 랍스터테일, 전복, 주꾸미, 새우, 가리비, 오징어 ...',
     'info2': '2021-02-05',
     'director2': '보경 Bokyoung',
     'link2': 'https://www.youtube.com/watch?v=LrTljxRQm4c',
     'img-link3': 'https://i.ytimg.com/vi/ORQd1W9n4TA/hqdefault.jpg',
     'title3': '양배추를 이렇게 만들었더니 고기처럼 맛있어요! 순식간에 양배추 한 통이 사라져요 Cabbage Recipe',
     'genre3': '양배추를 이렇게 만들었더니 고기처럼 맛있어서 놀랐어요 요즘 무농약 양배추가 많이 보여서 자주 사먹다보니 새로운 양배추요리를 만들어 봤어요 집에 처치곤란한 ...',
     'info3': '2021-08-14',
     'director3': '하음쿠킹 Haeum Cooking',
     'link3': 'https://www.youtube.com/watch?v=ORQd1W9n4TA'
     },

    {'idx': 4, 'type': 'D',
     'cover': 'https://blog.kakaocdn.net/dn/dPqhNx/btre348O6qb/59pTuaAj4B0hJpeoLnOic0/img.png',
     'suggest': '“독서로 잔잔한 힐링하기!”',
     'img-link1': 'https://bookthumb-phinf.pstatic.net/cover/206/535/20653532.jpg?type=m1&udate=20210912',
     'title1': '오케팅', 'genre1': '특별하지 않아도 누구나 5% 부자가 되는 전략', 'info1': '대한출판사', 'director1': '오두환',
     'link1': 'https://book.naver.com/bookdb/book_detail.nhn?bid=20653532',
     'img-link2': 'https://bookthumb-phinf.pstatic.net/cover/196/181/19618143.jpg?type=m1&udate=20210912',
     'title2': '소크라테스 익스프레스', 'genre2': '철학이 우리 인생에 스며드는 순간', 'info2': '어크로스', 'director2': '에릭 와이너',
     'link2': 'https://book.naver.com/bookdb/book_detail.nhn?bid=19618143',
     'img-link3': 'https://bookthumb-phinf.pstatic.net/cover/207/771/20777131.jpg?type=m1&udate=20210912',
     'title3': '달러구트 꿈 백화점2', 'genre3': '단골손님을 찾습니다', 'info3': '팩토리나인', 'director3': '이미예',
     'link3': 'http://book.naver.com/bookdb/book_detail.nhn?bid=20777131'},

    {'idx': 5, 'type': 'F',
     'cover': 'https://blog.kakaocdn.net/dn/piJdH/btre5a1KXg3/Esxzje14oW7jg0bGtYfkD0/img.png',
     'suggest': '“오감만족! 넷플릭스 시청하기”',
     'img-link1':'https://images.justwatch.com/poster/246775914/s166',
     'title1':'알고있지만,',
     'genre1':'드라마, 로맨스',
     'info1':'시간 01:10분',
     'director1':'감독 : Kim Ga-ram',
     'link1':' https://www.netflix.com/kr/title/81435649',
     'img-link2':'https://images.justwatch.com/poster/116767348/s166',
     'title2':'킹덤',
     'genre2':'SF, 공포, 드라마, 스릴러, 액션',
     'info2':'',
     'director2':'출연자 : 주지훈, 류승룡, 배두나',
     'link2':' https://www.netflix.com/kr/title/80180171',
     'img-link3':'https://images.justwatch.com/poster/239555642/s166',
     'title3':'스위트홈',
     'genre3':'SF, 드라마',
     'info3':'',
     'director3':'감독 : Lee Eung-bok',
     'link3':' https://www.netflix.com/kr/title/81061734'}
]

likeDoc = [
    {'idx': 1, 'name':'like', 'count': 0},
]



db.qna.insert_many(doc);
db.ans.insert_many(ansDoc);
db.like.insert_many(likeDoc);