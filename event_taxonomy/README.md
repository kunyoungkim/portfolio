# 프로젝트 목적
이벤트 택소노미가 가독성 좋게 정의되어있지 않고, app은 사용자 행동데이터를 수집하고 있지 않다. web과 app은 사용자 경험이 다르기 때문에 통합적으로 이벤트를 수집한 뒤, 플랫폼으로 나눠서 데이터를 확인해야한다. 이렇게 확인한 데이터로 개선하려고 하는 지표는 다음과 같다.
- Activation 퍼널 전환률
    - 이벤트 기반 세그먼트별 전환률 차이 확인 후, 전환률이 높은 세그먼트의 행동을 유도
    - 사용자 속성 세그먼트별 전환률 차이 확인 후, 전환률이 높은 세그먼트의 행동을 유도
    - 퍼널 이탈률이 높은 지점에서 CRM 마케팅
    - 퍼널 이탈률이 높은 지점에서 퍼널 순서 바꾸기 또는 퍼널 단계 축소
    - ...
<br>

# 프로젝트 상세 개요
- Period: 2023.02.27 ~ 2024.04.26
- Tool: GA4, GTM, Firebase
- Programming Languages: JavaScript
<br>

# 프로젝트 내용
## 1. 매출로 이어지는 핵심 Activation 퍼널 설정
- 중개사: 매물 광고 문의 퍼널
- 임대인: 매물 등록 퍼널
- 임차인: 문의 퍼널
<br>

## 2. 사용자 행동 데이터 수집할 툴 선정
- 무료로 웹, 앱 이벤트 수집이 모두 가능한 GTM, Firebase를 활용하기로 결정
- 이후 GA4, 루커로 퍼널 및 주요 이벤트를 모니터링 할 수 있는 대시보드 제작하기로 결정
<br>

## 3. Activation 퍼널 전환율 파악을 위한 이벤트 텍소노미 정의
- GA4, Firebase를 통해 수집할 웹앱 통합 이벤트 정의
- 이벤트 택소노미 정의 방식
    - 퍼널 단계별 페이지뷰 및 클릭 이벤트 정의
    - 같은 경험의 이벤트라면, 똑같은 이벤트 이름 사용(장점: 가독성, GTM 태그 및 트리거 관리의 편의성)
    - pcweb, moweb, ios, aos 총 4개 플랫폼의 이벤트 이름 및 매개변수를 똑같이 맞춤(장점: 가독성, GA4에서 간단하게 통합적으로 데이터를 살펴볼 수 있음)
    - 모든 이벤트에 고정적으로 사용할 수 있는 매개변수는 모든 이벤트에 사용(장점: 세그먼트를 나눌때 간편하게 나눌 수 있음)
![image](https://github.com/user-attachments/assets/828096b3-fe88-4ffd-9085-cc6acedcb7b0)
<br>

## 4. GTM 및 개발자와 협업을 통해 이벤트 수집 시작
- WEB 데이터 수집: 백엔드에서 데이터 레이어로 보내주는 데이터와 프론트에서 세팅해준 hr태그의 속성 값을 수집할 있게 [GTM의 사용자 맞춤 자바스크립트 변수](https://github.com/kunyoungkim/portfolio/blob/main/event_taxonomy/gtm_hr_tag.js)로 설정하여 트리거 및 매개변수로 활용
- APP 데이터 수집: 이벤트 및 매개변수를 WEB과 동일하게 맞추고, platform 매개변수로 구분. 앱 개발자에게 Firebase로 이벤트 설치 요청
- QA: PCWEB, MOWEB은 GTM으로, iOS, Andriod는 Firebase Analytics로 디버깅 모두 직접 진행 후, 최종적으로 운영 서버에 배포
  
<div style="display: flex; align-items: center; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/57b82158-ef1f-439f-b1dc-d5f1a276438a" alt="Image 1" style="width: 45%;"/>
    <img src="https://github.com/user-attachments/assets/7b0656c9-5519-47ba-9407-d0d638af4c83" alt="Image 2" style="width: 45%;"/>
</div>
