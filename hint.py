from connect import *

hints = [    # 힌트 이미지가 없다면 "imageUrl"에 None을 넣는다
    [{"text": "첫 번째 힌트\n\n나는 스토리를 좋아해!", "imageUrl": None},
     {"text": "두 번째 힌트\n\n나는 OCN의 캐릭터야!", "imageUrl": None},
     {"text": "세 번째 힌트\n\n나는 OCN의 '오'와 스토리의 '토리'를 합친 이름의 <오토리>야.", "imageUrl": None}],
    [{"text": "첫 번째 힌트\n\n오른쪽이 보이지 않는다", "imageUrl": None},
     {"text": "두 번째 힌트\n\n각각 왼쪽 절반만 보인다", "imageUrl": None},
     {"text": "세 번째 힌트\n\n단어별로 왼쪽 절반만 읽으면 <이 바다가 그가 죽은 동해>가 나옵니다.", "imageUrl": images.answer_1}],
    [{"text": "첫 번째 힌트\n\n각 글자를 십자선을 통해 4등분으로 나누고, 화살표를 따라가보세요.", "imageUrl": None},
     {"text": "두 번째 힌트", "imageUrl": images.hint_2_2},
     {"text": "세 번째 힌트\n\n십자선을 기준으로 화살표가 가리키는 방향을 보면 빈 공간이나 자음, 또는 모음이 나오는데 이를 이어 읽으면 <은장도>가 나옵니다.", "imageUrl": images.answer_2}],
    [{"text": "첫 번째 힌트\n\n지문에 맞도록 손가락을 실제로 놓아보세요.", "imageUrl": None},
     {"text": "두 번째 힌트", "imageUrl": images.hint_3_2},
     {"text": "세 번째 힌트\n\n손가락이 표현하는 단어는 <TABLE>이다.", "imageUrl": images.answer_3}],
    [{"text": "첫 번째 힌트\n\n쪽지가 붙어 있는 부위가 없는 인형이 다음 글자에 해당하는 인형입니다.", "imageUrl": None},
     {"text": "두 번째 힌트\n\n당신이 첫 번째 글자에 해당하는 인형이며, 쪽지는 당신의 오른손에 있습니다.", "imageUrl": None},
     {"text": "세 번째 힌트\n\n당신이 F가 적힌 쪽지를 오른손에 들고 있습니다. 오른손이 없는 인형을 찾으면 그 인형은 I가 적힌 쪽지를 왼쪽 어깨에 붙이고 있습니다. 다시 왼쪽 어깨가 없는 인형을 찾으면 그 인형은 N이 적힌 쪽지를 오른발에 붙이고 있습니다, 이 과정을 반복해 얻은 알파벳들을 나열하면 F,I,N,E,A,R,T인데 T가 적힌 쪽지를 오른쪽 어깨에 붙이고 있는 인형의 다음 글자인 오른쪽 어깨가 없는 인형이 존재하지 않기 때문에 T가 마지막 글자입니다. 따라서 답은 <FINEART>가 됩니다.", "imageUrl": images.answer_4}],
    [{"text": "첫 번째 힌트\n\n각 가로줄/세로줄 별로 문양들이 공통으로 포함하는 칸을 찾아주세요.", "imageUrl": None},
     {"text": "두 번째 힌트\n\n예를 들어, 첫 번째 가로줄은 ㅁ을 의미합니다. 이렇게 세로줄끼리 조합하여 한 글자, 가로줄끼리 조합하여 한 글자가 됩니다.", "imageUrl": images.hint_5_2},
     {"text": "세 번째 힌트\n\n세로줄들에서 자음과 모음을 조합하면 소, 가로줄들에서 자음과 모음을 조합하면 문이 됩니다. 따라서 답은 <소문>.", "imageUrl": images.answer_5}],
    [{"text": "첫 번째 힌트", "imageUrl": images.hint_6_1},
     {"text": "두 번째 힌트", "imageUrl": images.hint_6_2},
     {"text": "세 번째 힌트\n\n정답은 <VOICE>.", "imageUrl": images.answer_6}],
    [{"text": "첫 번째 나오면 안되는 힌트", "imageUrl": images.simple_image},
     {"text": "두 번째 나오면 안되는 힌트", "imageUrl": images.simple_image},
     {"text": "세 번째 나오면 안되는 힌트\n\n정답은 <VOICE>.", "imageUrl": images.simple_image}]
]

@app.route('/confirm_hint', methods=['POST'])
def confirm_hint():
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
    saw_badend = (get_saw_badend(user_id) == 1)
    hint_count = get_hint_cnt(user_id)
    
    if prev_block_id == blockId.인트로_4 or prev_block_id == blockId.배_2 or prev_block_id == blockId.교회_4 or prev_block_id == blockId.고시원_4 or prev_block_id == blockId.지하실_3 or prev_block_id == blockId.지하실_9 or prev_block_id == blockId.자물쇠_1:
        pass
    else:
        return response_from("여기서는 힌트를 사용할 수 없다.",
                quickReplies = [
                    {
                        "label": "돌아가기",
                        "action": "block",
                        "blockId" : prev_block_id
                    }
                ])
    
    return response_from("마지막 힌트가 있어. 이 힌트는 문제의 풀이와 정답을 포함하고 있는데, 그래도 사용할래? " if saw_badend and hint_count == 2 else "힌트를 사용할래?",
                quickReplies = [
                    {
                        "label": "돌아가기",
                        "action": "block",
                        "blockId" : prev_block_id
                    },
                    {
                        "label": "사용하기",
                        "action": "block",
                        "blockId" : blockId.힌트
                    }
                ])

@app.route('/hint', methods=['POST'])
def hint():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    prev_block_id = get_save(user_id)
    
    problem_num = 0
    if prev_block_id == blockId.인트로_4:
        problem_num = 0
    elif prev_block_id == blockId.배_2:
        problem_num = 1
    elif prev_block_id == blockId.교회_4:
        problem_num = 2
    elif prev_block_id == blockId.고시원_4:
        problem_num = 3
    elif prev_block_id == blockId.지하실_3:
        problem_num = 4
    elif prev_block_id == blockId.지하실_9:
        problem_num = 5
    elif prev_block_id == blockId.자물쇠_1:
        problem_num = 6
    else:
        return response_from("여기서는 힌트를 사용할 수 없다.",
                quickReplies = [
                    {
                        "label": "돌아가기",
                        "action": "block",
                        "blockId" : prev_block_id
                    }
                ])
    
    saw_badend = (get_saw_badend(user_id) == 1)
    hint_count = increase_hint_cnt(user_id)
    hint = hints[problem_num][hint_count-1]
    return response_from(hint["text"] + "\n\n이 문제에서 사용한 힌트 개수: %d/%d" % (hint_count, 3 if saw_badend else 2), hint["imageUrl"], 
            quickReplies = [
                {
                    "label": "돌아가기",
                    "action": "block",
                    "blockId" : prev_block_id
                }
            ])
