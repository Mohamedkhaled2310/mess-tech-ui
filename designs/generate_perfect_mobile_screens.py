# -*- coding: utf-8 -*-
import os
import subprocess
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS

DESIGNS_DIR = r"E:\mess\designs"

FRAME_WRAPPER_CSS = """
:root {
  --navy-950: #070d18;
  --navy-900: #0b1120;
  --navy-850: #0f172a;
  --navy-800: #172136;
  --navy-700: #1e293b;
  --navy-600: #334155;
  --cyan-500: #0099e5;
  --cyan-400: #38bdf8;
  --cyan-600: #0284c7;
  --emerald-500: #10b981;
  --emerald-600: #059669;
  --amber-500: #f59e0b;
  --rose-500: #ef4444;
  --slate-100: #f1f5f9;
  --slate-200: #e2e8f0;
  --slate-400: #94a3b8;
  --slate-500: #64748b;
  --bg-page: #f8fafc;
}

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Cairo', sans-serif; }
body {
  background: radial-gradient(circle at 50% 20%, #172a4d 0%, #070d18 80%);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 20px;
  min-height: 100vh;
}
.mono { font-family: 'JetBrains Mono', monospace; direction: ltr; display: inline-block; }

.phone-device-container {
  width: 420px;
  background: #000;
  border: 10px solid #1e293b;
  border-radius: 46px;
  box-shadow: 0 25px 60px rgba(0,0,0,0.65), 0 0 0 2px rgba(255,255,255,0.1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
  direction: rtl;
  text-align: right;
  background-color: var(--bg-page);
}

.phone-status-bar {
  background: var(--navy-900);
  padding: 10px 20px 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  color: #fff;
  position: relative;
  z-index: 50;
  direction: ltr;
}
.phone-dynamic-island {
  position: absolute;
  top: 7px;
  left: 50%;
  transform: translateX(-50%);
  width: 95px;
  height: 22px;
  background: #000;
  border-radius: 20px;
}

.device-header-title {
  text-align: center;
  color: #fff;
  margin-bottom: 20px;
  max-width: 500px;
}
.device-header-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0, 153, 229, 0.15);
  border: 1px solid rgba(0, 153, 229, 0.4);
  color: var(--cyan-400);
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 8px;
}
.device-header-title h2 {
  font-size: 22px;
  font-weight: 900;
  color: #fff;
}
.device-header-title p {
  font-size: 12.5px;
  color: #94a3b8;
  margin-top: 4px;
}
"""

def render_device(html_path, png_path, height=2200):
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size=540,{height}",
        "--force-device-scale-factor=1.5",
        "--virtual-time-budget=3000",
        f"--screenshot={png_path}",
        f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
    ]
    subprocess.run(cmd, check=True)
    size_kb = os.path.getsize(png_path) / 1024
    print(f"Rendered: {os.path.basename(png_path)} ({size_kb:.1f} KB)")

