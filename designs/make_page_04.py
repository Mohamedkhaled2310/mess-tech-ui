# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS, get_header_html, get_footer_html
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP

DESIGNS_DIR = r"E:\mess\designs"

HTML_CONTENT = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | مقارنة المواصفات الفنية لـ 4 موديلات سويتشات معتمدة</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    .breadcrumb-bar {{
      max-width: 1340px;
      margin: 18px auto 0;
      padding: 0 48px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      color: var(--slate-500);
    }}
    .breadcrumb-bar a {{ color: var(--slate-500); text-decoration: none; }}

    /* Comparison Page Container */
    .compare-container {{
      max-width: 1340px;
      margin: 24px auto 0;
      padding: 0 48px;
    }}
    .compare-header-box {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 24px 28px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }}
    .compare-title-wrap h1 {{
      font-size: 24px;
      font-weight: 900;
      color: var(--navy-900);
    }}
    .compare-title-wrap p {{
      font-size: 13.5px;
      color: #64748b;
      margin-top: 4px;
    }}
    .compare-toggle-control {{
      display: flex;
      align-items: center;
      gap: 12px;
      background: #f1f5f9;
      padding: 8px 16px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 700;
      color: var(--navy-900);
    }}

    /* Comparison Matrix Table */
    .matrix-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
    }}
    .matrix-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: right;
    }}
    .matrix-table th.col-feature {{
      width: 20%;
      background: #f8fafc;
      padding: 18px 20px;
      font-size: 13.5px;
      font-weight: 800;
      color: var(--navy-900);
      border-bottom: 1px solid var(--slate-200);
      border-left: 1px solid var(--slate-200);
    }}
    .matrix-table th.col-prod {{
      width: 20%;
      background: #fff;
      padding: 20px 16px;
      text-align: center;
      border-bottom: 2px solid var(--slate-200);
      border-left: 1px solid var(--slate-200);
      vertical-align: top;
    }}
    .matrix-table th.col-prod:last-child {{ border-left: none; }}
    .prod-thumb-box {{
      height: 90px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #f8fafc;
      border-radius: 8px;
      padding: 8px;
      margin-bottom: 12px;
    }}
    .prod-brand-pill {{
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 4px;
    }}
    .prod-model-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 800;
      color: var(--navy-900);
      margin-bottom: 8px;
      display: block;
    }}
    .prod-price-tag {{
      font-size: 18px;
      font-weight: 900;
      color: var(--navy-900);
      margin-bottom: 12px;
    }}
    .btn-matrix-add {{
      width: 100%;
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      white-space: nowrap;
      flex-shrink: 0;
    }}

    /* Table Rows */
    .row-category-header td {{
      background: var(--navy-900);
      color: #fff;
      font-size: 13.5px;
      font-weight: 800;
      padding: 10px 20px;
      letter-spacing: 0.5px;
    }}
    .matrix-table td {{
      padding: 14px 18px;
      font-size: 13px;
      color: #334155;
      border-bottom: 1px solid var(--slate-200);
      border-left: 1px solid var(--slate-200);
      vertical-align: middle;
    }}
    .matrix-table td:last-child {{ border-left: none; }}
    .matrix-table td.cell-label {{
      background: #f8fafc;
      font-weight: 700;
      color: var(--navy-900);
    }}
    .diff-highlight {{
      background: rgba(0, 153, 229, 0.05);
      font-weight: 700;
      color: var(--navy-900);
    }}
    .badge-diff-best {{
      background: #ecfdf5;
      color: #059669;
      border: 1px solid #a7f3d0;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 800;
      margin-top: 4px;
      display: inline-block;
    }}
  </style>
