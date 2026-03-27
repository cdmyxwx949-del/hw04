#!/usr/bin/env python
# coding: utf-8

# In[2]:


import whisper
import pyaudio
import numpy as np
import wave
import os
import time

# 加载模型
model = whisper.load_model("base")

# 录音参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 3  # 每3秒识别一次
WAVE_OUTPUT_FILENAME = "temp.wav"

p = pyaudio.PyAudio()

print("✅ 实时语音识别已启动，说话即可识别...")

while True:
    # 开始录音
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # 停止录音
    stream.stop_stream()
    stream.close()

    # 保存临时音频
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # 识别
    result = model.transcribe(WAVE_OUTPUT_FILENAME, language="zh")
    text = result["text"].strip()
    
    if text:
        print("你说：" + text)

    # 删除临时文件
    os.remove(WAVE_OUTPUT_FILENAME)


# In[ ]:




