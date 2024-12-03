from connect import *
#텍스트수정완료
@app.route('/boat_1', methods=['POST'])
def boat_1():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    cur_progress = get_progress(user_id)
    
    if cur_progress == 0:
        set_progress(user_id, 1)
    save_block(user_id, block_id)
    return response_from("“코드 제로 사건 발생. 6세 정도 되는 남자아이가 며칠 전 유괴된 후 ‘악지도’라는 섬에서 목격됐다는 신고가 접수됐습니다. " + get_user_name(user_id) + " 형사님! 바로 출동하시고 계속 브리핑해주세요.”",
            quickReplies = [
                {
                    "label": "다음",
                    "action": 'block',
                    "blockId": blockId.배_2
                }
            ])

@app.route('/boat_2', methods=['POST'])
def boat_2():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": """배를 타고 섬으로 들어가는 도중, 선장님이 무어라 얘기하시는 것이 들려왔다 ‘피곤하다..’
“자신의 오른쪽 눈을 찌르고 바다에 뛰어들어 자살한 귀신이 뱃사람들에게 씌곤 하더래요. 그래서 뱃사람들이…  벗어나기 위해…무슨 주문…”"""
                    }
                },
                {
                    "simpleText": {
                        "text": """졸음이 몰려와 선실에 들어가던 도중,  오른쪽 눈을 뾰족한 무언가로 찌르는 고통이 느껴져 쓰러지고 말았다. 으으… 귀신…? 주문…?
--------------------
(답을 채팅으로 입력하세요!)"""
                    }
                },
                {
                    "simpleImage": {
                        "imageUrl": images.problem_1,
                        "altText": "배 안쪽 널빤지", 
                        "forwardable": False
                    }
                }
                
            ],
            "quickReplies": [
                {
                    "label": "돌아가기",
                    "action": 'block',
                    "blockId": blockId.배_1
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

@app.route('/boat_3', methods=['POST'])
def boat_3():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                    {
                        "simpleImage": {
                            "imageUrl": images.background_2,    #흐릿한약지도
                            "altText": "흐릿한약지도", 
                            "forwardable": False
                        }
                    },
                        {
                        "simpleText": {
                            "text": """섬은 온통 자욱한 안개로 덮여있었다. 안개를 헤치며 마을로 이어지는 길을 따라 걷던 도중 무전기가 울렸다.

“최근 악지도에서 지직… 연기에 감염된… 지직… 변종 인간으로 변하는 사태가 있었다고 합니다. 조심하세요… """+ get_user_name(user_id) + """ 형사님”

제대로 듣기 위해 회신을 시도했지만 어째서인지 묵묵부답이었다. 조금 더 걷자 마을 입구와 섬마을 치고는 과한 크기의 교회가 나타났다. 조사를 위해 난 교회로 들어갔다. """
                        }
                    }
                ],
            "quickReplies": [
                {
                    "label": "다음",
                    "action": 'block',
                    "blockId": blockId.교회_1
                }
            ]
        }
    }
    
    save_block(user_id, block_id)
    return jsonify(res)