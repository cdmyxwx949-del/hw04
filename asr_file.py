#!/usr/bin/env python
# coding: utf-8

# In[2]:


import whisper

# 加载模型（base 最轻量，最快）
model = whisper.load_model("base")

# 识别音频文件（把 test.wav 换成你自己的音频文件名）
result = model.transcribe("test.wav", language="zh")

# 输出结果
print("\n【识别结果】")
print(result["text"])


# In[ ]:




