# 🎬 FINAL-PJT <span style="color:red">"MOCO"</span>

> #### 🔹 ***MOCO란?*** 
>
> ​				Movie Community의 약자로 영화 데이터 조회 및 커뮤니티 사이트를 제공하는 페이지 입니다.





# 	o. 프로젝트 기간

##### 			💜 시작일 : 2022-05-20 (Fri)

##### 			🧡 기획 및 모델링 : 2022-05-20 (Fri)

##### 			💛 백엔드 구현 : 2022-05-20 (Fri) ~  05-24 (Tue)

##### 			💚 프론트엔드 구현 : 2022-05-23 (Mon) ~ 05-26(Thu)

##### 			💙 발표일 : 2022-05-27 (Fri)





## 	I. 팀원 정보 및 업무 분담 내역

##### 			🤴 <u>강병수</u> (팀장) 

   -  <span style="color:skyblue">**백엔드**</span> => 서버 구축 및 주요 기능 구현 담당, 발표 담당

##### 			👸 <u>김가흔</u> 

- <span style="color:skyblue">**프론트엔드** </span>=> UI 및 컴포넌트 구성 담당, PPT 및 개발일지 담당





## 	II. 목표 서비스 구현 및 실제 구현 정도

#### 			🎯목표 서비스 : 영화 커뮤니티 "MOCO"

##### 							-  TMDB 데이터 및 JSON Data를 활용한 영화 데이터 제공

##### 							-  영화 추천 알고리즘 : 장르별 / 감독별 / 최신순 / 평점순 / 관객수

##### 							-  CRUD 구현을 기반으로 커뮤니티 페이지 제공

##### 							-  USER accounts를 바탕으로 사용자 인증 





## 	III. 데이터베이스 모델링(ERD)



![image-20220520152302252](README.assets/image-20220520152302252.png)



## 	IV. 필수 기능에 대한 설명

#### 			💻 Using : VSCODE, HTML, CSS, JS, ,Axios, BootStrap, FontAwsome

#### 			✔   <span style="color:blue"><u>CRUD</u></span>

##### 						-	*CREATE*  : 게시글 작성, 한줄평 작성, 리뷰 작성, 댓글 작성

##### 						-	*READ*  : 영화 정보 및 디테일 페이지 조회 가능

##### 						-	*UPDATE*  : 사용자 인증된 유저만 수정 가능

##### 						-	*DELETE*  :  사용자 인증된 유저만 삭제 가능



#### 			✔   <span style="color:yellow"><u>Rating</u></span>

##### 						-	JS 기능을 바탕으로 드래그를 통해 별점으로  평점을 표현할 수 있도록 기능 구현



#### 			✔   <span style="color:pink"><u>Movie Recommend</u></span>

##### 						-	장르 코드를 이용하여 일치하는 장르로 나만의 영화 추천 (Django DB 기반)

##### 						-	현재상영작, 차기상영작, 관객수, 평점순을 바탕으로 내림차수를 통한 영화 추천

- ###### axios 통신 데이터를 기반으로 TMDB 데이터를 사용하여 해당 알고리즘 완성



#### ✔   <span style="color:orange"><u>Authority</u></span>

##### -    superuser의 경우, 데이터베이스 영화를 추가하거나 삭제할 수 있는 권한이 주어짐



#### ✔   <span style="color:magenta"><u>Search</u></span>

##### -    TMDB Movie Search를 기반으로 영화 정보 받아오기

##### -    검색 결과시 해당 영화가 데이터 베이스에 없는 경우, 해당 영화를 데이터 베이스에 추가 가능

##### -    검색 결과시 해당 영화가 데이터 베이스에 있는 경우, 중복 추가 경고 메세지창 출력





## 	V. 배포 서버 URL (배포했을 경우)









## 	VI. 기타 (느낀 점)

#### 			🤴🏻강병수

> 

#### 			👸🏻김가흔 

> 



