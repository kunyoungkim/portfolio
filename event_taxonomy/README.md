## 이벤트 텍소노미 정의
### 1. 핵심 지표 설정
- 매출과 직간접적으로 연관되어있는 지표 정리
- [데이터 분석을 통해 중개사 매출과 후행지표들의 관계 파악](https://github.com/kunyoungkim/portfolio/blob/main/event_taxonomy/sales_analysis.ipynb)
- 부동산 중개 플랫폼 특성상 이사를 하는 주기에만 앱을 사용하므로, Retention과 같은 지표보다는 유저가 중개사에게 문의를 남기는 데까지의 Activation 퍼널에 대한 지표가 가장 중요하다고 판단
<br>

### 2. 사용자 행동 데이터 수집할 툴 선정
- 무료로 사용이 가능하고, GA4에서 데이터를 확인할 수 있게끔 GTM, Firebase를 활용하기로 결정
- join이 필요한 데이터 또는 ETL 작업이 필요한 데이터를 대비하여 빅쿼리에 일 단위 스케줄링 데이터 수집(스트리밍 X)
- Appsflyer의 Attribution 데이터는 MySQL에 적재. Attribution 기준으로 코호트 분석을 할 땐 user_id 기준으로 빅쿼리와 Mysql 데이터를 파이썬으로 join해서 사용하기로 함
<br>

### 3. Activation 퍼널 전환율 파악을 위한 이벤트 텍소노미 정의
- GA4, Firebase를 통해 수집할 웹앱 통합 이벤트 정의
- 퍼널 단계별 페이지뷰 및 클릭 이벤트 정의
- 코호트별로 전환율을 비교하기 위해 다양한 매개변수 수집(빌딩 타입, 매물 가격, 로그인 타입 등)
![image](https://github.com/user-attachments/assets/828096b3-fe88-4ffd-9085-cc6acedcb7b0)
<br>

### 4. GTM 및 개발자와 협업을 통해 이벤트 수집 시작
- 이벤트 이름 카더널리티를 줄이기 위해 page_id와 같은 매개변수 수집이 가능하게끔 개발자에게 요청
- WEB: GTM의 사용자 맞춤 자바스크립트 변수를 통해 백엔드에서 보내주는 데이터와 hr태그의 속성 및 속성 값을 통해 매개변수 수집
- APP: 이벤트 및 매개변수를 WEB과 동일하게 맞추고, platform 매개변수로 구분. 개발자에게 이벤트 설치 요청
- PCWEB, MOWEB, iOS, Andriod 디버깅 모두 직접 진행 후, 최종적으로 운영 서버에 배포
<div style="display: flex; align-items: center; gap: 10px;">
    <img src="https://github.com/user-attachments/assets/57b82158-ef1f-439f-b1dc-d5f1a276438a" alt="Image 1" style="width: 45%;"/>
    <img src="https://github.com/user-attachments/assets/6d08aa16-3d6f-4f46-9831-c379222db970" alt="Image 2" style="width: 45%;"/>
</div>