</head>
<body>

  {get_header_html(active_cat="switches")}

  <!-- Breadcrumbs -->
  <div class="breadcrumb-bar">
    <a href="#">الرئيسية</a>
    <span>›</span>
    <a href="#">سويتشات الشبكات</a>
    <span>›</span>
    <span class="breadcrumb-current">مقارنة المواصفات الفنية لـ 4 موديلات جنب بعض</span>
  </div>

  <main class="compare-container">
    <div class="compare-header-box">
      <div class="compare-title-wrap">
        <h1>مقارنة المواصفات الفنية لـ 4 موديلات جنب بعض</h1>
        <p>مقارنة شاملة توضح الفروق الدقيقة في البورتات، سرعة الـ Uplink، طاقة الـ PoE، والأسعار لتسهيل اختيار الموديل المناسب للمشروع</p>
      </div>
      <div class="compare-toggle-control">
        <input type="checkbox" id="diffToggle" checked>
        <label for="diffToggle">تمييز الفروق في المواصفات (Highlight Differences)</label>
      </div>
    </div>

    <div class="matrix-card">
      <table class="matrix-table">
        <thead>
          <tr>
            <th class="col-feature">الموديل والماركة</th>

            <!-- Model 1 -->
            <th class="col-prod">
              <div class="prod-thumb-box">{SVG_CISCO_SWITCH}</div>
              <div class="prod-brand-pill" style="color:var(--cyan-600);">Cisco Systems</div>
              <span class="prod-model-num">WS-C2960X-24TD-L</span>
              <div class="prod-price-tag">19,850 <small style="font-size:12px; font-weight:600;">ج.م</small></div>
              <button class="btn-matrix-add">أضف للسلة</button>
            </th>

            <!-- Model 2 -->
            <th class="col-prod">
              <div class="prod-thumb-box">{SVG_MIKROTIK}</div>
              <div class="prod-brand-pill" style="color:var(--navy-900);">MikroTik</div>
              <span class="prod-model-num">CRS328-24P-4S+RM</span>
              <div class="prod-price-tag">22,400 <small style="font-size:12px; font-weight:600;">ج.م</small></div>
              <button class="btn-matrix-add">أضف للسلة</button>
            </th>

            <!-- Model 3 -->
            <th class="col-prod">
              <div class="prod-thumb-box">{SVG_CISCO_SWITCH}</div>
              <div class="prod-brand-pill" style="color:var(--cyan-500);">Ubiquiti UniFi</div>
              <span class="prod-model-num">USW-Pro-24-PoE</span>
              <div class="prod-price-tag">26,800 <small style="font-size:12px; font-weight:600;">ج.م</small></div>
              <button class="btn-matrix-add">أضف للسلة</button>
            </th>

            <!-- Model 4 -->
            <th class="col-prod">
              <div class="prod-thumb-box">{SVG_FORTINET}</div>
              <div class="prod-brand-pill" style="color:var(--rose-500);">Fortinet</div>
              <span class="prod-model-num">FS-124E-POE</span>
              <div class="prod-price-tag">21,500 <small style="font-size:12px; font-weight:600;">ج.م</small></div>
              <button class="btn-matrix-add">أضف للسلة</button>
            </th>
          </tr>
        </thead>
        <tbody>
          <!-- Category 1: Interfaces -->
          <tr class="row-category-header">
            <td colspan="5">1. المنافذ والسرعات (Network Interfaces)</td>
          </tr>
          <tr>
            <td class="cell-label">عدد منافذ Gigabit RJ45</td>
            <td>24 Port (10/100/1000)</td>
            <td>24 Port (10/100/1000)</td>
            <td>24 Port (10/100/1000)</td>
            <td>24 Port (10/100/1000)</td>
          </tr>
          <tr>
            <td class="cell-label">منافذ الـ Uplink عالية السرعة</td>
            <td class="diff-highlight">2 × 10G SFP+</td>
            <td class="diff-highlight">
              4 × 10G SFP+
              <br><span class="badge-diff-best">الأعلى (4 منافذ 10G)</span>
            </td>
            <td class="diff-highlight">2 × 10G SFP+</td>
            <td class="diff-highlight">4 × 1G SFP فقط</td>
          </tr>
          <tr>
            <td class="cell-label">منفذ الإدارة والكونسول (Console)</td>
            <td>RJ45 + USB Type-B</td>
            <td>RJ45 Serial Console</td>
            <td>إدارة سحابية UniFi Controller</td>
            <td>RJ45 Serial Management</td>
          </tr>

          <!-- Category 2: PoE Power -->
          <tr class="row-category-header">
            <td colspan="5">2. طاقة التغذية عبر الشبكة (PoE Power & Budget)</td>
          </tr>
          <tr>
            <td class="cell-label">معيار الـ PoE المدعوم</td>
            <td>802.3af (PoE) / 802.3at (PoE+)</td>
            <td>Passive PoE / 802.3af / 802.3at</td>
            <td class="diff-highlight">
              PoE+ & PoE++ (802.3bt)
              <br><span class="badge-diff-best">يدعم PoE++ حتى 60W</span>
            </td>
            <td>802.3af / 802.3at (PoE+)</td>
          </tr>
          <tr>
            <td class="cell-label">إجمالي ميزانية الـ PoE (Budget)</td>
            <td class="diff-highlight">370W</td>
            <td class="diff-highlight">
              500W Dual Internal PSU
              <br><span class="badge-diff-best">أعلى طاقة 500 وات</span>
            </td>
            <td class="diff-highlight">400W</td>
            <td class="diff-highlight">180W</td>
          </tr>

          <!-- Category 3: Performance -->
          <tr class="row-category-header">
            <td colspan="5">3. الأداء والمعالجة (Switching & Layer Performance)</td>
          </tr>
          <tr>
            <td class="cell-label">سعة التبديل (Switching Capacity)</td>
            <td class="diff-highlight">
              216 Gbps
              <br><span class="badge-diff-best">الأسرع معمارياً</span>
            </td>
            <td class="diff-highlight">128 Gbps</td>
            <td class="diff-highlight">88 Gbps</td>
            <td class="diff-highlight">56 Gbps</td>
          </tr>
          <tr>
            <td class="cell-label">معدل تمرير الحزم (Forwarding Rate)</td>
            <td class="diff-highlight">95.2 Mpps</td>
            <td class="diff-highlight">95.2 Mpps</td>
            <td class="diff-highlight">65.5 Mpps</td>
            <td class="diff-highlight">41.6 Mpps</td>
          </tr>
          <tr>
            <td class="cell-label">طبقة التشغيل ونظام الإدارة</td>
            <td>Layer 2 + Layer 3 Lite (Cisco IOS)</td>
            <td>RouterOS Level 5 / SwOS Dual Boot</td>
            <td>Full Layer 3 (UniFi Network)</td>
            <td>Layer 2 / FortiLink Management</td>
          </tr>

          <!-- Category 4: Specs & Datasheet -->
          <tr class="row-category-header">
            <td colspan="5">4. الداتاشيت والمواصفات الفنية المعتمدة</td>
          </tr>
          <tr>
            <td class="cell-label">تحميل الداتاشيت الرسمية</td>
            <td><a href="#" style="color:var(--cyan-600); font-weight:700;">تحميل Datasheet PDF</a></td>
            <td><a href="#" style="color:var(--cyan-600); font-weight:700;">تحميل Datasheet PDF</a></td>
            <td><a href="#" style="color:var(--cyan-600); font-weight:700;">تحميل Datasheet PDF</a></td>
            <td><a href="#" style="color:var(--cyan-600); font-weight:700;">تحميل Datasheet PDF</a></td>
          </tr>
          <tr>
            <td class="cell-label">حالة التوريد والاعتماد</td>
            <td>أصلي جديد بالكرتونة (Sealed)</td>
            <td>أصلي جديد بالكرتونة (Sealed)</td>
            <td>أصلي جديد بالكرتونة (Sealed)</td>
            <td>أصلي جديد بالكرتونة (Sealed)</td>
          </tr>
          <tr>
            <td class="cell-label">حالة التوفر والتسليم</td>
            <td colspan="4" style="background:#f0fdf4; color:#166534; font-weight:700; text-align:center;">
              ✓ متوفر تسليم فوري من المخازن الرئيسية لكافة الموديلات مع إمكانية المعاينة وفحص السيريال
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>

  {get_footer_html()}

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "page_04_product_comparison.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "04_صفحة_مقارنة_المواصفات_Desktop_Product_Comparison.png")
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,2200",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=3000",
    f"--screenshot={png_path}",
    f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
]
subprocess.run(cmd, check=True)
print(f"Rendered: {png_path} ({os.path.getsize(png_path)/1024:.1f} KB)")

