import secrets
from abc import ABC, abstractmethod


class AbstractTokensHelper(ABC):
    @abstractmethod
    def token_exists(
        self,
        token: str,
    ) -> bool:
        """
        :param token:
        :return:
        """

    @abstractmethod
    def add_token(
        self,
        token: str,
    ):
        """
        :param token:
        :return:
        """

    @abstractmethod
    def get_tokens(self) -> list[str]:
        pass

    @abstractmethod
    def delete_token(
        self,
        token: str,
    ) -> bool:
        pass

    @classmethod
    def generate_token(cls):
        return secrets.token_urlsafe(16)

    def generate_and_save_token(self) -> str:
        token = self.generate_token()
        self.add_token(token)
        return token
