# 問卷隨機分派系統

簡單的問卷隨機分派系統，用於在飯店問卷和醫療問卷之間平衡分派受訪者。

## 🎯 功能

- ⚡ **零延遲** - 點連結立即跳轉，完全無感分派
- ⚖️ **公平分派** - 自動追蹤，確保兩份問卷 50:50 分派
- 📄 **極簡設計** - 只有一個連結，無任何 UI
- ♾️ **無限制** - 支持無限數量的受訪者分派
- 💾 **本地存儲** - 使用瀏覽器 localStorage 記錄分派數據

## 🚀 立即使用

**直接分享這個連結給受訪者：**

```
https://tiara-lin.github.io/affective_AI_ch/
```

受訪者點擊連結即可：
- ⚡ **立即跳轉**到隨機分派的問卷
- 📄 沒有任何頁面或 UI
- 💾 後台自動記錄分派（無感操作）

## 🔗 問卷連結

- **飯店問卷**: https://tassel.syd1.qualtrics.com/jfe/form/SV_cCtJgUMGbUGfyxE
- **醫療問卷**: https://tassel.syd1.qualtrics.com/jfe/form/SV_1TXCuW7dGUxH7Aa

## 📊 分派邏輯

系統自動追蹤每份問卷的分派數量：

- 如果兩份問卷人數相同 → **隨機選擇**
- 如果一份較少 → **優先分派到較少的那份**

結果：100 個訪客會分派為大約 **50:50** 而不是隨機的 45:55 或 40:60

## 📁 文件結構

```
├── index.html              # 主程式（35 行代碼）
├── README.md              # 項目說明
├── app.py                 # Flask 版本（備用）
├── survey_randomizer.py   # 本地 Python 版本（備用）
└── .github/               # GitHub Actions 配置
```

## 🔧 本地運行

如果要在本地測試：

1. 直接用瀏覽器打開 `index.html` 即可
2. 或用簡單的 HTTP 伺服器：
```bash
python -m http.server 8000
```
訪問 http://localhost:8000

## 📈 查看統計

頁面會自動顯示：
- 總分派人數
- 飯店問卷分派數和百分比
- 醫療問卷分派數和百分比
- 進度條視覺化

## 🔄 重置統計

如果需要清空所有統計數據，在瀏覽器控制台執行：

```javascript
localStorage.removeItem('survey_distribution');
```

或直接清除瀏覽器的網站數據。

## 💡 進階用法

### 1. 自定義問卷 URL

編輯 `index.html` 中的 `SURVEYS` 物件：

```javascript
const SURVEYS = {
    hotel: "你的飯店問卷 URL",
    medical: "你的醫療問卷 URL"
};
```

### 2. 查看分派統計

在瀏覽器控制台執行：

```javascript
JSON.parse(localStorage.getItem('survey_distribution'))
// 返回: { "hotel": 50, "medical": 50 }
```

### 3. 自定義分派邏輯

編輯 `index.html` 中的 `getBalancedSurvey()` 函數。

## 🌐 部署方式

### GitHub Pages（推薦，已配置）
已自動配置為 GitHub Pages 項目，每次 push 都會自動部署。

### 其他靜態網站服務
- Netlify
- Vercel  
- Firebase Hosting

直接上傳 `index.html` 即可。

## 📝 注意事項

- **跨域問題**：如果自己的 Qualtrics 連結被限制，可能需要在 iframe 中打開
- **分派數據**：統計數據存在瀏覽器中，清除瀏覽器數據會重置
- **跨設備**：不同設備/瀏覽器的統計數據獨立

## 🐛 故障排除

**問題：點擊後沒有跳轉**
- 檢查 Qualtrics URL 是否正確
- 確認瀏覽器允許跳轉

**問題：統計數據消失**
- 這是正常的，瀏覽器清除數據會導致重置
- 可以自行修改代碼改用伺服器存儲

## 📄 許可

MIT License

---

**有問題？** 在 GitHub 上提 Issue 或 PR！
