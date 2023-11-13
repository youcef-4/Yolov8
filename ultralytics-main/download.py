import urllib.request

url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
filename = "yolov8n.pt"
urllib.request.urlretrieve(url, filename)