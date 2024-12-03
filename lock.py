from connect import *
#텍스트 변경완.
@app.route('/lock_1', methods=['POST'])
def lock_1():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    cur_progress = get_progress(user_id)     
    
    
    save_block(user_id, block_id)
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": images.problem_6_1,    #철문
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleImage": {
                        "imageUrl": images.problem_6_2,    #자물쇠
                        "altText": "이미지 로딩 실패", 
                        "forwardable": False
                    }
                },
                {
                    "simpleText": {
                        "text": ("""무전 후, 아이를 업은 채 열려 있는 다른 통로를 찾아 서둘러 위로 올라갔다. 긴 오르막의 끝에서 발견한 격자가 새겨진 철문은 알파벳 자물쇠로 굳게 잠겨 있었다.""" if cur_progress == 5 else '') + 
                         """
--------------------
(답을 채팅으로 입력하세요!)"""
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
    
    if cur_progress == 5:
        set_progress(user_id, 6)
        
    return jsonify(res)
