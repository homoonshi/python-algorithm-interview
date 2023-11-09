#List Comprehension

import collections
import re

paragraph = input()
banned = input()

def mostCommonWord(paragraph : str, banned : list[str]) -> str :
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split()
         if word not in banned]

    counts = collections.defaultdict(int)

    for word in words:
        counts[word]+=1

    return max(counts,key=counts.get())

print(mostCommonWord(paragraph,banned))

