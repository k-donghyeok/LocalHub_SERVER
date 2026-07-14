# LocalHub Server

부산 관광 장소 데이터를 검색하고, 그 검색 결과에 근거한 챗봇 응답을 제공합니다.


## 실행

만약 .venv 가상환경이 없다면

```powershell
python3 -m venv .venv

# 활성화

source .venv/bin/activate

# install
pip install -r requirements.txt

```

# 실행
```powershell
python -m uvicorn app.main:app --reload
```

OpenAI 응답을 사용하려면ㄴ `.env`를 만들고 API 키를 설정합니다.
키가 없어도 질문의 지역·카테고리를 추출하고 SQLite 검색 결과를 그대로 반환합니다.

## API

`POST /chat`은 자연어 질문에서 GPT로 `location`, `contentTypeIds`를 추출한 뒤 SQLite의
`places` 테이블을 조회합니다. 추출한 `location`은 `places.addr1`, `places.addr2`에 포함되는지로만 검색합니다.

```json
{"query": "해운대 근처 카페 추천해줘"}
```

조회된 장소 후보만 사용해 GPT가 질문과의 관련도 순으로 최대 3곳을 추천합니다.

API 문서는 서버 실행 후 `/docs`에서 확인할 수 있습니다.
