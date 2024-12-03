from connect import *

@app.route('/woodendoll_1', methods=['POST'])
def woodendoll_1():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""첫 번째 목각인형 그림이다.""", imageUrl = images.problem_4[1],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_2', methods=['POST'])
def woodendoll_2():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""두 번째 목각인형 그림이다.""", imageUrl = images.problem_4[2],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_3', methods=['POST'])
def woodendoll_3():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""세 번째 목각인형 그림이다.""", imageUrl = images.problem_4[3],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_4', methods=['POST'])
def woodendoll_4():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""네 번째 목각인형 그림이다.""", imageUrl = images.problem_4[4],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_5', methods=['POST'])
def woodendoll_5():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""다섯 번째 목각인형 그림이다.""", imageUrl = images.problem_4[5],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_6', methods=['POST'])
def woodendoll_6():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""여섯 번째 목각인형 그림이다.""", imageUrl = images.problem_4[6],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_7', methods=['POST'])
def woodendoll_7():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""일곱 번째 목각인형 그림이다.""", imageUrl = images.problem_4[7],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_8', methods=['POST'])
def woodendoll_8():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""여덟 번째 목각인형 그림이다.""", imageUrl = images.problem_4[8],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_9', methods=['POST'])
def woodendoll_9():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""아홉 번째 목각인형 그림이다.""", imageUrl = images.problem_4[9],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])

@app.route('/woodendoll_10', methods=['POST'])
def woodendoll_10():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    block_id = content['userRequest']['block']['id']
    
    # save_block(user_id, block_id)
    return response_from("""열 번째 목각인형 그림이다.""", imageUrl = images.problem_4[10],
            quickReplies = [
                {
                    "label": "돌아간다",
                    "action": 'block',
                    "blockId": blockId.지하실_3
                }
            ])
