# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS
from prepare_svgs import SVG_CISCO_SWITCH, SVG_FORTINET

DESIGNS_DIR = r"E:\mess\designs"

HTML_CONTENT = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | تصميم تجربة الموبايل (Mobile First Responsive Showcase)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    body {{
      background: radial-gradient(circle at 50% 20%, #172a4d 0%, #0b1120 70%);
      color: #fff;
      padding: 40px 24px;
      min-height: 100vh;
    }}

    .showcase-header {{
      text-align: center;
      max-width: 900px;
      margin: 0 auto 40px;
    }}
    .showcase-tag {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 153, 229, 0.15);
      border: 1px solid rgba(0, 153, 229, 0.4);
      color: var(--cyan-400);
      padding: 4px 14px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 14px;
    }}
    .showcase-title {{
      font-size: 32px;
      font-weight: 900;
      color: #fff;
      margin-bottom: 12px;
    }}
    .showcase-title span {{ color: var(--cyan-400); }}
    .showcase-subtitle {{
      font-size: 15px;
      color: #94a3b8;
      line-height: 1.6;
    }}

    /* Phones Display Grid */
    .phones-showcase-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 36px;
      max-width: 1300px;
      margin: 0 auto;
      align-items: start;
    }}

    /* Phone Device Frame (iPhone 15 Pro Style) */
    .phone-mockup-frame {{
      background: #000;
      border: 10px solid #1e293b;
      border-radius: 44px;
      box-shadow: 0 25px 60px rgba(0,0,0,0.6), 0 0 0 2px rgba(255,255,255,0.1);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
      height: 820px;
    }}

    /* Dynamic Island & Status Bar */
    .phone-top-bar {{
      background: #0b1120;
      padding: 10px 18px 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: #fff;
      position: relative;
      z-index: 20;
    }}
    .dynamic-island {{
      position: absolute;
      top: 8px;
      left: 50%;
      transform: translateX(-50%);
      width: 90px;
      height: 22px;
      background: #000;
      border-radius: 20px;
    }}

    /* Screen Inner Content */
    .phone-screen-content {{
      background: var(--bg-page);
      color: var(--navy-900);
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      position: relative;
    }}

    /* Screen Title Badge */
    .screen-title-banner {{
      text-align: center;
      margin-top: 14px;
      font-size: 15px;
      font-weight: 800;
      color: #cbd5e1;
    }}
    .screen-title-banner span {{
      color: var(--cyan-400);
    }}

    /* Mobile Header Component */
    .m-header {{
      background: var(--navy-900);
      padding: 12px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--navy-700);
    }}
    .m-logo {{ height: 28px; }}
    .m-actions {{ display: flex; gap: 8px; }}
    .m-icon-btn {{
      background: var(--navy-800);
      border: 1px solid var(--navy-700);
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      position: relative;
    }}

    /* Mobile Sticky Bottom Nav */
    .m-bottom-nav {{
      background: var(--navy-900);
      border-top: 1px solid var(--navy-700);
      padding: 8px 12px 14px;
      display: flex;
      justify-content: space-around;
      align-items: center;
      position: sticky;
      bottom: 0;
      z-index: 30;
    }}
    .m-nav-link {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3px;
      color: #94a3b8;
      font-size: 10px;
      font-weight: 700;
      text-decoration: none;
    }}
    .m-nav-link.active {{ color: var(--cyan-400); }}

    /* Screen 1 specific elements */
    .m-search-box {{
      background: var(--navy-900);
      padding: 0 16px 14px;
    }}
    .m-search-input {{
      width: 100%;
      background: var(--navy-800);
      border: 1px solid var(--navy-700);
      border-radius: 8px;
      padding: 8px 12px;
      color: #fff;
      font-size: 12px;
      outline: none;
    }}
    .m-cats-scroll {{
      display: flex;
      gap: 8px;
      padding: 12px 16px;
      overflow-x: auto;
      background: #fff;
      border-bottom: 1px solid var(--slate-200);
    }}
    .m-cat-chip {{
      background: #f1f5f9;
      padding: 5px 12px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
      color: #334155;
      white-space: nowrap;
    }}
    .m-cat-chip.active {{
      background: var(--cyan-500);
      color: #fff;
    }}

    /* Screen 2 specific elements (Product Sticky CTA Bar) */
    .m-product-sticky-bar {{
      background: #fff;
      border-top: 1px solid var(--slate-200);
      padding: 10px 14px 16px;
      display: flex;
      align-items: center;
      gap: 10px;
      position: sticky;
      bottom: 0;
      box-shadow: 0 -4px 12px rgba(0,0,0,0.05);
      z-index: 40;
    }}
    .btn-m-cart {{
      flex: 1;
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 10px 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .btn-m-whatsapp {{
      width: 42px;
      height: 42px;
      background: #22c55e;
      color: #fff;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: none;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <div class="showcase-header">
    <div class="showcase-tag">Mobile-First Experience (تجربة الهواتف الذكية)</div>
    <h1 class="showcase-title">تصميم متجر <span>MESS TECH</span> المتجاوب مع الموبايل</h1>
    <p class="showcase-subtitle">
      واجهات مهيأة بالكامل لمهندسي الشبكات ومسؤولي المشتريات أثناء العمل الميداني، مع شريط سفلي ثابت، بحث سريع بأرقام الموديلات، وزر واتساب المباشر للاستفسارات السريعة.
    </p>
  </div>

  <div class="phones-showcase-grid">

    <!-- Phone 1: Mobile Homepage -->
    <div>
      <div class="phone-mockup-frame">
        <div class="phone-top-bar">
          <span>9:41</span>
          <div class="dynamic-island"></div>
          <span style="font-family:sans-serif;">5G 100%</span>
        </div>

        <div class="phone-screen-content">
          <!-- Header -->
          <div class="m-header">
            <img src="assets/logo_white.png" class="m-logo" alt="Logo">
            <div class="m-actions">
              <div class="m-icon-btn"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></div>
              <div class="m-icon-btn"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg></div>
            </div>
          </div>

          <!-- Mobile Search -->
          <div class="m-search-box">
            <input type="text" class="m-search-input" placeholder="ابحث برقم الموديل (مثل WS-C2960X)...">
          </div>

          <!-- Horizontal Categories -->
          <div class="m-cats-scroll">
            <div class="m-cat-chip active">الكل</div>
            <div class="m-cat-chip">سويتشات</div>
            <div class="m-cat-chip">راوترات</div>
            <div class="m-cat-chip">فايروول</div>
            <div class="m-cat-chip">واي فاي</div>
            <div class="m-cat-chip">راكات</div>
          </div>

          <!-- Hero Promo -->
          <div style="background:#0f172a; color:#fff; padding:16px; margin:12px; border-radius:12px; border:1px solid #1e293b;">
            <span style="background:rgba(0,153,229,0.15); color:var(--cyan-400); font-size:10px; font-weight:700; padding:2px 8px; border-radius:999px;">أجهزة أصلية معتمدة</span>
            <h3 style="font-size:16px; font-weight:800; margin:6px 0 4px;">حلول وتجهيزات الشبكات للشركات</h3>
            <p style="font-size:11.5px; color:#94a3b8; line-height:1.4;">توريد فوري مع فحص ومطابقة المواصفات الهندسية.</p>
          </div>

          <!-- Weekly Deal Mini -->
          <div style="padding:0 12px; margin-bottom:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <b style="font-size:13px; color:var(--navy-900);">العروض الحالية بمؤقت ⚡</b>
              <span class="mono" style="font-size:11px; color:#f59e0b; font-weight:700;">02d : 14h : 28m</span>
            </div>
            <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:12px;">
              <div style="height:90px; margin-bottom:8px;">{SVG_CISCO_SWITCH}</div>
              <div class="mono" style="font-size:11px; font-weight:700; color:#475569;">WS-C2960X-24TD-L</div>
              <div style="font-size:13px; font-weight:800; margin:3px 0;">سيسكو كاتاليست 24 بورت PoE+</div>
              <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">
                <span style="font-size:15px; font-weight:900; color:var(--navy-900);">19,850 ج.م</span>
                <button style="background:var(--cyan-500); color:#fff; border:none; padding:6px 14px; border-radius:6px; font-size:11.5px; font-weight:700; white-space:nowrap; display:inline-flex;">أضف للسلة</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Sticky Bottom Navigation -->
        <div class="m-bottom-nav">
          <a href="#" class="m-nav-link active">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
            <span>الرئيسية</span>
          </a>
          <a href="#" class="m-nav-link">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
            <span>الأقسام</span>
          </a>
          <a href="#" class="m-nav-link">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            <span>المقارنة</span>
          </a>
          <a href="#" class="m-nav-link">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
            <span>السلة</span>
          </a>
        </div>
      </div>
      <div class="screen-title-banner">1. الصفحة الرئيسية <span>(Mobile Homepage)</span></div>
    </div>

    <!-- Phone 2: Mobile Product Details -->
    <div>
      <div class="phone-mockup-frame">
        <div class="phone-top-bar">
          <span>9:41</span>
          <div class="dynamic-island"></div>
          <span style="font-family:sans-serif;">5G 100%</span>
        </div>

        <div class="phone-screen-content">
          <div class="m-header">
            <span style="font-size:12px; color:#fff;">← رجوع</span>
            <span style="font-size:13px; font-weight:800; color:#fff;">تفاصيل الموديل</span>
            <div class="m-icon-btn"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg></div>
          </div>

          <div style="padding:16px;">
            <!-- Gallery -->
            <div style="background:#fff; border:1px solid var(--slate-200); border-radius:12px; padding:14px; text-align:center; margin-bottom:14px;">
              <div style="height:140px; margin-bottom:10px;">{SVG_CISCO_SWITCH}</div>
              <div class="mono" style="font-size:12px; font-weight:700; color:var(--cyan-600);">WS-C2960X-24TD-L</div>
            </div>

            <h2 style="font-size:16px; font-weight:900; line-height:1.4; color:var(--navy-900); margin-bottom:8px;">
              سويتش سيسكو كاتاليست 24 بورت جيجابت PoE+ مع منفذين 10G SFP+
            </h2>

            <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:12px;">
              <div>
                <span style="font-size:22px; font-weight:900; color:var(--navy-900);">19,850 ج.م</span>
                <span style="font-size:12px; color:#94a3b8; text-decoration:line-through; margin-right:6px;">23,200</span>
              </div>
              <span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:700; padding:2px 8px; border-radius:4px;">متوفر بالمخزن</span>
            </div>

            <!-- Download Datasheet Pill -->
            <div style="background:#0f172a; color:#fff; padding:10px 14px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <span style="font-size:12px; font-weight:700;">تحميل Datasheet PDF الرسمي</span>
              <span style="background:var(--cyan-500); padding:3px 10px; border-radius:4px; font-size:11px; font-weight:800;">3.4 MB</span>
            </div>

            <!-- Specs Grid Mini -->
            <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:12px;">
              <div style="font-size:12.5px; font-weight:800; margin-bottom:8px; color:var(--navy-900);">المواصفات الفنية:</div>
              <div style="font-size:11.5px; color:#475569; display:flex; flex-direction:column; gap:5px;">
                <div style="display:flex; justify-content:space-between;"><span>البورتات:</span><b>24x Gigabit RJ45</b></div>
                <div style="display:flex; justify-content:space-between;"><span>طاقة الـ PoE:</span><b>370W PoE+ (802.3at)</b></div>
                <div style="display:flex; justify-content:space-between;"><span>الأبلينك:</span><b>2x 10G SFP+</b></div>
                <div style="display:flex; justify-content:space-between;"><span>الحالة:</span><b style="color:#059669;">أصلي جديد بالكرتونة</b></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sticky Product Action Bar -->
        <div class="m-product-sticky-bar">
          <button class="btn-m-cart" style="white-space:nowrap; display:inline-flex; align-items:center; justify-content:center; gap:6px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
            أضف للسلة
          </button>
          <a href="https://wa.me/201000000000" class="btn-m-whatsapp" title="واتساب المبيعات">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.592 2.654-.696c1.029.575 1.748.817 2.806.817 3.181 0 5.767-2.587 5.768-5.766.001-3.182-2.585-5.768-5.768-5.768zm0 10.37c-.894 0-1.67-.238-2.427-.69l-.174-.103-1.802.472.48-1.758-.113-.181c-.504-.805-.77-1.524-.769-2.544 0-2.535 2.062-4.597 4.597-4.597 2.536 0 4.598 2.063 4.598 4.598 0 2.535-2.063 4.597-4.597 4.597z"/></svg>
          </a>
        </div>
      </div>
      <div class="screen-title-banner">2. صفحة المنتج والمواصفات <span>(Mobile Product)</span></div>
    </div>

    <!-- Phone 3: Mobile Checkout -->
    <div>
      <div class="phone-mockup-frame">
        <div class="phone-top-bar">
          <span>9:41</span>
          <div class="dynamic-island"></div>
          <span style="font-family:sans-serif;">5G 100%</span>
        </div>

        <div class="phone-screen-content">
          <div class="m-header">
            <span style="font-size:12px; color:#fff;">← السلة</span>
            <span style="font-size:13px; font-weight:800; color:#fff;">إتمام الطلب السريع</span>
            <span></span>
          </div>

          <div style="padding:16px;">
            <!-- COD Badge -->
            <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:8px; padding:10px 12px; margin-bottom:14px; font-size:12px; color:#14532d;">
              <b>الدفع كاش عند الاستلام (COD) فقط</b>
              <div style="font-size:11px; margin-top:2px;">لا حاجة لبطاقات بنكية، عاين شحنتك ثم ادفع.</div>
            </div>

            <!-- Customer inputs -->
            <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:14px;">
              <input type="text" class="form-input" style="padding:9px 12px; font-size:12px;" value="م. أحمد فتحي" placeholder="الاسم بالكامل">
              <input type="text" class="form-input mono" style="padding:9px 12px; font-size:12px;" value="0100 234 5678" placeholder="رقم الهاتف الأساسي">
              <select class="form-input" style="padding:9px 12px; font-size:12px;">
                <option>القاهرة (شحن مجاني للطلبات فوق 20k)</option>
                <option>الجيزة</option>
                <option>الإسكندرية</option>
              </select>
              <input type="text" class="form-input" style="padding:9px 12px; font-size:12px;" value="المعادي الجديدة، شارع النصر" placeholder="العنوان التفصيلي">
            </div>

            <!-- Order Total Card -->
            <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:12px; margin-bottom:14px;">
              <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:6px;">
                <span>المجموع:</span>
                <span>43,200 ج.م</span>
              </div>
              <div style="display:flex; justify-content:space-between; font-size:12px; color:#059669; margin-bottom:6px;">
                <span>الشحن (القاهرة):</span>
                <span>مجاني (0 ج.م)</span>
              </div>
              <div style="display:flex; justify-content:space-between; font-size:12px; color:#ef4444; margin-bottom:8px;">
                <span>خصم الكوبون:</span>
                <span>- 1,000 ج.م</span>
              </div>
              <div style="display:flex; justify-content:space-between; font-size:16px; font-weight:900; border-top:1px solid var(--slate-100); padding-top:8px;">
                <span>المستحق نقدياً:</span>
                <span style="color:var(--cyan-600);">42,200 ج.م</span>
              </div>
            </div>

            <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:13px; border-radius:10px; font-size:14px; font-weight:900; cursor:pointer; white-space:nowrap; display:inline-flex; justify-content:center; align-items:center;">
              تأكيد الطلب (الدفع عند الاستلام) ✓
            </button>
          </div>
        </div>
      </div>
      <div class="screen-title-banner">3. إتمام الطلب خطوة واحدة <span>(Mobile Checkout)</span></div>
    </div>

  </div>

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "page_06_mobile_showcase.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "06_نسخة_الموبايل_Mobile_Screens_Showcase.png")
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
print(f"Rendered: {png_path} ({os.path.getsize(png_path)/1024:.1f} KB)")

