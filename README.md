# hw04
大模型文案、剪映声音克隆与开源语音识别实践

任务一
文件：text_gen.md                            # 标题、大模型生成全文、模型与 Prompt 说明

任务二
文件：tea_life_voice.mp3                     # 生成克隆音频
     jianying.md.pdf                        # 剪映产出说明

任务三
文件：asr_file.py                            # 音频文件识别脚本
     asr_realtime.py                        # 麦克风实时识别脚本
     asr_report.md.py                       # ASR 报告与代码
     exeriment_log.md.pdf                   # 记录实验过程与结果
     ffmpeg-8.1.tar.xz                      # 音视频处理工具 / 库
     PyAudio-0.2.14-cp311-win_amd64.whl     # Python 在 Windows 上用来录音的驱动文件
     requirements.txt                       # 可复现代码
若复现时出现问题，可将问题截图问ai（由于我运行时报错太多，安装太多，可能会遗漏代码）。

运行命令
1. 环境配置
   # 1. 创建并激活Anaconda环境（推荐）
conda create -n asr_env python=3.11 -y
conda activate asr_env

# 2. 安装核心依赖
conda install -c conda-forge ffmpeg pyaudio numpy=2.3.1 -y
pip install -r requirements.txt

2. 运行脚本
   # 切换到项目目录
cd C:\Users\32414\Desktop\asr_project

# 音频文件识别（替换test.wav为你的音频）
python asr_file.py

# 麦克风实时识别
python asr_realtime.py

