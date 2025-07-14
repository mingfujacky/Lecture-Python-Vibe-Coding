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

# Python Course Featuring Vibe Coding Activities

歡迎來到 Vibe Coding Python 課程的 GitHub Repository！  
這是專為 **零程式基礎的初學者設計**，以 **AI 助理（如 ChatGPT 或 GitHub Copilot）** 為工具的Python入門課程。

# 🎯 課程目標
- 學會撰寫有效的提示（prompts），協助 AI 產出程式碼  
- 培養程式邏輯思維與除錯能力（debugging with AI）  
- 使用 Python 解決資料處理與自動化的實務問題  
- 執行並完成一個結合 AI 協作的迷你專題

# 🗂️ 資料夾結構
📁 labs/                # 平時練習與實驗
📁 projects/            # 期末專題與範例
📁 reflection_logs/     # 學生反思紀錄
📁 exams/               # 期中與期末考試範例
📁 syllabus/            # 課程大綱與週次安排
📁 assets/              # 補充資料與範例檔案

# 🚀 如何開始
1. Clone 或 fork 本 repo  
2. 安裝 VS Code 或使用 Google Colab 打開 `.ipynb` 檔案
3. 安裝 VS Code 或使用 Thonny 打開 `.py` 檔案  
4. 開始修改提示語、閱讀 AI 產生的程式碼，並記錄你的學習過程  
5. 完成 lab + reflection.md
6. 後開發並報告期末專題 🎉

# 🔧 建議工具
- [ChatGPT](https://chat.openai.com/)
- [Github Copilot](https://github.com/features/copilot)
- [VS Code](https://code.visualstudio.com/)
- [Thonny](https://thonny.org)
- [Google Colab](https://colab.research.google.com/)
- [Python Tutor](https://pythontutor.com/)
- [Online Judge](https://formosa.oj.cs.nycu.edu.tw/groups/55/problems/)

# 🧩 適合對象
- 沒有程式背景的新手  
- 想學習如何與 AI 合作開發的學習者  
- 高中、大學生、職涯轉職者等

# 📄 授權
本教材遵循  Apache-2.0 License，歡迎教師與學生自由修改與再利用。