def make_mob_01():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | شاشة الموبايل - الصفحة الرئيسية</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">Mobile UI/UX Experience</div>
    <h2>01. الصفحة الرئيسية <span dir="ltr" class="mono" style="color:var(--cyan-400);">(Mobile Homepage)</span></h2>
    <p>واجهة متجاوبة بالكامل لمهندسي الشبكات والمشترين مع بحث سريع وشريط ملاحة سفلي ثابت</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span style="font-weight:700;">9:41</span>
      <div class="phone-dynamic-island"></div>
      <span style="font-size:10px;">5G 100%</span>
    </div>

    <!-- COD Announcement -->
    <div style="background:var(--navy-950); color:#34d399; font-size:11px; font-weight:700; padding:6px 14px; display:flex; justify-content:space-between;">
      <span>✓ الدفع كاش عند الاستلام (COD) فقط</span>
      <span style="color:#fff; font-size:10px;">استلام مجاني من الفرع</span>
    </div>

    <!-- Header -->
    <div style="background:var(--navy-900); padding:10px 14px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--navy-700);">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="color:#fff; font-size:18px;">☰</span>
        <img src="assets/logo_white.png" style="height:28px;" alt="Logo">
      </div>
      <div style="display:flex; gap:6px;">
        <span style="background:var(--navy-800); border:1px solid var(--navy-700); color:#fff; width:30px; height:30px; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:800;">3</span>
        <span style="background:var(--navy-800); border:1px solid var(--navy-700); color:#34d399; width:30px; height:30px; border-radius:6px; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:800;">2</span>
        <a href="https://wa.me/201000000000" style="background:#22c55e; color:#fff; width:30px; height:30px; border-radius:6px; display:flex; align-items:center; justify-content:center; text-decoration:none; font-size:13px;">💬</a>
      </div>
    </div>

    <!-- Mobile Search -->
    <div style="background:var(--navy-900); padding:0 14px 12px;">
      <input type="text" style="width:100%; background:var(--navy-800); border:1px solid #2d3b55; border-radius:8px; padding:8px 12px; color:#fff; font-size:12px; outline:none;" placeholder="ابحث برقم الموديل (مثل WS-C2960X، FG-60F)...">
    </div>

    <!-- Category Scroller -->
    <div style="display:flex; gap:6px; padding:10px 12px; overflow-x:auto; background:#fff; border-bottom:1px solid var(--slate-200);">
      <span style="background:var(--cyan-500); color:#fff; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; white-space:nowrap;">الكل</span>
      <span style="background:#f1f5f9; color:#334155; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; white-space:nowrap;">سويتشات</span>
      <span style="background:#f1f5f9; color:#334155; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; white-space:nowrap;">راوترات</span>
      <span style="background:#f1f5f9; color:#334155; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; white-space:nowrap;">فايروول</span>
      <span style="background:#f1f5f9; color:#334155; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:700; white-space:nowrap;">واي فاي</span>
    </div>

    <!-- Hero Card -->
    <div style="background:radial-gradient(circle at 80% 20%, #172a4d 0%, #0b1120 80%); color:#fff; padding:16px; margin:12px; border-radius:12px; border:1px solid #1e293b;">
      <span style="background:rgba(0,153,229,0.2); color:var(--cyan-400); font-size:10px; font-weight:700; padding:2px 8px; border-radius:999px;">● الموزع المعتمد</span>
      <h3 style="font-size:17px; font-weight:900; margin:6px 0 4px;">حلول وتجهيزات الشبكات للشركات</h3>
      <p style="font-size:11px; color:#94a3b8; line-height:1.4; margin-bottom:10px;">نوفر أكبر البراندات (Cisco, Fortinet, MikroTik) مع الدفع كاش عند الاستلام COD وضمان سنتين.</p>
      <div style="display:flex; gap:8px;">
        <span style="flex:1; background:var(--cyan-500); color:#fff; text-align:center; padding:7px; border-radius:6px; font-size:11.5px; font-weight:800;">تصفح المعدات</span>
        <span style="background:rgba(255,255,255,0.1); color:#fff; padding:7px 12px; border-radius:6px; font-size:11px; font-weight:700;">طلب عرض سعر RFQ</span>
      </div>
    </div>

    <!-- Weekly Deal with Timer -->
    <div style="padding:0 12px; margin-bottom:12px;">
      <div style="background:#1e293b; color:#fff; padding:8px 12px; border-radius:10px 10px 0 0; display:flex; justify-content:space-between; align-items:center;">
        <b style="font-size:12px;">⚡ عروض الأسبوع بمؤقت</b>
        <span class="mono" style="font-size:11px; color:#f59e0b; font-weight:800;">02d : 14h : 28m : 45s</span>
      </div>
      <div style="background:#fff; border:1px solid var(--slate-200); border-top:none; border-radius:0 0 10px 10px; padding:12px;">
        <div style="height:110px; background:#f8fafc; border-radius:8px; display:flex; align-items:center; justify-content:center; margin-bottom:8px;">
          {SVG_CISCO_SWITCH}
        </div>
        <div class="mono" style="font-size:11px; font-weight:700; color:var(--cyan-600);">WS-C2960X-24TD-L</div>
        <div style="font-size:13px; font-weight:800; color:var(--navy-900); margin:2px 0 6px;">سويتش سيسكو كاتاليست 24 بورت PoE+ مع 2x 10G SFP+</div>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--slate-100); padding-top:8px;">
          <div>
            <div style="font-size:17px; font-weight:900; color:var(--navy-900);">19,850 ج.م</div>
            <div style="font-size:11px; color:#94a3b8; text-decoration:line-through;">23,200 ج.م</div>
          </div>
          <button style="background:var(--cyan-500); color:#fff; border:none; padding:7px 14px; border-radius:6px; font-size:11.5px; font-weight:800; cursor:pointer;">طلب بالدفع COD</button>
        </div>
      </div>
    </div>

    <!-- Brands -->
    <div style="background:#fff; padding:10px; margin:8px 0; border-top:1px solid var(--slate-200); border-bottom:1px solid var(--slate-200); display:flex; justify-content:space-around; font-size:12px; font-weight:900;">
      <span style="color:#0284c7;">CISCO</span>
      <span style="color:#ef4444;">FORTINET</span>
      <span style="color:#0f172a;">MIKROTIK</span>
      <span style="color:#0099e5;">UBIQUITI</span>
    </div>

    <!-- Product list item -->
    <div style="padding:0 12px; display:flex; flex-direction:column; gap:8px; margin-bottom:12px;">
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:10px; display:flex; gap:10px; align-items:center;">
        <div style="width:70px; height:70px; background:#f8fafc; border-radius:6px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
          {SVG_MIKROTIK}
        </div>
        <div style="flex:1;">
          <div class="mono" style="font-size:10.5px; font-weight:700; color:#475569;">CRS328-24P-4S+RM</div>
          <div style="font-size:12px; font-weight:800; line-height:1.3; margin:2px 0;">سويتش مايكروتك 24 بورت PoE ذكي 500W مع 4x 10G</div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
            <b style="font-size:14px; color:var(--navy-900);">22,400 ج.م</b>
            <span style="background:#f0f9ff; color:var(--cyan-600); border:1px solid #bae6fd; font-size:10.5px; font-weight:800; padding:3px 8px; border-radius:4px;">أضف للسلة</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Nav -->
    <div style="background:#0b1120; border-top:1px solid #1e293b; padding:8px 10px 12px; display:flex; justify-content:space-around; align-items:center;">
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:var(--cyan-400); font-size:10px; font-weight:700;"><span>🏠</span><span>الرئيسية</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>📁</span><span>الأقسام</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>⚖️</span><span>المقارنة</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🛒</span><span>السلة</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>👤</span><span>حسابي</span></div>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_01_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png")
    render_device(html_file, png_file, height=1300)

def make_mob_02():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | شاشة الموبايل - تفاصيل المنتج</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">Mobile UI/UX Experience</div>
    <h2>02. صفحة المنتج والمواصفات <span dir="ltr" class="mono" style="color:var(--cyan-400);">(Mobile Product Details)</span></h2>
    <p>عرض دقيق للموديل ومنافذ البوردة مع تحميل الداتاشيت وزر عائم للشراء المباشر عبر COD وواتساب</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span style="font-weight:700;">9:41</span>
      <div class="phone-dynamic-island"></div>
      <span style="font-size:10px;">5G 100%</span>
    </div>

    <div style="background:var(--navy-900); color:#fff; padding:10px 14px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--navy-700);">
      <span style="font-size:12px; color:#cbd5e1;">← رجوع</span>
      <span style="font-size:13px; font-weight:800;">سيسكو كاتاليست 2960X</span>
      <span style="font-size:12px; color:var(--cyan-400);">مشاركة ↗</span>
    </div>

    <div style="background:#fff; border:1px solid var(--slate-200); border-radius:12px; padding:12px; margin:12px; text-align:center;">
      <div style="height:120px; display:flex; align-items:center; justify-content:center; margin-bottom:8px;">
        {SVG_CISCO_SWITCH}
      </div>
      <div style="display:flex; justify-content:center; gap:6px;">
        <span style="border:1.5px solid var(--cyan-500); background:#f0f9ff; color:var(--cyan-600); border-radius:6px; padding:3px 8px; font-size:10px; font-weight:700;">واجهة البورتات</span>
        <span style="border:1.5px solid var(--slate-200); background:#f8fafc; color:#64748b; border-radius:6px; padding:3px 8px; font-size:10px; font-weight:700;">منافذ 10G SFP+</span>
        <span style="border:1.5px solid var(--slate-200); background:#f8fafc; color:#64748b; border-radius:6px; padding:3px 8px; font-size:10px; font-weight:700;">الباور الخلفي</span>
      </div>
    </div>

    <div style="padding:0 14px 14px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
        <span style="background:#e0f2fe; color:var(--cyan-600); font-size:10.5px; font-weight:800; padding:2px 8px; border-radius:4px;">CISCO SYSTEMS</span>
        <span class="mono" style="font-size:11.5px; font-weight:700; background:#f1f5f9; padding:2px 8px; border-radius:4px;">WS-C2960X-24TD-L</span>
      </div>

      <h3 style="font-size:15px; font-weight:900; line-height:1.4; color:var(--navy-900); margin-bottom:8px;">
        سويتش سيسكو كاتاليست 24 بورت جيجابت PoE+ مع منفذين 10G SFP+
      </h3>

      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:10px 12px; margin-bottom:10px;">
        <div style="display:flex; justify-content:space-between; align-items:baseline;">
          <div>
            <span style="font-size:20px; font-weight:900; color:var(--navy-900);">19,850 ج.م</span>
            <span style="font-size:11.5px; color:#94a3b8; text-decoration:line-through; margin-right:4px;">23,200 ج.م</span>
          </div>
          <span style="background:#fef2f2; color:#ef4444; font-size:10.5px; font-weight:800; padding:2px 6px; border-radius:4px;">وفر 14%</span>
        </div>
        <div style="font-size:11px; color:#059669; font-weight:700; margin-top:2px;">● متوفر بالمخزون (متبقي 6 قطع في فرع القاهرة)</div>
      </div>

      <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:8px 10px; margin-bottom:10px; font-size:11px; color:#14532d;">
        <b>الدفع نقداً عند الاستلام (COD) فقط:</b>
        <div style="font-size:10px; margin-top:1px;">عاين جهازك وافحص الفاتورة الضريبية مع المندوب قبل دفع أي مبالغ.</div>
      </div>

      <div style="background:#0f172a; color:#fff; padding:10px 12px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <div>
          <div style="font-size:12px; font-weight:800;">الداتاشيت الرسمية (Datasheet PDF)</div>
          <div style="font-size:10px; color:#94a3b8;">ملف المواصفات المعتمد من سيسكو • 3.4 MB</div>
        </div>
        <span style="background:var(--cyan-500); padding:4px 10px; border-radius:6px; font-size:10.5px; font-weight:800;">تحميل PDF</span>
      </div>

      <table style="width:100%; border-collapse:collapse; background:#fff; border:1px solid var(--slate-200); border-radius:8px; overflow:hidden; font-size:11.5px; margin-bottom:10px;">
        <tr><td style="background:#f8fafc; padding:6px 10px; font-weight:700; width:40%;">البورتات</td><td style="padding:6px 10px;"><b>24x 1GbE RJ45 Ports</b></td></tr>
        <tr><td style="background:#f8fafc; padding:6px 10px; font-weight:700;">طاقة PoE</td><td style="padding:6px 10px;"><b>370W PoE+ (802.3at)</b></td></tr>
        <tr><td style="background:#f8fafc; padding:6px 10px; font-weight:700;">منافذ الأبلينك</td><td style="padding:6px 10px;"><b>2x 10G SFP+ Uplinks</b></td></tr>
        <tr><td style="background:#f8fafc; padding:6px 10px; font-weight:700;">سعة التبديل</td><td style="padding:6px 10px;"><b>216 Gbps Capacity</b></td></tr>
        <tr><td style="background:#f8fafc; padding:6px 10px; font-weight:700;">الضمان</td><td style="padding:6px 10px;"><b style="color:#059669;">سنتين استبدال معتمد</b></td></tr>
      </table>
    </div>

    <!-- Fixed Bottom Sticky Bar -->
    <div style="background:#fff; border-top:1px solid var(--slate-200); padding:10px 14px 14px; display:flex; align-items:center; gap:8px;">
      <button style="flex:1; background:var(--cyan-500); color:#fff; border:none; padding:11px; border-radius:8px; font-size:13px; font-weight:800; cursor:pointer;">
        أضف للسلة (الدفع عند الاستلام)
      </button>
      <a href="https://wa.me/201000000000?text=استفسار%20عن%20سيسكو%202960X" style="width:42px; height:42px; background:#22c55e; color:#fff; border-radius:8px; display:flex; align-items:center; justify-content:center; text-decoration:none; font-size:18px;" title="واتساب المبيعات">
        💬
      </a>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_02_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_02_صفحة_المنتج_والمواصفات_Mobile_Product_Details.png")
    render_device(html_file, png_file, height=1250)

