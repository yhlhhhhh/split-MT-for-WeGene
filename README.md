# split-MT-for-WeGene
此工具可以用微基因微解读给出的用户单倍群数据提取出母系单倍群并将其切割，切割出的上游结果以列表形式返回。
# import
此段代码是利用re模块进行单倍群切割的，所以
```python
import re
```
微基因官方是以json形式给出的用户单倍群信息，所以
```python
import sys
import json
```
# 读取数据
```python
body = sys.stdin.read()
inputs = json.loads(body)['inputs']
```
# 提取出用户的母系单倍群
```python
haplogroup = inputs['haplogroup']
mtdic = haplogroup['mt']
MT = mtdic['haplogroup']
```
# 将母系单倍群中的字母与数字分离
```python
letter_group = re.split("\d",MT)
number_group = re.split('\D',MT)
```
如果说用户的母系单倍群是A8a2a那么输出结果如下
```python
['A', 'a', 'a'] ['', '8', '2', '']
```
如果说用户的母系单倍群是A8那么输出结果如下
```python
['A', ''] ['', '8']
```
如果说用户的母系单倍群是A那么输出结果如下
```python
['A'] ['', '']
```
如果说用户的母系单倍群是A15c那么输出结果如下
```python
['A', '', 'c'] ['', '15', '']
```
# 将后的两个列表中的元素整理，并合成含有特定元素的列表
```python
Simple_MT1 = letter_group[0]     #如A,B,C......
number1 = number_group[1]
letter1 = letter_group[1]
Simple_MT2 = Simple_MT1 + number1   #如A8,B4,C4......
Simple_MT3 = Simple_MT2 + letter1   #如A8a，B4a......
Simple_MT = [Simple_MT1,Simple_MT2,Simple_MT3]
```
# 返回结果
```python
return Simple_MT
```
# 如果要在自己的脚本用的时候
```python
import sys
import json
from MT_split_tool import split_mt
body = sys.stdin.read()
inputs = json.loads(body)['inputs']
split_mt()
```
# 输出结果示例
|原始单倍群|输出结果|备注|
|:---:|:---:|:---:|
|A|报错|事先将只有一个字母的结果处理好即可|
|A8|['A', 'A8', 'A8']|--|
|A8a2a|['A', 'A8', 'A8a']|--|
|A2ab|['A', 'A2', 'A2ab']|--|
|M80'D|报错|事先将带其他除数字和字母的字符串进行处理|
