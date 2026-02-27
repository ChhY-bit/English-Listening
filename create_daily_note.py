import os
from datetime import datetime

# 模板常量
NOTE_TEMPLATE = r"""# English Listening Practice

**Date:** {date}
**Time:** {time}

---

## Meterial Resource:
type your text
<url>your url link here</url>


## Roughly:
<span style="color:blue">Listen roughly and record the key words.</span>


## Carefully:
<span style="color:blue">Listen carefully and write down as much as you can get.</span>

## Correction:
<span style="color:blue">Check the original material and correct the mistakes.</span>

## Summary:
<span style="color:blue">Summarize the fallible points and new words.</span>

---
## <span style="color:red">Keep on! You will do better tomorrow!</span>
"""

def create_daily_note():
    """创建每日英语听力练习笔记文件

    Returns:
        str: 创建或已存在文件的完整路径
    """
    # 获取当前日期和时间（使用本地时区）
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    time_str = today.strftime("%H%M%S")
    time_str2 = today.strftime("%H:%M:%S")
    
    # 生成文件名（精确到秒）
    filename = f"{date_str}_{time_str}_English_Listening.md"
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    
    # 检查文件是否已存在
    if os.path.exists(filepath):
        print(f"文件已存在: {filename}")
        return filepath
    
    # 生成文件内容
    content = NOTE_TEMPLATE.format(date=today.strftime("%Y-%m-%d"), time=time_str2)
    
    # 创建文件（添加异常处理）
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 已创建文件: {filename}")
    except (IOError, OSError) as e:
        print(f"❌ 创建文件失败: {e}")
        return None
    
    return filepath

if __name__ == "__main__":
    create_daily_note()
