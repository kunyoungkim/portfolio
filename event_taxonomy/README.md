### 이벤트 텍소노미 정의
**1. 핵심 지표 설정**
- 부동산 중개 플랫폼 특성상 이사를 하는 주기에만 앱을 사용하므로, Retention보다는 유저가 중개사에게 문의를 남기는 데까지의 Activation 퍼널이 가장 중요하다고 판단.
- 데이터 분석을 통해 중개사 매출과 유저로부터 받은 문의수와의 상관관계 파악
<br>

**2. Activation 퍼널 전환율 파악을 위한 이벤트 텍소노미 정의**
- GA4, Firebase를 통해 웹앱 통합 이벤트 정의
- 퍼널 단계별 페이지뷰 및 클릭 이벤트 정의
- 코호트별로 전환율을 비교하기 위해 다양한 매개변수 수집(빌딩 타입, 매물 가격, 로그인 타입 등) 
![image](https://github.com/user-attachments/assets/828096b3-fe88-4ffd-9085-cc6acedcb7b0)
<br>

**3. GTM 및 개발자와 협업을 통해 이벤트 수집 시작**
- 이벤트 이름 카더널리티를 줄이기 위해 page_id와 같은 매개변수 수집이 가능하게 개발자에게 요청
- WEB: GTM의 사용자 맞춤 자바스크립트 변수를 통해 백엔드에서 보내주는 데이터와 hr태그의 속성 및 속성 값를 통해 page_id 등 매개변수를 수집
- APP: 이벤트 및 매개변수를 WEB과 동일하게 맞추고, platform 매개변수로 구분. 개발자에게 이벤트 설치 요청.
![image](https://github.com/user-attachments/assets/92d3c38d-0b86-40db-9120-78857715885a) ![image](https://github.com/user-attachments/assets/3a39dc1f-7dfa-487d-b6b3-af0389a7f681)

<br>

**4. 측정 시작**
