# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dub_dict ={}
        res =[]

        for dir in paths:
            idx = dir.find(" ")
            if(idx ==-1):
                continue
            parent_path = dir[:idx]
            file_n = dir[idx+1:]

            raw_file = []
            for c in file_n:
                
                if(c ==")"):
                    raw_file.append(c)
                    content = self.fetch_contnet("".join(raw_file))
                    if(content[1] in dub_dict):
                        dub_dict[content[1]].append(parent_path+"/"+content[0])
                    else:
                        dub_dict[content[1]]=[parent_path+"/"+content[0]]
                    
                    raw_file.clear()
                else:
                    raw_file.append(c)

        
        return [v for _, v in dub_dict.items() if len(v) >1]
    def fetch_contnet(self, file:str):
        file =file.strip()
        content = []
        content_start = False
        filename =[]


        for c in file:
            if(content_start):
                if(c ==")"):
                    break
                else:
                    content.append(c)
            elif(c =="("):
                content_start = True
            else:
                filename.append(c)


        return ("".join(filename), "".join(content))
