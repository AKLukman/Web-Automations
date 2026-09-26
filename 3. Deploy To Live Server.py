"""
aaPanel Internet Address: https://84.247.147.56:11442/16319392
aaPanel Internal Address: https://84.247.147.56:11442/16319392
username: evozfyzw
password: a8d627fd

--------


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9091, reload=True)

--------

python3.12 -m venv venv
source venv/bin/activate
pip install playwright
playwright install chromium
pip install fastapi uvicorn

uvicorn main:app --reload
xvfb-run uvicorn main:app --reload


nano /etc/systemd/system/youtube.service

[Unit]
Description=YouTube Scraping Service
After=network.target

[Service]
User=root
WorkingDirectory=/www/wwwroot/youtube
ExecStart=/usr/bin/xvfb-run -a /www/wwwroot/youtube/venv/bin/uvicorn main:app --host 0.0.0.0 --port 9094
Restart=always
Environment=DISPLAY=:99

[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl start youtube
sudo systemctl enable youtube
sudo systemctl status youtube

"""

