## 📚 목차

1. [프로젝트 개요](#프로젝트-개요)

2. [팀](#팀)
   
3. [서비스 소개](#서비스-소개)
  
    1. [서비스 기획 목표](#1-서비스-기획-목표)
   
    2. [ERD](#2-erd)
   
    3. [Component Structure](#3-component-structure)

    4. [구현 기능](#4-구현-기능)

    5. [영화 추천 알고리즘](#5-영화-추천-알고리즘)
   
4. [설치 및 실행](#설치-및-실행)
   
5. [느낀 점](#느낀-점)


<hr>

## 프로젝트 개요

#### 1. 기간
2024.05.16 ~ 2024.05.23

#### 2. 개발 환경
- Vue 3.4.27
- Pinia 2.1.7
- Django 4.2.13
- Sqlite3 3.21.0
- HTML/CSS/JavaScript

#### 3. 팀 노션
[OTTogether](https://hail-cave-17f.notion.site/3301bf3f454f40d2ac56d909186a0a42?pvs=4)

#### 4. 프로젝트 파일 구조

#### Frontend
```
📦src
 ┣ 📂assets
 ┃ ┣ 📜arrow-left-circle.svg
 ┃ ┣ 📜box-arrow-in-right.svg
 ┃ ┣ 📜caret-down-square.svg
 ┃ ┣ 📜coin.svg
 ┃ ┣ 📜disneyplus.svg
 ┃ ┣ 📜main-img.png
 ┃ ┣ 📜movie-repeat.svg
 ┃ ┣ 📜netflix.svg
 ┃ ┣ 📜person-add.svg
 ┃ ┣ 📜recommend-rewrite.svg
 ┃ ┗ 📜watcha.svg
 ┣ 📂components
 ┃ ┣ 📂common
 ┃ ┃ ┣ 📜MovieNavbar.vue
 ┃ ┃ ┗ 📜OTTNavbar.vue
 ┃ ┣ 📂movies
 ┃ ┃ ┣ 📜MovieCard.vue
 ┃ ┃ ┣ 📜MovieDetailInfo.vue
 ┃ ┃ ┣ 📜MovieRecommend.vue
 ┃ ┃ ┗ 📜Recommend.vue
 ┃ ┗ 📂otts
 ┃ ┃ ┣ 📜MyPartyCard.vue
 ┃ ┃ ┣ 📜MyPartyCreated.vue
 ┃ ┃ ┣ 📜MyPartyJoined.vue
 ┃ ┃ ┗ 📜PartyCard.vue
 ┣ 📂router
 ┃ ┗ 📜index.js
 ┣ 📂stores
 ┃ ┗ 📜movie.js
 ┣ 📂views
 ┃ ┣ 📜AIRecommendView.vue
 ┃ ┣ 📜HomeView.vue
 ┃ ┣ 📜LoginView.vue
 ┃ ┣ 📜MovieDetailView.vue
 ┃ ┣ 📜MyPageView.vue
 ┃ ┣ 📜OTTHomeView.vue
 ┃ ┣ 📜PartyCreateView.vue
 ┃ ┣ 📜PartyJoinView.vue
 ┃ ┗ 📜SignupView.vue
 ┣ 📜App.vue
 ┗ 📜main.js

```


<br></br>


## 팀
<table>
   <thead>
      <th>이름</th>
      <th>역할</th>
   </thead>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/MINJOO-KIM"><img src="https://avatars.githubusercontent.com/u/64532143?v=4" width="100px;" alt=""/><br /><sub><b>FE : 김민주</b></sub></a><br /></td>
       <td>
          <ul>
             <li>UI/UX 디자인, CSS</li>
             <li>영화 취향 입력, 추천, 상세 페이지 프론트엔드 기능 구현</li>
             <li>OTT 공유 커뮤니티 페이지 프론트엔드 기능 구현</li>
             <li>회원가입, 로그인 페이지 프론트엔드 기능 구현</li>
          </ul>
       </td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/seonminKim1122"><img src="https://avatars.githubusercontent.com/u/124031561?v=4" width="100px;" alt=""/><br /><sub><b>BE : 김선민</b></sub></a><br /></td>
       <td>
          <ul>
             <li>API 서버 개발</li>
             <li>취향 기반 영화 추천 알고리즘 개발</li>
             <li>Open AI API 를 활용한 AI 기반의 영화 추천 기능 개발</li>
             <li>전반적인 CSS 작업</li>
          </ul>
       </td>
    </tr>
  </tbody>
</table>



<br></br>

## 서비스 소개

### 1. 서비스 기획 목표
- 설문을 통해 선호하는 장르, 감독, 배우 정보를 파악하고 이를 바탕으로 영화 추천
- 추천된 영화를 시청할 수 있는 OTT 플랫폼에 대한 정보 제공
- OTT 계정 공유를 통해 추천 받은 영화를 보다 저렴하게 볼 수 있는 기회 제공

<br>

#### 목표 구현 체크리스트
[Account]
- [X] 토큰 기반 인증 시스템
- [ ] Token 모델 커스텀을 통한 유효 기간 설정
- [ ] https 및 refresh token 적용을 통한 보안 강화

[OTT]
- [X] OTT 계정 공유 서비스 CRUD

[Recommendation]
- [X] 취향 설문 기반 영화 추천 기능
- [X] 기 추천 영화 목록 바탕 중복 추천 방지
- [X] 동적 쿼리 작성을 통한 영화 필터링 코드 단순화
- [X] Open AI API, TMDB API 를 활용한 영화 추천 및 DB 확장

[Development]
- [X] 상황에 맞는 status code 및 response data 응답
- [X] 예외 처리를 통해 예상치 못한 상황에도 서비스 이용에 문제가 없도록 구현
- [X] Pinia 및 Local Storage 를 활용한 상태 관리
- [X] SPA 구현 및 확장성을 컴포넌트 구조화
- [ ] 중복 로직 함수화를 통한 유지보수 편의성 증대

[Search]
- [X] 레벤슈타인 거리 기반 DB 검색
- [ ] DB에 존재하는 값 바탕으로 유저 입력값 자동완성



<br>

### 2. ERD
[OTTogether ERD](https://www.erdcloud.com/d/wnBKgdEYokYj8EfQF)

![image](https://github.com/MINJOO-KIM/Movie/assets/124031561/50c6fcf2-67ad-428e-88e1-5635e83f44e7)

<br></br>

### 3. Component Structure
![Untitled](https://github.com/MINJOO-KIM/Movie/assets/124031561/b1a8096d-6184-4d80-b55a-982298213a4c)

<br></br>


### 4. 구현 기능
<table>
  <thead>
    <tr>
      <th>Chat GPT 기반 영화 추천</th>
      <th>취향 설문</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="assets\ai-recommend.gif" width="400px"></td>
      <td><img src="assets\survery.gif" width="400px"></td>
    </tr>
  </tbody>
  <thead>
    <tr>
      <th>취향 기반 영화 추천</th>
      <th>영화 상세 조회</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="assets\survery-recommend.gif" width="400px"></td>
      <td><img src="assets\movie-detail.gif" width="400px"></td>
    </tr>
  </tbody>
  <thead>
    <tr>
      <th>회원가입</th>
      <th>로그인/로그아웃</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="assets\signup.gif" width="400px"></td>
      <td><img src="assets\login-logout.gif" width="400px"></td>
    </tr>
  </tbody>
  <thead>
    <tr>
      <th>계정 공유 파티 개설</th>
      <th>계정 공유 파티 조회</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="assets\party-create.gif" width="400px"></td>
      <td><img src="assets\party-search.gif" width="400px"></td>
    </tr>
  </tbody>
  <thead>
    <tr>
      <th>계정 공유 파티 참여</th>
      <th>마이 페이지</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="assets\party-participate.gif" width="400px"></td>
      <td><img src="assets\my-page.gif" width="400px"></td>
    </tr>
  </tbody>
  <thead>
    <tr>
      <th>계정 공유 파티 수정</th>
      <th>계정 공유 파티 탈퇴</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="assets\party-update.gif" width="400px"></td>
      <td><img src="assets\party-leave.gif" width="400px"></td>
    </tr>
  </tbody>
</table>

<br><br>
### 5. 영화 추천 알고리즘

#### 사용자 취향 기반 영화 추천
- 취향 기반 영화 추천 알고리즘은 `필터링`에 기반합니다.
- 유저가 입력한 '최근 재미있게 본 영화'로부터 '장르, 감독, 배우' 정보를 추출하고 추가 선택 입력 사항이 있는 경우 이를 포함시킵니다.
- 추출한 정보와 DB 에 저장된 정보를 비교해 `레벤슈타인 거리`가 가장 짧은 대상이 유저가 입력한 정보의 대상이라고 판단합니다.
- 결과 정보를 바탕으로 (장르, 감독, 배우) => (장르, 감독) => (장르, 배우) => (장르) 순으로 조건을 만족하는 영화를 조회합니다.
- 조회 결과가 5개가 되는 순간 추가 탐색을 하지 않고 추천 영화를 반환합니다.
- 이미 추천 받은 영화가 있는 경우 해당 영화는 제외하고 조회하여 중복 추천을 방지합니다.
<br><br>

#### ※ 레벤슈타인 거리란?
두 비교군의 삽입, 삭제, 교체 연산에 대한 비용을 계산하여 연산 비용이 높을 수록 다르다고 판단하는 방법
<br><br>
일반적으로 영화 제목, 선호하는 감독, 배우 등의 정보는 입력 시 DB 에 저장된 문자열과 아주 근소한 오차가 존재할 가능성이 높으므로 레벤슈타인 거리를 이용하면 올바른 조회가 가능할 것이라 생각하여 적용

<hr>

#### AI 영화 추천
- `Open AI API` 를 활용한 영화 추천
- 유저가 입력한 쿼리에 자체 제작한 프롬프트를 적용해 영화 제목을 리스트 형태로 받고, TMDB API 를 이용해 영화의 ID 및 상세 정보를 조회합니다.
- 현재 자체 DB 에 저장되어 있지 않은 영화인 경우 DB 에 저장 후 반환하고, 저장되어 있는 경우 DB 에서 데이터를 꺼내 반환합니다.
- 이를 통해 AI 기반 추천은 물론 서비스 운영을 지속할 수록 자체 DB 를 확장할 수 있습니다.

<br></br>


## 설치 및 실행
### 1. 프로젝트 다운로드
  ```
  git clone [GITHUB_URL]
  ```
<br>

### 2. 패키지 설치
  ```python
  # django 프로젝트(backend) 로 이동 후
  pip install -r requirements.txt
  ```

  ```javascript
  // vue 프로젝트(front/movie-recommend) 로 이동 후
  npm install
  ```
<br>

### 3. `.env` 파일 생성 및 API 키 작성
django 프로젝트(backend) 바로 아래에 .env 파일을 생성하고 아래와 같이 작성합니다.
```
OPEN_AI_API_KEY='your_open_ai_api_key'
TMDB_API_TOKEN='your_tmdb_api_token'
``` 
<br>

### 4. Migration
```python
# django 프로젝트(backend) 로 이동 후
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data.json
```
<br>

### 5. 실행
```python
# django 프로젝트(backend) 로 이동 후
python manage.py runserver
```

```javascript
// vue 프로젝트(front/movie-recommend) 로 이동 후
npm run dev
```


<br></br>

## 느낀 점
### 김민주
프론트엔드와 백엔드의 통신을 통해 데이터를 원하는 형태로 화면에 보여주는 방법을 이해할 수 있었습니다. 특히 API 명세서를 활용하여 요청과 응답에 필요한 코드를 작성하면서 서로 소통하고 있다는 것을 느꼈습니다.<br>
백엔드 측에서 보내주는 상태코드를 그저 동작이나 에러 확인용을 넘어서 내부 동작에서도 활용할 수 있다는 것을 알게 되었습니다.<br>
프론트엔드를 혼자 담당하여 프로젝트를 진행하다보니 시간 안에 끝내야한다는 압박감은 있었지만 하나 하나씩 해결해나간다는 마음으로 완성할 수 있었습니다.<br>
 상태 코드와 에러메시지를 보면서 에러 또한 하나씩 해결해나가고, 협업하며 성취감을 느낄 수 있던 시간이었습니다. 개발을 하면서 어떤 점을 더 꼼꼼하게 신경쓰고, 어떤 부분에 대해 고민해야하는지 시야를 넓힐 수 있었습니다. 


<br><br>

### 김선민
API 서버를 설계하고 구축하면서 성공적으로 로직을 수행하는 상황 뿐만 아니라 여러 예외 상황들에 대해 고려하고 각 상황에 맞는 응답을 하는 것의 중요성을 배울 수 있는 프로젝트였습니다.<br>
특히 파티 참여와 같이 동일한 400 code 더라도 이미 참여하고 있는 파티라서 참여가 이루어지지 않은 건지, 파티에 인원이 가득 차서 참여가 이루어지지 않은 건지 등을 구분하여 response data 를 구성하였습니다.<br>
이를 통해 유저 입장에서 현재 내가 어떤 문제에 봉착한 상황인지를 인지할 수 있게 하여 유저가 서비스를 이용하는 데 어려움을 덜어줄 수 있다는 점을 배웠습니다.


<br></br>

##  예상되는 기술적인 질문 2가지
### [Frontend]<br>
### Q. props란 무엇인가요?
#### A.
props 는 상위 컴포넌트에서 하위 컴포넌트로 데이터를 전달할 때 사용하는 옵션입니다.<br><br>
vue 의 데이터 흐름은 위에서 아래로 흐르기 때문에 하위 컴포넌트에서 상위 컴포넌트의 state 를 직접 참조할 수 없습니다.<br><br>
따라서 props 를 사용하는 것이고 props 통해 state 가 전달되면 전달 받은 컴포넌트의 속성이 됩니다.

<br><br>

### Q. Vue 에서 pinia 를 사용하는 이유가 무엇인가요?
#### A.
pinia 는 전역 상태 뿐만 아니라 개별 컴포넌트에서만 필요한 로컬 상태도 관리할 수 있으며 컴포넌트 간 상태 공유를 쉽게 할 수 있다는 장점이 있습니다.<br><br>
pinia 는 Vue 3 의 reactive 함수를 사용해 상태를 관리하는데 이를 통해 상태 변화를 실시간으로 추적하고 반응형으로 처리하여 성능 최적하에 용이합니다.

### [Backend]<br>
### Q. 필터링 쿼리를 만드는 부분에서 Q 객체를 이용했다. QuerySet 에 filter 를 통해서도 필터링이 가능한데 Q 객체를 사용해서 필터링 쿼리를 만든 이유가 무엇인가요?

#### A. 
Q 객체를 이용하면 필터링 조건의 입력에 따라 동적으로 필터링 쿼리를 만들 수 있어 코드가 간결해지고 이로 인해 유지보수도 보다 편리해진다고 생각했습니다. <br><br>
현재 필터링 조건은 장르, 감독, 배우 3가지인데 각 요소의 입력 여부에 따라 총 8가지 경우의 수가 나올 수 있습니다.<br><br>
동적으로 쿼리를 만들지 않게 되면 모든 케이스에 대한 분기 처리를 해주어야 하므로 if-elif-else 문이 남발되어 코드가 복잡해질 가능성이 있고, 필터링 요소가 추가되는 경우 기하급수적으로 코드의 복잡도가 높아질 수 있는 문제가 있습니다.<br><br>
반면 Q 객체를 이용하여 입력이 존재할 때만 필터링 쿼리에 추가하는 방식을 사용하면 필터링 요소가 증가하더라도 손쉽게 이를 구현할 수 있는 장점이 있다고 생각했습니다. 
