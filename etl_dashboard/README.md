# 프로젝트 목적
AAARRR 프레임워크에 따라 전사 OMTM과 팀별 KPI를 설정하고, 이를 매일 모니터링하며 목표 대비 달성률을 체크합니다. 이를 기반으로 피드백을 반복해 지표를 개선합니다. 

# 프로젝트 상세 개요
- Period : 2024.04.29 ~ 2024.06.28 
- Programming Languages : Python(3.10.9), MySQL(8.0.31)
- Cloud : Google Cloud Platform
- Database : MySQL(8.0.31), BigQuery
- API : GA4, Appsflyer, Slack
- Web Framwork : Streamlit (ver.1.28.1)

# 주요 라이브러리 버전
- [requirement.txt](etl_dashboard/requirement.txt) 참조

# 주요 기능
- 본 프로젝트에서 자체 개발 및 활용한 주요 메서드는 다음과 같습니다.

| Funtions | Location | Description |
| --- | --- | --- |
| extract_ga4_data | extract_ga4.py | for fetching data from GA4 API |

# 함수 상세 설명
## extract_ga4_data
