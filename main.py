from Group import Group
from SNS import SNS


class Student:
    def __init__(self, sns: SNS, group: Group):
        self._sns = sns
        self._group = group

    def get_sns(self) -> SNS:
        return self._sns

    def set_sns(self, sns: SNS) -> None:
        self._sns = sns

    def get_group(self) -> Group:
        return self._group

    def set_group(self, group: Group) -> None:
        self._group = group



