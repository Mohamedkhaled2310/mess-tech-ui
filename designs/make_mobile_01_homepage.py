# -*- coding: utf-8 -*-
import os
import subprocess
from mobile_framework import MOBILE_COMMON_CSS, get_mobile_header, get_mobile_bottom_nav
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP

DESIGNS_DIR = r"E:\mess\designs"

HTML_CONTENT = f"""<!DOCTYPE html>
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

    /* Hero Banner Mobile */
    .m-hero-card {{
      background: radial-gradient(circle at 80% 20%, #172a4d 0%, #0b1120 80%);
      color: #fff;
      padding: 20px 16px;
      margin: 12px 14px;
      border-radius: 14px;
      border: 1px solid #1e293b;
      box-shadow: 0 4px 14px rgba(0,0,0,0.25);
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
    .m-hero-title {{
      font-size: 20px;
      font-weight: 900;
      line-height: 1.35;
      margin-bottom: 8px;
    }}
    .m-hero-title span {{ color: var(--cyan-400); }}
    .m-hero-desc {{
      font-size: 12px;
      color: #94a3b8;
      line-height: 1.5;
      margin-bottom: 14px;
    }}
    .m-hero-btn-row {{
      display: flex;
      gap: 8px;
    }}
    .m-btn-hero-primary {{
      flex: 1;
      background: var(--cyan-500);
      color: #fff;
      text-align: center;
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 800;
      text-decoration: none;
    }}
    .m-btn-hero-rfq {{
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.2);
      color: #fff;
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
    }}

    /* Weekly Deal Card */
    .m-deal-section {{
      padding: 0 14px;
      margin-bottom: 18px;
    }}
    .m-deal-header-bar {{
      background: linear-gradient(90deg, #1e293b 0%, #0f172a 100%);
      border: 1px solid #334155;
      border-radius: 12px 12px 0 0;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #fff;
    }}
    .m-deal-title {{
      font-size: 13px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .m-deal-timer-chips {{
      display: flex;
      gap: 4px;
      font-size: 11px;
    }}
    .m-timer-chip {{
      background: #172136;
      border: 1px solid #334155;
      padding: 2px 6px;
      border-radius: 4px;
      color: #f59e0b;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
    }}
    .m-deal-body {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-top: none;
      border-radius: 0 0 12px 12px;
      padding: 14px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }}
    .m-deal-img-box {{
      height: 120px;
      background: #f8fafc;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 10px;
      margin-bottom: 10px;
    }}
    .m-deal-name {{
      font-size: 14px;
      font-weight: 800;
      color: var(--navy-900);
      line-height: 1.4;
      margin-bottom: 8px;
    }}
    .m-deal-progress {{
      margin-bottom: 12px;
    }}
    .m-deal-progress-text {{
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: #64748b;
      margin-bottom: 3px;
      font-weight: 700;
    }}
    .m-progress-bar-track {{
      height: 5px;
      background: #e2e8f0;
      border-radius: 999px;
      overflow: hidden;
    }}
    .m-progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #f59e0b, #ef4444);
    }}
    .m-deal-footer-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--slate-100);
      padding-top: 10px;
    }}
    .m-price-current {{
      font-size: 19px;
      font-weight: 900;
      color: var(--navy-900);
    }}
    .m-price-old {{
      font-size: 12px;
      color: #94a3b8;
      text-decoration: line-through;
    }}
    .m-btn-add-cart {{
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 800;
      cursor: pointer;
    }}

    /* Section Headers */
    .m-section-head {{
      padding: 0 16px;
      margin: 20px 0 10px;
      display: flex;
      justify-content: space-between;
      align-items: baseline;
    }}
    .m-section-title {{
      font-size: 16px;
      font-weight: 900;
      color: var(--navy-900);
    }}
    .m-section-more {{
      font-size: 12px;
      color: var(--cyan-600);
      font-weight: 700;
      text-decoration: none;
    }}

    /* Products List / Grid */
    .m-products-list {{
      padding: 0 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .m-item-card-row {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 12px;
      padding: 12px;
      display: flex;
      gap: 12px;
      align-items: center;
    }}
    .m-item-thumb {{
      width: 80px;
      height: 80px;
      background: #f8fafc;
      border: 1px solid var(--slate-100);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4px;
      flex-shrink: 0;
    }}
    .m-item-details {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}
    .m-item-brand {{
      font-size: 10.5px;
      font-weight: 800;
      color: var(--cyan-600);
      text-transform: uppercase;
    }}
    .m-item-model {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      color: #334155;
    }}
    .m-item-name {{
      font-size: 12.5px;
      font-weight: 800;
      color: var(--navy-900);
      line-height: 1.35;
      height: 34px;
      overflow: hidden;
    }}
    .m-item-specs-strip {{
      display: flex;
      gap: 4px;
      margin: 3px 0;
    }}
    .m-spec-tag {{
      background: #f1f5f9;
      font-size: 9.5px;
      font-weight: 700;
      color: #475569;
      padding: 1px 5px;
      border-radius: 3px;
    }}
    .m-item-bottom-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 4px;
    }}
    .m-item-price {{
      font-size: 15px;
      font-weight: 900;
      color: var(--navy-900);
    }}
    .m-btn-mini-add {{
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      color: var(--cyan-600);
      font-size: 11.5px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
    }}

    /* Mobile Brand Partners */
    .m-brands-strip {{
      background: #fff;
      padding: 14px 16px;
      margin: 20px 0;
      border-top: 1px solid var(--slate-200);
      border-bottom: 1px solid var(--slate-200);
      display: flex;
      justify-content: space-around;
      align-items: center;
    }}
    .m-brand-logo-text {{
      font-size: 13px;
      font-weight: 900;
      color: #475569;
      letter-spacing: 0.5px;
    }}

    /* Value Proposition Mobile */
    .m-value-strip {{
      background: #0f172a;
      color: #fff;
      padding: 20px 16px;
      margin: 16px 14px;
      border-radius: 14px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .m-value-point {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .m-value-icon {{
      width: 28px;
      height: 28px;
      background: rgba(0, 153, 229, 0.2);
      color: var(--cyan-400);
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 12px;
      flex-shrink: 0;
    }}
    .m-value-text h5 {{
      font-size: 13px;
      font-weight: 800;
      margin-bottom: 2px;
    }}
    .m-value-text p {{
      font-size: 11px;
      color: #94a3b8;
      line-height: 1.4;
    }}

    /* Mobile Footer */
    .m-footer {{
      background: var(--navy-950);
      color: var(--slate-400);
      padding: 24px 16px 36px;
      text-align: center;
      border-top: 1px solid #1e293b;
      font-size: 12px;
    }}
    .m-footer-call {{
      background: var(--navy-900);
      border: 1px solid var(--navy-700);
      border-radius: 10px;
      padding: 12px;
      margin: 12px 0 16px;
    }}
  </style>
</head>
<body>

  {get_mobile_header(active_nav="home")}

  <!-- Categories Horizontal Scroller -->
  <div class="m-cats-scroller">
    <a href="#" class="m-cat-tag active">الكل</a>
    <a href="#" class="m-cat-tag">سويتشات الشبكات</a>
    <a href="#" class="m-cat-tag">راوترات وسيرفرات</a>
    <a href="#" class="m-cat-tag">جدران الحماية Firewalls</a>
    <a href="#" class="m-cat-tag">أكسس بوينت وواي فاي</a>
    <a href="#" class="m-cat-tag">راكات وكبائن</a>
    <a href="#" class="m-cat-tag">مغذيات UPS</a>
  </div>

  <!-- Hero Card Mobile -->
  <div class="m-hero-card">
    <div class="m-hero-badge">
      <span>●</span>
      الموزع المعتمد لحلول الشبكات والأمان
    </div>
    <h1 class="m-hero-title">
      تجهيز البنية التحتية والشبكات<br>
      بأعلى معايير <span>Enterprise المعتمدة</span>
    </h1>
    <p class="m-hero-desc">
      نوفر سويتشات وراوترات وفايروول لأكبر الماركات (Cisco, Fortinet, MikroTik, Ubiquiti) مع الدفع كاش عند الاستلام (COD) وضمان استبدال معتمد.
    </p>
    <div class="m-hero-btn-row">
      <a href="#" class="m-btn-hero-primary">تصفح السويتشات</a>
      <a href="#" class="m-btn-hero-rfq">طلب عرض أسعار (RFQ)</a>
    </div>
  </div>

  <!-- Weekly Deals Section with Countdown -->
  <div class="m-deal-section">
    <div class="m-deal-header-bar">
      <div class="m-deal-title">
        <span style="color:#f59e0b;">⚡</span>
        عروض التوريد الأسبوعية
      </div>
      <div class="m-deal-timer-chips">
        <span class="m-timer-chip">02d</span>
        <span class="m-timer-chip">14h</span>
        <span class="m-timer-chip">28m</span>
        <span class="m-timer-chip">45s</span>
      </div>
    </div>
    <div class="m-deal-body">
      <div class="m-deal-img-box">
        {SVG_CISCO_SWITCH}
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
        <span style="font-size:11px; font-weight:800; color:var(--cyan-600);">CISCO SYSTEMS</span>
        <span class="mono" style="font-size:11px; font-weight:700; background:#f1f5f9; padding:1px 6px; border-radius:4px;">WS-C2960X-24TD-L</span>
      </div>
      <h3 class="m-deal-name">سويتش سيسكو كاتاليست 24 بورت جيجابت PoE+ مع 2x 10G SFP+</h3>
      <div class="m-deal-progress">
        <div class="m-deal-progress-text">
          <span>تم حجز 74% من الكمية المخصصة</span>
          <span style="color:#ef4444;">متبقي 5 قطع</span>
        </div>
        <div class="m-progress-bar-track">
          <div class="m-progress-bar-fill" style="width:74%;"></div>
        </div>
      </div>
      <div class="m-deal-footer-row">
        <div>
          <div class="m-price-current">19,850 <small style="font-size:12px; color:#64748b;">ج.م</small></div>
          <div class="m-price-old">23,200 ج.م</div>
        </div>
        <button class="m-btn-add-cart">طلب بالدفع COD</button>
      </div>
    </div>
  </div>

  <!-- Brand Strip -->
  <div class="m-brands-strip">
    <span class="m-brand-logo-text" style="color:#0284c7;">CISCO</span>
    <span class="m-brand-logo-text" style="color:#ef4444;">FORTINET</span>
    <span class="m-brand-logo-text" style="color:#0f172a;">MIKROTIK</span>
    <span class="m-brand-logo-text" style="color:#0099e5;">UBIQUITI</span>
  </div>

  <!-- Best Sellers Section -->
  <div class="m-section-head">
    <h2 class="m-section-title">الأكثر طلباً وتوريداً للمشروعات</h2>
    <a href="#" class="m-section-more">عرض الكل ←</a>
  </div>

  <div class="m-products-list">
    <!-- Item 1: MikroTik -->
    <div class="m-item-card-row">
      <div class="m-item-thumb">{SVG_MIKROTIK}</div>
      <div class="m-item-details">
        <div class="m-item-brand" style="color:#0f172a;">MikroTik</div>
        <div class="m-item-model">CRS328-24P-4S+RM</div>
        <div class="m-item-name">سويتش مايكروتك 24 بورت PoE ذكي 500W مع 4 منافذ 10G SFP+</div>
        <div class="m-item-specs-strip">
          <span class="m-spec-tag">24 PoE</span>
          <span class="m-spec-tag">4x 10G</span>
          <span class="m-spec-tag">RouterOS</span>
        </div>
        <div class="m-item-bottom-row">
          <span class="m-item-price">22,400 ج.م</span>
          <button class="m-btn-mini-add">أضف للسلة</button>
        </div>
      </div>
    </div>

    <!-- Item 2: Fortinet -->
    <div class="m-item-card-row">
      <div class="m-item-thumb">{SVG_FORTINET}</div>
      <div class="m-item-details">
        <div class="m-item-brand" style="color:#ef4444;">Fortinet</div>
        <div class="m-item-model">FortiGate FG-60F</div>
        <div class="m-item-name">جدار حماية فورتينت 60F للأمن السيبراني والشبكات المشتركة</div>
        <div class="m-item-specs-strip">
          <span class="m-spec-tag">10G Firewall</span>
          <span class="m-spec-tag">Dual WAN</span>
          <span class="m-spec-tag">SD-WAN</span>
        </div>
        <div class="m-item-bottom-row">
          <span class="m-item-price">28,900 ج.م</span>
          <button class="m-btn-mini-add">أضف للسلة</button>
        </div>
      </div>
    </div>

    <!-- Item 3: UniFi AP -->
    <div class="m-item-card-row">
      <div class="m-item-thumb">{SVG_UBIQUITI_AP}</div>
      <div class="m-item-details">
        <div class="m-item-brand" style="color:#0099e5;">Ubiquiti UniFi</div>
        <div class="m-item-model">U6-PRO</div>
        <div class="m-item-name">أكسس بوينت يوني فاي واي فاي 6 احترافي للشركات والمشروعات</div>
        <div class="m-item-specs-strip">
          <span class="m-spec-tag">Wi-Fi 6</span>
          <span class="m-spec-tag">5.3 Gbps</span>
          <span class="m-spec-tag">PoE Powered</span>
        </div>
        <div class="m-item-bottom-row">
          <span class="m-item-price">8,700 ج.م</span>
          <button class="m-btn-mini-add">أضف للسلة</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Value Props Mobile -->
  <div class="m-value-strip">
    <div class="m-value-point">
      <div class="m-value-icon">✓</div>
      <div class="m-value-text">
        <h5>الدفع كاش عند الاستلام (COD) فقط</h5>
        <p>معاينة الأجهزة وسريالات الموديلات والفاتورة الضريبية مع المندوب قبل السداد.</p>
      </div>
    </div>
    <div class="m-value-point">
      <div class="m-value-icon">PDF</div>
      <div class="m-value-text">
        <h5>داتاشيت معتمدة لكل جهاز</h5>
        <p>مواصفات فنية دقيقة وقابلة للتحميل من صفحة كل موديل بضغطة واحدة.</p>
      </div>
    </div>
    <div class="m-value-point">
      <div class="m-value-icon">⚡</div>
      <div class="m-value-text">
        <h5>استلام فوري من الفرع مجاناً</h5>
        <p>مقر الشركة في المعادي / القاهرة متاح للاستلام المباشر والمعاينة الفورية.</p>
      </div>
    </div>
  </div>

  <!-- Mobile Footer -->
  <footer class="m-footer">
    <img src="assets/logo_white.png" style="height:28px; margin-bottom:10px;" alt="MESS TECH">
    <p style="line-height:1.6; margin-bottom:12px;">شركة MESS TECH المتخصصة في حلول الشبكات والبنية التحتية وأمن المعلومات للشركات والمشروعات.</p>
    
    <div class="m-footer-call">
      <div style="font-size:11px; color:#94a3b8;">للتواصل المباشر مع مهندسي المبيعات:</div>
      <div class="mono" style="font-size:16px; font-weight:800; color:var(--cyan-400); margin:4px 0;">+20 100 234 5678</div>
    </div>

    <div style="font-size:11px; color:#64748b;">جميع الحقوق محفوظة © 2026 MESS TECH</div>
  </footer>

  {get_mobile_bottom_nav(active="home")}

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "mobile_page_01_homepage.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png")
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=430,2250",
    "--force-device-scale-factor=2.0",
    "--virtual-time-budget=3000",
    f"--screenshot={png_path}",
    f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
]
subprocess.run(cmd, check=True)
print(f"Rendered: {png_path} ({os.path.getsize(png_path)/1024:.1f} KB)")

