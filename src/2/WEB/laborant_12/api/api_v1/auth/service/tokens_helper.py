from abc import ABC, abstractmethod
import secrets
import string

class AbstractTokensHelper(ABC):
    @abstractmethod
    def token_exists(self, token: str) -> bool:
        pass
    
    @abstractmethod
    def add_token(self, token: str) -> bool:
        pass

    @abstractmethod
    def delete_token(self, token: str) -> bool:
        pass

    @abstractmethod
    def get_tokens(self) -> list[str]:
        pass
    
    @classmethod
    def _generate_token(self) -> str:
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(16))

    def generate_and_save_token(self) -> bool:
        token = self._generate_token()
        self.add_token(token)
        return token
