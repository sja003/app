import requests

# Flask 서버 주소
url = "http://127.0.0.1:5000/analyze"

# 보낼 데이터
data = {
    "category": "커피전문점",
    "month": "2025-04"
}

# POST 요청 보내기
response = requests.post(url, json=data)

# 결과 출력
print(response.json())
