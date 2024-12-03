from connect import *
#텍스트 고쳤음!
@app.route('/sharehouse_1', methods=['POST'])
def sharehouse_1():
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
                        "text": """‘옆 건물에서 아이 소리가 들렸다’는 센터장님의 지령을 따라 발길이 닿은 곳은 곧 무너질 듯한 낡은 건물 앞. 고개를 들면 보이는 작은 간판에는 ‘에덴 고시원’이라고 적혀 있었다."""
                    }
                },
                {
                    "simpleImage": {
                        "imageUrl": images.background_4,    #시체
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                 {
                    "simpleText": {
                        "text": """카펫과 테이블, 자루 몇 개가 놓인 평범한 창고 같은 방 한가운데에 시체가 누워있었다. 역한 냄새를 풍기는 시체 옆에는 이상한 사진이 떨어져 있었다."""
                    }
                }
            ] if cur_progress == 2 else [
                {
                    "simpleImage": {
                        "imageUrl": images.background_4,    #시체
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                }
            ],
            "quickReplies": [
                 {
                    "label": "시체를 조사한다.",
                    "action": 'block',
                    "blockId": blockId.고시원_2
                },
               {
                    "label": "방의 물건들을 조사한다.",
                    "action": 'block',
                    "blockId": blockId.고시원_3
               },
                {
                    "label": "이상한 사진을 조사한다.",
                    "action": 'block',
                    "blockId": blockId.고시원_4
               }
            ]
        }
    }
    
    if cur_progress == 2:
        set_progress(user_id, 3)
    save_block(user_id, block_id)
    return jsonify(res)


@app.route('/sharehouse_2', methods=['POST'])
def sharehouse_2():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    save_block(user_id, block_id)
    return response_from("""이미 부패가 시작된 남성의 시신이었다. 특이하게도 모든 치아가 뽑혀 바닥에 나뒹굴고 있었다. 사인은 과다출혈인 것 같았다.""",
            quickReplies = [
                {
                    "label": "돌아간다.",
                    "action": 'block',
                    "blockId": blockId.고시원_1
                }
            ])



@app.route('/sharehouse_3', methods=['POST'])
def sharehouse_3():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    save_block(user_id, block_id)
    return response_from("""특별할 것 없어 보이는 카펫과 테이블이 있었다. 자루 안에는 오래된 공구들이 들어있었다.""",
            quickReplies = [
                {
                    "label": "돌아간다.",
                    "action": 'block',
                    "blockId": blockId.고시원_1
                }
            ])


@app.route('/sharehouse_4', methods=['POST'])
def sharehouse_4():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage":{
                        "imageUrl": images.problem_3,    #사진
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": """사진에는 난잡하게 찍힌 지문들, 그리고 사람의 양손이 찍혀 있었다. 성인보단 확연히 작은 그 손은 아이의 것 같아 보였다.
--------------------
(답을 채팅으로 입력하세요!)"""
                    }
                }
                
            ],
            "quickReplies": [
                {
                    "label": "돌아간다.",
                    "action": 'block',
                    "blockId": blockId.고시원_1
                },
                {
                    "label": "힌트",
                    "action": 'block',
                    "blockId": blockId.힌트확인
                }
            ]
        }
    }
    
    save_block(user_id, block_id)
    return jsonify(res)



