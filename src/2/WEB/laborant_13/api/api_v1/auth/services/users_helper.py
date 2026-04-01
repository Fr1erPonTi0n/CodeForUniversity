from abc import ABC, abstractmethod


class AbstractUserHelper(ABC):

    @abstractmethod
    def get_user_password(
        self,
        username: str,
    ) -> str | None:
        """
        :param:
        :return:
        """

    @classmethod
    def check_passwords_match(
        cls,
        password1: str,
        password2: str,
    ):
        return password1 == password2

    def validate_user_password(
        self,
        username: str,
        password: str,
    ):
        """
        :param:
        :return:
        """

        db_password = self.get_user_password(username)
        print(db_password)
        if db_password is None:
            return False
        return self.check_passwords_match(
            password1=db_password,
            password2=password,
        )
