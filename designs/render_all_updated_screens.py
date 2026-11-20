# -*- coding: utf-8 -*-
import os
import subprocess
import shutil

DESIGNS_DIR = r"E:\mess\designs"
ROOT_DIR = r"E:\mess"

def run_script(script_name):
    path = os.path.join(DESIGNS_DIR, script_name)
    print(f"\n=======================================================")
    print(f"RUNNING: {script_name}")
    print(f"=======================================================")
    res = subprocess.run(["python", path], capture_output=True, text=True, encoding="utf-8")
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    if res.returncode != 0:
        print(f"FAILED with code {res.returncode}")
    else:
        print(f"SUCCESS: {script_name}")

def render_html(html_file, png_file, width=1440, height=2200):
    html_path = os.path.join(DESIGNS_DIR, html_file)
    png_path = os.path.join(DESIGNS_DIR, png_file)
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--force-device-scale-factor=1.5",
        f"--virtual-time-budget=3000",
        f"--screenshot={png_path}",
        f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
    ]
    print(f"Rendering: {html_file} -> {png_file}...")
    subprocess.run(cmd, check=True)
    size_kb = os.path.getsize(png_path) / 1024
    print(f"SUCCESS: {png_file} ({size_kb:.1f} KB)")

# Run desktop page generators
run_script("make_page_01.py")
run_script("make_page_02.py")
run_script("make_page_03.py")
run_script("make_page_04.py")
run_script("make_page_05.py")
run_script("script_update_desktop_customer_pages.py")

# Render updated admin pages 14 and 16
render_html("page_14_admin_orders_table.html", "14_جدول_إدارة_الطلبات_Desktop_Admin_Orders_Table.png", 1440, 1800)
render_html("page_16_admin_customers.html", "16_إدارة_العملاء_والشركات_Desktop_Admin_Customers.png", 1440, 1800)

# Run mobile updates
run_script("update_all_mobile_screens.py")

# Copy all PNGs to root
print("\nCopying PNGs to root E:\\mess...")
for f in os.listdir(DESIGNS_DIR):
    if f.endswith(".png"):
        src = os.path.join(DESIGNS_DIR, f)
        dst = os.path.join(ROOT_DIR, f)
        shutil.copy2(src, dst)
print("PNGs successfully copied to root!")

# Rebuild Figma Board
run_script("build_final_figma_board.py")
print("\n>>> ALL RENDERS AND FIGMA BOARD FULLY UPDATED!")
