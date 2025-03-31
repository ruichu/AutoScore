import json
import os
import time
import flask
from flask import request, make_response

import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *
from lark_oapi.api.im.v1 import *

from auto_score import auto_score

lark_client = None

def initialize(context):
    global lark_client
    lark_app_id = os.getenv('LARK_APP_ID')
    lark_app_secret = os.getenv('LARK_APP_SECRET')

    # 创建client
    lark_client = lark.Client.builder() \
        .app_id(lark_app_id) \
        .app_secret(lark_app_secret) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

def get_record_raw(record_id):
    # 构造请求对象
    request: BatchGetAppTableRecordRequest = BatchGetAppTableRecordRequest.builder() \
        .app_token("VvAabUKgtaHjzTsFNB4cEuuAnxU") \
        .table_id("tblmbILHF8WAFtr9") \
        .request_body(BatchGetAppTableRecordRequestBody.builder()
            .record_ids([record_id])
            .user_id_type("open_id")
            .with_shared_url(False)
            .automatic_fields(False)
            .build()) \
        .build()

    # 发起请求
    response: BatchGetAppTableRecordResponse = lark_client.bitable.v1.app_table_record.batch_get(request)

    if not response.success():
        lark.logger.error(
            f"client.bitable.v1.app_table_record.batch_get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
        return None

    return response.data.records[0].fields

def get_record(record_id):
    record_raw = get_record_raw(record_id)
    print(record_raw)
    record_data = {}
    for key in record_raw:
        if len(key) < 10:   # 过滤掉系统字段
            continue
        value = record_raw[key]
        index = key[:10]      # 截取字段名
        if isinstance(value, list):     #[{'text': '33\n', 'type': 'text'}, {'text': '三\n', 'type': 'text'}, {'text': '散', 'type': 'text'}]
            value = ''.join([slice.get('text', '') for slice in value])
        record_data[index] = { "question": key, "value": value }

    user_id = record_raw['提交人'][0]['id']

    return record_data, user_id

def send_message(user_id, message):
    content = {"text" : message}
    # 构造请求对象
    request: CreateMessageRequest = CreateMessageRequest.builder() \
        .receive_id_type("open_id") \
        .request_body(CreateMessageRequestBody.builder()
            .receive_id(user_id)
            .msg_type("text")
            .content(json.dumps(content))
            .build()) \
        .build()

    # 发起请求
    response: CreateMessageResponse = lark_client.im.v1.message.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.message.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
        return

def add_user_score(user_id, score):
    request: CreateAppTableRecordRequest = CreateAppTableRecordRequest.builder() \
        .app_token("VvAabUKgtaHjzTsFNB4cEuuAnxU") \
        .table_id("tblwModBiyYWqwDp") \
        .request_body(AppTableRecord.builder()
            .fields({"分数":score, "姓名":[{"id": user_id}]})
            .build()) \
        .build()

    # 发起请求
    response: CreateAppTableRecordResponse = lark_client.bitable.v1.app_table_record.create(request)
    
    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.bitable.v1.app_table_record.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}, resp: \n{json.dumps(json.loads(response.raw.content), indent=4, ensure_ascii=False)}")
        return

# Flask app should start in global layout
app = flask.Flask(__name__)

def handler(environ, start_response):
    #flask app return WSGI application
    return app(environ, start_response)

@app.route('/', methods=['GET'])
def get_handler():
    return make_response("hello world", 200)

@app.route('/', methods=['POST'])
def post_handler():
    print(request.form)
    #response_content = {"score":str(request.form)}
    record_data, user_id = get_record(request.form.get('record'))
    
    print(json.dumps(record_data, indent=4, ensure_ascii=False))

    scores = auto_score(record_data)

    scores_show = ['以下得分由AI自动评定，仅供参考：']
    for index, score in enumerate(scores):
        scores_show.append(f'第{index+1}题得分：{score}分')
    total_score = sum(scores)
    scores_show.append(f'总分：{total_score}分')

    send_message(user_id, '\n'.join(scores_show))

    if total_score >= 50:       # 大于50分才记录
        add_user_score(user_id, total_score)

    return make_response("OK", 200)

if __name__ == '__main__':
    initialize(None)
    app.run(debug=True)
