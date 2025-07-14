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

# 電腦程式與計算分析(一) 課程大綱  
**授課教師**：林志偉（國立陽明交通大學 學士後電子與光子學程）  
**學分時數**：3 學分  
**授課時間**：F567
**授課地點**：ED117   
**聯絡方式**：jacky.jw.lin@nycu.edu.tw
**助教名單**：TBD

# 🎯 課程目標
- 養成問題拆解與運算思維，設計流程解決實務問題
- 學習 Python 語法與常用模組
- 透過 **AI 輔助（ChatGPT / Copilot）** 協作完成程式專案
- 培養「閱讀與修改程式碼」的能力，而非死背語法

# 🧠 課程特色
- 不強調語法記憶，而是著重「如何與 AI 合作寫程式」
- 採用 **Vibe Coding 教學風格**：從 prompt 出發，靠理解與除錯前進
- 實作導向，搭配 Thonny 以及 VS Code IDE 進行實驗
- 鼓勵學生以迷你專案發展出屬於自己的應用

# 📅 週次進度表（共 16 週）
<style scoped>
table {
  font-size: 10px;
}
</style>
| 週次 | 日期 | 主題 |
|------|------|------|
| 1 | 09/05 | 課程介紹、AI 工具介紹（ChatGPT、Colab） |
| 2 | 09/12 | Python 基礎：資料型別與運算子 |
| 3 | 09/19 | 條件判斷、流程控制、內建函式 |
| 4 | 09/26 | 練習 Online Judge，函式設計 |
| 5 | 10/03 | 模組與變數作用範圍 |
| 6 | 10/10 | 國慶日停課 |
| 7 | 10/17 | 字串、數值與邏輯運算整合練習 |
| 8 | 10/24 | 🧪 期中考 |
| 9 | 10/31 | Tuple, List, Set, Dictionary |
|10 | 11/07 | 條件/迴圈綜合練習、模組封裝 |
|11 | 11/14 | 類別與物件導論 |
|12 | 11/21 | Toolbox: 檔案操作 |
|13 | 11/28 | Toolbox: Numpy 與 Matplotlib |
|14 | 12/05 | 🛠️ 專題發表 I |
|15 | 12/12 | 🛠️ 專題發表 II |
|16 | 12/19 | 📝 期末考 |

# 📝 評分方式

| 項目 | 比例 |
|------|------|
| 期中考 | 20% |
| 期末考 | 20% |
| 期末專案（團隊） | 20% |
| 作業練習（含 Reflection Logs） | 10% |
| 線上程式挑戰（OJ） | 20% |
| 出席與課堂參與 | 10% |

# 📚 教材與工具

- **Python Basics: A Practical Introduction to Python 3**  
  作者：David Amos 等人｜ISBN：1775093328  [📘](https://www.books.com.tw/products/0010955256?sloc=main)
  
- [課程教材：Syntax ](https://github.com/mingfujacky/Lecture-Python.git)
- [課程教材：Vibe Coding](https://github.com/mingfujacky/Lecture-Python-Vibe-Coding.git)

# 💬 注意事項

- 請自備筆電並確保課堂練習可順利執行
- 作業逾期恕不受理
- 期末專案將以小組方式進行。全班將依照選課人數分成若干小組。每組需開發一個應用系統，以展示其 Python 程式設計能力。專案主題不限。
- 共五次點名，每次點名
  - 出席：2分
  - 沒出席有請假：1分 (在學生請假系統中填寫假單)
  - 沒出席沒請假：0分
- 如需協助，請聯絡老師或助教，並善用 ChatGPT 當作你最可靠的助理