import time
import datetime

# import lark_oapi as lark
from lark_oapi import JSON as LarkJSON
from lark_oapi.api.auth.v3 import \
    InternalTenantAccessTokenRequest, \
    InternalTenantAccessTokenRequestBody, \
    InternalTenantAccessTokenResponse

from feishu_client import FeiShuClient


class TenantAccessToken:
    feishu_client: FeiShuClient

    tenant_access_token: str
    last_update_time: time.time

    def __init__(
            self,
            feishu_client: FeiShuClient
    ):
        self.tenant_access_token = ""

        # 初始化上次时间为2小时01分钟，这样确保开始时一定会更新一次。
        current_time = datetime.datetime.now()
        start_time = (
                current_time
                - datetime.timedelta(hours=2)
                - datetime.timedelta(minutes=1)
        )
        self.last_update_time = time.mktime(start_time.timetuple())

        self.feishu_client = feishu_client

    def get_tenant_access_token(self) -> str:
        if self.check_is_need_update():
            print("[Tenant Access Token] Need update.")
            if not self.update():
                print("Update Error!")

        return self.tenant_access_token

    def update_time(self) -> None:
        self.last_update_time = time.time()

    def check_is_need_update(self) -> bool:
        start_time = self.last_update_time
        end_time = time.time()

        elapsed_time = end_time - start_time
        elapsed_hours = elapsed_time // 3600
        # elapsed_minutes = (elapsed_time % 3600) // 60

        return elapsed_hours >= 2

    def update(self) -> bool:
        print("[Tenant Access Token] Updating...")

        if not self.feishu_client.is_valid():
            return False

        app_id = self.feishu_client.app_id
        app_secret = self.feishu_client.app_secret

        request: InternalTenantAccessTokenRequest = (
            InternalTenantAccessTokenRequest.builder().request_body(
                InternalTenantAccessTokenRequestBody.builder()
                .app_id(app_id)
                .app_secret(app_secret)
                .build()
            ).build()
        )

        response: InternalTenantAccessTokenResponse = \
            (
                self.feishu_client.client.auth.v3.tenant_access_token.internal(request)
            )

        if not response.success():
            # lark.logger.error(
            #     f"client.auth.v3.tenant_access_token.internal failed, "
            #     f"code: {response.code}, "
            #     f"msg: {response.msg}, "
            #     f"log_id: {response.get_log_id()}"
            # )
            return False

        try:
            json_obj: dict = LarkJSON.unmarshal(response.raw.content.decode(encoding="utf-8"), dict)
            if "tenant_access_token" in json_obj.keys():
                self.tenant_access_token = json_obj["tenant_access_token"]
                self.update_time()
                return True
        except Exception as e:
            print(e)
            return False

        return False


if __name__ == "__main__":
    app_id = ""
    app_secret = ""

    feishu_client = FeiShuClient(app_id=app_id, app_secret=app_secret)

    tenant_access_token = TenantAccessToken(feishu_client=feishu_client)

    print(tenant_access_token.get_tenant_access_token())
