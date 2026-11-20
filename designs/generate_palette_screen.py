# -*- coding: utf-8 -*-
"""
generate_palette_screen.py
Creates page_00_design_system_palette.html and renders 
00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png
"""

import os
import subprocess
import shutil

DESIGNS_DIR = r"E:\mess\designs"
ROOT_DIR = r"E:\mess"

HTML_CONTENT = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | دليل الألوان ونظام التصميم (Design System & Color Palette)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --navy-950: #070d18;
      --navy-900: #0b1120;
      --navy-850: #0f172a;
      --navy-800: #172136;
      --navy-700: #1e293b;
      --navy-600: #334155;
      --navy-500: #475569;
      --cyan-500: #0099e5;
      --cyan-400: #38bdf8;
      --cyan-600: #0284c7;
      --emerald-500: #10b981;
      --emerald-600: #059669;
      --amber-500: #f59e0b;
      --rose-500: #ef4444;
      --rose-accent: #f43f5e;
      --slate-100: #f1f5f9;
      --slate-200: #e2e8f0;
      --slate-300: #cbd5e1;
      --slate-400: #94a3b8;
      --slate-500: #64748b;
      --bg-page: #0b1120;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Cairo', sans-serif; }
    body { background: #070d18; color: #fff; direction: rtl; text-align: right; padding: 48px; min-height: 100vh; }
    .mono { font-family: 'JetBrains Mono', monospace; direction: ltr; display: inline-block; }

    .header-banner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 32px;
      border-bottom: 1px solid #1e293b;
      margin-bottom: 40px;
    }
    .brand-title {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .brand-logo-img { height: 46px; }
    .system-title h1 {
      font-size: 26px;
      font-weight: 900;
      color: #fff;
    }
    .system-title p {
      font-size: 13.5px;
      color: var(--cyan-400);
      margin-top: 3px;
    }
    .version-pill {
      background: rgba(0, 153, 229, 0.15);
      border: 1px solid rgba(0, 153, 229, 0.4);
      color: var(--cyan-400);
      padding: 6px 16px;
      border-radius: 999px;
      font-size: 12.5px;
      font-weight: 800;
    }

    .palette-grid-section {
      margin-bottom: 44px;
    }
    .section-headline {
      font-size: 17px;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 18px;
    }
    .section-headline span.tag {
      background: #1e293b;
      color: var(--slate-400);
      font-size: 11.5px;
      padding: 2px 10px;
      border-radius: 6px;
      font-weight: 600;
    }

    /* Cards Grid */
    .swatches-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }

    .swatch-card {
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
      transition: transform 0.2s, border-color 0.2s;
    }
    .swatch-card:hover {
      transform: translateY(-4px);
      border-color: var(--cyan-500);
    }
    .swatch-color-box {
      height: 100px;
      position: relative;
      padding: 12px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
    }
    .swatch-badge-name {
      position: absolute;
      top: 10px;
      right: 10px;
      font-size: 10.5px;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(0,0,0,0.45);
      color: #fff;
      backdrop-filter: blur(4px);
    }
    .swatch-info-box {
      padding: 14px 16px;
      background: #0f172a;
    }
    .swatch-name-ar {
      font-size: 14px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 4px;
    }
    .swatch-role-desc {
      font-size: 11.5px;
      color: var(--slate-400);
      line-height: 1.4;
      margin-bottom: 10px;
      min-height: 32px;
    }
    .swatch-codes-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 8px;
      border-top: 1px solid rgba(255,255,255,0.08);
      font-size: 12px;
    }
    .swatch-hex {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--cyan-400);
    }
    .swatch-variable {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      color: var(--slate-400);
    }

    /* Live Component Preview Strip */
    .components-showcase-box {
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 16px;
      padding: 24px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      margin-top: 36px;
    }
  </style>
</head>
<body>

  <!-- Header Banner -->
  <div class="header-banner">
    <div class="brand-title">
      <img src="assets/logo_white.png" class="brand-logo-img" alt="MESS TECH Logo">
      <div class="system-title">
        <h1>دليل الألوان ونظام التصميم (Design System & Color Palette)</h1>
        <p>الألوان الرسمية لمتجر MESS TECH للتجارة الإلكترونية والتقنية • متطابقة مع الهوية البصرية وتجربة المستخدم B2C</p>
      </div>
    </div>
    <div class="version-pill">
      MESS UI Tokens • Version 2.4
    </div>
  </div>

  <!-- SECTION 1: BRAND CORE PALETTE -->
  <div class="palette-grid-section">
    <div class="section-headline">
      <span>🔷 ألوان العلامة التجارية الأساسية (Brand Core & Primary)</span>
      <span class="tag">الهوية المستوحاة من الشعار والشبكات</span>
    </div>

    <div class="swatches-grid">
      <!-- 1. Electric Cyan -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#0099e5;">
          <span class="swatch-badge-name">Primary 500</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">أزرق سيان كهربائي (Electric Cyan)</div>
          <div class="swatch-role-desc">اللون الرئيسي للعلامة: أزرار البحث، التحديدات النشطة، وأزرار الشراء الرئيسية.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#0099E5</span>
            <span class="swatch-variable mono">--cyan-500</span>
          </div>
        </div>
      </div>

      <!-- 2. Cyan Glow -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#38bdf8;">
          <span class="swatch-badge-name">Cyan Light 400</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">أزرق سماوي مضيء (Sky Glow)</div>
          <div class="swatch-role-desc">النصوص المميزة، الروابط التفاعلية، والتأثيرات الضوئية على الخلفيات الداكنة.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#38BDF8</span>
            <span class="swatch-variable mono">--cyan-400</span>
          </div>
        </div>
      </div>

      <!-- 3. Deep Tech Navy -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#0b1120;">
          <span class="swatch-badge-name">Navy Dark 900</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">كحلي تكنولوجي داكن (Deep Navy)</div>
          <div class="swatch-role-desc">اللون الداكن الرئيسي: شريط الرأس الرئيسي (Navbar)، العناوين، وبطاقات الديسكتوب.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#0B1120</span>
            <span class="swatch-variable mono">--navy-900</span>
          </div>
        </div>
      </div>

      <!-- 4. Ultra Navy Midnight -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#070d18;">
          <span class="swatch-badge-name">Midnight 950</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">كحلي غامق للغاية (Midnight Black)</div>
          <div class="swatch-role-desc">شريط الإعلانات العلوي، الفوتر السفلي، وإطار هاتف الآيفون الموبايل.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#070D18</span>
            <span class="swatch-variable mono">--navy-950</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- SECTION 2: FUNCTIONAL & E-COMMERCE ACCENTS -->
  <div class="palette-grid-section">
    <div class="section-headline">
      <span>⚡ ألوان تجربة التسوق والتفاعل (E-Commerce Functional Accents)</span>
      <span class="tag">الثقة، التحفيز للشراء، والمفضلة</span>
    </div>

    <div class="swatches-grid">
      <!-- 1. Emerald Green (COD & Stock) -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#10b981;">
          <span class="swatch-badge-name">Emerald 500</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">أخضر زمردي (Success & COD)</div>
          <div class="swatch-role-desc">لون الدفع عند الاستلام، توفر المنتج فوراً، وشريط الشحن المنزلي المجاني.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#10B981</span>
            <span class="swatch-variable mono">--emerald-500</span>
          </div>
        </div>
      </div>

      <!-- 2. Amber Gold (Buy Now & Deals) -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#f59e0b;">
          <span class="swatch-badge-name">Amber 500</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">برتقالي ذهبي دافئ (Warm Buy Now)</div>
          <div class="swatch-role-desc">زر الشراء السريع "شراء الآن"، نجوم التقييمات، والعد التنازلي للعروض.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#F59E0B</span>
            <span class="swatch-variable mono">--amber-500</span>
          </div>
        </div>
      </div>

      <!-- 3. Rose Crimson (Wishlist & Save Badge) -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#f43f5e;">
          <span class="swatch-badge-name">Rose 500</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">وردي ياقوتي (Wishlist & Love)</div>
          <div class="swatch-role-desc">أيقونات المفضلة (Wishlist ❤️)، شارات التخفيض وفر X%، ونقاط التنبيه.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#F43F5E</span>
            <span class="swatch-variable mono">--rose-accent</span>
          </div>
        </div>
      </div>

      <!-- 4. Pure Clean White -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#ffffff; border-bottom:1px solid #cbd5e1;">
          <span class="swatch-badge-name" style="background:#0f172a; color:#fff;">Pure White</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">أبيض نقي (Card Background)</div>
          <div class="swatch-role-desc">خلفية كروت المنتجات، البطاقات البيضاء، والقوائم المنسدلة في المتجر.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono" style="color:#fff;">#FFFFFF</span>
            <span class="swatch-variable mono">#ffffff</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- SECTION 3: NEUTRALS & SURFACES -->
  <div class="palette-grid-section">
    <div class="section-headline">
      <span>🌫️ الرماديات والأسطح المحايدة (Neutral UI Surfaces)</span>
      <span class="tag">القراءة المريحة والحدود الأنيقة</span>
    </div>

    <div class="swatches-grid">
      <!-- 1. Page Background -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#f8fafc; border-bottom:1px solid #cbd5e1;">
          <span class="swatch-badge-name" style="background:#0f172a; color:#fff;">Slate 50</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">خلفية الصفحات (Page Light Canvas)</div>
          <div class="swatch-role-desc">الخلفية الهادئة والمريحة لعين المشتري في جميع صفحات المتجر والشيك أوت.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono" style="color:#fff;">#F8FAFC</span>
            <span class="swatch-variable mono">--bg-page</span>
          </div>
        </div>
      </div>

      <!-- 2. Slate 200 Borders -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#e2e8f0; border-bottom:1px solid #cbd5e1;">
          <span class="swatch-badge-name" style="background:#0f172a; color:#fff;">Slate 200</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">رمادي الفواصل والحدود (Borders)</div>
          <div class="swatch-role-desc">خطوط الحدود الفاصلة، إطارات الكروت، وجداول مقارنة ومواصفات الأجهزة.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono" style="color:#fff;">#E2E8F0</span>
            <span class="swatch-variable mono">--slate-200</span>
          </div>
        </div>
      </div>

      <!-- 3. Slate 500 Secondary Text -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#64748b;">
          <span class="swatch-badge-name">Slate 500</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">رمادي النصوص الثانوية (Subtitles)</div>
          <div class="swatch-role-desc">النصوص الإرشادية، تفاصيل أكواد الموديلات (SKU)، ومسميات المواصفات.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#64748B</span>
            <span class="swatch-variable mono">--slate-500</span>
          </div>
        </div>
      </div>

      <!-- 4. Dark Border Navy 700 -->
      <div class="swatch-card">
        <div class="swatch-color-box" style="background:#1e293b;">
          <span class="swatch-badge-name">Navy 700</span>
        </div>
        <div class="swatch-info-box">
          <div class="swatch-name-ar">كحلي الفواصل الداكنة (Dark Borders)</div>
          <div class="swatch-role-desc">فواصل الهيدر، خطوط التقسيم في الثيم الداكن، وتحديد حقول الإدخال النشطة.</div>
          <div class="swatch-codes-row">
            <span class="swatch-hex mono">#1E293B</span>
            <span class="swatch-variable mono">--navy-700</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Live UI Tokens Preview Strip -->
  <div class="components-showcase-box">
    <div>
      <div style="font-size:15px; font-weight:800; color:#fff; margin-bottom:4px;">تطبيق الألوان الحي في المتجر (Live Components Preview)</div>
      <div style="font-size:12px; color:var(--slate-400);">تناسق الأزرار والشارات وفق نظام التصميم المعتمد</div>
    </div>

    <div style="display:flex; align-items:center; gap:14px;">
      <!-- Buy Now Button -->
      <button style="background:linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color:#fff; border:none; padding:10px 20px; border-radius:8px; font-size:13px; font-weight:800; display:flex; align-items:center; gap:6px;">
        <span>⚡</span> شراء الآن
      </button>

      <!-- Add to Cart Button -->
      <button style="background:#0099e5; color:#fff; border:none; padding:10px 20px; border-radius:8px; font-size:13px; font-weight:800; display:flex; align-items:center; gap:6px;">
        <span>🛒</span> أضف للسلة
      </button>

      <!-- Wishlist Heart -->
      <button style="width:40px; height:40px; background:#fff; border:1px solid #fecdd3; border-radius:8px; color:#f43f5e; font-size:16px; cursor:pointer;">
        ❤️
      </button>

      <!-- COD Badge -->
      <span style="background:#ecfdf5; border:1.5px solid #10b981; color:#065f46; padding:6px 14px; border-radius:999px; font-size:12px; font-weight:800; display:flex; align-items:center; gap:6px;">
        <span style="width:8px; height:8px; background:#10b981; border-radius:50%;"></span>
        الدفع نقداً عند الاستلام COD
      </span>

      <!-- 14-Day Return -->
      <span style="background:rgba(56, 189, 248, 0.12); border:1px solid rgba(56, 189, 248, 0.35); color:#38bdf8; padding:6px 14px; border-radius:999px; font-size:12px; font-weight:700;">
        ✓ إرجاع مجاني 14 يوماً
      </span>
    </div>
  </div>

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "page_00_design_system_palette.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png")
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,1100",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=3000",
    f"--screenshot={png_path}",
    f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
]
subprocess.run(cmd, check=True)
size_kb = os.path.getsize(png_path) / 1024
print(f"Rendered: {png_path} ({size_kb:.1f} KB)")

# Copy to root
shutil.copy2(png_path, os.path.join(ROOT_DIR, "00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png"))
print("Copied to root!")
