from connect import *

@app.route('/user/create', methods=['POST'])
def user_create():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    
    check_existing_user_query = "SELECT user_id from inventory where user_id = '%s';" % (user_id)
    user_exist = (len(use_query(check_existing_user_query)) == 1)
    if not user_exist:
        return response_from("[시작하기] 버튼을 눌러 시작해주세요.",
                quickReplies = [
                    {
                        "label": "시작하기",
                        "action": 'block',
                        "blockId": blockId.인트로_1
                    }
                ])
    
    prev_block_id = get_cell(user_id, 'user_info','prev_block_id')
    
    return response_from("""플레이 기록이 있습니다. 이어서 하시겠습니까? 처음부터 다시 시작하려면 '다시 시작하자'를 입력해주세요!""",
        quickReplies = [
            {
                "label": "이어서 하자",
                "action": 'block',
                "blockId": prev_block_id
            }
        ]
    )

# @app.route('/user/delete', methods=['POST'])
# def user_delete():
#     content = request.get_json()
#     user_id = content['userRequest']['user']['id']
    
#     query = "DELETE FROM inventory WHERE `user_id` = '%s'" % (user_id)
#     use_query(query)
#     query = "DELETE FROM user_info WHERE `user_id` = '%s'" % (user_id)
#     use_query(query)
    
#     return response_from("너 누구니")

@app.route('/user/reset', methods=['POST'])
def user_reset():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    
    query = "DELETE FROM inventory WHERE `user_id` = '%s'" % (user_id)
    use_query(query)
    query = "DELETE FROM user_info WHERE `user_id` = '%s'" % (user_id)
    use_query(query)
    
    
    return response_from("모든 진행상황이 초기화되었습니다.",
            quickReplies = [
                {
                    "label": "시작하기",
                    "action": 'block',
                    "blockId": blockId.인트로_1
                }
            ])

@app.route('/user/continue', methods=['POST'])
def user_continue():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    
    check_existing_user_query = "SELECT user_id from inventory where user_id = '%s'" % (user_id)
    user_exist = (len(use_query(check_existing_user_query)) == 1)
    if not user_exist:
        return response_from("플레이 기록이 없습니다. [시작하기] 버튼을 통해 시작해주세요.",
                quickReplies = [
                    {
                        "label": "시작하기",
                        "action": 'block',
                        "blockId": blockId.인트로_1
                    }
                ])
        
    prev_block_id = get_save(user_id)
    
    return response_from("잠시 멍 때렸나보다. 계속할까?",
            quickReplies = [
                {
                    "label": "계속하자",
                    "action": 'block',
                    "blockId": prev_block_id
                }
            ])

@app.route('/user/rule', methods=['POST'])
def user_rule():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    
    check_existing_user_query = "SELECT user_id from inventory where user_id = '%s';" % (user_id)
    user_exist = (len(use_query(check_existing_user_query)) == 1)
    if not user_exist:
        return response_from("플레이 기록이 없습니다. [시작하기] 버튼을 통해 시작해주세요.",
                quickReplies = [
                    {
                        "label": "시작하기",
                        "action": 'block',
                        "blockId": blockId.인트로_1
                    }
                ])
    
    prev_block_id = get_save(user_id)
    
    return response_from("""넌 OCN <보이스>의 골든타임 센터 출동팀 신입요원이 되어서 사건들을 해결하게 될 거야. 
이야기를 진행하는 중 문제를 만난다면 채팅창에 정답을 입력해줘. 혹시 문제가 어렵다면 각 문제별로 두 번까지 힌트를 쓸 수 있으니 걱정은 말라고! 
아, 그렇지만 너무 방심하는 것도 금물이야! 문제를 세 번 이상 틀릴 경우 안 좋은 일이 생길 수 있거든… 
게임을 하면서 얻게 되는 아이템을 확인하고 싶으면 선택지의 '가방을 보자'를, 룰을 다시 듣고 싶다면 '규칙을 보자'를 클릭해줘.
혹시 진행 도중 오류가 발생하거나, 이야기를 처음부터 다시 보고 싶다면 ‘다시 시작하자’ 를 채팅창에 입력해주면 돼!""",
            quickReplies = [
                {
                    "label": "돌아가기", 
                    "action": 'block',
                    "blockId": prev_block_id
                }
            ])


