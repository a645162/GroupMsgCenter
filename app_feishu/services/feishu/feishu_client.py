from typing import Optional

# import lark_oapi as lark
from lark_oapi import Client as LarkClient


class FeiShuClient(object):
    app_id: str = ""
    app_secret: str = ""

    client: Optional[LarkClient]

    def __init__(self, app_id: Optional[str] = None, app_secret: Optional[str] = None):
        if not (app_id and app_secret and self.set_app_info(app_id, app_secret)):
            self.app_id = ""
            self.app_secret = ""

        self.client: Optional[LarkClient] = None

        self.update_client()

    def set_app_info(self, app_id: str, app_secret: str) -> bool:
        app_id = app_id.strip()
        app_secret = app_secret.strip()

        if len(app_id) == 0 or len(app_secret) == 0:
            return False

        self.app_id = app_id
        self.app_secret = app_secret

        return self.update_client()

    def is_valid(self) -> bool:
        app_id = self.app_id.strip()
        app_secret = self.app_secret.strip()

        if len(app_id) == 0 or len(app_secret) == 0:
            return False

        return self.client is not None

    def update_client(self) -> bool:
        app_id = self.app_id
        app_secret = self.app_secret

        if not app_id or not app_secret:
            return False

        app_id = app_id.strip()
        app_secret = app_secret.strip()

        if len(app_id) == 0 or len(app_secret) == 0:
            return False

        try:
            self.client = (
                LarkClient
                .builder()
                .app_id(app_id)
                .app_secret(app_secret)
                .build()
            )
            return True
        except Exception as e:
            # lark.logger.error(
            #     f"lark.Client.builder() failed, "
            #     f"error: {e},"
            #     f"app_id: {app_id}, "
            #     f"app_secret: {app_secret}"
            # )
            return False
