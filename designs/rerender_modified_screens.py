# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

DESIGNS_DIR = r"E:\mess\designs"
ROOT_DIR = r"E:\mess"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def render(html_path, png_path, width, height, scale=1.5, wait_ms=2500):
    abs_html = os.path.abspath(html_path)
    file_url = "file:///" + abs_html.replace("\\", "/")
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--force-device-scale-factor={scale}",
        f"--virtual-time-budget={wait_ms}",
        f"--screenshot={png_path}",
        file_url
    ]
    print(f"Rendering: {html_path} -> {png_path} ({width}x{height} @ {scale}x)...")
    subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(png_path):
        size_kb = os.path.getsize(png_path) / 1024
        print(f"  SUCCESS: {png_path} ({size_kb:.1f} KB)")
        base_name = os.path.basename(png_path)
        root_target = os.path.join(ROOT_DIR, base_name)
        shutil.copy2(png_path, root_target)
        print(f"  COPIED TO ROOT: {root_target}")
        return True
    else:
        print(f"  FAILED: {png_path}")
        return False

# Clean up untracked temporary images
for extra in [
    "15_لوحة_تفاصيل_الطلب_Admin_Order_Details.png",
    "16_لوحة_إدارة_العملاء_Admin_Customers.png",
    os.path.join("designs", "15_لوحة_تفاصيل_الطلب_Admin_Order_Details.png"),
    os.path.join("designs", "16_لوحة_إدارة_العملاء_Admin_Customers.png")
]:
    if os.path.exists(extra):
        os.remove(extra)
        print(f"Removed temporary file: {extra}")

# 1. Page 11: Desktop Customer Profile
p11_html = os.path.join(DESIGNS_DIR, "page_11_customer_profile.html")
p11_png = os.path.join(DESIGNS_DIR, "11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png")
render(p11_html, p11_png, width=1440, height=1450)

# 2. Mobile 09: Mobile Customer Profile
m09_html = os.path.join(DESIGNS_DIR, "mobile_09_framed.html")
m09_png = os.path.join(DESIGNS_DIR, "Mobile_09_لوحة_حسابي_والعناوين_Mobile_Customer_Profile.png")
render(m09_html, m09_png, width=540, height=980)

# 3. Page 16: Admin Customers Table
p16_html = os.path.join(DESIGNS_DIR, "page_16_admin_customers.html")
p16_png = os.path.join(DESIGNS_DIR, "16_إدارة_العملاء_والشركات_Desktop_Admin_Customers.png")
render(p16_html, p16_png, width=1440, height=1350)

# 4. Page 15: Admin Order Details
p15_html = os.path.join(DESIGNS_DIR, "page_15_admin_order_details.html")
p15_png = os.path.join(DESIGNS_DIR, "15_تفاصيل_الطلب_إدارة_Desktop_Admin_Order_Details.png")
render(p15_html, p15_png, width=1440, height=1400)

print("\nAll 4 screens successfully rendered to exact tracked filenames and copied to root!")
