from connect import *
#끝
@app.route('/basement_4', methods=['POST'])
def basement_4():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    cur_progress = get_progress(user_id) 
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": """벽 너머에는 희미한 모니터 불빛이 어두운 방을 비추고 있었다. 모니터 화면에는 그토록 찾아 헤맨 아이의 모습이 나오고 있었다. 아이는 소름 끼치는 표정을 지으며 카메라를 응시하고 있었다."""
                    }
                },
                {
                    "simpleImage": {
                        "imageUrl": images.background_6_1,
                        "altText": "아이 사진", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": """“센터장님 아이를 찾았습니다. 그런데… 무언가 이상합니다” 음산한 기운에 나는 뒤를 돌아보았다."""
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "뒤를 돌아본다",
                    "action": 'block',
                    "blockId": blockId.지하실_5
                }
            ]
        }
    }
    
    if cur_progress == 4:
        set_progress(user_id, 5)
    save_block(user_id, blockId.지하실_5)
    return jsonify(res)

@app.route('/basement_5', methods=['POST'])
def basement_5():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.background_6,
                        "altText": "아이 확대사진"
                    }
                },
                {
                    "simpleText": {
                        "text": """“너도 카운터냐?”  화면의 아이는 바로 앞까지 다가와 있었다. 숨이 멎을 것 같은 중압감에 아무것도 할 수 없었다."""
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "주변을 둘러본다",
                    "action": 'block',
                    "blockId": blockId.지하실_6
                }
            ]
        }
    }
    
    save_block(user_id, blockId.지하실_6)
    return jsonify(res)

@app.route('/basement_6', methods=['POST'])
def basement_6():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    save_block(user_id, blockId.지하실_7)
    return response_from("""아무것도 보이지 않는다.""",
            quickReplies = [
                {
                    "label": "다시 주변을 둘러본다.",
                    "action": 'block',
                    "blockId": blockId.지하실_7
                }
            ])

@app.route('/basement_7', methods=['POST'])
def basement_7():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    save_block(user_id, blockId.지하실_8)
    return response_from("""아무것도 보이지 않는다. 아이가 점점 다가오고 있다.""",
            quickReplies = [
                {
                    "label": "한번 더 주변을 둘러본다.",
                    "action": 'block',
                    "blockId": blockId.지하실_8
                }
            ])

@app.route('/basement_8', methods=['POST'])
def basement_8():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.problem_5_1,
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleImage": {
                        "imageUrl": images.problem_5_2,
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": """모니터 뒤로 노란 종이가 떨어져 있다. 손을 간신히 움직여 종이를 집었다. ‘부적이다.  뒤는 사용법인 것 같다 ’ 그 순간, 부적을 든 손 아래로 방바닥이 보였다."""
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "다음",
                    "action": 'block',
                    "blockId": blockId.지하실_9
                }
            ]
        }
    }
    
    save_block(user_id, block_id)
    return jsonify(res)

@app.route('/basement_9', methods=['POST'])
def basement_9():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    save_block(user_id, block_id)
    return response_from("""이건 분명...
--------------------
(답을 채팅으로 입력하세요!)""",
            imageUrl = images.problem_5_3,
            quickReplies = [
                {
                    "label": "힌트",
                    "action": 'block',
                    "blockId": blockId.힌트확인
                }
            ])
