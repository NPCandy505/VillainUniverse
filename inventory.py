from connect import *

item_info = {
    "piece_1": {
        "name": "조각 1",
        "description": "강가를 찍은 사진이 붙어 있다.\n",
        "true_description": "강\n",
        "imageUrl": images.piece_1,
        "blockId": blockId.조각_1
    },
    "piece_2": {
        "name": "조각 2",
        "description": "조각에 주먹 그림이 그려져 있다.\n",
        "true_description": "권(拳)\n",
        "imageUrl": images.piece_2,
        "blockId": blockId.조각_2
    },
    "piece_3": {
        "name": "조각 3",
        "description": "아마 일주일을 표현한 그림인 것 같다.\n",
        "true_description": "주\n",
        "imageUrl": images.piece_3,
        "blockId": blockId.조각_3
    },
    "piece_4": {
        "name": "조각 4",
        "description": "거울에 비치는 모습이 그려진 조각이다.\n",
        "true_description": "거울\n",
        "imageUrl": images.piece_4,
        "blockId": blockId.조각_4
    },
    "piece_5": {
        "name": "조각 5",
        "description": "조각 안에서 탈출구가 보인다.\n",
        "true_description": "탈출\n",
        "imageUrl": images.piece_5,
        "blockId": blockId.조각_5
    },
    "note": {
        "name": "수첩",
        "description": "강권주의 거울로부터 탈출하라\n",
        "true_description": "강권주의 거울로부터 탈출하라\n",
        "imageUrl": images.note,
        "blockId": blockId.수첩
    }
}

cards = {
    item: {
        "title": item_info[item]["name"],
        "description": item_info[item]["description"],
        "thumbnail": {
            "imageUrl": item_info[item]["imageUrl"]
        }
    } for item in item_info
}

true_cards = {
    item: {
        "title": item_info[item]["name"],
        "description": item_info[item]["true_description"],
        "thumbnail": {
            "imageUrl": item_info[item]["imageUrl"]
        }
    } for item in item_info
}

replies = {
    item: {
        "label": item_info[item]["name"],
        "action": "block",
        "messageText": item_info[item]["name"],
        "blockId": item_info[item]["blockId"]
    } for item in item_info
}

@app.route('/inventory', methods=['POST'])
def inventory():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
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
    
    cur_progress = get_progress(user_id)
    
    items = use_query("SELECT * FROM inventory WHERE `user_id` = '%s';" % (user_id))[0] # a dictionary
    #print(items)
    del items['user_id']
    
    item_cnt = 0
    for item in items:
        if items[item] == 1:
            item_cnt += 1
    #print(item_cnt)
    
    prev_block_id = get_save(user_id)
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "가방\n여태까지 주운 물건들이다."
                    }
                },
                {
                    "carousel": {
                        "type": "basicCard",    # 마지막 문제를 푼 직후에는 아이템 설명이 true_description으로 바뀜
                        "items": [cards[item] for item in items if items[item] == 1] if cur_progress != 7 else [true_cards[item] for item in items if items[item] == 1]
                    }
                }
            ] if item_cnt != 0 else [
                {
                    "simpleText": {
                        "text": "가방\n아직 주운 물건이 없다."
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "가방 닫기",
                    "action": "block",
                    "messageText": "가방을 닫을래",
                    "blockId": prev_block_id
                }
            ] + [replies[item] for item in items if items[item] == 1]
        }
    }
    return jsonify(res)

