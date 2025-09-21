# 🍽️ Delicious in Seoul (Django)

**Django 학습 프로젝트**  
위코드 부트캠프 이후 복습 겸 제작한 음식점 검색 & 커뮤니티 API 서버입니다.  
회원가입/로그인, 음식점 데이터 관리, 커뮤니티 게시판 기능 등을 구현했습니다.

---

## 📌 개발 개요
- **개발 목적**: Django 심화 학습 및 AWS/S3, 카카오 API 적용 경험
- **개발 기간**: 2022년 7월 (개인 복습 프로젝트)
- **개발 인원**: 1명 (정지민, [@jiminnote](https://github.com/jiminnote))

---

## 🛠️ 사용 기술
- **Backend**: Python, Django, MySQL  
- **Infra**: AWS (S3, EC2, RDS), Boto3  
- **Auth**: JWT, Kakao API 소셜 로그인  
- **ETC**: CORS headers, Logging

---

## ✨ 주요 기능

### 👤 사용자 (Users)
- 회원가입 (이메일/비밀번호 유효성 검증 포함)
- 로그인 / JWT 토큰 발급
- 사용자 정보 관리

### 🍴 음식점 (Restaurants)
- 메인 카테고리 / 서브 카테고리 분류
- 음식점 상세정보 (주소, 전화번호, 주차 여부, 운영시간 등)
- 메뉴 및 가격 관리
- 음식점 이미지 업로드 (AWS S3)

### 📝 커뮤니티 (Communities)
- 사용자별 게시글 작성
- 게시글 이미지 업로드
- 지역, 분야, 카테고리 분류

---

## 📂 프로젝트 구조
```
delicious_in_seoul/
┣ communities/      # 커뮤니티 앱
┣ restaurants/      # 음식점/카테고리 앱
┣ users/            # 사용자 앱
┣ core/             # 공통 모듈 (TimestampModel, 유효성 검증 등)
┣ seoul/            # 메인 프로젝트 설정
┣ requirements.txt  # 패키지 목록
┗ manage.py
```

---


## 🚀 실행 방법
```bash
# 가상환경 세팅
python -m venv venv
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
python manage.py runserver
```

---

📝 학습 포인트
* Django 모델링 및 관계 설정 (ForeignKey, ManyToMany)
* 유효성 검증 (Regex 기반 이메일/비밀번호/닉네임 체크)
* JWT 인증과 소셜 로그인(Kakao API)
* AWS S3를 이용한 이미지 업로드
* CORS 설정 및 로깅 환경 구축

⸻

📌 Reference
* Kakao Developers
* AWS Docs
* Django 공식문서
