## 📚 목차

1. [프로젝트 개요](#-프로젝트-개요)

2. [팀](#-팀)
   
3. [서비스 소개](#-서비스-소개)
  
    1. [서비스 기획 목표](#서비스-기획-목표)
   
    2. [ERD](#ERD)
   
    3. [Component Structure](#Component-Structure)

    4. [구현 기능](#구현-기능)

    5. [영화 추천 알고리즘](#영화-추천-알고리즘)
   
4. [설치 및 실행](#-설치-및-실행)
   
5. [오픈소스 출처](#-오픈소스-출처)
   
6. [느낀점](#-느낀점)

<hr>

## OTTogether 프로젝트 개요

#### 1. 기간
2024.05.16 ~ 2024.05.23

#### 2. 기술 스택
- Vue
- Django
- Sqlite3


<br></br>


## 팀
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/MINJOO-KIM"><img src="https://avatars.githubusercontent.com/u/64532143?v=4" width="100px;" alt=""/><br /><sub><b>FE : 김민주</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/seonminKim1122"><img src="https://avatars.githubusercontent.com/u/124031561?v=4" width="100px;" alt=""/><br /><sub><b>BE : 김선민</b></sub></a><br /></td>
    </tr>
  </tbody>
</table>


<br></br>

## 서비스 소개

#### 1. 서비스 기획 목표
- 설문을 통해 선호하는 장르, 감독, 배우 정보를 파악하고 이를 바탕으로 영화 추천
- 추천된 영화를 시청할 수 있는 OTT 플랫폼에 대한 정보 제공
- OTT 계정 공유를 통해 추천 받은 영화를 보다 저렴하게 볼 수 있는 기회 제공

<br>

#### 2. ERD
[OTTogether ERD](https://www.erdcloud.com/d/wnBKgdEYokYj8EfQF)

![image](https://github.com/MINJOO-KIM/Movie/assets/124031561/50c6fcf2-67ad-428e-88e1-5635e83f44e7)

<br>

#### 3. Component Structure

<br>

#### 4. 구현 기능
<table>
  <thead>
    <tr>
      <th>Navbar 를 통한 이동</th>
      <th>취향 설문</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
    </tr>
  </tbody>
  <thead>
    <tr>
      <th>영화 추천</th>
      <th>영화 상세 조회</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
    </tr>
  </tbody>
  <thead>
    <tr>
      <th>회원가입</th>
      <th>로그인</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
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
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
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
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
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
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
      <td><img src="https://www.loomly.com/hs-fs/hubfs/Imported_Blog_Media/earth-Apr-03-2024-12-19-31-1897-AM.gif?width=540&height=540&name=earth-Apr-03-2024-12-19-31-1897-AM.gif" width="400px"></td>
    </tr>
  </tbody>
</table>

#### 5. 영화 추천 알고리즘
- 취향 기반 영화 추천 알고리즘은 '필터링'에 기반합니다.
- 유저가 입력한 '최근 재미있게 본 영화'로부터 '장르, 감독, 배우' 정보를 추출하고 추가 선택 입력 사항이 있는 경우 이를 포함시킵니다.
- (장르, 감독, 배우) => (장르, 감독) => (장르, 배우) => (장르) 순으로 조건을 만족하는 영화를 탐색하고 찾은 영화가 5개 이상 되는 순간 추가 탐색을 하지 않고 추천 영화를 반환합니다.
- 이미 추천 받은 영화가 있는 경우 해당 영화는 제외하고 조회하여 중복 추천을 방지합니다.

<br></br>
