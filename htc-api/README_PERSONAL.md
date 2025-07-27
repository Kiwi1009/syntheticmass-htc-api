# HTC API - Massachusetts High Tech Counsel Project

這是一個基於 Flask 的 REST API，用於提供麻薩諸塞州的地理和人口統計數據。

## 功能特色

- 提供麻薩諸塞州各縣的地理和統計數據
- 支援 GeoJSON 格式的地理數據
- 包含合成健康數據
- 支援緩存機制
- 跨域請求支援 (CORS)

## 快速開始

### 環境要求

- Python 3.7+
- pip

### 安裝步驟

1. **克隆專案**
   ```bash
   git clone <your-github-repo-url>
   cd syntheticmass/htc-api/api
   ```

2. **創建虛擬環境**
   ```bash
   python -m venv venv
   ```

3. **啟動虛擬環境**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **安裝依賴項**
   ```bash
   pip install -r requirements_py3.txt
   ```

5. **運行 API**
   ```bash
   python htc_api_demo.py
   ```

### 測試 API

API 啟動後，您可以訪問以下端點：

- **API 文檔**: http://localhost:8080/htc/api/v1
- **測試端點**: http://localhost:8080/htc/api/v1/test
- **縣級列表**: http://localhost:8080/htc/api/v1/counties/list
- **縣級統計**: http://localhost:8080/htc/api/v1/counties/stats
- **特定縣級數據**: http://localhost:8080/htc/api/v1/counties/name/Worcester

## API 端點

### 基本端點

- `GET /htc/api/v1` - API 文檔
- `GET /htc/api/v1/test` - 測試端點

### 縣級數據

- `GET /htc/api/v1/counties/list` - 獲取所有縣級列表
- `GET /htc/api/v1/counties/stats` - 獲取縣級統計數據
- `GET /htc/api/v1/counties/name/{county_name}` - 按名稱查詢縣級數據

### 示例請求

```bash
# 獲取縣級列表
curl http://localhost:8080/htc/api/v1/counties/list

# 獲取 Worcester 縣的數據
curl http://localhost:8080/htc/api/v1/counties/name/Worcester

# 獲取縣級統計數據
curl http://localhost:8080/htc/api/v1/counties/stats
```

## 文件結構

```
htc-api/
├── api/
│   ├── htc_api.py          # 原始 API 文件 (需要數據庫)
│   ├── htc_api_demo.py     # 演示版本 (使用模擬數據)
│   ├── htc_api_simple.py   # 簡化版本
│   ├── requirements.txt    # 原始依賴項 (Python 2.7)
│   ├── requirements_py3.txt # Python 3 依賴項
│   ├── postgis2geojson.py  # PostGIS 到 GeoJSON 轉換
│   └── .gitignore          # Git 忽略文件
└── db/
    └── README.md           # 數據庫相關說明
```

## 注意事項

1. **數據庫連接**: 原始版本需要 PostgreSQL 數據庫，演示版本使用模擬數據
2. **Python 版本**: 原始版本為 Python 2.7，演示版本支援 Python 3
3. **依賴項**: 使用 `requirements_py3.txt` 安裝 Python 3 兼容的套件

## 開發

### 添加新的端點

在 `htc_api_demo.py` 中添加新的路由：

```python
@app.route('/htc/api/v1/new-endpoint', methods=['GET'])
@cache.cached(timeout=300)
def new_endpoint():
    return jsonify({"message": "New endpoint"})
```

### 修改緩存時間

```python
@cache.cached(timeout=600)  # 10 分鐘緩存
```

## 授權

本專案基於 Apache License 2.0 授權。

## 貢獻

歡迎提交 Issue 和 Pull Request！

## 聯繫

如有問題，請在 GitHub 上創建 Issue。 