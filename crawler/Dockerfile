# 使用 Python 3.11 作為基礎映像
FROM python:3.11

# 設置工作目錄
WORKDIR /app

# 複製當前目錄下的所有文件到 Docker 容器內
COPY . /app

# 安裝爬蟲所需的依賴
RUN pip install --no-cache-dir -r requirements.txt

# 執行爬蟲
CMD ["python", "scraper.py"]