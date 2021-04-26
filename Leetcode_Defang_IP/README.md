# Leetcode_Defang_IP

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
```Python
class Solution:
    def defangIPaddr(self, address: str) -> str:
```
---

This can be done with a single string replace method.
```Python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]") # Take given input(address), replace . with [.]
```
