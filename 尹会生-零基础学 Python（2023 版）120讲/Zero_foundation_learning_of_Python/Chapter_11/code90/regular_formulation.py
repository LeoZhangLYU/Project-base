# NOTE: 非规范化数据分类
#  完全无格式数据
#  有特定规律的数据：json、以特定符号分隔的数据
#  规范数据：数据中有空数据、空格、特殊字符、乱码
dict1 = {'a': 123, 'b': 456}
import json

print(json.dumps(dict1))

json_string = '{"a":123, "b":456}'
print(json.loads(json_string))

import re

strings = 'Words, words. words.'
print(re.split(r'\W+', strings))

# NOTE: 类型转换库
#  常见的结构化文本格式有json和xml两种
#  可以采用json.dumps()将Python对象编码成JSON字符串
#  可以采用json.loads()将已编码的JSON字符串解码为Python对象
#  可以采用xml.etree包对xml格式进行解析

# NOTE: 正则表达式
#  元字符：. 1个字符；* 0个或多个字符；？ 0个或1个字符；+ 多个字符；() 分组符号
#  Python使用re库实现正则表达式的匹配操作，并在匹配指定字符后，能够实现数据的查找和删除功能
#  更复杂的功能数据处理可以使用：re.sub(pattern,repl,strings,count,flags)
