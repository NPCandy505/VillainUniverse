from connect import *
import string

##에필로그 텍스트 수정완료
bad_ends = [        ########## 텍스트랑 썸네일 이미지랑 영상 수정해야 함 ##########
    {"text": "BAD ENDING - 이런이런, 내가 낸 문제를 세 번 틀려버렸어! 문제가 너무 어려웠나? 지금은 튜토리얼이기 때문에 아무 일도 일어나지 않지만, 실전에 투입된 상황에서 문제를 세 번 연속으로 틀리면 배드엔딩을 볼 수 있으니 조심하라구! 참고로 메뉴에서 [힌트]를 사용할 수 있으니 어떻게 풀어야 할 지 막혔다면 한 번 사용해보는 건 어때? 배드 엔딩을 보고 나면 강력한 세 번째 힌트도 볼 수 있어!", "imageUrl": None, "videoUrl": None},
    {"text": "BAD ENDING", "imageUrl": None, "videoUrl": None},
    {"text": "BAD ENDING Ⅰ - 될지어다", "imageUrl": images.badend_2, "videoUrl": "https://youtu.be/kndO_FyZvoU"},
    {"text": "BAD ENDING Ⅱ - 최고의 작품", "imageUrl": images.badend_3, "videoUrl": "https://youtu.be/i9kzlhTfkWo"},
    {"text": "BAD ENDING Ⅲ - 옥션 파브르", "imageUrl": images.badend_4, "videoUrl": "https://youtu.be/7jPATT0rHoc"},
    {"text": "BAD ENDING Ⅳ - 최강의 악귀", "imageUrl": images.badend_5, "videoUrl": "https://youtu.be/6PSGMRqwwNU"},
    {"text": "BAD ENDING", "imageUrl": None, "videoUrl": None}
]

def bad_ending(user_id, prev_block_id):    # 이거 누가 구현해줬으면 좋겠다 내가 구현해야지
    problem_num = 0
    if prev_block_id == blockId.인트로_4:
        problem_num = 0
        prev_block_id = blockId.인트로_3
    elif prev_block_id == blockId.배_2:
        problem_num = 1
        prev_block_id = blockId.배_1
    elif prev_block_id == blockId.교회_4:
        problem_num = 2
        prev_block_id = blockId.교회_1
    elif prev_block_id == blockId.고시원_4:
        problem_num = 3
        prev_block_id = blockId.고시원_1
    elif prev_block_id == blockId.지하실_3:
        problem_num = 4
        prev_block_id = blockId.지하실_1
    elif prev_block_id == blockId.지하실_9:
        problem_num = 5
        prev_block_id = blockId.지하실_4
    elif prev_block_id == blockId.자물쇠_1:
        problem_num = 6
        prev_block_id = blockId.자물쇠_1
    bad_end = bad_ends[problem_num]
    set_saw_badend(user_id, 1)
    save_block(user_id, prev_block_id)
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": bad_end['text']
                    }
                },
                {
                    "basicCard": {
                        "thumbnail": {
                            "imageUrl": bad_end['imageUrl']
                        },
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "Bad ending",
                                "webLinkUrl": bad_end['videoUrl']
                            }
                        ]
                    }
                }
            ] if problem_num is 2 or problem_num is 3 or problem_num is 4 or problem_num is 5 else [
                {
                    "simpleText": {
                        "text": bad_end['text']
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "챕터 시작으로 돌아가기",
                    "action": "block",
                    "blockId" : prev_block_id
                }
            ]
        }
    }
    
    return jsonify(res)

