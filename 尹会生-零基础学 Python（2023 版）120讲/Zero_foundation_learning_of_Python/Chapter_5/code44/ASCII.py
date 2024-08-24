# NOTE: 常见操作系统的文件编码
#  windows默认使用GBK编码
#  Linux和macos使用UTF-8编码

f = open('demo_GBK.txt', 'w', encoding='GBK')
f.write("人生苦短，我用Python")
f.close()

f = open('demo_GBK.txt', 'r', encoding='GBK')
data = f.readlines()
print(data)
f.close()

# NOTE: 总结
#  以不正确的编码打开文件会产生乱码
#  通过encoding参数能够以指定的编码打开文件