def make_mob_03():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | شاشة الموبايل - الفلاتر وتصفح الأقسام</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">Mobile UI/UX Experience</div>
    <h2>03. الفلاتر والبحث التقني <span dir="ltr" class="mono" style="color:var(--cyan-400);">(Mobile Catalog & Filters)</span></h2>
    <p>تجربة استعراض وفلترة السويتشات مع درج فلاتر سفلي متجاوب للمواصفات الفنية</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span style="font-weight:700;">9:41</span>
      <div class="phone-dynamic-island"></div>
      <span style="font-size:10px;">5G 100%</span>
    </div>

    <div style="background:var(--navy-900); padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
      <span style="color:#fff; font-size:13px; font-weight:800;">سويتشات الشبكات (18 موديل)</span>
      <span style="background:rgba(16,185,129,0.2); color:#34d399; font-size:10px; font-weight:700; padding:2px 8px; border-radius:4px;">دفع COD</span>
    </div>

    <div style="background:var(--navy-900); padding:0 14px 10px; border-bottom:1px solid var(--navy-700);">
      <input type="text" style="width:100%; background:var(--navy-800); border:1px solid #2d3b55; border-radius:8px; padding:7px 10px; color:#fff; font-size:11.5px; outline:none;" placeholder="ابحث داخل السويتشات...">
    </div>

    <div style="background:#f8fafc; border-bottom:1px solid var(--slate-200); padding:8px 12px; display:flex; gap:8px;">
      <button style="flex:1; background:var(--navy-900); color:#fff; border:none; padding:8px; border-radius:6px; font-size:11.5px; font-weight:800; cursor:pointer;">
        ⚙️ الفلاتر التقنية (4 نشطة)
      </button>
      <button style="background:#fff; border:1px solid var(--slate-300); padding:8px 10px; border-radius:6px; font-size:11.5px; font-weight:700;">
        ترتيب: الأكثر طلباً ▾
      </button>
    </div>

    <div style="display:flex; gap:4px; padding:6px 12px; background:#fff; overflow-x:auto; border-bottom:1px solid var(--slate-100);">
      <span style="background:#e0f2fe; color:var(--cyan-600); padding:2px 8px; border-radius:999px; font-size:10px; font-weight:700; white-space:nowrap;">Cisco ✕</span>
      <span style="background:#e0f2fe; color:var(--cyan-600); padding:2px 8px; border-radius:999px; font-size:10px; font-weight:700; white-space:nowrap;">24 Port GbE ✕</span>
      <span style="background:#e0f2fe; color:var(--cyan-600); padding:2px 8px; border-radius:999px; font-size:10px; font-weight:700; white-space:nowrap;">PoE+ 370W ✕</span>
      <span style="background:#e0f2fe; color:var(--cyan-600); padding:2px 8px; border-radius:999px; font-size:10px; font-weight:700; white-space:nowrap;">10G SFP+ ✕</span>
    </div>

    <div style="padding:10px; display:grid; grid-template-columns:1fr 1fr; gap:8px;">
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:8px; padding:8px;">
        <div style="height:70px; background:#f8fafc; border-radius:6px; display:flex; align-items:center; justify-content:center; margin-bottom:6px;">
          {SVG_CISCO_SWITCH}
        </div>
        <div class="mono" style="font-size:10px; font-weight:700; color:var(--cyan-600);">WS-C2960X-24TD-L</div>
        <div style="font-size:11px; font-weight:800; line-height:1.3; height:28px; overflow:hidden; margin:2px 0;">سيسكو 24 بورت PoE+ 370W</div>
        <div style="font-size:13px; font-weight:900; color:var(--navy-900);">19,850 ج.م</div>
        <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:5px; border-radius:4px; font-size:10.5px; font-weight:800; margin-top:4px;">طلب COD</button>
      </div>

      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:8px; padding:8px;">
        <div style="height:70px; background:#f8fafc; border-radius:6px; display:flex; align-items:center; justify-content:center; margin-bottom:6px;">
          {SVG_MIKROTIK}
        </div>
        <div class="mono" style="font-size:10px; font-weight:700; color:#0f172a;">CRS328-24P-4S+RM</div>
        <div style="font-size:11px; font-weight:800; line-height:1.3; height:28px; overflow:hidden; margin:2px 0;">مايكروتك 24 بورت ذكي 500W</div>
        <div style="font-size:13px; font-weight:900; color:var(--navy-900);">22,400 ج.م</div>
        <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:5px; border-radius:4px; font-size:10.5px; font-weight:800; margin-top:4px;">طلب COD</button>
      </div>
    </div>

    <!-- Filter Drawer -->
    <div style="background:rgba(11,17,32,0.85); padding:16px 12px 0; border-radius:18px 18px 0 0; border-top:2px solid var(--cyan-500); margin-top:10px;">
      <div style="background:#fff; border-radius:14px 14px 0 0; padding:14px 14px 20px;">
        <div style="width:36px; height:4px; background:#cbd5e1; border-radius:999px; margin:0 auto 10px;"></div>
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--slate-100); padding-bottom:6px; margin-bottom:8px;">
          <b style="font-size:13px; color:var(--navy-900);">فلاتر المواصفات الفنية</b>
          <span style="font-size:11px; color:var(--rose-500); font-weight:700;">إعادة ضبط</span>
        </div>

        <div style="font-size:11.5px; font-weight:800; color:var(--navy-900); margin:6px 0 2px;">الماركة:</div>
        <div style="display:flex; justify-content:space-between; font-size:12px; padding:3px 0;"><label><input type="checkbox" checked> <b>Cisco Systems</b></label> <span>(14)</span></div>
        <div style="display:flex; justify-content:space-between; font-size:12px; padding:3px 0;"><label><input type="checkbox"> MikroTik</label> <span>(12)</span></div>

        <div style="font-size:11.5px; font-weight:800; color:var(--navy-900); margin:8px 0 2px;">عدد منافذ الشبكة:</div>
        <div style="display:flex; justify-content:space-between; font-size:12px; padding:3px 0;"><label><input type="checkbox" checked> <b>24 Port Gigabit</b></label> <span>(18)</span></div>
        <div style="display:flex; justify-content:space-between; font-size:12px; padding:3px 0;"><label><input type="checkbox"> 48 Port Gigabit</label> <span>(12)</span></div>

        <div style="font-size:11.5px; font-weight:800; color:var(--navy-900); margin:8px 0 2px;">طاقة الـ PoE:</div>
        <div style="display:flex; justify-content:space-between; font-size:12px; padding:3px 0;"><label><input type="checkbox" checked> <b>PoE+ (370W)</b></label> <span>(15)</span></div>

        <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:10px; border-radius:8px; font-size:12.5px; font-weight:800; margin-top:12px; cursor:pointer;">
          تطبيق الفلاتر (عرض 18 منتج) ✓
        </button>
      </div>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_03_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_03_الفلاتر_وتصفح_المنتجات_Mobile_Catalog_Filters.png")
    render_device(html_file, png_file, height=1250)