def open_room(user_id, prev_block_id, block_id, utterance, answer, text, imageUrl=None, item=None):
    if utterance.strip().upper().replace(' ', '') == answer.strip().upper():    # 답을 맞힌 경우
        init_wrong_cnt(user_id)
        init_hint_cnt(user_id)
        if item != None:
            get_item(user_id, item)
        set_saw_badend(user_id, 0)
        save_block(user_id, block_id)
        if prev_block_id == blockId.자물쇠_1:    # 엔딩 직전이면 바로 progress를 하나 증가
            set_progress(user_id, 7)
        return response_from(
            text,
            imageUrl,
            [
                {
                    "label": "다음 챕터로 진행",
                    "action": 'block',
                    "blockId": block_id
                }
            ] if prev_block_id != blockId.자물쇠_1 else [
                {
                    "label": "다음 챕터로 진행",
                    "action": 'block',
                    "blockId": block_id
                },
                {
                    "label": "가방 확인",
                    "action": 'block',
                    "blockId": blockId.인벤토리
                }
            ]
        )
    else:
        wrong_cnt = increase_wrong_cnt(user_id)
        if wrong_cnt >= allowed_wrong_cnt:
            init_wrong_cnt(user_id)
            return bad_ending(user_id, prev_block_id)
        else:
            return response_from("""정답이 아닌 듯 하다.\n\n남은 정답 기회: """ + str(allowed_wrong_cnt - wrong_cnt) + "번",
                quickReplies = [
                    {
                        "label": "돌아가기",
                        "action": "block",
                        "blockId": prev_block_id
                    }
                ])
    
