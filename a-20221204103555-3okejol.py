from asyncore import write

# 打开
with open(r"[English] Lecture 15 Efficient Methods and Hardware for Deep Learning [DownSub.com].txt","r", encoding="utf-8") as f: # 前面的r是防止转义，后面的r是为了可读
    strs = f.read()

# 操作
re = []
for i, s in enumerate(strs):
    if s=="\n" and strs[i-1]!='\n':
        re.append(" ")
    else:
        re.append(s)
re = list(map(str, re))
re = "".join(re)

# 写入
with open(r"[English] Lecture 15 Efficient Methods and Hardware for Deep Learning [DownSub.com].txt","w", encoding="utf-8") as f:
    f.write(re)