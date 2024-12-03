from flask import Flask, request, jsonify
from connect import *

@app.route('/test', methods = ['POST'])
def test():
    print("test")
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": """안녕 나는 테스트 텍스트야"""
                    }
                }
            ],
            "quickReplies": [
                {
                    "label": "안녕 테스트 텍스트",
                    "messageText": "안녕 텍스트 테스트",
                    "action": 'message'
                }
            ]
        }
    }

    return jsonify(res)