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
  <title>MESS TECH | سويتشات الشبكات - فلاتر المواصفات الفنية والموديلات</title>
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
      gap: 10px;
      font-size: 13px;
      color: var(--slate-500);
    }}
    .breadcrumb-bar a {{ color: var(--slate-500); text-decoration: none; }}
    .breadcrumb-current {{ color: var(--navy-900); font-weight: 700; }}

    /* Catalog Layout */
    .catalog-container {{
      max-width: 1340px;
      margin: 24px auto 0;
      padding: 0 48px;
      display: grid;
      grid-template-columns: 290px 1fr;
      gap: 32px;
      align-items: start;
    }}

    /* Sidebar Filters */
    .filter-sidebar {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 20px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }}
    .filter-header-main {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--slate-200);
      margin-bottom: 18px;
    }}
    .filter-title {{
      font-size: 16px;
      font-weight: 800;
      color: var(--navy-900);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .btn-reset-filters {{
      font-size: 12px;
      color: var(--rose-500);
      background: none;
      border: none;
      font-weight: 700;
      cursor: pointer;
    }}
    .filter-group {{
      margin-bottom: 22px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--slate-100);
    }}
    .filter-group:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
    .filter-group-title {{
      font-size: 13.5px;
      font-weight: 800;
      color: var(--navy-900);
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .filter-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 9px;
    }}
    .filter-checkbox-label {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 13px;
      color: #334155;
      cursor: pointer;
    }}
    .filter-check-wrap {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .filter-count-badge {{
      font-size: 11px;
      color: #94a3b8;
      background: #f1f5f9;
      padding: 1px 6px;
      border-radius: 999px;
    }}
    .price-slider-preview {{
      display: flex;
      justify-content: space-between;
      font-size: 12.5px;
      font-weight: 700;
      color: var(--navy-900);
      margin-top: 8px;
    }}

    /* Main Products Area */
    .catalog-main-content {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .catalog-top-bar {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 12px;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .catalog-heading h1 {{
      font-size: 20px;
      font-weight: 900;
      color: var(--navy-900);
    }}
    .catalog-heading p {{
      font-size: 12.5px;
      color: #64748b;
      margin-top: 2px;
    }}
    .catalog-sort-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      color: #64748b;
    }}
    .sort-select {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 7px 12px;
      font-size: 13px;
      font-weight: 600;
      color: var(--navy-900);
      outline: none;
    }}

    /* Active Filter Chips */
    .active-chips-strip {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }}
    .chip-item {{
      background: #e0f2fe;
      color: var(--cyan-600);
      border: 1px solid #bae6fd;
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .chip-remove {{ cursor: pointer; color: #0284c7; font-weight: 800; }}

    /* Products Grid 2x3 */
    .catalog-products-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }}
    .cat-product-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.2s;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }}
    .cat-product-card:hover {{
      border-color: var(--cyan-500);
      box-shadow: 0 8px 20px rgba(0, 153, 229, 0.1);
      transform: translateY(-2px);
    }}
    .card-top-badges {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .badge-cod-mini {{
      background: rgba(16, 185, 129, 0.12);
      color: #059669;
      border: 1px solid rgba(16, 185, 129, 0.3);
      font-size: 10.5px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
    }}
    .badge-stock-dot {{
      display: flex;
      align-items: center;
      gap: 5px;
      font-size: 11px;
      font-weight: 700;
      color: #10b981;
    }}
    .dot-green {{ width: 6px; height: 6px; background: #10b981; border-radius: 999px; }}
    .cat-img-box {{
      height: 120px;
      background: #f8fafc;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px;
      margin-bottom: 12px;
    }}
    .cat-product-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--navy-900);
      line-height: 1.45;
      height: 42px;
      overflow: hidden;
      margin-bottom: 10px;
    }}
    .tech-badges-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      background: #f8fafc;
      border: 1px solid var(--slate-100);
      border-radius: 6px;
      padding: 8px;
      margin-bottom: 14px;
    }}
    .tech-badge-item {{
      font-size: 11px;
      color: #475569;
    }}
    .tech-badge-item b {{
      color: var(--navy-900);
      font-family: 'JetBrains Mono', sans-serif;
    }}
    .cat-card-footer {{
      margin-top: auto;
      padding-top: 12px;
      border-top: 1px solid var(--slate-100);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .cat-card-actions {{
      display: flex;
      gap: 6px;
    }}
    .btn-icon-compare {{
      width: 34px;
      height: 34px;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #475569;
      cursor: pointer;
    }}
    .btn-card-add-cart {{
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 8px 14px;
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
  </style>
</head>
<body>

  {get_header_html(active_cat="switches")}

  <!-- Breadcrumbs -->
  <div class="breadcrumb-bar">
    <a href="#">الرئيسية</a>
    <span>›</span>
    <a href="#">سويتشات الشبكات والبنية التحتية</a>
    <span>›</span>
    <span class="breadcrumb-current">بحث بالمواصفات والفلاتر التقنية (18 موديل)</span>
  </div>

  <main class="catalog-container">

    <!-- Filters Sidebar -->
    <aside class="filter-sidebar">
      <div class="filter-header-main">
        <div class="filter-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>
          فلاتر المواصفات
        </div>
        <button class="btn-reset-filters">إعادة ضبط</button>
      </div>

      <!-- Filter: Brand -->
      <div class="filter-group">
        <div class="filter-group-title">
          <span>الشركة المصنعة (Brand)</span>
        </div>
        <ul class="filter-list">
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox" checked>
              <b>Cisco Systems</b>
            </span>
            <span class="filter-count-badge">14</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>MikroTik RouterOS</span>
            </span>
            <span class="filter-count-badge">12</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>Ubiquiti UniFi</span>
            </span>
            <span class="filter-count-badge">9</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>Fortinet FortiSwitch</span>
            </span>
            <span class="filter-count-badge">8</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>Aruba Networks</span>
            </span>
            <span class="filter-count-badge">6</span>
          </li>
        </ul>
      </div>

      <!-- Filter: Ports Count -->
      <div class="filter-group">
        <div class="filter-group-title">
          <span>عدد منافذ الشبكة (Ports)</span>
        </div>
        <ul class="filter-list">
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox" checked>
              <b>24 Port Gigabit</b>
            </span>
            <span class="filter-count-badge">18</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>48 Port Gigabit</span>
            </span>
            <span class="filter-count-badge">12</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>16 Port GbE</span>
            </span>
            <span class="filter-count-badge">7</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>8 Port Desktop/Rack</span>
            </span>
            <span class="filter-count-badge">5</span>
          </li>
        </ul>
      </div>

      <!-- Filter: PoE Budget -->
      <div class="filter-group">
        <div class="filter-group-title">
          <span>تغذية الطاقة عبر الشبكة (PoE)</span>
        </div>
        <ul class="filter-list">
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox" checked>
              <b>PoE+ (802.3at حتى 370W)</b>
            </span>
            <span class="filter-count-badge">15</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>Ultra PoE++ (740W+)</span>
            </span>
            <span class="filter-count-badge">4</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>Standard PoE (180W)</span>
            </span>
            <span class="filter-count-badge">6</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>Non-PoE (Data Only)</span>
            </span>
            <span class="filter-count-badge">8</span>
          </li>
        </ul>
      </div>

      <!-- Filter: Uplinks -->
      <div class="filter-group">
        <div class="filter-group-title">
          <span>منافذ الـ Uplink عالية السرعة</span>
        </div>
        <ul class="filter-list">
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox" checked>
              <b>2x / 4x 10G SFP+</b>
            </span>
            <span class="filter-count-badge">16</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>1G SFP Standard</span>
            </span>
            <span class="filter-count-badge">10</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>25G / 40G QSFP+</span>
            </span>
            <span class="filter-count-badge">3</span>
          </li>
        </ul>
      </div>

      <!-- Filter: Availability -->
      <div class="filter-group">
        <div class="filter-group-title">
          <span>حالة التوفر بالمخزون</span>
        </div>
        <ul class="filter-list">
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox" checked>
              <b>متوفر فوراً بالمخزن (تسليم 24 س)</b>
            </span>
            <span class="filter-count-badge">24</span>
          </li>
          <li class="filter-checkbox-label">
            <span class="filter-check-wrap">
              <input type="checkbox">
              <span>اطلب للتوريد (مشروعات)</span>
            </span>
            <span class="filter-count-badge">11</span>
          </li>
        </ul>
      </div>
    </aside>

    <!-- Main Products Column -->
    <section class="catalog-main-content">
      <!-- Top Sort Bar -->
      <div class="catalog-top-bar">
        <div class="catalog-heading">
          <h1>سويتشات الشبكات المعتمدة للشركات والمشروعات</h1>
          <p>عرض 18 موديل مطابق للفلاتر التقنية المختارة</p>
        </div>
        <div class="catalog-sort-wrap">
          <span>ترتيب حسب:</span>
          <select class="sort-select">
            <option>الأكثر طلباً وتوريداً</option>
            <option>الموديل (تصاعدي A-Z)</option>
            <option>السعر: من الأقل للأعلى</option>
            <option>السعر: من الأعلى للأقل</option>
            <option>أعلى ميزانية PoE</option>
          </select>
        </div>
      </div>

      <!-- Active Filter Chips -->
      <div class="active-chips-strip">
        <span style="font-size:12px; color:#64748b; font-weight:700;">الفلاتر المطبقة:</span>
        <div class="chip-item">Cisco Systems <span class="chip-remove">✕</span></div>
        <div class="chip-item">24 Port Gigabit <span class="chip-remove">✕</span></div>
        <div class="chip-item">PoE+ 370W+ <span class="chip-remove">✕</span></div>
        <div class="chip-item">10G SFP+ Uplinks <span class="chip-remove">✕</span></div>
        <div class="chip-item">متوفر بالمخزون <span class="chip-remove">✕</span></div>
        <a href="#" style="font-size:12px; color:var(--rose-500); text-decoration:none; font-weight:700; margin-right:8px;">مسح الكل</a>
      </div>

      <!-- Grid of 6 Cards -->
      <div class="catalog-products-grid">
        <!-- 1. Cisco 2960X 24TD -->
        <div class="cat-product-card">
          <div class="card-top-badges">
            <span class="badge-stock-dot"><span class="dot-green"></span> متاح فوراً</span>
          </div>
          <div class="cat-img-box">{SVG_CISCO_SWITCH}</div>
          <div style="font-size:11px; font-weight:700; color:var(--cyan-600); text-transform:uppercase;">Cisco Systems</div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#334155; margin-bottom:4px;">WS-C2960X-24TD-L</div>
          <h3 class="cat-product-title">سويتش سيسكو كاتاليست 24 بورت جيجابت PoE+ مع 2x 10G SFP+</h3>
          <div class="tech-badges-grid">
            <div class="tech-badge-item">بورتات: <b>24x 1G</b></div>
            <div class="tech-badge-item">طاقة: <b>PoE+ 370W</b></div>
            <div class="tech-badge-item">أبلينك: <b>2x 10G</b></div>
            <div class="tech-badge-item">طبقة: <b>Layer 2/3</b></div>
          </div>
          <div class="cat-card-footer">
            <div>
              <div style="font-size:16px; font-weight:900; color:var(--navy-900);">19,850 <small style="font-size:11px;">ج.م</small></div>
              <div style="font-size:11.5px; color:#94a3b8; text-decoration:line-through;">23,200 ج.م</div>
            </div>
            <div class="cat-card-actions">
              <button class="btn-icon-compare" title="مقارنة"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></button>
              <button class="btn-card-add-cart">أضف للسلة</button>
            </div>
          </div>
        </div>

        <!-- 2. MikroTik CRS328 -->
        <div class="cat-product-card">
          <div class="card-top-badges">
            <span class="badge-stock-dot"><span class="dot-green"></span> متاح فوراً</span>
          </div>
          <div class="cat-img-box">{SVG_MIKROTIK}</div>
          <div style="font-size:11px; font-weight:700; color:var(--navy-900); text-transform:uppercase;">MikroTik</div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#334155; margin-bottom:4px;">CRS328-24P-4S+RM</div>
          <h3 class="cat-product-title">سويتش مايكروتك كلاود 24 بورت PoE ذكي مع 4 منافذ SFP+ 10G</h3>
          <div class="tech-badges-grid">
            <div class="tech-badge-item">بورتات: <b>24x 1G</b></div>
            <div class="tech-badge-item">طاقة: <b>PoE 500W</b></div>
            <div class="tech-badge-item">أبلينك: <b>4x 10G</b></div>
            <div class="tech-badge-item">نظام: <b>RouterOS</b></div>
          </div>
          <div class="cat-card-footer">
            <div>
              <div style="font-size:16px; font-weight:900; color:var(--navy-900);">22,400 <small style="font-size:11px;">ج.م</small></div>
              <div style="font-size:11.5px; color:#94a3b8; text-decoration:line-through;">25,500 ج.م</div>
            </div>
            <div class="cat-card-actions">
              <button class="btn-icon-compare" title="مقارنة"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></button>
              <button class="btn-card-add-cart">أضف للسلة</button>
            </div>
          </div>
        </div>

        <!-- 3. Cisco Catalyst 9200L -->
        <div class="cat-product-card">
          <div class="card-top-badges">
            <span class="badge-stock-dot"><span class="dot-green"></span> متاح فوراً</span>
          </div>
          <div class="cat-img-box">{SVG_CISCO_SWITCH}</div>
          <div style="font-size:11px; font-weight:700; color:var(--cyan-600); text-transform:uppercase;">Cisco Systems</div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#334155; margin-bottom:4px;">C9200L-24P-4X-E</div>
          <h3 class="cat-product-title">سويتش سيسكو كاتاليست الجيل القادم 9200L مع 4x 10G Uplink</h3>
          <div class="tech-badges-grid">
            <div class="tech-badge-item">بورتات: <b>24x 1G</b></div>
            <div class="tech-badge-item">طاقة: <b>PoE+ 370W</b></div>
            <div class="tech-badge-item">أبلينك: <b>4x 10G</b></div>
            <div class="tech-badge-item">طبقة: <b>Full Layer 3</b></div>
          </div>
          <div class="cat-card-footer">
            <div>
              <div style="font-size:16px; font-weight:900; color:var(--navy-900);">34,500 <small style="font-size:11px;">ج.م</small></div>
              <div style="font-size:11.5px; color:#94a3b8; text-decoration:line-through;">38,000 ج.م</div>
            </div>
            <div class="cat-card-actions">
              <button class="btn-icon-compare" title="مقارنة"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></button>
              <button class="btn-card-add-cart">أضف للسلة</button>
            </div>
          </div>
        </div>

        <!-- 4. Ubiquiti UniFi Pro 24 PoE -->
        <div class="cat-product-card">
          <div class="card-top-badges">
            <span class="badge-stock-dot"><span class="dot-green"></span> متاح فوراً</span>
          </div>
          <div class="cat-img-box">{SVG_CISCO_SWITCH}</div>
          <div style="font-size:11px; font-weight:700; color:var(--cyan-500); text-transform:uppercase;">Ubiquiti UniFi</div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#334155; margin-bottom:4px;">USW-Pro-24-PoE</div>
          <h3 class="cat-product-title">سويتش يوبيكويتي يوني فاي برو 24 بورت مع شاشة لمس AR</h3>
          <div class="tech-badges-grid">
            <div class="tech-badge-item">بورتات: <b>24x 1G</b></div>
            <div class="tech-badge-item">طاقة: <b>PoE++ 400W</b></div>
            <div class="tech-badge-item">أبلينك: <b>2x 10G</b></div>
            <div class="tech-badge-item">إدارة: <b>UniFi OS</b></div>
          </div>
          <div class="cat-card-footer">
            <div>
              <div style="font-size:16px; font-weight:900; color:var(--navy-900);">26,800 <small style="font-size:11px;">ج.م</small></div>
              <div style="font-size:11.5px; color:#94a3b8; text-decoration:line-through;">29,900 ج.م</div>
            </div>
            <div class="cat-card-actions">
              <button class="btn-icon-compare" title="مقارنة"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></button>
              <button class="btn-card-add-cart">أضف للسلة</button>
            </div>
          </div>
        </div>

        <!-- 5. Fortinet FortiSwitch 124E-POE -->
        <div class="cat-product-card">
          <div class="card-top-badges">
            <span class="badge-stock-dot"><span class="dot-green"></span> متاح فوراً</span>
          </div>
          <div class="cat-img-box">{SVG_FORTINET}</div>
          <div style="font-size:11px; font-weight:700; color:var(--rose-500); text-transform:uppercase;">Fortinet</div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#334155; margin-bottom:4px;">FS-124E-POE</div>
          <h3 class="cat-product-title">سويتش فورتينت فورتي سويتش 24 بورت متوافق مع FortiGate</h3>
          <div class="tech-badges-grid">
            <div class="tech-badge-item">بورتات: <b>24x 1G</b></div>
            <div class="tech-badge-item">طاقة: <b>PoE 180W</b></div>
            <div class="tech-badge-item">أبلينك: <b>4x 1G SFP</b></div>
            <div class="tech-badge-item">ربط: <b>FortiLink</b></div>
          </div>
          <div class="cat-card-footer">
            <div>
              <div style="font-size:16px; font-weight:900; color:var(--navy-900);">21,500 <small style="font-size:11px;">ج.م</small></div>
              <div style="font-size:11.5px; color:#94a3b8; text-decoration:line-through;">24,000 ج.م</div>
            </div>
            <div class="cat-card-actions">
              <button class="btn-icon-compare" title="مقارنة"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></button>
              <button class="btn-card-add-cart">أضف للسلة</button>
            </div>
          </div>
        </div>

        <!-- 6. Cisco Catalyst 48 Port (Demonstrating Strikethrough or Custom RFQ) -->
        <div class="cat-product-card">
          <div class="card-top-badges">
            <span class="badge-stock-dot" style="color:#f59e0b;"><span class="dot-green" style="background:#f59e0b;"></span> اطلب للتوريد</span>
          </div>
          <div class="cat-img-box">{SVG_CISCO_SWITCH}</div>
          <div style="font-size:11px; font-weight:700; color:var(--cyan-600); text-transform:uppercase;">Cisco Systems</div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#334155; margin-bottom:4px;">WS-C2960X-48FPD-L</div>
          <h3 class="cat-product-title">سويتش سيسكو كاتاليست 48 بورت جيجابت Full PoE+ 740W</h3>
          <div class="tech-badges-grid">
            <div class="tech-badge-item">بورتات: <b>48x 1G</b></div>
            <div class="tech-badge-item">طاقة: <b>PoE+ 740W</b></div>
            <div class="tech-badge-item">أبلينك: <b>2x 10G</b></div>
            <div class="tech-badge-item">طبقة: <b>Layer 2/3</b></div>
          </div>
          <div class="cat-card-footer">
            <div>
              <div style="font-size:15px; font-weight:800; color:var(--cyan-600);">اسأل عن السعر</div>
              <div style="font-size:11px; color:#64748b;">(متاح للتوريد الفوري)</div>
            </div>
            <div class="cat-card-actions">
              <button class="btn-icon-compare" title="مقارنة"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></button>
              <button class="btn-card-add-cart">أضف للسلة</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  {get_footer_html()}

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "page_03_catalog_filters.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "03_صفحة_الفلاتر_والبحث_Desktop_Catalog_Filters.png")
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

