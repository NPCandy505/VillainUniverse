from flask import Flask, request, jsonify, send_from_directory
from connect import *
import user, inventory, items, intro, boat, church, sharehouse, basement1, basement2, lock, ending, hint, fallback, test, woodendoll

#app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello goorm!"

@app.route('/simpleskillanswer', methods=['POST'])
def simpleskillanswer():
    userid, _, _, blockid, utterance = get_user_block_utterance(request)
    
    # res = {
    #     "version": "2.0",
    #     "template": {
    #         "outputs": [
    #             {
    #                 "simpleText": {
    #                     "text": "simplie skill answer"
    #                 }
    #             },
    #             {
    #                 "simpleImage": {
    #                     "imageUrl": images.simple_image,
    #                     "altText": "이미지다"
    #                 }
    #             }
    #         ]
    #     }
    # }

    print('user utterance: '+utterance)
    print('user block id: '+str(blockid))
    print('user id: '+str(userid))

    return response_from("simpleskillanswer", imageUrl = images.simple_image)

@app.route('/complexskillanswer', methods=['POST'])
def complexskillanswer():
    userid, _, _, blockid, utterance = get_user_block_utterance(request)
    
    # res = {
    #     "version": "2.0",
    #     "template": {
    #         "outputs": [
    #             {
    #                 "simpleText": {
    #                     "text": "simplie skill answer"
    #                 }
    #             },
    #             {
    #                 "simpleImage": {
    #                     "imageUrl": images.simple_image,
    #                     "altText": "이미지다"
    #                 }
    #             }
    #         ]
    #     }
    # }
    
    print('Complex Skill Answer Has Responded.')
    print('user utterance: '+utterance)
    print('user block id: '+str(blockid))
    print('user id: '+str(userid))

    return response_from("complexskillanswer", imageUrl = images.simple_image)

@app.route('/images/<path:filename>')
def give_image(filename):
    return send_from_directory('./images/', filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)

