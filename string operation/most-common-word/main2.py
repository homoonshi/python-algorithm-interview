#List Comprehension, Counter

import collections
import re

paragraph = input()
banned = input()

def mostCommonWord(paragraph : str, banned : list[str]) -> str :
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split()
         if word not in banned]

    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]

print(mostCommonWord(paragraph,banned))

