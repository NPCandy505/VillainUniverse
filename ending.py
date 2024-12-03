from connect import *
#텍스트 수정완료
@app.route('/ending_1', methods=['POST'])
def ending_1():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    user_name = get_user_name(user_id)
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.background_8,
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": """“벌써 나왔네요?”
익숙한 목소리에 옆을 돌아보니 강권주 센터장님이 서있었다. 그런데 센터장님이 어떻게 여기에..? 그때, 무전기가 연결되었다.
“""" + user_name + """ 형사님 들리십니까? 강권주 센터장입니다. 섬에 들어간다는 무전 이후로 연결이 끊겨 구조대를 파견하려던 참입니다. 지금 어떤 상황입니까? 왜 제 목소리가 거기서 들리는 거죠?”
‘그럴 리가 없다. 분명 센터장님과 계속 무전을 했는데...’
“형사님 들리십니까? """+ user_name + """ 형사님!!”"""
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "다음",
                    "action": 'block',
                    "blockId": blockId.엔딩_2
                }
            ]
        }
    }
    
    
    save_block(user_id, block_id)
    return jsonify(res)

@app.route('/ending_2', methods=['POST'])
def ending_2():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.background_9,
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": """“당신과 나는 아주 특별한 운명을 타고 났어요. 당신은 살리고, 나는 죽이고...”

--------------------
최종 빌런의 정체가 궁금하다면 <보이스4> tvN 6/18(금) 첫방송 에서 확인하세요!"""
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "이벤트 참여하기",
                    "action": 'block',
                    "blockId": blockId.이벤트
                }
            ]
        }
    }
    
    save_block(user_id, block_id)
    return jsonify(res)

@app.route('/event', methods=['POST'])
def event():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    user_name = get_user_name(user_id)
    
    save_block(user_id, block_id)
    return response_from("""[이벤트 참여권]

""" + user_name + """ 요원! 미션 완수를 축하드립니다!
OCN <빌런유니버스> 이벤트에 참여하여 골드바 획득 기회를 얻으세요!
현재 화면을 캡쳐하신 후 본인 인스타그램에 6월 18일 자정까지 #빌런유니버스 #이벤트 #OCN 을 태그하여 올려주시면 추첨을 통해 10분께 '순금 미니 골드바'를 드립니다.""",
            quickReplies = [
                {
                    "label": "처음으로 돌아가기",
                    "action": 'block',
                    "blockId": blockId.인트로_1
                }
            ])

