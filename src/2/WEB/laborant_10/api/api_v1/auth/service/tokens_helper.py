from abc import ABC, abstractmethod

class AbstractTokensHelper(ABC):
    @abstractmethod
    def token_exists(self, token: str) -> bool:
        pass
    
    @abstractmethod
    def add_token(self, token: str) -> bool:
        pass
    
    @classmethod
    def _generate_token(self):
        pass

    def generate_and_save_token(self) -> bool:
        token = self._generate_token()
