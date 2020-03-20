-- 동아리 분류 삽입 

-- 문화 / 체육 분과
insert club_types (club_type_name) values('음악');
insert club_types (club_type_name) values('체육');
insert club_types (club_type_name) values('문화');
insert club_types (club_type_name) values('공연');
-- 종교 / 봉사 분과
insert club_types (club_type_name) values('봉사');
insert club_types (club_type_name) values('종교');
-- 학술 분과
insert club_types (club_type_name) values('학술');

-- 동아리 생성 
-- 1. 문화/체육 분과 
-- 1.1. 중앙 동아리 
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("클래시아" , "클래식 기타를 통한 연주법 배우기, 버스킹 공연" , 1, 0, 4 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("Fire Bat" , "야구를 통한 체력향상과 친목도모" , 1, 0, 5 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("일루젼" , "마술에 대한 이해와 교육" , 1, 0, 6 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("화소" , "꽃을 통한 문화캠페인 기획" , 1, 0, 6 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("렌즈맨" , "사진 촬영, 출사 및 여행" , 1, 0, 6 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("폭시" , "전통무예인 국궁 배우기" , 1, 0, 5 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("러너스 하이" , "등산, 마라톤, 라이딩 등 건강정보공유 및 야외운동 동아리" , 1 ,0, 5,"",1);

-- 1.2. 비 중앙 동아리 
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id,club_desc, user_id)
values ("랠리유" , "테니스 동아리" , 0, 0, 5, "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id,club_desc, user_id)
values ("FNO" , "힙합 공연 비트메이킹 DJ 믹스마스터링" , 0, 0, 7, "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id,club_desc, user_id)
values ("ZOOM" , "디지털 카메라 촬영" , 0, 0, 6, "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id,club_desc, user_id)
values ("D.M" , "댄스, 힙합, 순수무용" , 0, 0, 7, "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id,club_desc, user_id)
values ("데굴데굴" , "볼링을 통한 체력향상 및 친목도모" , 0, 0, 5, "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id,club_desc, user_id)
values ("Plague" , "춤 연습, 춤을 통한 활동 및 친목도모" , 0, 0, 7, "",1);

-- 2. 종교 / 봉사 분과
-- 2.1. 중앙 동아리 
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("동행길" , "교내 길고양이 돌봄" , 1, 0, 9 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("ACT" , "성경공부와 봉사활동 동아리" , 1, 0, 8 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("RCY" , "불우이웃돕기, 공동체의식 함양" , 1, 0, 8 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("보담" , "아동, 노인, 의료, 대외활동, 인형극 봉사" , 1, 0, 8 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("펫밀리" , "반려동물에 대한 이해와 친목도모" , 1, 0, 8 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("뚜벅초가 간다" , "할머니 할아버지와 함께하는 농작물 셰어 프로젝트" , 1, 0, 8 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("가브리엘" , "찬양으로 선교하는 동아리" , 1, 0, 8 , "",1);

-- 2.2. 비 중앙 동아리 
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("은빛샘" , "할아버지 할머니를 위한 무료급식, 치료" , 0, 0, 8, '',1);

-- 3. 학술 분과
-- 3.1. 중앙 동아리 
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("멋쟁이사자처럼" , "IT교육, 웹 플랫폼 개발, 창업 동아리" , 1, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("Draftmation" , "애니메이션 및 미디어컨텐츠 연구 동아리" , 1, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("CREATOR" , "어플리케이션 제작" , 1, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("Team Recovery" , "테이핑 및 물리치료 동아리" , 1, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("Yahait" , "공모전, 창업, 4차 산업, 코딩" , 1, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("불기둥" , "공모전 참여, 기업분석, 증권(주식)연구" , 1, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("ELL" , "법률 스터디" , 1, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("빛감" , "사진, 영상 등 멀티미디어 작품활동" , 1, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("Team M.F.S" , "대학생 자작자동차 대회" , 1, 0, 10 , "",1);

-- 3.2. 비 중앙 동아리
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("Final Cut" , "영화제작 및 평론" , 0, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("DSC Sahmyook" , "Google 기술 개발 프로젝트 동아리" , 0, 0, 10 , "",1);
insert clubs (club_name, club_introduce, is_central, is_united, club_type_id, club_desc, user_id)
values ("에스키스" , "건축 공모전 및 포트폴리오 제작" , 0, 0, 10 , "",1);