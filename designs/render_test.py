# -*- coding: utf-8 -*-
import os
import subprocess
import time

DESIGNS_DIR = r"E:\mess\designs"
ASSETS_DIR = os.path.join(DESIGNS_DIR, "assets")

def render(html_name, png_name, width=1440, height=2200, scale=1.5):
    html_file = os.path.join(DESIGNS_DIR, html_name)
    png_file = os.path.join(DESIGNS_DIR, png_name)
    file_url = "file:///" + os.path.abspath(html_file).replace("\\", "/")
    
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--force-device-scale-factor={scale}",
        "--virtual-time-budget=3000",
        f"--screenshot={png_file}",
        file_url
    ]
    print(f"Rendering {html_name} -> {png_name}...")
    subprocess.run(cmd, check=True)
    if os.path.exists(png_file):
        print(f"OK: {png_name} ({os.path.getsize(png_file)/1024:.1f} KB)")
    else:
        print(f"ERR: {png_name} not generated")

print("Render function ready!")

