from flask import Flask, request, jsonify
import pymysql
import blockId
import images

app = Flask(__name__)

skill_db = pymysql.connect(user='skilluser', passwd='dalpengi', host='0.0.0.0', db='botuser', charset='utf8mb4')

allowed_wrong_cnt = 3    # 최대 정답 도전 횟수

def get_user_block_utterance(req):
    content = req.get_json()
    user_id = content['userRequest']['user']['id']
    user_name = get_user_name(user_id)
    prev_block_id = get_save(user_id)
    block_id = content['userRequest']['block']['id']
    utterance = content['userRequest']['utterance']
    
    return (user_id, user_name, prev_block_id, block_id, utterance)


def response_from(text, imageUrl=None, quickReplies=None):
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ] if imageUrl is None else [
                {
                    "simpleText": {
                        "text": text
                    }
                },
                {
                    "simpleImage": {
                        "imageUrl": imageUrl,
                        "altText": "이미지 로딩 실패",
                        "forwardable": False
                    }
                }
            ]
        } if quickReplies is None else {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ] if imageUrl is None else [
                {
                    "simpleText": {
                        "text": text
                    }
                },
                {
                    "simpleImage": {
                        "imageUrl": imageUrl,
                        "altText": "이미지 로딩 실패",
                        "forwardable": False
                    }
                }
            ],
            "quickReplies": quickReplies
        }
    }
    return jsonify(res)

def use_query(query):
    skill_db.ping(reconnect = True)
    cursor = skill_db.cursor(pymysql.cursors.DictCursor)
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    skill_db.commit()
    cursor.close()
    return result

def get_cell(user_id, table, column):
    query = "SELECT %s FROM %s WHERE `user_id` = '%s';" % (column, table, user_id)
    cell = use_query(query)[0][column]
    return cell

def set_cell(user_id, table, column, contents): # contents should be non-string; if string type is used for contents, add '·' 
    query = "UPDATE %s SET `%s` = %s WHERE `user_id` = '%s';" % (table, column, contents, user_id)
    use_query(query)

def save_block(user_id, block_id):
    set_cell(user_id, 'user_info', 'prev_block_id', "'" + block_id + "'")

def get_item(user_id, item):
    set_cell(user_id, 'inventory', item, '1')
    
def get_save(user_id):
    return get_cell(user_id, 'user_info', 'prev_block_id')

def set_user_name(user_id, user_name):
    set_cell(user_id, 'user_info', 'user_name', "'" + user_name + "'")

def get_user_name(user_id):
    return get_cell(user_id, 'user_info', 'user_name')

def get_saw_badend(user_id):
    return get_cell(user_id, 'user_info', 'saw_badend')

def set_saw_badend(user_id, saw_badend):
    return set_cell(user_id, 'user_info', 'saw_badend', str(saw_badend))

def init_wrong_cnt(user_id):
    set_cell(user_id, 'user_info', 'wrong_cnt', '0')

def get_wrong_cnt(user_id):
    return get_cell(user_id, 'user_info', 'wrong_cnt')

def increase_wrong_cnt(user_id):
    cur_wrong_cnt = get_wrong_cnt(user_id)
    if cur_wrong_cnt >= allowed_wrong_cnt:
        return allowed_wrong_cnt
    set_cell(user_id, 'user_info', 'wrong_cnt', str(cur_wrong_cnt + 1))
    return cur_wrong_cnt + 1

def init_hint_cnt(user_id):
    set_cell(user_id, 'user_info', 'hint_cnt', '0')

def get_hint_cnt(user_id):
    return get_cell(user_id, 'user_info', 'hint_cnt')

def increase_hint_cnt(user_id):
    cur_hint_cnt = get_hint_cnt(user_id)
    if cur_hint_cnt >= 3:
        return 3
    if cur_hint_cnt == 2 and get_saw_badend(user_id) == 0:
        return 2
    set_cell(user_id, 'user_info', 'hint_cnt', str(cur_hint_cnt + 1))
    return cur_hint_cnt + 1

def get_progress(user_id):
    return get_cell(user_id, 'user_info', 'progress')

def set_progress(user_id, progress):
    return set_cell(user_id, 'user_info', 'progress', str(progress))
