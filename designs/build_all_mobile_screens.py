# -*- coding: utf-8 -*-
import os
import subprocess
from mobile_framework import MOBILE_COMMON_CSS, get_mobile_header, get_mobile_bottom_nav
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS

DESIGNS_DIR = r"E:\mess\designs"

def run_chrome_render(html_path, png_path, height=2200):
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size=430,{height}",
        "--force-device-scale-factor=2.0",
        "--virtual-time-budget=3000",
        f"--screenshot={png_path}",
        f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
    ]
    subprocess.run(cmd, check=True)
    size_kb = os.path.getsize(png_path) / 1024
    print(f"Rendered: {os.path.basename(png_path)} ({size_kb:.1f} KB)")

# ==========================================
# 1. MOBILE HOMEPAGE
# ==========================================
def build_mobile_01():
    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | الصفحة الرئيسية للموبايل (Mobile Homepage)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {MOBILE_COMMON_CSS}
    .m-hero-card {{
      background: radial-gradient(circle at 80% 20%, #172a4d 0%, #0b1120 80%);
      color: #fff;
      padding: 20px 14px;
      margin: 12px 12px;
      border-radius: 14px;
      border: 1px solid #1e293b;
    }}
    .m-hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 153, 229, 0.15);
      border: 1px solid rgba(0, 153, 229, 0.4);
      color: var(--cyan-400);
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
      margin-bottom: 10px;
    }}
    .m-hero-title {{ font-size: 20px; font-weight: 900; line-height: 1.35; margin-bottom: 8px; }}
    .m-hero-title span {{ color: var(--cyan-400); }}
    .m-hero-desc {{ font-size: 12px; color: #94a3b8; line-height: 1.5; margin-bottom: 14px; }}
    .m-hero-btn-row {{ display: flex; gap: 8px; }}
    .m-btn-hero-primary {{
      flex: 1; background: var(--cyan-500); color: #fff; text-align: center;
      padding: 9px 12px; border-radius: 8px; font-size: 12.5px; font-weight: 800; text-decoration: none;
    }}
    .m-btn-hero-rfq {{
      background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.2);
      color: #fff; padding: 9px 12px; border-radius: 8px; font-size: 12px; font-weight: 700; text-decoration: none;
    }}
    .m-deal-section {{ padding: 0 12px; margin-bottom: 18px; }}
    .m-deal-header-bar {{
      background: linear-gradient(90deg, #1e293b 0%, #0f172a 100%);
      border: 1px solid #334155; border-radius: 12px 12px 0 0; padding: 10px 14px;
      display: flex; justify-content: space-between; align-items: center; color: #fff;
    }}
    .m-deal-timer-chips {{ display: flex; gap: 4px; font-size: 11px; }}
    .m-timer-chip {{
      background: #172136; border: 1px solid #334155; padding: 2px 6px;
      border-radius: 4px; color: #f59e0b; font-weight: 800; font-family: 'JetBrains Mono', monospace;
    }}
    .m-deal-body {{
      background: #fff; border: 1px solid var(--slate-200); border-top: none;
      border-radius: 0 0 12px 12px; padding: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }}
    .m-deal-img-box {{
      height: 120px; background: #f8fafc; border-radius: 8px; display: flex;
      align-items: center; justify-content: center; padding: 10px; margin-bottom: 10px;
    }}
    .m-deal-name {{ font-size: 14px; font-weight: 800; color: var(--navy-900); line-height: 1.4; margin-bottom: 8px; }}
    .m-progress-bar-track {{ height: 5px; background: #e2e8f0; border-radius: 999px; overflow: hidden; }}
    .m-progress-bar-fill {{ height: 100%; background: linear-gradient(90deg, #f59e0b, #ef4444); }}
    .m-deal-footer-row {{
      display: flex; justify-content: space-between; align-items: center;
      border-top: 1px solid var(--slate-100); padding-top: 10px; margin-top: 10px;
    }}
    .m-price-current {{ font-size: 19px; font-weight: 900; color: var(--navy-900); }}
    .m-btn-add-cart {{
      background: var(--cyan-500); color: #fff; border: none; padding: 8px 16px;
      border-radius: 8px; font-size: 12.5px; font-weight: 800; cursor: pointer;
    }}
    .m-section-head {{
      padding: 0 14px; margin: 20px 0 10px; display: flex; justify-content: space-between; align-items: baseline;
    }}
    .m-products-list {{ padding: 0 12px; display: flex; flex-direction: column; gap: 10px; }}
    .m-item-card-row {{
      background: #fff; border: 1px solid var(--slate-200); border-radius: 12px;
      padding: 12px; display: flex; gap: 12px; align-items: center;
    }}
    .m-item-thumb {{
      width: 76px; height: 76px; background: #f8fafc; border: 1px solid var(--slate-100);
      border-radius: 8px; display: flex; align-items: center; justify-content: center; padding: 4px; flex-shrink: 0;
    }}
    .m-brands-strip {{
      background: #fff; padding: 12px 14px; margin: 18px 0;
      border-top: 1px solid var(--slate-200); border-bottom: 1px solid var(--slate-200);
      display: flex; justify-content: space-around; align-items: center;
    }}
    .m-value-strip {{
      background: #0f172a; color: #fff; padding: 18px 14px; margin: 16px 12px;
      border-radius: 14px; display: flex; flex-direction: column; gap: 12px;
    }}
    .m-footer {{
      background: var(--navy-950); color: var(--slate-400); padding: 22px 14px 34px;
      text-align: center; border-top: 1px solid #1e293b; font-size: 12px;
    }}
  </style>
</head>
<body>
  {get_mobile_header(active_nav="home")}

  <div class="m-cats-scroller">
    <a href="#" class="m-cat-tag active">الكل</a>
    <a href="#" class="m-cat-tag">سويتشات الشبكات</a>
    <a href="#" class="m-cat-tag">راوترات وسيرفرات</a>
    <a href="#" class="m-cat-tag">جدران الحماية</a>
    <a href="#" class="m-cat-tag">أكسس بوينت وواي فاي</a>
    <a href="#" class="m-cat-tag">راكات وكبائن</a>
  </div>

  <div class="m-hero-card">
    <div class="m-hero-badge">● الموزع المعتمد لحلول الشبكات والأمان</div>
    <h1 class="m-hero-title">تجهيز البنية التحتية والشبكات بأعلى معايير <span>Enterprise المعتمدة</span></h1>
    <p class="m-hero-desc">نوفر سويتشات وراوترات وفايروول لأكبر الماركات مع الدفع كاش عند الاستلام (COD) وضمان استبدال سنتين.</p>
    <div class="m-hero-btn-row">
      <a href="#" class="m-btn-hero-primary">تصفح السويتشات والمعدات</a>
      <a href="#" class="m-btn-hero-rfq">طلب عرض أسعار (RFQ)</a>
    </div>
  </div>

  <div class="m-deal-section">
    <div class="m-deal-header-bar">
      <div style="font-size:13px; font-weight:800; display:flex; align-items:center; gap:6px;">
        <span style="color:#f59e0b;">⚡</span> عروض التوريد الأسبوعية
      </div>
      <div class="m-deal-timer-chips">
        <span class="m-timer-chip">02d</span>
        <span class="m-timer-chip">14h</span>
        <span class="m-timer-chip">28m</span>
        <span class="m-timer-chip">45s</span>
      </div>
    </div>
    <div class="m-deal-body">
      <div class="m-deal-img-box">{SVG_CISCO_SWITCH}</div>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
        <span style="font-size:11px; font-weight:800; color:var(--cyan-600);">CISCO SYSTEMS</span>
        <span class="mono" style="font-size:11px; font-weight:700; background:#f1f5f9; padding:1px 6px; border-radius:4px;">WS-C2960X-24TD-L</span>
      </div>
      <h3 class="m-deal-name">سويتش سيسكو كاتاليست 24 بورت جيجابت PoE+ مع 2x 10G SFP+</h3>
      <div style="margin-bottom:8px;">
        <div style="display:flex; justify-content:space-between; font-size:11px; color:#64748b; margin-bottom:3px; font-weight:700;">
          <span>تم حجز 74% من الكمية</span>
          <span style="color:#ef4444;">متبقي 5 قطع</span>
        </div>
        <div class="m-progress-bar-track"><div class="m-progress-bar-fill" style="width:74%;"></div></div>
      </div>
      <div class="m-deal-footer-row">
        <div>
          <div class="m-price-current">19,850 <small style="font-size:12px; color:#64748b;">ج.م</small></div>
          <div style="font-size:11.5px; color:#94a3b8; text-decoration:line-through;">23,200 ج.م</div>
        </div>
        <button class="m-btn-add-cart">طلب بالدفع COD</button>
      </div>
    </div>
  </div>

  <div class="m-brands-strip">
    <span style="font-weight:900; font-size:13px; color:#0284c7;">CISCO</span>
    <span style="font-weight:900; font-size:13px; color:#ef4444;">FORTINET</span>
    <span style="font-weight:900; font-size:13px; color:#0f172a;">MIKROTIK</span>
    <span style="font-weight:900; font-size:13px; color:#0099e5;">UBIQUITI</span>
  </div>

  <div class="m-section-head">
    <h2 style="font-size:16px; font-weight:900;">الأكثر طلباً للمشروعات</h2>
    <a href="#" style="font-size:12px; color:var(--cyan-600); font-weight:700; text-decoration:none;">عرض الكل ←</a>
  </div>

  <div class="m-products-list">
    <div class="m-item-card-row">
      <div class="m-item-thumb">{SVG_MIKROTIK}</div>
      <div style="flex:1;">
        <div class="mono" style="font-size:11px; font-weight:700; color:#475569;">CRS328-24P-4S+RM</div>
        <div style="font-size:12.5px; font-weight:800; color:var(--navy-900); line-height:1.35; margin:2px 0;">سويتش مايكروتك 24 بورت PoE ذكي 500W مع 4 منافذ 10G</div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
          <span style="font-size:15px; font-weight:900; color:var(--navy-900);">22,400 ج.م</span>
          <button style="background:#f0f9ff; border:1px solid #bae6fd; color:var(--cyan-600); font-size:11.5px; font-weight:800; padding:4px 10px; border-radius:6px; cursor:pointer;">أضف للسلة</button>
        </div>
      </div>
    </div>

    <div class="m-item-card-row">
      <div class="m-item-thumb">{SVG_FORTINET}</div>
      <div style="flex:1;">
        <div class="mono" style="font-size:11px; font-weight:700; color:#ef4444;">FortiGate FG-60F</div>
        <div style="font-size:12.5px; font-weight:800; color:var(--navy-900); line-height:1.35; margin:2px 0;">جدار حماية فورتينت 60F للأمن السيبراني والشبكات</div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
          <span style="font-size:15px; font-weight:900; color:var(--navy-900);">28,900 ج.م</span>
          <button style="background:#f0f9ff; border:1px solid #bae6fd; color:var(--cyan-600); font-size:11.5px; font-weight:800; padding:4px 10px; border-radius:6px; cursor:pointer;">أضف للسلة</button>
        </div>
      </div>
    </div>
  </div>

  <div class="m-value-strip">
    <div style="display:flex; gap:10px; align-items:flex-start;">
      <div style="width:26px; height:26px; background:rgba(0,153,229,0.2); color:var(--cyan-400); border-radius:6px; display:flex; align-items:center; justify-content:center; font-weight:800; font-size:12px;">✓</div>
      <div>
        <h5 style="font-size:13px; font-weight:800; margin-bottom:2px;">الدفع كاش عند الاستلام (COD) فقط</h5>
        <p style="font-size:11px; color:#94a3b8; line-height:1.4;">معاينة الأجهزة وسريالات الموديلات والفاتورة الضريبية مع المندوب قبل السداد.</p>
      </div>
    </div>
  </div>

  <footer class="m-footer">
    <img src="assets/logo_white.png" style="height:26px; margin-bottom:8px;" alt="MESS TECH">
    <div style="font-size:11px; color:#64748b;">جميع الحقوق محفوظة © 2026 MESS TECH</div>
  </footer>

  {get_mobile_bottom_nav(active="home")}
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_page_01_homepage.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png")
    run_chrome_render(html_file, png_file, height=2150)

# ==========================================
# 2. MOBILE PRODUCT DETAILS
# ==========================================
def build_mobile_02():
    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | صفحة المنتج للموبايل (Mobile Product Details)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {MOBILE_COMMON_CSS}
    .m-top-back-bar {{
      background: var(--navy-900); color: #fff; padding: 12px 14px;
      display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--navy-700);
    }}
    .m-gallery-card {{
      background: #fff; border: 1px solid var(--slate-200); border-radius: 12px;
      padding: 16px; margin: 12px; text-align: center;
    }}
    .m-gallery-img-box {{ height: 160px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px; }}
    .m-thumbs-strip {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; }}
    .m-thumb {{
      border: 1.5px solid var(--slate-200); border-radius: 6px; padding: 4px 8px; font-size: 10px; font-weight: 700; color: #64748b; background: #f8fafc;
    }}
    .m-thumb.active {{ border-color: var(--cyan-500); color: var(--cyan-600); background: #f0f9ff; }}
    .m-info-block {{ padding: 0 14px 20px; }}
    .m-price-box {{
      background: #fff; border: 1px solid var(--slate-200); border-radius: 12px;
      padding: 14px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }}
    .m-cod-pill {{
      background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px;
      padding: 10px 12px; margin-bottom: 12px; font-size: 11.5px; color: #166534; display: flex; align-items: center; gap: 8px;
    }}
    .m-datasheet-card {{
      background: #0f172a; color: #fff; padding: 12px 14px; border-radius: 10px;
      display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;
    }}
    .m-specs-table-mini {{
      width: 100%; border-collapse: collapse; background: #fff; border: 1px solid var(--slate-200);
      border-radius: 10px; overflow: hidden; margin-bottom: 14px; font-size: 12px;
    }}
    .m-specs-table-mini td {{ padding: 10px 12px; border-bottom: 1px solid var(--slate-100); }}
    .m-specs-table-mini td.label {{ background: #f8fafc; font-weight: 700; color: #334155; width: 40%; }}
    
    /* Fixed Sticky Bottom Action Bar */
    .m-sticky-cta-bar {{
      position: sticky; bottom: 0; background: #fff; border-top: 1px solid var(--slate-200);
      padding: 10px 14px 14px; display: flex; align-items: center; gap: 10px;
      box-shadow: 0 -4px 16px rgba(0,0,0,0.08); z-index: 100;
    }}
    .btn-m-cta-cart {{
      flex: 1; background: var(--cyan-500); color: #fff; border: none; padding: 12px 14px;
      border-radius: 10px; font-size: 13.5px; font-weight: 800; cursor: pointer;
      display: flex; align-items: center; justify-content: center; gap: 8px;
    }}
    .btn-m-cta-whatsapp {{
      width: 44px; height: 44px; background: #22c55e; color: #fff; border-radius: 10px;
      display: flex; align-items: center; justify-content: center; text-decoration: none; border: none;
    }}
  </style>
</head>
<body>
  <!-- Top Bar -->
  <div class="m-top-back-bar">
    <a href="#" style="color:#cbd5e1; text-decoration:none; font-size:12px; font-weight:700;">← رجوع للسويتشات</a>
    <span style="font-size:13px; font-weight:800;">سيسكو كاتاليست 2960X</span>
    <span style="font-size:12px; color:var(--cyan-400);">مشاركة ↗</span>
  </div>

  <!-- Gallery -->
  <div class="m-gallery-card">
    <div class="m-gallery-img-box">{SVG_CISCO_SWITCH}</div>
    <div class="m-thumbs-strip">
      <span class="m-thumb active">واجهة البورتات</span>
      <span class="m-thumb">منافذ 10G SFP+</span>
      <span class="m-thumb">الباور الخلفي</span>
      <span class="m-thumb">طقم الراك 1U</span>
    </div>
  </div>

  <!-- Info -->
  <div class="m-info-block">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
      <span style="background:#e0f2fe; color:var(--cyan-600); font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">CISCO SYSTEMS</span>
      <span class="mono" style="font-size:12px; font-weight:700; background:#f1f5f9; padding:2px 8px; border-radius:4px;">WS-C2960X-24TD-L</span>
    </div>

    <h1 style="font-size:17px; font-weight:900; line-height:1.4; color:var(--navy-900); margin-bottom:10px;">
      سويتش سيسكو كاتاليست 24 بورت جيجابت PoE+ مع منفذين 10G SFP+ فئة المؤسسات
    </h1>

    <div class="m-price-box">
      <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:8px;">
        <div>
          <span style="font-size:24px; font-weight:900; color:var(--navy-900);">19,850 <small style="font-size:13px; color:#64748b;">ج.م</small></span>
          <span style="font-size:13px; color:#94a3b8; text-decoration:line-through; margin-right:6px;">23,200 ج.م</span>
        </div>
        <span style="background:#fef2f2; color:#ef4444; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">خصم 14%</span>
      </div>
      <div style="font-size:11.5px; color:#059669; font-weight:700;">● متوفر فوراً بالمخزون (متبقي 6 قطع في فرع القاهرة)</div>
    </div>

    <!-- COD Guarantee -->
    <div class="m-cod-pill">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 12 15 16 10"/></svg>
      <div>
        <b>الدفع نقداً عند الاستلام (COD) فقط:</b>
        <div style="font-size:10.5px; margin-top:1px;">عاين جهازك وافحص الفاتورة الضريبية مع المندوب قبل دفع أي مبلغ.</div>
      </div>
    </div>

    <!-- Download Datasheet -->
    <div class="m-datasheet-card">
      <div>
        <div style="font-size:12.5px; font-weight:800;">الداتاشيت الرسمية (Official Datasheet)</div>
        <div style="font-size:10.5px; color:#94a3b8;">ملف المواصفات الفنية المعتمد من سيسكو • 3.4 MB</div>
      </div>
      <span style="background:var(--cyan-500); padding:4px 10px; border-radius:6px; font-size:11px; font-weight:800;">تحميل PDF</span>
    </div>

    <!-- Specs Table -->
    <table class="m-specs-table-mini">
      <tbody>
        <tr><td class="label">إجمالي البورتات</td><td><b>24x 1GbE RJ45 Ports</b></td></tr>
        <tr><td class="label">طاقة PoE Budget</td><td><b>370W PoE+ (802.3at)</b></td></tr>
        <tr><td class="label">منافذ الـ Uplink</td><td><b>2x 10G SFP+ عالية السرعة</b></td></tr>
        <tr><td class="label">سعة التبديل</td><td><b>216 Gbps Switching Capacity</b></td></tr>
        <tr><td class="label">الطبقة والإدارة</td><td><b>Layer 2 / Layer 3 Lite Managed</b></td></tr>
        <tr><td class="label">الضمان المحلي</td><td><b style="color:#059669;">سنتين استبدال معتمد</b></td></tr>
      </tbody>
    </table>

    <!-- Direct WhatsApp Inquiry notice -->
    <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:10px 12px; margin-bottom:14px; font-size:11.5px; color:#15803d;">
      💬 <b>استفسار فوري عبر واتساب:</b> تواصل مباشرة مع مهندس المبيعات برقم الموديل بدون الحاجة لأي حساب تجاري معقد.
    </div>
  </div>

  <!-- Sticky Bottom CTA -->
  <div class="m-sticky-cta-bar">
    <button class="btn-m-cta-cart">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
      أضف للسلة (الدفع عند الاستلام)
    </button>
    <a href="https://wa.me/201000000000?text=استفسار%20عن%20سيسكو%20WS-C2960X-24TD-L" class="btn-m-cta-whatsapp" title="تواصل واتساب">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.592 2.654-.696c1.029.575 1.748.817 2.806.817 3.181 0 5.767-2.587 5.768-5.766.001-3.182-2.585-5.768-5.768-5.768zm0 10.37c-.894 0-1.67-.238-2.427-.69l-.174-.103-1.802.472.48-1.758-.113-.181c-.504-.805-.77-1.524-.769-2.544 0-2.535 2.062-4.597 4.597-4.597 2.536 0 4.598 2.063 4.598 4.598 0 2.535-2.063 4.597-4.597 4.597z"/></svg>
    </a>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_page_02_product_details.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_02_صفحة_المنتج_والمواصفات_Mobile_Product_Details.png")
    run_chrome_render(html_file, png_file, height=1600)

# ==========================================
# 3. MOBILE CATALOG & FILTERS
# ==========================================
def build_mobile_03():
    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | تصفح وفلاتر السويتشات للموبايل (Mobile Catalog & Filters)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {MOBILE_COMMON_CSS}
    .m-cat-title-bar {{
      padding: 12px 14px; background: #fff; border-bottom: 1px solid var(--slate-200);
      display: flex; justify-content: space-between; align-items: center;
    }}
    .m-filter-toggle-row {{
      padding: 10px 14px; background: #f8fafc; border-bottom: 1px solid var(--slate-200);
      display: flex; gap: 8px; align-items: center;
    }}
    .m-btn-filter-toggle {{
      flex: 1; background: var(--navy-900); color: #fff; border: none; padding: 9px 12px;
      border-radius: 8px; font-size: 12px; font-weight: 800; display: flex; align-items: center; justify-content: center; gap: 6px;
    }}
    .m-btn-sort-toggle {{
      background: #fff; border: 1px solid var(--slate-300); color: #334155; padding: 9px 12px;
      border-radius: 8px; font-size: 12px; font-weight: 700;
    }}
    .m-active-chips-scroll {{
      display: flex; gap: 6px; padding: 8px 14px; background: #fff; overflow-x: auto;
      border-bottom: 1px solid var(--slate-100);
    }}
    .m-filter-chip {{
      background: #e0f2fe; color: var(--cyan-600); border: 1px solid #bae6fd;
      padding: 3px 8px; border-radius: 999px; font-size: 10.5px; font-weight: 700; white-space: nowrap;
    }}
    .m-catalog-grid-2 {{
      padding: 12px; display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
    }}
    .m-grid-prod-card {{
      background: #fff; border: 1px solid var(--slate-200); border-radius: 10px;
      padding: 10px; display: flex; flex-direction: column;
    }}
    .m-grid-img-wrap {{
      height: 80px; background: #f8fafc; border-radius: 6px; display: flex;
      align-items: center; justify-content: center; padding: 6px; margin-bottom: 8px;
    }}
    
    /* Bottom Sheet Filter Drawer Preview */
    .m-bottom-sheet-overlay {{
      background: rgba(11, 17, 32, 0.7); padding: 20px 14px 0; margin-top: 16px;
      border-radius: 20px 20px 0 0; border-top: 2px solid var(--cyan-500);
    }}
    .m-sheet-card {{
      background: #fff; border-radius: 16px 16px 0 0; padding: 18px 16px 24px;
    }}
    .m-sheet-handle {{
      width: 40px; height: 4px; background: #cbd5e1; border-radius: 999px; margin: 0 auto 14px;
    }}
    .m-filter-item-check {{
      display: flex; justify-content: space-between; font-size: 12.5px; padding: 6px 0; color: #334155;
    }}
  </style>
</head>
<body>
  {get_mobile_header(active_nav="categories")}

  <div class="m-cat-title-bar">
    <div>
      <h1 style="font-size:15px; font-weight:900; color:var(--navy-900);">سويتشات الشبكات للشركات</h1>
      <div style="font-size:11px; color:#64748b;">18 موديل مطابق للفلاتر التقنية</div>
    </div>
    <span class="m-badge-cod">دفع عند الاستلام COD</span>
  </div>

  <!-- Filter & Sort Bar -->
  <div class="m-filter-toggle-row">
    <button class="m-btn-filter-toggle">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
      تصفية المواصفات (4 نشطة)
    </button>
    <button class="m-btn-sort-toggle">ترتيب: الأكثر طلباً ▾</button>
  </div>

  <!-- Active Chips -->
  <div class="m-active-chips-scroll">
    <span class="m-filter-chip">Cisco ✕</span>
    <span class="m-filter-chip">24 Port GbE ✕</span>
    <span class="m-filter-chip">PoE+ 370W ✕</span>
    <span class="m-filter-chip">10G SFP+ ✕</span>
    <span style="font-size:10.5px; color:var(--rose-500); font-weight:700; align-self:center; cursor:pointer;">مسح الكل</span>
  </div>

  <!-- Products Grid (2 columns on mobile) -->
  <div class="m-catalog-grid-2">
    <!-- Card 1: Cisco -->
    <div class="m-grid-prod-card">
      <div class="m-grid-img-wrap">{SVG_CISCO_SWITCH}</div>
      <div class="mono" style="font-size:10px; font-weight:700; color:var(--cyan-600);">WS-C2960X-24TD-L</div>
      <h3 style="font-size:11.5px; font-weight:800; color:var(--navy-900); line-height:1.35; height:32px; overflow:hidden; margin:3px 0;">سيسكو كاتاليست 24 بورت PoE+ 370W</h3>
      <div style="font-size:10px; color:#64748b; margin-bottom:6px;">2x 10G SFP+ • Layer 2/3</div>
      <div style="font-size:14px; font-weight:900; color:var(--navy-900); margin-top:auto;">19,850 ج.م</div>
      <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:6px; border-radius:6px; font-size:11px; font-weight:800; margin-top:6px; cursor:pointer;">طلب بالدفع COD</button>
    </div>

    <!-- Card 2: MikroTik -->
    <div class="m-grid-prod-card">
      <div class="m-grid-img-wrap">{SVG_MIKROTIK}</div>
      <div class="mono" style="font-size:10px; font-weight:700; color:#0f172a;">CRS328-24P-4S+RM</div>
      <h3 style="font-size:11.5px; font-weight:800; color:var(--navy-900); line-height:1.35; height:32px; overflow:hidden; margin:3px 0;">مايكروتك 24 بورت ذكي 500W</h3>
      <div style="font-size:10px; color:#64748b; margin-bottom:6px;">4x 10G SFP+ • RouterOS</div>
      <div style="font-size:14px; font-weight:900; color:var(--navy-900); margin-top:auto;">22,400 ج.م</div>
      <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:6px; border-radius:6px; font-size:11px; font-weight:800; margin-top:6px; cursor:pointer;">طلب بالدفع COD</button>
    </div>
  </div>

  <!-- Filter Bottom Sheet (Interactive Drawer Showcase) -->
  <div class="m-bottom-sheet-overlay">
    <div class="m-sheet-card">
      <div class="m-sheet-handle"></div>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid var(--slate-100); padding-bottom:8px;">
        <b style="font-size:14px; color:var(--navy-900);">تصفية المواصفات الفنية</b>
        <span style="font-size:11.5px; color:var(--rose-500); font-weight:700; cursor:pointer;">إعادة ضبط</span>
      </div>

      <div style="font-size:12px; font-weight:800; color:var(--navy-900); margin:8px 0 4px;">الشركة المصنعة:</div>
      <div class="m-filter-item-check"><label><input type="checkbox" checked> <b>Cisco Systems</b></label> <span>(14)</span></div>
      <div class="m-filter-item-check"><label><input type="checkbox"> MikroTik</label> <span>(12)</span></div>

      <div style="font-size:12px; font-weight:800; color:var(--navy-900); margin:10px 0 4px;">عدد منافذ الشبكة:</div>
      <div class="m-filter-item-check"><label><input type="checkbox" checked> <b>24 Port Gigabit</b></label> <span>(18)</span></div>
      <div class="m-filter-item-check"><label><input type="checkbox"> 48 Port Gigabit</label> <span>(12)</span></div>

      <div style="font-size:12px; font-weight:800; color:var(--navy-900); margin:10px 0 4px;">طاقة الـ PoE:</div>
      <div class="m-filter-item-check"><label><input type="checkbox" checked> <b>PoE+ (370W)</b></label> <span>(15)</span></div>

      <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:12px; border-radius:10px; font-size:13px; font-weight:800; margin-top:14px; cursor:pointer;">
        تطبيق الفلاتر (عرض 18 منتج) ✓
      </button>
    </div>
  </div>

  {get_mobile_bottom_nav(active="categories")}
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_page_03_catalog_filters.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_03_الفلاتر_وتصفح_المنتجات_Mobile_Catalog_Filters.png")
    run_chrome_render(html_file, png_file, height=1400)

# ==========================================
# 4. MOBILE SINGLE-STEP CHECKOUT
# ==========================================
def build_mobile_04():
    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | إتمام الطلب بالموبايل (Mobile One-Step Checkout COD)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {MOBILE_COMMON_CSS}
    .m-checkout-top-bar {{
      background: var(--navy-900); color: #fff; padding: 12px 14px;
      display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--navy-700);
    }}
    .m-checkout-card {{
      background: #fff; border: 1px solid var(--slate-200); border-radius: 12px;
      padding: 14px; margin: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }}
    .m-card-title-row {{
      display: flex; align-items: center; gap: 8px; font-size: 13.5px; font-weight: 800;
      color: var(--navy-900); margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid var(--slate-100);
    }}
    .m-input-label {{ font-size: 11.5px; font-weight: 700; color: #475569; margin-bottom: 3px; display: block; }}
    .m-text-input {{
      width: 100%; background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px;
      padding: 9px 12px; font-size: 12.5px; color: var(--navy-900); outline: none; margin-bottom: 10px;
    }}
    .m-delivery-options {{ display: flex; gap: 8px; margin-bottom: 12px; }}
    .m-del-pill {{
      flex: 1; border: 1.5px solid var(--slate-200); border-radius: 8px; padding: 10px 8px;
      background: #f8fafc; cursor: pointer; text-align: center; font-size: 11.5px; font-weight: 700;
    }}
    .m-del-pill.active {{ border-color: var(--cyan-500); background: #f0f9ff; color: var(--cyan-600); }}
    
    /* Fixed Bottom Checkout Confirm */
    .m-checkout-sticky-footer {{
      position: sticky; bottom: 0; background: #fff; border-top: 1px solid var(--slate-200);
      padding: 12px 14px 16px; box-shadow: 0 -4px 16px rgba(0,0,0,0.08); z-index: 100;
    }}
    .btn-m-confirm-order {{
      width: 100%; background: var(--cyan-500); color: #fff; border: none; padding: 14px;
      border-radius: 10px; font-size: 14.5px; font-weight: 900; cursor: pointer;
      display: flex; align-items: center; justify-content: center; gap: 8px;
    }}
  </style>
</head>
<body>
  <!-- Header -->
  <div class="m-checkout-top-bar">
    <a href="#" style="color:#cbd5e1; text-decoration:none; font-size:12px;">← السلة</a>
    <span style="font-size:13.5px; font-weight:800;">إتمام الطلب في خطوة واحدة</span>
    <span style="font-size:11px; color:#34d399;">🔒 آمن 100%</span>
  </div>

  <!-- COD Notice -->
  <div style="background:#f0fdf4; border:1px solid #86efac; border-radius:10px; padding:12px; margin:12px; font-size:11.5px; color:#14532d;">
    <b>الدفع نقداً عند الاستلام (COD) فقط</b>
    <div style="font-size:10.5px; margin-top:2px;">لا حاجة لكروت أو دفع إلكتروني. عاين الشحنة وسريالات الموديلات والفاتورة أولاً ثم ادفع كاش.</div>
  </div>

  <!-- Step 1: Customer Contact -->
  <div class="m-checkout-card">
    <div class="m-card-title-row">
      <span style="background:var(--navy-900); color:var(--cyan-400); width:20px; height:20px; border-radius:4px; display:inline-flex; align-items:center; justify-content:center; font-size:11px;">1</span>
      <span>بيانات العميل والتواصل (شراء سريع كضيف)</span>
    </div>

    <label class="m-input-label">الاسم بالكامل أو اسم الشركة *</label>
    <input type="text" class="m-text-input" value="م. أحمد فتحي (شركة دلتا)">

    <label class="m-input-label">رقم الهاتف الأساسي (مطلوب لمندوب التوصيل) *</label>
    <input type="text" class="m-text-input mono" value="0100 234 5678">

    <label class="m-input-label">البريد الإلكتروني (لتلقي إشعار وبوليصة الطلب)</label>
    <input type="email" class="m-text-input mono" value="ahmed.fathi@deltatech.com">
  </div>

  <!-- Step 2: Shipping & Address -->
  <div class="m-checkout-card">
    <div class="m-card-title-row">
      <span style="background:var(--navy-900); color:var(--cyan-400); width:20px; height:20px; border-radius:4px; display:inline-flex; align-items:center; justify-content:center; font-size:11px;">2</span>
      <span>طريقة الاستلام وعنوان الشحن</span>
    </div>

    <div class="m-delivery-options">
      <div class="m-del-pill active">
        <div>توصيل للمقر/الشركة</div>
        <div style="font-size:10px; color:#059669; margin-top:2px;">شحن سريع مؤمن</div>
      </div>
      <div class="m-del-pill">
        <div>استلام من الفرع</div>
        <div style="font-size:10px; color:var(--cyan-600); margin-top:2px;">مجاناً (0 ج.م)</div>
      </div>
    </div>

    <label class="m-input-label">المحافظة (لحساب الشحن آلياً) *</label>
    <select class="m-text-input" style="font-weight:700;">
      <option selected>القاهرة (شحن مجاني فوق 20,000 ج.م)</option>
      <option>الجيزة (شحن مجاني)</option>
      <option>الإسكندرية والوجه البحري</option>
      <option>الصعيد والمحافظات البعيدة</option>
    </select>

    <label class="m-input-label">العنوان التفصيلي (الشارع، رقم المبنى، الدور) *</label>
    <input type="text" class="m-text-input" value="المعادي الجديدة، شارع النصر، عمارة 14">
  </div>

  <!-- Step 3: Order Summary -->
  <div class="m-checkout-card">
    <div class="m-card-title-row">
      <span style="background:var(--navy-900); color:var(--cyan-400); width:20px; height:20px; border-radius:4px; display:inline-flex; align-items:center; justify-content:center; font-size:11px;">3</span>
      <span>ملخص الطلب والحساب</span>
    </div>

    <div style="font-size:12px; color:#475569; display:flex; flex-direction:column; gap:6px;">
      <div style="display:flex; justify-content:space-between;">
        <span>سويتش سيسكو كاتاليست 2960X (x2):</span>
        <b>39,700 ج.م</b>
      </div>
      <div style="display:flex; justify-content:space-between;">
        <span>كابينة راك 9U جداري (x1):</span>
        <b>3,500 ج.م</b>
      </div>
      <div style="display:flex; justify-content:space-between; color:#059669;">
        <span>الشحن للمحافظة (القاهرة):</span>
        <b>مجاني (0 ج.م)</b>
      </div>
      <div style="display:flex; justify-content:space-between; color:#ef4444;">
        <span>كوبون الخصم (MESS2026):</span>
        <b>- 1,000 ج.م</b>
      </div>
      <div style="display:flex; justify-content:space-between; font-size:16px; font-weight:900; color:var(--navy-900); border-top:1px solid var(--slate-100); padding-top:8px; margin-top:4px;">
        <span>المستحق نقدياً (COD):</span>
        <span style="color:var(--cyan-600);">42,200 ج.م</span>
      </div>
    </div>
  </div>

  <!-- Sticky Confirm Footer -->
  <div class="m-checkout-sticky-footer">
    <button class="btn-m-confirm-order">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
      تأكيد الطلب الآن - الدفع عند الاستلام (COD)
    </button>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_page_04_checkout_cod.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_04_السلة_واتمام_الطلب_COD_Mobile_Checkout.png")
    run_chrome_render(html_file, png_file, height=1350)

# ==========================================
# 5. MOBILE COMPARISON MATRIX
# ==========================================
def build_mobile_05():
    html_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | مقارنة الموديلات للموبايل (Mobile Product Comparison)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {MOBILE_COMMON_CSS}
    .m-comp-header {{
      padding: 12px 14px; background: #fff; border-bottom: 1px solid var(--slate-200);
    }}
    .m-comp-cards-scroll {{
      display: flex; gap: 10px; padding: 12px; overflow-x: auto;
    }}
    .m-comp-model-card {{
      width: 260px; background: #fff; border: 1.5px solid var(--slate-200);
      border-radius: 12px; padding: 12px; flex-shrink: 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }}
    .m-comp-img-box {{
      height: 90px; background: #f8fafc; border-radius: 8px; display: flex;
      align-items: center; justify-content: center; padding: 6px; margin-bottom: 8px;
    }}
    .m-comp-spec-row {{
      display: flex; justify-content: space-between; font-size: 11.5px; padding: 6px 0;
      border-bottom: 1px solid var(--slate-100);
    }}
    .m-comp-spec-row.diff {{ background: rgba(0, 153, 229, 0.06); padding: 6px 4px; border-radius: 4px; }}
  </style>
</head>
<body>
  {get_mobile_header(active_nav="compare")}

  <div class="m-comp-header">
    <h1 style="font-size:15px; font-weight:900; color:var(--navy-900);">مقارنة المواصفات للموبايل (اسحب للمقارنة)</h1>
    <div style="font-size:11px; color:#64748b;">مقارنة الفروق بين سيسكو ومايكروتك ويوبيكويتي وفورتينت</div>
  </div>

  <!-- Horizontal Swipable Comparison Cards -->
  <div class="m-comp-cards-scroll">

    <!-- Model 1: Cisco -->
    <div class="m-comp-model-card" style="border-color:var(--cyan-500);">
      <div style="font-size:10px; font-weight:800; color:var(--cyan-600);">CISCO SYSTEMS</div>
      <div class="mono" style="font-size:12px; font-weight:800; color:var(--navy-900);">WS-C2960X-24TD-L</div>
      <div class="m-comp-img-box">{SVG_CISCO_SWITCH}</div>
      <div style="font-size:16px; font-weight:900; color:var(--navy-900); margin-bottom:8px;">19,850 ج.م</div>
      <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:7px; border-radius:6px; font-size:11.5px; font-weight:800; margin-bottom:10px; cursor:pointer;">طلب بالدفع COD</button>

      <div class="m-comp-spec-row"><span>البورتات:</span><b>24x 1GbE</b></div>
      <div class="m-comp-spec-row diff"><span>الأبلينك:</span><b style="color:var(--cyan-600);">2x 10G SFP+</b></div>
      <div class="m-comp-spec-row diff"><span>طاقة الـ PoE:</span><b>370W PoE+</b></div>
      <div class="m-comp-spec-row diff"><span>سعة التبديل:</span><b>216 Gbps</b></div>
      <div class="m-comp-spec-row"><span>الطبقة:</span><b>Layer 2/3 Lite</b></div>
      <div class="m-comp-spec-row"><span>الضمان:</span><b style="color:#059669;">سنتين معتمد</b></div>
    </div>

    <!-- Model 2: MikroTik -->
    <div class="m-comp-model-card">
      <div style="font-size:10px; font-weight:800; color:#0f172a;">MIKROTIK</div>
      <div class="mono" style="font-size:12px; font-weight:800; color:var(--navy-900);">CRS328-24P-4S+RM</div>
      <div class="m-comp-img-box">{SVG_MIKROTIK}</div>
      <div style="font-size:16px; font-weight:900; color:var(--navy-900); margin-bottom:8px;">22,400 ج.م</div>
      <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:7px; border-radius:6px; font-size:11.5px; font-weight:800; margin-bottom:10px; cursor:pointer;">طلب بالدفع COD</button>

      <div class="m-comp-spec-row"><span>البورتات:</span><b>24x 1GbE</b></div>
      <div class="m-comp-spec-row diff"><span>الأبلينك:</span><b style="color:var(--cyan-600);">4x 10G SFP+ (الأعلى)</b></div>
      <div class="m-comp-spec-row diff"><span>طاقة الـ PoE:</span><b style="color:#059669;">500W Dual PSU</b></div>
      <div class="m-comp-spec-row diff"><span>سعة التبديل:</span><b>128 Gbps</b></div>
      <div class="m-comp-spec-row"><span>الطبقة:</span><b>RouterOS L5</b></div>
      <div class="m-comp-spec-row"><span>الضمان:</span><b>سنة معتمدة</b></div>
    </div>

    <!-- Model 3: Fortinet -->
    <div class="m-comp-model-card">
      <div style="font-size:10px; font-weight:800; color:#ef4444;">FORTINET</div>
      <div class="mono" style="font-size:12px; font-weight:800; color:var(--navy-900);">FS-124E-POE</div>
      <div class="m-comp-img-box">{SVG_FORTINET}</div>
      <div style="font-size:16px; font-weight:900; color:var(--navy-900); margin-bottom:8px;">21,500 ج.م</div>
      <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:7px; border-radius:6px; font-size:11.5px; font-weight:800; margin-bottom:10px; cursor:pointer;">طلب بالدفع COD</button>

      <div class="m-comp-spec-row"><span>البورتات:</span><b>24x 1GbE</b></div>
      <div class="m-comp-spec-row diff"><span>الأبلينك:</span><b>4x 1G SFP</b></div>
      <div class="m-comp-spec-row diff"><span>طاقة الـ PoE:</span><b>180W PoE+</b></div>
      <div class="m-comp-spec-row diff"><span>سعة التبديل:</span><b>56 Gbps</b></div>
      <div class="m-comp-spec-row"><span>الطبقة:</span><b>FortiLink Layer 2</b></div>
      <div class="m-comp-spec-row"><span>الضمان:</span><b style="color:#059669;">سنتين معتمد</b></div>
    </div>

  </div>

  {get_mobile_bottom_nav(active="compare")}
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_page_05_comparison.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_05_مقارنة_الموديلات_Mobile_Product_Comparison.png")
    run_chrome_render(html_file, png_file, height=950)

if __name__ == "__main__":
    print("Building mobile screens...")
    build_mobile_01()
    build_mobile_02()
    build_mobile_03()
    build_mobile_04()
    build_mobile_05()
    print("All mobile screens generated successfully!")
