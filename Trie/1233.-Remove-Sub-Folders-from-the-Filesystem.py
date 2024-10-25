class Trie:
    def __init__(self):
        self.children={}
        self.isEnd=False

    def add(self,path):
        cur=self
        for f in path.split("/"):
            if f not in cur.children:
                cur.children[f]=Trie()
            cur=cur.children[f]
        cur.isEnd=True

    def prefix(self,path):
        cur=self
        folder=path.split("/")
        for i in range(len(folder)-1):
            cur=cur.children[folder[i]]
            if cur.isEnd:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # folder.sort()
        # res=set()
        # for files in folder:
        #     res.add(files)
        #     for i in range(len(files)):
        #         if files[i]=="/" and files[:i] in res:
        #             res.remove(files)
        #             break
        # return list(res)

        trie=Trie()

        for f in folder:
            trie.add(f)
        
        res=[]
        for f in folder:
            if not trie.prefix(f):
                res.append(f)
        return res





