class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record=list()
        ans=list()
        for ele in strs:
            temp=dict()
            for i in ele:
                if i in temp:
                    temp[i]+=1
                    continue
                temp[i]=1
            if temp in record:
                index=record.index(temp)
                ans[index].append(ele)
                continue
            record.append(temp)
            ans.append([ele])
        return ans
