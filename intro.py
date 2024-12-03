from connect import *

@app.route('/intro_1', methods=['POST'])
def intro_1():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    check_existing_user_query = "SELECT user_id from inventory where user_id = '%s';" % (user_id)
    user_exist = (len(use_query(check_existing_user_query)) == 1)
    if user_exist:
        prev_block_id = get_save(user_id)
        if get_save(user_id) == blockId.이벤트:    # 엔딩 직후 처음으로 온 상황이면 초기화(이후 유저 정보 재추가)
            delete_user_query = "DELETE FROM inventory WHERE `user_id` = '%s'" % (user_id)
            use_query(delete_user_query)
            delete_user_query = "DELETE FROM user_info WHERE `user_id` = '%s'" % (user_id)
            use_query(delete_user_query)
        else:
            return response_from("""플레이 기록이 있습니다. 이어서 하시겠습니까? 처음부터 다시 시작하려면 '다시 시작하자'를 입력해주세요!""",
                    quickReplies = [
                        {
                            "label": "이어서 하자",
                            "action": 'block',
                            "blockId": prev_block_id
                        }
                    ]
                )
        
    add_new_user_query = "INSERT INTO inventory(`user_id`) VALUES ('%s')" % (user_id)
    use_query(add_new_user_query)
    add_new_user_query = "INSERT INTO user_info(`user_id`) VALUES ('%s')" % (user_id)
    use_query(add_new_user_query)
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.otori_1,    #오토리
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": """안녕~! 나는 OCN의 마스코트 캐릭터, 오토리야! OCN <빌런 유니버스>에 온 걸 환영해!!"""
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "안녕, 오토리!",
                    "action": 'block',
                    "blockId": blockId.인트로_2
                }
            ]
        }
    }
    
    save_block(user_id, blockId.인트로_2)
    return jsonify(res)

@app.route('/intro_2', methods=['POST'])
def intro_2():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": """넌 이제 <보이스>의 골든타임 센터 출동팀 신입요원이 되어서 사건들을 해결하게 될 거야. 
이야기를 진행하는 중 문제를 만난다면 채팅창에 정답을 입력해줘. 혹시 문제가 어렵다면 각 문제별로 두 번까지 힌트를 쓸 수 있으니 걱정은 말라고!
아, 그렇지만 너무 방심하는 것도 금물이야! 문제를 세 번 이상 틀릴 경우 안 좋은 일이 생길 수 있거든… 하지만 너무 걱정하지는 마! 문제를 푸는데 도움이 되는 작은 선물도 준비되어 있으니까!
게임을 하면서 얻게 되는 아이템을 확인하고 싶으면 선택지의 '가방을 보자'를, 룰을 다시 듣고 싶다면 '규칙을 보자'를 클릭해줘.
혹시 진행 도중 오류가 발생하거나, 이야기를 처음부터 다시 보고 싶다면 ‘다시 시작하자’ 를 채팅창에 입력해주면 돼!"""    
                    }    #혹시 이거 모든 문제가 3번틀리면 배드인가?ㅇㅇ지금은 그런데 난이도 조절을 위해 조정할 수 있게 해놓았어
                }        #이거 계속하자 에 대한 설명은 뭐라고 쓰지? 갑자기 멈추면 계속하자 입력해줘 하면 되나
#써야 할 것: 힌트 3번쓸수있다, 다시하려면 다시 시작하자 입력, 가방은 왼쪽에서, 몇몇 문제는 많이틀리면 안좋을수도잇어~    #넣지뭐 넣고 잇겟슴 그냥 이 텍스트 한번더 출력하면 될것같은데
            ],
            "quickReplies": [
                {
                    "label": "준비 완료!",
                    "action": 'block',
                    "blockId": blockId.인트로_3
                }
            ]
        }
    }
    
    save_block(user_id, block_id)
    return jsonify(res)

@app.route('/intro_3', methods=['POST'])
def intro_3():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": """자, 출발하기 전에 너의 이름을 알려줘! 입력창에 이름을 적어주면 돼 :D"""
                    }
                }
                
            ]
        }
    }
    
    save_block(user_id, block_id)
    return jsonify(res)

@app.route('/intro_4', methods=['POST'])
def intro_4():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": """안녕, """ + get_user_name(user_id) + """ 요원! 이제 마지막으로, 튜토리얼 문제를 낼 거야. 이 문제는 튜토리얼 문제라서 퍼즐 문제가 아니라 넌센스 문제를 준비했어! 정답을 알고 있다면, 입력창에 올리고 메시지로 보내줘. 답이 맞으면 다음으로 진행할 수 있을 거야!
--------------------
그럼 문제! 나의 이름이 뭐라고 했지? (답을 채팅으로 입력하세요!)"""
                    }
                }
            ],
            "quickReplies": [
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

@app.route('/intro_5', methods=['POST'])
def intro_5():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.background_1,    #강권주 센터장님
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": """저기 강권주 센터장님 보이지? 우리 센터장님 지령을 잘 따라서 범인을 잡으면 돼! 자, 이제 준비 됐어? 준비됐으면 시작 버튼을 눌러줘!"""
                    }
                }
                
            ],
            "quickReplies": [
                {
                    "label": "시작",
                    "action": 'block',
                    "blockId": blockId.배_1
                }
            ]
        }
    }
    
    save_block(user_id, block_id)
    return jsonify(res)

