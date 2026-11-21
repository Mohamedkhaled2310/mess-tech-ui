# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

DESIGNS_DIR = r"E:\mess\designs"
ROOT_DIR = r"E:\mess"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# ==============================================================================
# 1. UPDATE page_00_design_system_palette.html
# ==============================================================================
p00_path = os.path.join(DESIGNS_DIR, "page_00_design_system_palette.html")
with open(p00_path, "r", encoding="utf-8") as f:
    p00 = f.read()

# Replace any occurrence of the old dark colors
p00 = p00.replace("#070d18", "#0a3658").replace("#070D18", "#0A3658")
p00 = p00.replace("#0b1120", "#0e4c77").replace("#0B1120", "#0E4C77")
p00 = p00.replace("#0f172a", "#125c90").replace("#0F172A", "#125C90")
p00 = p00.replace("#172136", "#176ea9").replace("#172136", "#176EA9")
p00 = p00.replace("كحلي غامق للغاية (Midnight Black)", "بترولي بحري عميق (Deep Marine Petrol)")
p00 = p00.replace("كحلي تكنولوجي داكن (Deep Navy)", "بترولي حيوي رئيسي (Vibrant Petrol)")
p00 = p00.replace("شريط الإعلانات العلوي، الفوتر السفلي", "الهيدر والفوتر وشريط التنقل العلوي بدون أي سواد")
p00 = p00.replace("اللون الداكن الرئيسي: شريط الرأس", "اللون البترولي المضيء للواجهات والكروت")

with open(p00_path, "w", encoding="utf-8") as f:
    f.write(p00)

p00_png = os.path.join(DESIGNS_DIR, "00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png")
cmd_00 = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,1650",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=2500",
    f"--screenshot={p00_png}",
    f"file:///{os.path.abspath(p00_path).replace(chr(92), '/')}"
]
subprocess.run(cmd_00, check=True)
shutil.copy2(p00_png, os.path.join(ROOT_DIR, "00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png"))
print("1. Rendered & Copied Design System Palette")

# ==============================================================================
# 2. UPDATE mobile_01_framed.html WITH REAL CAROUSEL BANNER & CATEGORY CARDS
# ==============================================================================
mob01_path = os.path.join(DESIGNS_DIR, "mobile_01_framed.html")
with open(mob01_path, "r", encoding="utf-8") as f:
    mob = f.read()

# Replace mobile hero card with real banner
old_mob_hero = """    <!-- Hero Card -->
    <div style="background:radial-gradient(circle at 80% 20%, #172a4d 0%, #0b1120 80%); color:#fff; padding:16px; margin:12px; border-radius:12px; border:1px solid #1e293b;">
      <span style="background:rgba(0,153,229,0.2); color:var(--cyan-400); font-size:10px; font-weight:700; padding:2px 8px; border-radius:999px;">● الموزع المعتمد</span>
      <h3 style="font-size:17px; font-weight:900; margin:6px 0 4px;">حلول وتجهيزات الشبكات للشركات</h3>
      <p style="font-size:11px; color:#94a3b8; line-height:1.4; margin-bottom:10px;">نوفر أكبر البراندات العالمية (Cisco, Fortinet, MikroTik) بأجهزة أصلية 100% معتمدة وضمان التوريد.</p>
      <div style="display:flex; gap:8px;">
        <span style="flex:1; background:var(--cyan-500); color:#fff; text-align:center; padding:8px; border-radius:6px; font-size:11.5px; font-weight:800; white-space:nowrap; display:inline-flex; justify-content:center; align-items:center;">تصفح المعدات</span>
      </div>
    </div>"""

new_mob_hero = """    <!-- Hero Carousel Banner (Mobile) -->
    <div style="margin:12px; border-radius:14px; overflow:hidden; border:1.5px solid #bfdbfe; box-shadow:0 6px 18px rgba(14,82,130,0.12); position:relative;">
      <img src="assets/banner_huawei_ekit.jpg" style="width:100%; height:150px; object-fit:cover; display:block;" alt="Huawei eKit Banner">
      <div style="position:absolute; bottom:8px; right:10px; background:rgba(10,54,88,0.85); color:#fff; font-size:11px; font-weight:800; padding:4px 10px; border-radius:6px;">
        أجهزة سويتشات وواي فاي أصلية ✓
      </div>
    </div>

    <!-- Category Quick Banners (Mobile) -->
    <div style="display:flex; gap:8px; padding:0 12px 10px; overflow-x:auto;">
      <div style="width:140px; flex-shrink:0; border-radius:10px; overflow:hidden; border:1px solid #bfdbfe;">
        <img src="assets/cat_banner_switches.jpg" style="width:100%; height:60px; object-fit:cover; display:block;" alt="Switches">
      </div>
      <div style="width:140px; flex-shrink:0; border-radius:10px; overflow:hidden; border:1px solid #bfdbfe;">
        <img src="assets/cat_banner_wifi.jpg" style="width:100%; height:60px; object-fit:cover; display:block;" alt="WiFi">
      </div>
      <div style="width:140px; flex-shrink:0; border-radius:10px; overflow:hidden; border:1px solid #bfdbfe;">
        <img src="assets/cat_banner_storage.jpg" style="width:100%; height:60px; object-fit:cover; display:block;" alt="Storage">
      </div>
    </div>"""

if old_mob_hero in mob:
    mob = mob.replace(old_mob_hero, new_mob_hero)

mob = mob.replace("#070d18", "#0a3658").replace("#0b1120", "#0e4c77").replace("#172a4d", "#125c90")

with open(mob01_path, "w", encoding="utf-8") as f:
    f.write(mob)

mob01_png = os.path.join(DESIGNS_DIR, "Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png")
cmd_mob = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=540,1260",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=2500",
    f"--screenshot={mob01_png}",
    f"file:///{os.path.abspath(mob01_path).replace(chr(92), '/')}"
]
subprocess.run(cmd_mob, check=True)
shutil.copy2(mob01_png, os.path.join(ROOT_DIR, "Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png"))
print("2. Rendered & Copied Mobile Homepage")

# ==============================================================================
# 3. RE-RENDER DESKTOP HOMEPAGE WITH FULL HEIGHT (2850px)
# ==============================================================================
p01_html_path = os.path.join(DESIGNS_DIR, "page_01_homepage.html")
p01_png_path = os.path.join(DESIGNS_DIR, "01_الصفحة_الرئيسية_Desktop_Homepage.png")
cmd_desk = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,2850",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=3000",
    f"--screenshot={p01_png_path}",
    f"file:///{os.path.abspath(p01_html_path).replace(chr(92), '/')}"
]
subprocess.run(cmd_desk, check=True)
shutil.copy2(p01_png_path, os.path.join(ROOT_DIR, "01_الصفحة_الرئيسية_Desktop_Homepage.png"))
print("3. Rendered & Copied Full-Height Desktop Homepage")

print("\nFinalizing complete!")
