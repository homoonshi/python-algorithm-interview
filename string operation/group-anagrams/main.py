import collections

str = list(input().split())

def groupAnagrams(strs : list[str])-> list[list[str]]:
    anagrams = collections.defaultdict(list)

    strs=sorted(strs)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    anagrams=sorted(anagrams.values(),reverse=True,key= lambda x : len(x))

    return list(anagrams)


print(groupAnagrams(str))

