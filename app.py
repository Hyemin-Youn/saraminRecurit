from flask import Flask, jsonify, request
from pymongo import MongoClient
from crawl_saramin import crawl_saramin

app = Flask(__name__)

# MongoDB 연결 설정 (JCloud MongoDB 서버 IP 사용)
client = MongoClient('mongodb://localhost:27017/')
db = client['my_database']  # 데이터베이스 이름 설정
collection = db['jobs']     # 컬렉션 이름 설정

# 크롤링 데이터 저장
df = crawl_saramin('python', pages=1)
for _, row in df.iterrows():
    collection.insert_one(row.to_dict())

@app.route('/add_job', methods=['POST'])
def add_job():
    {
    "회사명": "OpenAI",
    "제목": "AI Researcher",
    "링크": "https://example.com/job",
    "지역": "서울",
    "경력": "3년 이상",
    "학력": "대졸",
    "고용형태": "정규직",
    "마감일": "2024-12-31",
    "직무분야": "AI 개발",
    "연봉정보": "면접 후 협의"
    }

    job_data = request.json
    collection.insert_one(job_data)
    return jsonify({'message': 'Job added successfully'}), 201

@app.route('/get_jobs', methods=['GET'])
def get_jobs():
    {
    "회사명": "OpenAI",
    "제목": "AI Researcher",
    "링크": "https://example.com/job",
    "지역": "서울",
    "경력": "3년 이상",
    "학력": "대졸",
    "고용형태": "정규직",
    "마감일": "2024-12-31",
    "직무분야": "AI 개발",
    "연봉정보": "면접 후 협의"
    }

    jobs = list(collection.find({}, {'_id': 0}))  # _id 필드 제외
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)
