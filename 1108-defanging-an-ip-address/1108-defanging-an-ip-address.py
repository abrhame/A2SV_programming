class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = address.split(".")
        b = "[.]".join(a)
        return b