def make_mob_04():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | شاشة الموبايل - إتمام الطلب COD</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">Mobile UI/UX Experience</div>
    <h2>04. السلة وإتمام الطلب في خطوة واحدة <span dir="ltr" class="mono" style="color:var(--cyan-400);">(Mobile Checkout COD)</span></h2>
    <p>شراء سريع كضيف بدون تعقيد، مع حساب آلي للشحن حسب المحافظة وتأكيد الدفع كاش عند الاستلام</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span style="font-weight:700;">9:41</span>
      <div class="phone-dynamic-island"></div>
      <span style="font-size:10px;">5G 100%</span>
    </div>

    <div style="background:var(--navy-900); color:#fff; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
      <span style="font-size:12px; color:#cbd5e1;">← السلة</span>
      <span style="font-size:13px; font-weight:800;">إتمام الطلب في خطوة واحدة</span>
      <span style="font-size:10px; color:#34d399;">🔒 آمن</span>
    </div>

    <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:10px 12px; margin:10px; font-size:11.5px; color:#14532d;">
      <b>الدفع نقداً عند الاستلام (COD) فقط</b>
      <div style="font-size:10px; margin-top:2px;">لا حاجة لكروت بنكية. استلم شحنتك وافحص الأجهزة أولاً ثم ادفع كاش للمندوب.</div>
    </div>

    <!-- Step 1: Customer Contact -->
    <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:12px; margin:0 10px 10px;">
      <div style="display:flex; align-items:center; gap:6px; font-size:12.5px; font-weight:800; margin-bottom:8px; border-bottom:1px solid var(--slate-100); padding-bottom:6px;">
        <span style="background:var(--navy-900); color:var(--cyan-400); width:18px; height:18px; border-radius:4px; display:inline-flex; align-items:center; justify-content:center; font-size:10px;">1</span>
        <span>بيانات العميل (شراء كضيف)</span>
      </div>
      <input type="text" style="width:100%; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:6px; padding:7px 10px; font-size:12px; margin-bottom:6px;" value="م. أحمد فتحي (شركة دلتا)">
      <input type="text" class="mono" style="width:100%; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:6px; padding:7px 10px; font-size:12px; margin-bottom:6px;" value="0100 234 5678">
      <input type="email" class="mono" style="width:100%; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:6px; padding:7px 10px; font-size:12px;" value="ahmed.fathi@deltatech.com">
    </div>

    <!-- Step 2: Shipping & Address -->
    <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:12px; margin:0 10px 10px;">
      <div style="display:flex; align-items:center; gap:6px; font-size:12.5px; font-weight:800; margin-bottom:8px; border-bottom:1px solid var(--slate-100); padding-bottom:6px;">
        <span style="background:var(--navy-900); color:var(--cyan-400); width:18px; height:18px; border-radius:4px; display:inline-flex; align-items:center; justify-content:center; font-size:10px;">2</span>
        <span>عنوان التوصيل وحساب الشحن</span>
      </div>
      <div style="display:flex; gap:6px; margin-bottom:8px;">
        <div style="flex:1; border:1.5px solid var(--cyan-500); background:#f0f9ff; color:var(--cyan-600); border-radius:6px; padding:6px; text-align:center; font-size:11px; font-weight:700;">
          توصيل لمقر الشركة
        </div>
        <div style="flex:1; border:1.5px solid var(--slate-200); background:#f8fafc; color:#64748b; border-radius:6px; padding:6px; text-align:center; font-size:11px; font-weight:700;">
          استلام من الفرع (مجاناً)
        </div>
      </div>
      <select style="width:100%; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:6px; padding:7px 10px; font-size:12px; font-weight:700; margin-bottom:6px;">
        <option selected>القاهرة (شحن مجاني فوق 20,000 ج.م)</option>
        <option>الجيزة (شحن مجاني)</option>
        <option>الإسكندرية والوجه البحري</option>
      </select>
      <input type="text" style="width:100%; background:#f8fafc; border:1.5px solid #cbd5e1; border-radius:6px; padding:7px 10px; font-size:12px;" value="المعادي الجديدة، شارع النصر، عمارة 14">
    </div>

    <!-- Step 3: Order Totals -->
    <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:12px; margin:0 10px 12px; font-size:11.5px; color:#475569;">
      <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
        <span>سويتش سيسكو 2960X (x2):</span>
        <b>39,700 ج.م</b>
      </div>
      <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
        <span>كابينة راك 9U جداري (x1):</span>
        <b>3,500 ج.م</b>
      </div>
      <div style="display:flex; justify-content:space-between; margin-bottom:4px; color:#059669;">
        <span>الشحن (القاهرة):</span>
        <b>مجاني (0 ج.م)</b>
      </div>
      <div style="display:flex; justify-content:space-between; margin-bottom:6px; color:#ef4444;">
        <span>خصم الكوبون (MESS2026):</span>
        <b>- 1,000 ج.م</b>
      </div>
      <div style="display:flex; justify-content:space-between; font-size:15px; font-weight:900; color:var(--navy-900); border-top:1px solid var(--slate-100); padding-top:6px;">
        <span>المستحق نقدياً عند الاستلام:</span>
        <span style="color:var(--cyan-600);">42,200 ج.م</span>
      </div>
    </div>

    <!-- Sticky Confirm Order Button -->
    <div style="background:#fff; border-top:1px solid var(--slate-200); padding:10px 12px 14px;">
      <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:12px; border-radius:8px; font-size:13.5px; font-weight:900; cursor:pointer;">
        تأكيد الطلب الآن - الدفع عند الاستلام (COD) ✓
      </button>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_04_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_04_السلة_واتمام_الطلب_COD_Mobile_Checkout.png")
    render_device(html_file, png_file, height=1250)