@app.route('/fallback', methods=['POST'])
def fallback():
    content = request.get_json()
    user_id = content['userRequest']['user']['id']
    utterance = content['userRequest']['utterance']
    
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
    
    if prev_block_id == blockId.인트로_3:    # 유저 이름 설정
        utterance = utterance.strip()
        set_user_name(user_id, utterance)
        if utterance == '퍼플' or utterance.lower() == 'puple' or utterance == '카이스트퍼플' or utterance.lower().replace(' ', '') == 'kaistpuple':
            utterance = "우주 최강 퍼즐 동아리 KAIST Puple!\n\n" + utterance
        elif utterance == '선물' or utterance.lower() == 'present':
            utterance = "KAIST Puple이 제작한 첫 번째 미궁, [선물]. https://kaistpuple.com/present\n\n" + utterance
        elif utterance.lower() == 'inside' or utterance == '인사이드':
            utterance = "KAIST Puple이 제작한 첫 번째 카톡 방탈출, [Inside]. https://pf.kakao.com/_xeFfxdK\n\n" + utterance
        elif utterance.lower() == 'otory' or utterance == '오토리':
            utterance = "너도 오토리라고? 그럴 리가 없잖아!\n\n" + utterance
        elif utterance.lower() == 'ocn' or utterance == '오씨엔':
            utterance = 'No1. 스토리테인먼트, "스토리를 혁명하다" OCN\n\n' + utterance
        elif utterance == '강권주':
            utterance = "네가 강권주 센터장님이라고? 그럴 리가 없잖아!\n\n" + utterance
        elif utterance.lower() == 'sans' or utterance == '샌즈':
            utterance = "응? 뭔가 끔찍한 시간을 보낼 것 같은 기분이...\n\n" + utterance
        elif utterance.lower().replace(' ', '') == 'muyaho' or utterance == '무야호':
            utterance = "그만큼 신나신다는 거지~\n\n" + utterance
        elif utterance == '벽력일섬':
            utterance = """번개(천둥)의 호흡 제1형\n   " 벽력일섬 "\n   " 벽력일섬 "\n"sorry my mouse misfunctioned"\n\n""" + utterance
        elif utterance == '구해줘' or utterance == '보이스' or utterance.replace(' ', '') == '손더게스트' or utterance == '지청신' or utterance.replace(' ', '') == '타인은지옥이다':
            utterance = """OCN 작품이네! 너도 본 적 있어?\n\n""" + utterance
        return response_from(utterance + " 요원! 이 이름이 맞아?", quickReplies = 
            [
                {
                    "label": "응!",
                    "action": 'block',
                    "blockId": blockId.인트로_4
                }, 
                {
                    "label": "아니야",
                    "action": 'block',
                    "blockId": blockId.인트로_3
                }
            ]
        )
    
    if prev_block_id == blockId.인트로_4:
        return open_room(user_id, prev_block_id, blockId.인트로_5, utterance, NotImplemented,
                        """축하해!! 정답이야!! 이제 넌 골든타임센터 요원이 될 수 있는 자격을 모두 갖췄어! 앞으로 나올 문제들은 이렇게 만만한 문제가 아닐거니까 각오해!!""", images.otori_2) # 오토리
    
    if prev_block_id == blockId.배_2:
        return open_room(user_id, prev_block_id, blockId.배_3, utterance, NotImplemented, 
                        """주문을 외우자 고통이 사라지며 자연스레 눈이 감겼다….
“형사님, 일어나요!” 얼마나 쓰러져 있던 걸까, 정신을 차리니 섬에 도착해 있었다. ‘꿈인가…’ 잠결에 쥔 듯한 주먹에는 이상한 조각이 쥐어져 있었다. 어딘가 찜찜했지만 별생각 없이 주머니에 종이를 쑤셔 넣고는 비틀거리며 배를 내렸다.
--------------------
[조각 1]을 획득했다.""", item = 'piece_1')
    
    if prev_block_id == blockId.교회_4:
        return open_room(user_id, prev_block_id, blockId.고시원_1, utterance, NotImplemented,
                        """“은장도” 나지막이 외치자 시끄럽게 울리던 연설이 멈추고 천장에서 그림이 그려진 이상한 조각이 떨어졌다. 배에서 얻은 것과 같은 재질, 비슷한 그림이 그려져 있었다. 아무래도 납치된 아이와 관련된 단서는 없어 보여, 교회를 나가려던 그때, 센터장님으로부터의 무전이 들려왔다.
--------------------
[조각 2]를 획득했다.""", item = 'piece_2')
    
    if prev_block_id == blockId.고시원_4:
        return open_room(user_id, prev_block_id, blockId.지하실_1, utterance, NotImplemented,
                        """탁자 밑의 카펫을 들추자, 낡은 문이 있었다. 문틈에는 익숙한 조각이 끼워져 있었다. 살살 잡아당기자 쉽게 빠졌다.
“아이의 손이 찍힌 사진을 찾았습니다. 납치된 아이인지는 불분명합니다.” 조각을 주머니에 집어넣으며 오래 열리지 않았던 것 같은 그 문을 조심스레 잡아당겨 열었다. “지하실 진입합니다.”
--------------------
[조각 3]을 획득했다.""", item = 'piece_3')

    if prev_block_id == blockId.지하실_3:
        return open_room(user_id, prev_block_id, blockId.지하실_4, utterance, NotImplemented,
                        """“FINEART” 조심스럽게 벽에 걸려있는 그림들을 건드렸다. 놀랍게도 그림들은 벽 안으로 누를 수 있었다. 모든 그림을 누르자, 덜컹거리는 소리와 함께 중앙의 큰 그림이 돌아가기 시작했다. 익숙한 조각이 얌전히 벽 뒤에 놓여있었다.
--------------------
[조각 4]를 획득했다.""", item = 'piece_4')

    if prev_block_id == blockId.지하실_9:
        return open_room(user_id, prev_block_id, blockId.자물쇠_1, utterance, NotImplemented,
                        """“소문”이라고 외치자 무지갯빛이 땅에서 솟아나고 무언가가 굉음을 내며 아이에게서 빠져나갔다.
“신원 확보했습니다 센터장님, 그런데.. 설명해 드릴 일이 많습니다.”
“쉽지 않은 악귀였을 텐데… 수고 많으셨습니다 """ + get_user_name(user_id) +
"""형사님.”
긴장이 풀린 난 거친 숨을 몰아쉬며 방금 목숨을 구해주었을지도 모르는 부적을 살펴보았다. 평범하게 상상할 수 있는 형태의 부적이었다. 다만 두께가 이상하리만치 두꺼웠다. 조심스럽게 양손으로 부적을 찢자 아니나 다를까, 부적 안쪽 봉투 같은 공간에 또 다른 조각이 들어있었다.
--------------------
[조각 5]를 획득했다."""
                        , images.background_7, item = 'piece_5')
    
    if prev_block_id == blockId.자물쇠_1:
        return open_room(user_id, prev_block_id, blockId.엔딩_1, utterance, NotImplemented, 
                        """문을 열고 나오자 바깥은 어둑해져 있었다.
--------------------
[수첩]을 획득했다."""
                        , item = 'note')
    
    return response_from("'" + utterance + ".' 공허한 메아리만 울려퍼졌다.", quickReplies = [
        {
            "label": "돌아가기",
            "action": "block",
            "blockId": prev_block_id
        }
    ])
