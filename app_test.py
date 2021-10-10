import pytest
from app import Encrypt
class Text_Encrytion():
    def test1(self):
        sc=Encrypt()
        assert sc.cipher([])=='Svool dliow!'