def make_mob_05():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | شاشة الموبايل - مقارنة الموديلات</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">Mobile UI/UX Experience</div>
    <h2>05. مقارنة المواصفات للموبايل <span dir="ltr" class="mono" style="color:var(--cyan-400);">(Mobile Product Comparison)</span></h2>
    <p>مقارنة موديلات السويتشات بالسحب الأفقي مع إبراز الفروق في البورتات وطاقة PoE وسرعات الأبلينك</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span style="font-weight:700;">9:41</span>
      <div class="phone-dynamic-island"></div>
      <span style="font-size:10px;">5G 100%</span>
    </div>

    <div style="background:var(--navy-900); color:#fff; padding:10px 14px; display:flex; justify-content:space-between; align-items:center;">
      <span style="font-size:13px; font-weight:800;">مقارنة المواصفات (اسحب أفقياً)</span>
      <span style="font-size:11px; color:var(--cyan-400);">3 موديلات</span>
    </div>

    <div style="display:flex; gap:10px; padding:12px; overflow-x:auto;">
      <div style="width:240px; background:#fff; border:2px solid var(--cyan-500); border-radius:10px; padding:10px; flex-shrink:0;">
        <div style="font-size:10px; font-weight:800; color:var(--cyan-600);">CISCO SYSTEMS</div>
        <div class="mono" style="font-size:11.5px; font-weight:800; color:var(--navy-900);">WS-C2960X-24TD-L</div>
        <div style="height:70px; background:#f8fafc; border-radius:6px; display:flex; align-items:center; justify-content:center; margin:6px 0;">
          {SVG_CISCO_SWITCH}
        </div>
        <div style="font-size:16px; font-weight:900; color:var(--navy-900); margin-bottom:6px;">19,850 ج.م</div>
        <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:6px; border-radius:6px; font-size:11px; font-weight:800; margin-bottom:8px;">طلب بالدفع COD</button>

        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0; border-bottom:1px solid var(--slate-100);"><span>البورتات:</span><b>24x 1GbE</b></div>
        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0; border-bottom:1px solid var(--slate-100); background:#f0f9ff;"><span>الأبلينك:</span><b style="color:var(--cyan-600);">2x 10G SFP+</b></div>
        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0; border-bottom:1px solid var(--slate-100);"><span>طاقة PoE:</span><b>370W PoE+</b></div>
        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0; border-bottom:1px solid var(--slate-100); background:#f0f9ff;"><span>سعة التبديل:</span><b>216 Gbps</b></div>
        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0;"><span>الضمان:</span><b style="color:#059669;">سنتين معتمد</b></div>
      </div>

      <div style="width:240px; background:#fff; border:1.5px solid var(--slate-200); border-radius:10px; padding:10px; flex-shrink:0;">
        <div style="font-size:10px; font-weight:800; color:#0f172a;">MIKROTIK</div>
        <div class="mono" style="font-size:11.5px; font-weight:800; color:var(--navy-900);">CRS328-24P-4S+RM</div>
        <div style="height:70px; background:#f8fafc; border-radius:6px; display:flex; align-items:center; justify-content:center; margin:6px 0;">
          {SVG_MIKROTIK}
        </div>
        <div style="font-size:16px; font-weight:900; color:var(--navy-900); margin-bottom:6px;">22,400 ج.م</div>
        <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:6px; border-radius:6px; font-size:11px; font-weight:800; margin-bottom:8px;">طلب بالدفع COD</button>

        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0; border-bottom:1px solid var(--slate-100);"><span>البورتات:</span><b>24x 1GbE</b></div>
        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0; border-bottom:1px solid var(--slate-100); background:#f0f9ff;"><span>الأبلينك:</span><b style="color:var(--cyan-600);">4x 10G SFP+</b></div>
        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0; border-bottom:1px solid var(--slate-100);"><span>طاقة PoE:</span><b style="color:#059669;">500W Dual</b></div>
        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0; border-bottom:1px solid var(--slate-100); background:#f0f9ff;"><span>سعة التبديل:</span><b>128 Gbps</b></div>
        <div style="display:flex; justify-content:space-between; font-size:11px; padding:4px 0;"><span>الضمان:</span><b>سنة معتمدة</b></div>
      </div>
    </div>

    <div style="background:#0b1120; border-top:1px solid #1e293b; padding:8px 10px 12px; display:flex; justify-content:space-around; align-items:center;">
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🏠</span><span>الرئيسية</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>📁</span><span>الأقسام</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:var(--cyan-400); font-size:10px; font-weight:700;"><span>⚖️</span><span>المقارنة</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🛒</span><span>السلة</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>👤</span><span>حسابي</span></div>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_05_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_05_مقارنة_الموديلات_Mobile_Product_Comparison.png")
    render_device(html_file, png_file, height=1050)

if __name__ == "__main__":
    print("Re-rendering framed mobile screens with clean titles...")
    make_mob_01()
    make_mob_02()
    make_mob_03()
    make_mob_04()
    make_mob_05()
    print("All framed mobile screens updated!")
