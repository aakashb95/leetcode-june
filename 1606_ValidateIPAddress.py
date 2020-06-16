# Fastest - beats 90%
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def check4(ip):
            l = ip.split(".")
            if len(l) != 4:
                return False
            flag = []
            for s in l:
                try:
                    if len(s) > 1 and (s.startswith("0") == True or s.startswith("-")):
                        return False
                    elif 0 <= int(s) <= 255:
                        flag.append(True)
                    else:
                        flag.append(False)
                except:
                    return False
            return False if False in flag else True

        def check6(ip):
            l = ip.split(":")
            if len(l) != 8:
                return False
            flag = []
            for s in l:
                if len(s) > 0 and len(s) <= 4:
                    for char in s:
                        if char not in "0123456789abcdefABCDEF":
                            flag.append(False)
                    flag.append(True)
                else:
                    flag.append(False)

            return False if False in flag else True

        a = check4(IP)
        b = check6(IP)

        if a:
            return "IPv4"
        elif b:
            return "IPv6"
        else:
            return "Neither"


# Divide and Conquer -> More Understandable:
class Solution:
    def validIPAddress(self, IP: str) -> str:
        def check4(IP):
            flag = []
            if IP.count(".") == 3:
                l = IP.split(".")
                if len(l) == 4:
                    for s in l:
                        if len(s) > 1 and s[0] == "0":
                            flag.append(False)
                        elif s.isdigit():
                            if int(s) >= 0 and int(s) <= 255:
                                flag.append(True)
                            else:
                                flag.append(False)
                        else:
                            flag.append(False)
                else:
                    flag.append(False)
            else:
                flag.append(False)
            return all(flag)

        def check6(IP):
            flag = []
            hex_digits = "1234567890abcdefABCDEF"
            if IP.count(":") == 7:
                l = IP.split(":")
                if len(l) == 8:
                    for s in l:
                        if len(s) < 1 or len(s) > 4:
                            flag.append(False)
                        for chars in s:
                            if chars in hex_digits:
                                flag.append(True)
                            else:
                                flag.append(False)

                else:
                    flag.append(False)
            else:
                flag.append(False)
            return all(flag)

        a = check4(IP)
        b = check6(IP)

        if a:
            return "IPv4"
        elif b:
            return "IPv6"
        else:
            return "Neither"
