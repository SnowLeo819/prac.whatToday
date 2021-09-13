from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.what_today

db.qna.drop();
db.ans.drop();
db.like.drop();

# 작성중 내용, 완성본 아님

doc = [
    {'idx': 1, 'quiz': "코로나 시국 종료!<br>제일 먼저 가고 싶은 여행지는?", 'ans_01': "도시의 야경을 감상할 수 있는<br>뉴욕", 'ans_02': "다양한 액티비티가 가능한<br>스위스",
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
    # 추천 활동명, 추천멘트 1&2, 추천데이터 1~3위 (이미지주소, 이름, 장르or부제 , 출연진 등 세부 정보 1&2
    # 산책하기 : “ 산책으로 바깥공기 만끽하기! ”,  이미지주소1 이름1 부제1 출판사1, 저자1, 연결링크
    # 홈트하기 : “ 근손실 방지! 홈트하자~”,  https://i.ytimg.com/vi/VNQpP6C1fJg/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAqS476LBFSFFfW3g_e73Y3yupl4g
    #             전신 다이어트 유산소운동 [홈트레이닝], 부제1 출판사1, 저자1, 연결링크
    # 요리하기 : “ 맛있는건 언제나 옳지! 요리! ”,  이미지주소1 이름1 부제1 출판사1, 저자1, 연결링크
    # 독서하기 : “ 독서로 잔잔한 힐링하기! ”,  이미지주소1 이름1 부제1 출판사1, 저자1, 연결링크
    # 넷플릭스 : “ 오감만족! 넷플릭스 시청하기 ”, 이미지주소1 이름1 장르1 출연진1, 상영시간1

    # 주제 : suggest , img-link, title, genre,    info,                     director, link
    #        추천멘트 , 이미지주소, 제목, 장르(부제), 세부정보(상영시간이나 출판사), 감독(저자), 연결링크
    # {'idx': 1, 'type': 'A',
    # 'suggest1': '', 'img-link1': '', 'title1': '', 'genre1': '', 'info1':'', 'director1':'', 'link1': '',
    # 'suggest2': '', 'img-link2': '', 'title2': '', 'genre2': '', 'info2':'', 'director2':'', 'link2': ''
    # 'suggest3': '', 'img-link3': '', 'title3': '', 'genre3': '', 'info3':'', 'director3':'', 'link3': ''},





    {'idx': 1, 'type': 'A', 'suggest': '“ 근손실 방지! 홈트하자~”', 'name': '전신 다이어트 유산소운동 [홈트레이닝]', 'subname': '르라보 어나더 13 EDP',
     'desc': ' 암브록스, 자스민, 이끼, 암브레트 시드 등의 열 세가지 원료들이 섞여 중독성 있는 우디 머스크 계열의 향', 'keyword': ['포근한', '편안한', '성숙한']},

    {'idx': 2, 'type': 'B', 'img-link1':'https://i.ytimg.com/vi/mMxDrgF3yBY/hqdefault.jpg', 'title1':'[운동브이로그] 집순이의 홈트레이닝, 간장계란밥 해먹기, 운동하는 여자🍑',
     'genre1':'안녕하세요 여러분 디제이 아리에요 영상 많이 시청해주셔서 너무감사합니다!! 운동영상은 12분 부터!!!', 'info1':'2021-05-03T12:43:17Z', 'director1':'삐아리 BBI Ari', 'link1':'mMxDrgF3yBY',
     'img-link2':'https://i.ytimg.com/vi/_buwjp1ogAQ/hqdefault.jpg', 'title2':'3개월 맨몸 운동 홈트레이닝 루틴 설명',
     'genre2':'맨몸운동루틴 #홈트레이닝루틴 #맨몸운동변화 맨몸 운동 홈트레이닝으로 3개월 동안 진행한 운동 루틴 질문이 정말 많았어요. 그래서 제가 진행한 운동 루틴을 ...',
     'info2':'2021-01-30T02:00:04Z', 'director2':'습관의힘제이건', 'link2':'_buwjp1ogAQ',
     'img-link3':'https://i.ytimg.com/vi/myNjmnvI6x0/hqdefault.jpg', 'title3':'NO 층간소음 올인원 운동 - 40분 유산소운동 홈트 - 관절에 무리없이 체지방 태우기',
     'genre3':'NO 층간소음 NO 스쿼트 - 40분 유산소운동 홈트 - 관절에 무리없이 체지방 태우기] - 땀 많이 나고 숨이 많이 차는 올인원 운동입니다. NO 층간소음 30동작 유산소 ...',
     'info3':'2021-01-22T11:39:03Z', 'director3':'빅씨스', 'link3':'myNjmnvI6x0'},

    {'idx': 3, 'type': 'C', 'brand': 'Jo Malon', 'eng': 'Lime Basil & Mandarin Cologne', 'kor': '조말론 라임바질앤 만다린',
     'desc': '카리브해의 산들바람에서 실려온 듯한 라임향에 톡 쏘는 바질과 향기로운 백리향이 더해져 독특한 조합을 만들어 냅니다.',
     'keyword': ['상큼한', '신선한', '밝은', '시트러스']},

    {'idx': 4, 'type': 'D',
     'suggest1': '',
     'img-link1': 'https://bookthumb-phinf.pstatic.net/cover/206/535/20653532.jpg?type=m1&udate=20210912',
     'title1': '오케팅', 'genre1': '특별하지 않아도 누구나 5% 부자가 되는 전략', 'info1': '대한출판사', 'director1': '오두환',
     'link1': 'https://book.naver.com/bookdb/book_detail.nhn?bid=20653532',
     'suggest2': '',
     'img-link2': 'https://bookthumb-phinf.pstatic.net/cover/196/181/19618143.jpg?type=m1&udate=20210912',
     'title2': '소크라테스 익스프레스', 'genre2': '철학이 우리 인생에 스며드는 순간', 'info2': '어크로스', 'director2': '에릭 와이너',
     'link2': 'https://book.naver.com/bookdb/book_detail.nhn?bid=19618143',
     'suggest3': '',
     'img-link3': 'https://bookthumb-phinf.pstatic.net/cover/207/771/20777131.jpg?type=m1&udate=20210912',
     'title3': '달러구트 꿈 백화점2', 'genre3': '단골손님을 찾습니다', 'info3': '팩토리나인', 'director3': '이미예',
     'link3': 'http://book.naver.com/bookdb/book_detail.nhn?bid=20777131'},

    {'idx': 5, 'type': 'F', 'brand': 'BYREDO', 'eng': 'LA TULIPE', 'kor': '바이레도 라튤립',
     'desc': '한 계절에 처음 맺는 꽃봉오리처럼 활기 넘치고 매력적이고 낙천적인 느낌의 향수',
     'keyword': ['발랄한', '매력적인', '낙천적인', '플로럴']},
]

likeDoc = [
    {'idx': 1, 'name':'like', 'count': 0},
]



db.qna.insert_many(doc);
db.ans.insert_many(ansDoc);
db.like.insert_many(likeDoc);