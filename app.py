from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.what_today


## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/', methods=['GET'])
def home():
    return render_template('main.html')

@app.route('/Question', methods=['GET'])
def Question():
    return render_template('question.html')

@app.route('/answer', methods=['GET'])
def result():
    return render_template('answer.html')

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

# =======================
# 좋아요 가져오기
@app.route('/like', methods=['GET'])
def showLike():
    likeCount = list(db.like.find({}, {'_id': False}))
    return jsonify({'likedb': likeCount})

# 좋아요 수정 +1
@app.route('/like/+', methods=['POST'])
def likePlus():
    targetName = request.form['name_give']
    targetLike = db.like.find_one({'name': targetName})
    currentLike = targetLike['count']
    newLike = currentLike + 1
    db.like.update_one({'name': targetName}, {'$set': {'count': newLike}})
    return jsonify({'msg': '좋아요 완료!'})

# 좋아요 수정 -1
@app.route('/like/-', methods=['POST'])
def likeMinus():
    targetName = request.form['name_give']
    targetLike = db.like.find_one({'name': targetName})
    currentLike = targetLike['count']
    newLike = currentLike - 1
    db.like.update_one({'name': targetName}, {'$set': {'count': newLike}})
    return jsonify({'msg': '좋아요 취소ㅠㅠ'})

# =======================
# 퀴즈정보가 있으면 findDB로 연결(idx 번호롤 판단) / 다음 퀴즈 없는경우(idx번호 없을 때) 실패 반환
@app.route('/quiz', methods=['GET'])
def getQuiz():
    idx = request.args.get('idx')
    if idx is not None:
        data = findDB(idx)
        return jsonify({'result': 'success', 'quiz': data})
    return jsonify({'result': 'fail'})

# DB에서 퀴즈 정보 가져오기
def findDB(idx):
    data = list(db.qna.find({"idx": int(idx)}, {'_id': False}))
    return data

# 결과지 가져오기
@app.route('/ans', methods=['GET'])
def getAns():
    type = request.args.get('type')
    if type is not None:
        data = findAnsDB(type)
        return jsonify({'result': 'success', 'ans': data})
    return jsonify({'result': 'fail'})

# DB에서 결과값 찾기
def findAnsDB(type):
    data = list(db.ans.find({"type": type}, {'_id': False}))
    return data

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
