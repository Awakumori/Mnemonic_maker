import itertools
import jieba
from pypinyin import pinyin, lazy_pinyin
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()


def takeFirst(elem):
    return elem[0]


# 构特规泛扩限变结

str0 = ''
str1 = (lazy_pinyin(str0))

strs = list(itertools.permutations(str1, len(str1)))

results = []

for py_str in strs:
    result = dag(dagparams, py_str, path_num=1)
    for item in result:
        results.append((item.score, item.path))

results.sort(key=takeFirst, reverse=True)

print(results[0:3])
