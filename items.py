from connect import *

def make_item(image_url, item_description):
    return {    
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            "imageUrl": image_url,
                            "altText": "이미지 로딩 실패",
                            "forwardable": False
                        }
                    },
                    {
                        "simpleText": {
                            "text": item_description
                        }
                    }
                ],
                "quickReplies": [
                    {
                        "label": "돌아가자",
                        "action": 'block',
                        "blockId": blockId.인벤토리
                    }
                ]
            }
        }

@app.route('/items/piece1', methods=['POST'])
def piece1():
    res = make_item(images.piece_1, "조각 1")
    return jsonify(res)

@app.route('/items/piece2', methods=['POST'])
def piece2():
    res = make_item(images.piece_2, "조각 2")
    return jsonify(res)

@app.route('/items/piece3', methods=['POST'])
def piece3():
    res = make_item(images.piece_3, "조각 3")
    return jsonify(res)

@app.route('/items/piece4', methods=['POST'])
def piece4():
    res = make_item(images.piece_4, "조각 4")
    return jsonify(res)

@app.route('/items/piece5', methods=['POST'])
def piece5():
    res = make_item(images.piece_5, "조각 5")
    return jsonify(res)

@app.route('/items/note', methods=['POST'])
def note():
    res = make_item(images.note, "수첩")
    return jsonify(res)

