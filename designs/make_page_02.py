# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS, get_header_html, get_footer_html
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_UBIQUITI_AP

DESIGNS_DIR = r"E:\mess\designs"

HTML_CONTENT = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | سويتش سيسكو كاتاليست WS-C2960X-24TD-L Gigabit PoE+</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    /* Breadcrumbs */
    .breadcrumb-bar {{
      max-width: 1340px;
      margin: 18px auto 0;
      padding: 0 48px;
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      color: var(--slate-500);
    }}
    .breadcrumb-bar a {{ color: var(--slate-500); text-decoration: none; }}
    .breadcrumb-bar a:hover {{ color: var(--cyan-600); }}
    .breadcrumb-separator {{ color: #cbd5e1; }}
    .breadcrumb-current {{ color: var(--navy-900); font-weight: 700; }}

    /* Product Main Layout */
    .product-detail-container {{
      max-width: 1340px;
      margin: 24px auto 0;
      padding: 0 48px;
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 40px;
      align-items: start;
    }}

    /* Gallery (Right Side in RTL) */
    .gallery-column {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 2px 12px rgba(0,0,0,0.03);
    }}
    .main-image-display {{
      height: 320px;
      background: #f8fafc;
      border: 1px solid var(--slate-100);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      position: relative;
    }}
    .gallery-badge-zoom {{
      position: absolute;
      bottom: 12px;
      left: 12px;
      background: rgba(15, 23, 42, 0.7);
      color: #fff;
      font-size: 11.5px;
      padding: 4px 10px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .thumbnails-strip {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      margin-top: 16px;
    }}
    .thumb-item {{
      height: 74px;
      border: 2px solid var(--slate-200);
      border-radius: 8px;
      padding: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #f8fafc;
    }}
    .thumb-item.active {{
      border-color: var(--cyan-500);
      background: #f0f9ff;
    }}

    /* Datasheet Download Box */
    .datasheet-callout-box {{
      margin-top: 20px;
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      border: 1px solid #334155;
      border-radius: 12px;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #fff;
    }}
    .datasheet-info {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .datasheet-icon-wrap {{
      width: 44px;
      height: 44px;
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.3);
      color: #ef4444;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 900;
      font-size: 14px;
    }}
    .btn-download-ds {{
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 9px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      text-decoration: none;
    }}

    /* Info Column (Left Side in RTL) */
    .info-column {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .product-meta-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 6px;
    }}
    .brand-badge-pill {{
      background: #e0f2fe;
      color: var(--cyan-600);
      font-size: 12px;
      font-weight: 800;
      padding: 3px 12px;
      border-radius: 6px;
      text-transform: uppercase;
    }}
    .model-sku-badge {{
      background: #f1f5f9;
      color: #334155;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 6px;
      border: 1px solid #cbd5e1;
    }}
    .product-page-title {{
      font-size: 26px;
      font-weight: 900;
      color: var(--navy-900);
      line-height: 1.35;
    }}
    .rating-row {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 13px;
      color: #64748b;
    }}
    .stars-gold {{ color: #f59e0b; font-size: 14px; }}

    /* Pricing & Availability Card */
    .price-action-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
    }}
    .price-main-display {{
      display: flex;
      align-items: baseline;
      gap: 14px;
      margin-bottom: 12px;
    }}
    .price-val-big {{
      font-size: 32px;
      font-weight: 900;
      color: var(--navy-900);
    }}
    .price-val-strike {{
      font-size: 17px;
      color: #94a3b8;
      text-decoration: line-through;
    }}
    .save-badge {{
      background: #fef2f2;
      color: #ef4444;
      border: 1px solid #fecaca;
      font-size: 12px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 6px;
    }}
    .stock-status-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #ecfdf5;
      color: #059669;
      border: 1px solid #a7f3d0;
      padding: 5px 14px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 18px;
    }}

    /* COD Callout Banner inside Product Card */
    .cod-reassurance-box {{
      background: #f0fdf4;
      border: 1px solid #86efac;
      border-radius: 10px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      color: #14532d;
      font-size: 13px;
    }}

    /* Key Specs Matrix */
    .key-specs-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 22px;
    }}
    .key-spec-cell {{
      background: #f8fafc;
      border: 1px solid var(--slate-200);
      border-radius: 8px;
      padding: 10px;
    }}
    .key-spec-label {{
      font-size: 11.5px;
      color: #64748b;
      margin-bottom: 2px;
    }}
    .key-spec-val {{
      font-size: 13px;
      font-weight: 800;
      color: var(--navy-900);
      font-family: 'JetBrains Mono', sans-serif;
    }}

    /* Actions buttons */
    .cta-buttons-block {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .action-row-main {{
      display: flex;
      gap: 12px;
      align-items: center;
    }}
    .qty-picker {{
      display: flex;
      align-items: center;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 10px;
      padding: 4px;
    }}
    .qty-btn {{
      width: 38px;
      height: 38px;
      background: #fff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      font-size: 16px;
      font-weight: 700;
      cursor: pointer;
    }}
    .qty-display {{
      width: 44px;
      text-align: center;
      font-size: 15px;
      font-weight: 800;
    }}
    .btn-add-cart-primary {{
      flex: 1;
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 13px 24px;
      border-radius: 10px;
      font-size: 15px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(0, 153, 229, 0.3);
    }}
    .btn-whatsapp-direct {{
      background: #22c55e;
      color: #fff;
      border: none;
      padding: 13px 20px;
      border-radius: 10px;
      font-size: 14.5px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(34, 197, 94, 0.25);
    }}
    .btn-compare-action {{
      background: #f8fafc;
      border: 1px solid var(--slate-200);
      color: #334155;
      padding: 11px 18px;
      border-radius: 10px;
      font-size: 13.5px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      cursor: pointer;
    }}

    /* Tabs & Full Specs Table */
    .specs-tabs-container {{
      max-width: 1340px;
      margin: 48px auto 0;
      padding: 0 48px;
    }}
    .tabs-header-bar {{
      display: flex;
      gap: 8px;
      border-bottom: 2px solid var(--slate-200);
      margin-bottom: 24px;
    }}
    .tab-btn {{
      padding: 12px 24px;
      font-size: 15px;
      font-weight: 700;
      color: #64748b;
      border-bottom: 3px solid transparent;
      margin-bottom: -2px;
      text-decoration: none;
    }}
    .tab-btn.active {{
      color: var(--cyan-600);
      border-bottom-color: var(--cyan-600);
    }}
    .specs-table-box {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }}
    .specs-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: right;
    }}
    .specs-table th {{
      background: #f8fafc;
      padding: 14px 20px;
      font-size: 13.5px;
      font-weight: 800;
      color: var(--navy-900);
      border-bottom: 1px solid var(--slate-200);
      width: 28%;
    }}
    .specs-table td {{
      padding: 14px 20px;
      font-size: 13.5px;
      color: #334155;
      border-bottom: 1px solid var(--slate-100);
    }}
    .specs-table tr:hover td {{ background: #fafafa; }}

    /* Frequently Bought Together */
    .bundle-section {{
      max-width: 1340px;
      margin: 48px auto 0;
      padding: 0 48px;
    }}
    .bundle-box {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 28px;
      display: grid;
      grid-template-columns: 2.2fr 1fr;
      gap: 32px;
      align-items: center;
    }}
    .bundle-items-row {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .bundle-card-mini {{
      flex: 1;
      border: 1px solid var(--slate-200);
      border-radius: 10px;
      padding: 12px;
      background: #f8fafc;
    }}
    .bundle-plus-icon {{
      font-size: 20px;
      font-weight: 800;
      color: var(--slate-400);
    }}
    .bundle-pricing-summary {{
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      border-radius: 12px;
      padding: 20px;
      text-align: center;
    }}
  </style>
</head>
<body>

  {get_header_html(active_cat="switches")}

  <!-- Breadcrumbs -->
  <div class="breadcrumb-bar">
    <a href="#">الرئيسية</a>
    <span class="breadcrumb-separator">/</span>
    <a href="#">سويتشات الشبكات</a>
    <span class="breadcrumb-separator">/</span>
    <a href="#">Cisco Systems</a>
    <span class="breadcrumb-separator">/</span>
    <a href="#">Catalyst 2960-X Series</a>
    <span class="breadcrumb-separator">/</span>
    <span class="breadcrumb-current">WS-C2960X-24TD-L Gigabit PoE+</span>
  </div>

  <!-- Product Detail Core Section -->
  <main class="product-detail-container">

    <!-- Gallery Column -->
    <div class="gallery-column">
      <div class="main-image-display">
        {SVG_CISCO_SWITCH}
        <div class="gallery-badge-zoom">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
          معاينة دقيقة للمنافذ والبوردة
        </div>
      </div>

      <div class="thumbnails-strip">
        <div class="thumb-item active" title="الواجهة الأمامية والمنافذ">
          <span style="font-size:11px; font-weight:700; color:var(--cyan-600);">واجهة البورتات</span>
        </div>
        <div class="thumb-item" title="منافذ 10G SFP+">
          <span style="font-size:11px; font-weight:700; color:#64748b;">منافذ 10G Uplink</span>
        </div>
        <div class="thumb-item" title="الواجهة الخلفية ومروحة التبريد">
          <span style="font-size:11px; font-weight:700; color:#64748b;">الباور الخلفي</span>
        </div>
        <div class="thumb-item" title="أذان التثبيت بالراك Rackmount">
          <span style="font-size:11px; font-weight:700; color:#64748b;">طقم Rack 1U</span>
        </div>
      </div>

      <!-- Datasheet Download Callout -->
      <div class="datasheet-callout-box">
        <div class="datasheet-info">
          <div class="datasheet-icon-wrap">PDF</div>
          <div>
            <div style="font-size:14px; font-weight:800;">الداتاشيت الرسمية (Official Datasheet)</div>
            <div style="font-size:12px; color:#94a3b8;">ملف المواصفات الفنية المعتمد من سيسكو • 3.4 MB</div>
          </div>
        </div>
        <a href="#" class="btn-download-ds">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          تحميل الملف
        </a>
      </div>
    </div>

    <!-- Product Info Column -->
    <div class="info-column">
      <div>
        <div class="product-meta-header">
          <span class="brand-badge-pill">Cisco Systems</span>
          <span class="model-sku-badge">MODEL: WS-C2960X-24TD-L</span>
          <span class="model-sku-badge" style="background:#fff;">SKU: MESS-SW-CIS-2960X</span>
        </div>
        <h1 class="product-page-title">
          سويتش سيسكو كاتاليست 24 بورت جيجابت PoE+ مع منفذين 10G SFP+ فئة المؤسسات
        </h1>
        <div class="rating-row" style="margin-top:8px;">
          <span class="stars-gold">★★★★★</span>
          <span style="font-weight:700; color:var(--navy-900);">5.0</span>
          <span>(24 تقييم مهندسي شبكات ومشروعات)</span>
          <span>•</span>
          <span style="color:#10b981; font-weight:700;">أصلي 100% معتمد</span>
        </div>
      </div>

      <!-- Pricing & Actions Card -->
      <div class="price-action-card">
        <div class="price-main-display">
          <div class="price-val-big">19,850 <small style="font-size:16px; color:#64748b;">ج.م</small></div>
          <div class="price-val-strike">23,200 ج.م</div>
          <span class="save-badge">وفر 3,350 ج.م (-14%)</span>
        </div>

        <div style="display:flex; gap:12px; align-items:center; margin-bottom:14px;">
          <span class="stock-status-pill">
            <span style="width:8px; height:8px; background:#10b981; border-radius:999px;"></span>
            متوفر فوراً بالمخزون (متبقي 6 قطع في فرع القاهرة)
          </span>
          <span style="font-size:12px; color:#64748b;">أو خيار "اطلب للتوريد" للكميات الكبيرة</span>
        </div>

        <!-- Key Specs Matrix -->
        <div class="key-specs-grid">
          <div class="key-spec-cell">
            <div class="key-spec-label">المنافذ (Ports)</div>
            <div class="key-spec-val">24x 1GbE RJ45</div>
          </div>
          <div class="key-spec-cell">
            <div class="key-spec-label">منافذ الـ Uplink</div>
            <div class="key-spec-val">2x 10G SFP+</div>
          </div>
          <div class="key-spec-cell">
            <div class="key-spec-label">طاقة الـ PoE</div>
            <div class="key-spec-val">370W PoE+</div>
          </div>
          <div class="key-spec-cell">
            <div class="key-spec-label">سعة التبديل</div>
            <div class="key-spec-val">216 Gbps</div>
          </div>
          <div class="key-spec-cell">
            <div class="key-spec-label">الطبقة (Layer)</div>
            <div class="key-spec-val">Layer 2 / 3 Lite</div>
          </div>
          <div class="key-spec-cell">
            <div class="key-spec-label">المقاس القياسي</div>
            <div class="key-spec-val">1U Rackmount</div>
          </div>
        </div>

        <!-- Call to Actions -->
        <div class="cta-buttons-block">
          <div class="action-row-main">
            <div class="qty-picker">
              <button class="qty-btn">-</button>
              <div class="qty-display">1</div>
              <button class="qty-btn">+</button>
            </div>
            <button class="btn-add-cart-primary" style="white-space:nowrap; display:inline-flex; align-items:center; justify-content:center; gap:8px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
              أضف للسلة
            </button>
          </div>

          <!-- Direct WhatsApp Button (No Business API) -->
          <a href="https://wa.me/201000000000?text=استفسار%20عن%20سويتش%20سيسكو%20WS-C2960X-24TD-L" class="btn-whatsapp-direct" style="white-space:nowrap; display:inline-flex;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.592 2.654-.696c1.029.575 1.748.817 2.806.817 3.181 0 5.767-2.587 5.768-5.766.001-3.182-2.585-5.768-5.768-5.768zm0 10.37c-.894 0-1.67-.238-2.427-.69l-.174-.103-1.802.472.48-1.758-.113-.181c-.504-.805-.77-1.524-.769-2.544 0-2.535 2.062-4.597 4.597-4.597 2.536 0 4.598 2.063 4.598 4.598 0 2.535-2.063 4.597-4.597 4.597z"/></svg>
            <span>تواصل مع مهندس المبيعات عبر واتساب (استفسار فوري عن الموديل)</span>
          </a>

          <div style="display:flex; gap:12px;">
            <button class="btn-compare-action" style="flex:1; white-space:nowrap; display:inline-flex;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
              إضافة إلى جدول المقارنة (Compare)
            </button>
            <button class="btn-compare-action" style="flex:1; white-space:nowrap; display:inline-flex;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
              حفظ في قائمة المفضلة
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>

  <!-- Detailed Technical Specifications Table -->
  <section class="specs-tabs-container">
    <div class="tabs-header-bar">
      <a href="#" class="tab-btn active">المواصفات الفنية التفصيلية (Datasheet Specs)</a>
      <a href="#" class="tab-btn">نظرة عامة والبروتوكولات المدعومة</a>
      <a href="#" class="tab-btn">الضمان وشروط الشحن والتوريد</a>
      <a href="#" class="tab-btn">تقييمات مهندسي المشروعات (24)</a>
    </div>

    <div class="specs-table-box">
      <table class="specs-table">
        <tbody>
          <tr>
            <th>الموديل ورقم القطعة (Part Number)</th>
            <td><b class="mono">WS-C2960X-24TD-L</b> (Cisco Catalyst 2960-X Series)</td>
          </tr>
          <tr>
            <th>إجمالي منافذ الشبكة (Total Network Ports)</th>
            <td>24 × 10/100/1000 Gigabit Ethernet RJ45 مع مؤشرات LED للحالة والسرعة</td>
          </tr>
          <tr>
            <th>منافذ الـ Uplink عالية السرعة</th>
            <td>2 × 10 Gigabit Ethernet SFP+ (متوافقة أيضاً مع وحدات 1G SFP)</td>
          </tr>
          <tr>
            <th>طاقة وتوزيع PoE (Power over Ethernet)</th>
            <td>إجمالي ميزانية <b>370W</b> تدعم معيار 802.3at (PoE+ حتى 30W للبورت) و 802.3af</td>
          </tr>
          <tr>
            <th>سعة تحويل البيانات (Switching Bandwidth)</th>
            <td><b>216 Gbps</b> (Forwarding Bandwidth: 108 Gbps)</td>
          </tr>
          <tr>
            <th>معدل تمرير الحزم (Forwarding Rate)</th>
            <td><b>95.2 Mpps</b> (مليون حزمة في الثانية - 64-byte L3 packets)</td>
          </tr>
          <tr>
            <th>مستوى الإدارة ودعم الطبقات (Layer Support)</th>
            <td>Enterprise Layer 2 مع دعم Layer 3 Lite (Static Routing, RIPv1/v2, PBR)</td>
          </tr>
          <tr>
            <th>الذاكرة والمعالج الداخلي (CPU & Memory)</th>
            <td>APM86392 600MHz Dual Core, 512 MB DRAM, 128 MB Flash Memory</td>
          </tr>
          <tr>
            <th>الأبعاد والوزن ومقاس الراك (Form Factor)</th>
            <td>1U Rackmount قياسي (4.5 × 44.5 × 36.8 سم) • الوزن: 5.8 كجم • طقم Rack Ears متضمن</td>
          </tr>
          <tr>
            <th>الضمان المحلي والدعم الفني</th>
            <td>أجهزة أصلية معتمدة من الوكيل الرسمي مع دعم فني هندسي مخصص لتشغيل وضبط الشبكات</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- Frequently Bought Together Bundle -->
  <section class="bundle-section">
    <div class="section-head" style="margin-bottom:16px;">
      <h3 style="font-size:20px; font-weight:800; color:var(--navy-900);">منتجات متوافقة بتتشترى مع السويتش دائماً</h3>
    </div>
    <div class="bundle-box">
      <div class="bundle-items-row">
        <div class="bundle-card-mini" style="border-color:var(--cyan-500);">
          <div style="font-size:11px; color:var(--cyan-600); font-weight:800;">السويتش الأساسي</div>
          <div style="font-size:13px; font-weight:700; margin:4px 0;">Cisco Catalyst 24 Port</div>
          <div style="font-size:14px; font-weight:900; color:var(--navy-900);">19,850 ج.م</div>
        </div>
        <div class="bundle-plus-icon">+</div>
        <div class="bundle-card-mini">
          <div style="font-size:11px; color:#64748b; font-weight:700;">كابلات توصيل</div>
          <div style="font-size:13px; font-weight:700; margin:4px 0;">24x باتش كورد Cat6 أصلي</div>
          <div style="font-size:14px; font-weight:900; color:var(--navy-900);">1,450 ج.م</div>
        </div>
        <div class="bundle-plus-icon">+</div>
        <div class="bundle-card-mini">
          <div style="font-size:11px; color:#64748b; font-weight:700;">كابينة راك سيرفر</div>
          <div style="font-size:13px; font-weight:700; margin:4px 0;">راك جداري 9U مجهز بمراوح</div>
          <div style="font-size:14px; font-weight:900; color:var(--navy-900);">3,200 ج.م</div>
        </div>
      </div>
      <div class="bundle-pricing-summary">
        <div style="font-size:12px; color:#64748b;">إجمالي الباقة المجمعة (3 منتجات):</div>
        <div style="font-size:24px; font-weight:900; color:var(--navy-900); margin:4px 0;">23,900 <small style="font-size:14px;">ج.م</small></div>
        <button class="btn-add-cart-primary" style="width:100%; font-size:13.5px; padding:10px 16px; margin-top:8px; white-space:nowrap; display:inline-flex; justify-content:center; align-items:center; gap:8px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          أضف الباقة كاملة للسلة
        </button>
      </div>
    </div>
  </section>

  {get_footer_html()}

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "page_02_product_details.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "02_صفحة_المنتج_والمواصفات_Desktop_Product_Details.png")
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,2400",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=3000",
    f"--screenshot={png_path}",
    f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
]
subprocess.run(cmd, check=True)
print(f"Rendered: {png_path} ({os.path.getsize(png_path)/1024:.1f} KB)")

