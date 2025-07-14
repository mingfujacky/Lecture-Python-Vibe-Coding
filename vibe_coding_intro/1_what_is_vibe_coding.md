---
marp: true
theme: default
class: 
size: 16:9
paginate: true
footer: 國立陽明交通大學 電子與光子學士學位學程
headingDivider: 1
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
  
  .middle-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 75%;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid img {
    width: 100%;
  }
  .red-text {
    color: red;
  }
  
  .blue-text {
    color: blue;  
  }

  .small-text {
    font-size: 0.80rem;
  }
---

# 🤖 什麼是 Vibe Coding (氛圍編程)?
Vibe coding = coding with AI pair-programmers like Copilot or ChatGPT

- 提出者：OpenAI 前研究總監 Andrej Karpathy
- 利用生成式 AI（如 Copilot、ChatGPT）以自然語言生成程式
- 初學者能快速產出結果，減少挫折、提升學習樂趣
- 📺 [影片連結](https://youtu.be/8me0juJCpWM?si=3tcdojzGbhJKxFGo)

# 🧠 為什麼需要學 Vibe Coding？
- AI 不會取代人，但「使用 AI 的人」會取代不用 AI 的人
- 企業已進入 AI 優先時代，三年年資以下的工程師職缺大幅減少

# 🎓 學習者的焦慮與解法
- AI 無法獨立部署核心系統
- 企業需要的是能監督並有效使用 AI 的人

# 🚀 使用案例
- GitHub Copilot + VS Code：計算句子中最長單字
- ChatGPT + Thonny：閏年判斷程式
- Gemini + Colab：圖片背景移除工具

# 🔍 學習建議
- 從小處著手，逐步擴大功能
- 保持模組化，維持清晰的結構
- 信任經驗，檢視 AI 產出的程式碼

# 🔗 延伸閱讀
- [70% 問題：AI 輔助開發真實樣貌](https://www.thingsaboutweb.dev/zh-TW/posts/the-70-percent-problem)
- [AI 取代新鮮人職場挑戰](https://www.cw.com.tw/article/5135668)
