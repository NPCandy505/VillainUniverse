from connect import *
#텍스트수정완료
@app.route('/church_1', methods=['POST'])
def church_1():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    cur_progress = get_progress(user_id)
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.background_3,    #백정기
                        "altText": "교회 내부 사진", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": """오래된 TV 속에서 백발의 남자가 신도들에게 연설하고 있는 영상이 흘러나오고 있었다. 피곤한 탓인지 건물 구조의 문제인지, 머릿속에서 남자의 연설이 메아리쳤다. 어지러움을 느끼며 나는 교회를 둘러보았다."""
                    }
                }
            ] if cur_progress == 1 else [
                {
                    "simpleImage": {
                        "imageUrl": images.background_3,    #백정기
                        "altText": "교회 내부 사진", 
                        "forwardable": False
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "천사상을 조사한다.",
                    "action": 'block',
                    "blockId": blockId.교회_2
                },
               {
                    "label": "십자가를 조사한다.",
                    "action": 'block',
                    "blockId": blockId.교회_3
                   ########################################################################3
                   #text” 블록 바로 연결 : data 필드 생략. Check it
                   #아니면 아예 block 자체에 선택지를 넣는 방법으로 이어도 될 것 같음.
                   #확인 요망
                   #####################################################################
                }
            ]
        }
    }
    
    if cur_progress == 1:
        set_progress(user_id, 2)
    save_block(user_id, block_id)
    return jsonify(res)


@app.route('/church_2', methods=['POST'])
def church_2():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    save_block(user_id, block_id)
    return response_from("강단 앞에는 사람 크기의 천사상이 음울한 빛을 받으며 서 있었다. 날개 하나가 없는 것 외에 특별한 점은 보이지 않았다.",
            quickReplies = [
                {
                    "label": "돌아간다.",
                    "action": 'block',
                    "blockId": blockId.교회_1
                }
            ])


@app.route('/church_3', methods=['POST'])
def church_3():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    save_block(user_id, block_id)
    return response_from("벽에는 붉은색의 십자가가 걸려있었다. 십자가 밑의 석판에는 무언가 글씨 같은 것이 새겨져 있었다.", images.problem_2_off,    #불꺼진십자가
            quickReplies = [
                {
                    "label": "돌아간다.",
                    "action": 'block',
                    "blockId": blockId.교회_1
                },
                {
                    "label": "전구를 켜 본다.",
                    "action": 'block',
                    "blockId": blockId.교회_4
                }
            ])


@app.route('/church_4', methods=['POST'])
def church_4():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {            #text가 없는 유일한케이스라 그냥 res로햇슴
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.problem_2_on,    #불켜진십자가
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
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
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.교회_1
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
    return res



