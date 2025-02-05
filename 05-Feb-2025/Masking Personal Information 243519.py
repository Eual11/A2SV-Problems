# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string


import re
class Solution:
        def maskPII(self, s: str) -> str:
            if("@" not in s):
                split_string = "".join(re.split("[\+\(\) \-]", s))
                if(len(split_string) ==10):
                    return "***-***-"+split_string[-4:]
                return "+"+"*"*(len(split_string)-10)+"-***-***-"+split_string[-4:]

            else:
                username, domain = s.split("@")
                if(len(username) >1):
                    masked_username = username[0]+"*"*5+username[-1]
                else:
                   masked_username = username[0]+"*"*5 
                masked_username = masked_username.lower() 
                return masked_username+"@"+domain.lower()


 