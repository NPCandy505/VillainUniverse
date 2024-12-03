from connect import *
#했음.
@app.route('/basement_1', methods=['POST'])
def basement_1():
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
                        "text": """계단 밑은 끝이 보이지 않는 긴 복도였다. 핸드폰 불빛에 의지하며 걸은 지도 한참, 비상구에 쓰일 것 같은 철문이 나타났다. 살짝 힘을 주어 밀자, 문은 저항 없이 열렸다.."""
                    }
                },
                {
                    "simpleImage": {
                        "imageUrl": images.background_5,
                        "altText": "지하실 전경"
                    }
                },
                {
                    "simpleText": {
                        "text": """지하실 내부는 사뭇 다른 느낌의 방이었다. 벽에는 그림들이 가득했고, 최근까지도 사람이 사용했던 것 같은 느낌이 들었다. 
“이건..” 천장에 늘어뜨려진 와이어에 어울리지 않는 흰 종이가 붙어있었다. 오른팔을 쭉 뻗어 종이를 낚아챘다.  종이에는 알파벳 대문자 F가 크게 쓰여 있었다.  """
                    }
                },
            ] if cur_progress == 3 else [
                {
                    "simpleImage": {
                        "imageUrl": images.background_5,
                        "altText": "지하실 전경"
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "지하실 중앙의 큰 그림을 살펴본다.",
                    "action": 'block',
                    "blockId": blockId.지하실_2
                },
                {
                   "label": "큰 그림 옆의 작은 그림들을 살펴본다.",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ]
        }
    }
    
    if cur_progress == 3:
        set_progress(user_id, 4)
    save_block(user_id, block_id)
    return jsonify(res)


@app.route('/basement_2', methods=['POST'])
def basement_2():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    save_block(user_id, block_id)
    return response_from("""자세를 잡은  커다란 목각인형 그림, 그리고 또 다른 알파벳 종이가 있었다. 그림 구석의 먼지를 털어내자, 아주 작게 작가의 이름으로 보이는 한자가 쓰여있었다. ‘金木雅之’""", imageUrl = images.problem_4[0],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_1
                }
            ])



@app.route('/basement_3', methods=['POST'])
def basement_3():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    num = ['첫', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉', '열']
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "thumbnail": {
                                    "imageUrl": images.card_problem_4[i+1]
                                }
                            } for i in range(10)
                        ]
                    }
                },
                {
                    "simpleText": {
                        "text": """--------------------
(답을 채팅으로 입력하세요!)"""
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "돌아가기",
                    "action": 'block',
                    "blockId": blockId.지하실_1
                },
                {
                    "label": "힌트",
                    "action": 'block',
                    "blockId": blockId.힌트확인
                }
            ] + [
                {
                    "label": num[i] + """ 번째 그림""",
                    "action": 'block',
                    "blockId": blockId.목각인형[i]
                } for i in range(10)
            ]
        }
    }
    
    save_block(user_id, block_id)
    return jsonify(res)


