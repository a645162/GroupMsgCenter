# https://open.feishu.cn/document/server-docs/im-v1/message/create?appId=cli_a5777c1d3438d00d
# https://open.feishu.cn/document/server-docs/im-v1/message-content-description/create_json#11e75d0

import uuid

# import lark_oapi as lark
# from lark_oapi.api.im.v1 import *
from lark_oapi import Client as LarkClient
from lark_oapi import JSON as LarkJSON
from lark_oapi.api.im.v1 import (
    CreateMessageRequestBody,
    CreateMessageRequest,
    CreateMessageResponse
)

from feishu_client import FeiShuClient


def generate_uuid() -> str:
    return str(uuid.uuid4())


class FeiShuMsg:
    feishu_client: FeiShuClient

    def __init__(self, feishu_client: FeiShuClient):
        self.feishu_client = feishu_client

    def send_msg_by_user_id(self, user_id: str, msg: str) -> bool:
        if not self.feishu_client.is_valid():
            return False

        client: LarkClient = self.feishu_client.client

        content_dict: dict = {
            "text": msg
        }

        # 构造请求对象
        request: CreateMessageRequest = (
            CreateMessageRequest.builder()
            .receive_id_type("user_id")
            .request_body(
                CreateMessageRequestBody.builder()
                .receive_id(user_id)
                .msg_type("text")
                .content(LarkJSON.marshal(content_dict, indent=4))
                .uuid(generate_uuid())
                .build()
            )
            .build()
        )

        # 发起请求
        response: CreateMessageResponse = client.im.v1.message.create(request)

        # 处理失败返回
        if not response.success():
            print(
                f"client.im.v1.message.create failed, "
                f"code: {response.code}, "
                f"msg: {response.msg}, "
                f"log_id: {response.get_log_id()}"
            )
            return False

        # 处理业务结果
        # lark.logger.info(lark.JSON.marshal(response.data, indent=4))

        return True


if __name__ == "__main__":
    app_id = ""
    app_secret = ""

    feishu_client = FeiShuClient(app_id=app_id, app_secret=app_secret)

    feishuMsg = FeiShuMsg(feishu_client=feishu_client)

    feishuMsg.send_msg_by_user_id(user_id="", msg="hello world")
