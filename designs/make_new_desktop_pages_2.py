# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS, get_header_html, get_footer_html
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS
from render_helper import render_html_to_png

DESIGNS_DIR = r"E:\mess\designs"

# ==============================================================================
# PAGE 11: CUSTOMER PROFILE & ADDRESS BOOK (Desktop)
# ==============================================================================
PAGE_11_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة حسابي ودفتر العناوين المحفوظة - م. مصطفى الشافعي</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    .portal-container {{
      max-width: 1340px;
      margin: 32px auto;
      padding: 0 48px;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 32px;
      align-items: start;
    }}

    /* Sidebar Navigation */
    .portal-sidebar {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }}
    .user-profile-summary {{
      background: var(--navy-900);
      color: #fff;
      padding: 24px 20px;
      text-align: center;
    }}
    .user-avatar-circle {{
      width: 68px;
      height: 68px;
      background: linear-gradient(135deg, var(--cyan-500), #0284c7);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: 900;
      color: #fff;
      margin: 0 auto 12px;
      border: 3px solid rgba(255,255,255,0.2);
    }}
    .portal-nav-list {{
      list-style: none;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .portal-nav-item a {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 14px;
      border-radius: 8px;
      color: var(--navy-800);
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 700;
      transition: all 0.15s;
    }}
    .portal-nav-item.active a, .portal-nav-item a:hover {{
      background: #eff6ff;
      color: var(--cyan-600);
    }}

    /* Main Area */
    .metric-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-bottom: 24px;
    }}
    .metric-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 20px;
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .metric-icon {{
      width: 48px;
      height: 48px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
    }}

    .section-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 26px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.02);
      margin-bottom: 24px;
    }}
    .section-card h3 {{
      font-size: 17px;
      font-weight: 800;
      color: var(--navy-900);
      margin-bottom: 18px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--slate-100);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .address-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
    }}
    .address-card {{
      border: 1.5px solid var(--slate-200);
      border-radius: 12px;
      padding: 18px;
      position: relative;
    }}
    .address-card.default {{
      border-color: var(--cyan-500);
      background: #f0f9ff;
    }}
    .address-badge {{
      display: inline-block;
      padding: 2px 10px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 800;
      margin-bottom: 8px;
    }}
    .address-badge.default {{
      background: var(--cyan-500);
      color: #fff;
    }}

    .form-row-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
      margin-bottom: 16px;
    }}
    .portal-input {{
      width: 100%;
      border: 1.5px solid var(--slate-300);
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 13.5px;
      outline: none;
    }}
  </style>
</head>
<body>
  {get_header_html()}

  <div class="portal-container">
    <!-- Sidebar -->
    <aside class="portal-sidebar">
      <div class="user-profile-summary">
        <div class="user-avatar-circle">م ش</div>
        <h3 style="font-size:16px; font-weight:800; margin-bottom:2px;">م. مصطفى الشافعي</h3>
        <div style="font-size:12px; color:#94a3b8; margin-bottom:8px;">مدير تكنولوجيا المعلومات - IT Manager</div>
        <div style="display:inline-block; background:rgba(0, 153, 229, 0.2); border:1px solid rgba(0, 153, 229, 0.4); color:var(--cyan-400); padding:3px 10px; border-radius:999px; font-size:11px; font-weight:700;">
          كود العميل: <span class="mono">MST-4402</span>
        </div>
      </div>

      <ul class="portal-nav-list">
        <li class="portal-nav-item active"><a href="#"><span>📊</span> نظرة عامة وبيانات الحساب</a></li>
        <li class="portal-nav-item"><a href="12_سجل_الطلبات_السابقة_Desktop_Order_History.png"><span>📦</span> طلباتي السابقة (16)</a></li>
        <li class="portal-nav-item"><a href="#"><span>📍</span> دفتر العناوين المحفوظة</a></li>
        <li class="portal-nav-item"><a href="#"><span>🔒</span> أجهزتي وسيريالات الضمان</a></li>
        <li class="portal-nav-item"><a href="#"><span>📄</span> الفواتير الضريبية المعتمدة</a></li>
        <li class="portal-nav-item"><a href="#"><span>⚙️</span> إعدادات الأمان وكلمة المرور</a></li>
      </ul>
    </aside>

    <!-- Main Content -->
    <main>
      <!-- Metric Cards -->
      <div class="metric-grid">
        <div class="metric-card">
          <div class="metric-icon" style="background:#eff6ff; color:#2563eb;">🚚</div>
          <div>
            <div style="font-size:12px; color:var(--slate-500);">الطلبات الجارية والتوصيل:</div>
            <div style="font-size:20px; font-weight:900; color:var(--navy-900);">طلب واحد (قيد التوصيل)</div>
          </div>
        </div>

        <div class="metric-card">
          <div class="metric-icon" style="background:#ecfdf5; color:#059669;">✓</div>
          <div>
            <div style="font-size:12px; color:var(--slate-500);">الطلبات المكتملة والمستلمة:</div>
            <div style="font-size:20px; font-weight:900; color:var(--navy-900);">15 طلب توريد</div>
          </div>
        </div>

        <div class="metric-card">
          <div class="metric-icon" style="background:#fef3c7; color:#d97706;">🏢</div>
          <div>
            <div style="font-size:12px; color:var(--slate-500);">فئة حساب الشركة:</div>
            <div style="font-size:20px; font-weight:900; color:var(--navy-900);">شريك معتمد (Enterprise)</div>
          </div>
        </div>
      </div>

      <!-- Account Info Section -->
      <div class="section-card">
        <h3>
          <span>بيانات الحساب والشركة المعتمدة</span>
          <button style="background:var(--cyan-500); color:#fff; border:none; padding:7px 16px; border-radius:6px; font-size:12.5px; font-weight:700; cursor:pointer;">
            حفظ التعديلات
          </button>
        </h3>

        <div class="form-row-2">
          <div>
            <label style="font-size:12px; font-weight:700; color:var(--navy-900); display:block; margin-bottom:6px;">الاسم بالكامل</label>
            <input type="text" class="portal-input" value="مصطفى كمال الشافعي">
          </div>
          <div>
            <label style="font-size:12px; font-weight:700; color:var(--navy-900); display:block; margin-bottom:6px;">اسم الشركة أو المؤسسة</label>
            <input type="text" class="portal-input" value="شركة الأفق للحلول الرقمية وتكنولوجيا المعلومات">
          </div>
        </div>

        <div class="form-row-2">
          <div>
            <label style="font-size:12px; font-weight:700; color:var(--navy-900); display:block; margin-bottom:6px;">البريد الإلكتروني المعتمد</label>
            <input type="text" class="portal-input mono" value="m.elshafei@alofok-tech.com">
          </div>
          <div>
            <label style="font-size:12px; font-weight:700; color:var(--navy-900); display:block; margin-bottom:6px;">رقم الهاتف المسجل للتواصل</label>
            <input type="text" class="portal-input mono" value="+20 100 123 4567">
          </div>
        </div>

        <div class="form-row-2">
          <div>
            <label style="font-size:12px; font-weight:700; color:var(--navy-900); display:block; margin-bottom:6px;">رقم السجل التجاري (لإصدار الفواتير الرسمية)</label>
            <input type="text" class="portal-input mono" value="CR-984210-CAIRO">
          </div>
          <div>
            <label style="font-size:12px; font-weight:700; color:var(--navy-900); display:block; margin-bottom:6px;">رقم البطاقة الضريبية</label>
            <input type="text" class="portal-input mono" value="TR-748-291-002">
          </div>
        </div>
      </div>

      <!-- Address Book Section -->
      <div class="section-card">
        <h3>
          <span>دفتر العناوين ومواقع التوريد المحفوظة</span>
          <button style="background:#fff; color:var(--cyan-600); border:1.5px solid var(--cyan-500); padding:6px 14px; border-radius:6px; font-size:12.5px; font-weight:800; cursor:pointer;">
            + إضافة عنوان استلام جديد
          </button>
        </h3>

        <div class="address-grid">
          <!-- Default Address -->
          <div class="address-card default">
            <span class="address-badge default">المقر الرئيسي (الافتراضي للتسليم)</span>
            <div style="font-size:14px; font-weight:800; color:var(--navy-900); margin-bottom:4px;">مبنى تكنوبوليس الإداري - الدور 4</div>
            <div style="font-size:13px; color:var(--slate-600); line-height:1.6; margin-bottom:12px;">
              شارع التسعين الشمالي، مجمع البنوك، التجمع الخامس، القاهرة الجديدة.
            </div>
            <div style="font-size:12px; color:var(--slate-500); display:flex; justify-content:space-between; align-items:center; border-top:1px solid #bfdbfe; padding-top:8px;">
              <span>المستلم: م. مصطفى الشافعي</span>
              <span class="mono" style="font-weight:700;">01001234567</span>
            </div>
          </div>

          <!-- Second Address -->
          <div class="address-card">
            <span class="address-badge" style="background:#f1f5f9; color:var(--slate-600);">مستودع المشروعات والتنفيذ</span>
            <div style="font-size:14px; font-weight:800; color:var(--navy-900); margin-bottom:4px;">مستودع المنطقة الصناعية ب' - قطعة 14</div>
            <div style="font-size:13px; color:var(--slate-600); line-height:1.6; margin-bottom:12px;">
              مدينة العبور، المنطقة الصناعية الأولى، طريق مصر الإسماعيلية.
            </div>
            <div style="font-size:12px; color:var(--slate-500); display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--slate-100); padding-top:8px;">
              <span>المسؤول: مهندس الموقع م. طارق</span>
              <span class="mono" style="font-weight:700;">01123456788</span>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>

  {get_footer_html()}
</body>
</html>
"""

# ==============================================================================
# PAGE 12: ORDER HISTORY & INVOICES (Desktop)
# ==============================================================================
PAGE_12_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | سجل الطلبات والتوريدات السابقة - فواتير وتتبع</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    .history-container {{
      max-width: 1340px;
      margin: 32px auto;
      padding: 0 48px;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 32px;
      align-items: start;
    }}

    .portal-sidebar {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      overflow: hidden;
    }}
    .user-profile-summary {{
      background: var(--navy-900);
      color: #fff;
      padding: 24px 20px;
      text-align: center;
    }}
    .user-avatar-circle {{
      width: 68px;
      height: 68px;
      background: linear-gradient(135deg, var(--cyan-500), #0284c7);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: 900;
      color: #fff;
      margin: 0 auto 12px;
    }}
    .portal-nav-list {{
      list-style: none;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .portal-nav-item a {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 14px;
      border-radius: 8px;
      color: var(--navy-800);
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 700;
    }}
    .portal-nav-item.active a {{
      background: #eff6ff;
      color: var(--cyan-600);
    }}

    /* Filter Tabs */
    .filter-pills-bar {{
      display: flex;
      gap: 12px;
      margin-bottom: 24px;
    }}
    .filter-pill {{
      background: #fff;
      border: 1px solid var(--slate-200);
      padding: 8px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      color: var(--slate-600);
      cursor: pointer;
    }}
    .filter-pill.active {{
      background: var(--navy-900);
      color: #fff;
      border-color: var(--navy-900);
    }}

    /* Order Card */
    .order-history-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 24px;
      margin-bottom: 20px;
      box-shadow: 0 3px 12px rgba(0,0,0,0.02);
    }}
    .order-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--slate-100);
      margin-bottom: 16px;
    }}
    .order-badge-status {{
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 800;
    }}
    .order-badge-status.shipping {{
      background: #eff6ff;
      color: #2563eb;
      border: 1px solid #bfdbfe;
    }}
    .order-badge-status.delivered {{
      background: #ecfdf5;
      color: #059669;
      border: 1px solid #a7f3d0;
    }}

    .order-item-mini {{
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 10px 0;
    }}
    .order-item-mini-img {{
      width: 56px;
      height: 40px;
      background: #f8fafc;
      border: 1px solid var(--slate-200);
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2px;
    }}
  </style>
</head>
<body>
  {get_header_html()}

  <div class="history-container">
    <!-- Sidebar -->
    <aside class="portal-sidebar">
      <div class="user-profile-summary">
        <div class="user-avatar-circle">م ش</div>
        <h3 style="font-size:16px; font-weight:800; margin-bottom:2px;">م. مصطفى الشافعي</h3>
        <div style="font-size:12px; color:#94a3b8; margin-bottom:8px;">كود العميل: <span class="mono">MST-4402</span></div>
      </div>

      <ul class="portal-nav-list">
        <li class="portal-nav-item"><a href="11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png"><span>📊</span> نظرة عامة وبيانات الحساب</a></li>
        <li class="portal-nav-item active"><a href="#"><span>📦</span> طلباتي السابقة (16)</a></li>
        <li class="portal-nav-item"><a href="#"><span>📍</span> دفتر العناوين المحفوظة</a></li>
        <li class="portal-nav-item"><a href="#"><span>🔒</span> أجهزتي وسيريالات الضمان</a></li>
        <li class="portal-nav-item"><a href="#"><span>📄</span> الفواتير الضريبية المعتمدة</a></li>
      </ul>
    </aside>

    <!-- Main Content -->
    <main>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
        <h2 style="font-size:22px; font-weight:900; color:var(--navy-900);">سجل طلبات التوريد والشحنات</h2>
        <div style="font-size:13px; color:var(--slate-500);">إجمالي الطلبات المسجلة: <b>16 طلب</b></div>
      </div>

      <!-- Filter Pills -->
      <div class="filter-pills-bar">
        <div class="filter-pill active">جميع الطلبات (16)</div>
        <div class="filter-pill">قيد التوصيل الآن (1)</div>
        <div class="filter-pill">تم التسليم بنجاح (14)</div>
        <div class="filter-pill">طلبات ملغاة (1)</div>
      </div>

      <!-- Order 1: Active In-Transit -->
      <div class="order-history-card" style="border:1.5px solid #bfdbfe;">
        <div class="order-card-header">
          <div>
            <div style="display:flex; align-items:center; gap:12px;">
              <span class="mono" style="font-size:16px; font-weight:900; color:var(--navy-900);">#ORD-9824</span>
              <span class="order-badge-status shipping">🚚 مع المندوب - جاري التوصيل اليوم</span>
            </div>
            <div style="font-size:12px; color:var(--slate-500); margin-top:4px;">تاريخ الطلب: 15 نوفمبر 2026 • طريقة الدفع: <b>الدفع نقداً عند الاستلام (COD)</b></div>
          </div>
          <div style="text-align:left;">
            <div class="mono" style="font-size:18px; font-weight:900; color:var(--cyan-600);">37,950 ج.م</div>
            <div style="font-size:11.5px; color:var(--slate-500);">شامل الشحن والضريبة</div>
          </div>
        </div>

        <!-- Items -->
        <div class="order-item-mini">
          <div class="order-item-mini-img">{SVG_CISCO_SWITCH}</div>
          <div style="flex:1;">
            <div style="font-size:13.5px; font-weight:800;">سويتش سيسكو Catalyst 2960-X (24 Port Gigabit + 2x 10G SFP+)</div>
            <div style="font-size:11.5px; color:#059669;">✓ أجهزة أصلية معتمدة 100% • الكمية: 1</div>
          </div>
          <div class="mono" style="font-weight:700;">28,500 ج.م</div>
        </div>

        <div class="order-item-mini">
          <div class="order-item-mini-img">{SVG_MIKROTIK}</div>
          <div style="flex:1;">
            <div style="font-size:13.5px; font-weight:800;">راوتر كلاود مايكروتك MikroTik CCR2004-16G-2S+PC</div>
            <div style="font-size:11.5px; color:#059669;">✓ أجهزة أصلية معتمدة 100% • الكمية: 1</div>
          </div>
          <div class="mono" style="font-weight:700;">8,950 ج.م</div>
        </div>

        <div style="display:flex; justify-content:flex-end; gap:12px; margin-top:16px; padding-top:14px; border-top:1px solid var(--slate-100);">
          <a href="09_صفحة_تتبع_الطلب_Desktop_Order_Tracking.png" style="background:var(--cyan-500); color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:13px; font-weight:700; text-decoration:none; display:inline-flex; align-items:center; gap:6px;">
            تتبع الشحنة لحظياً
          </a>
          <button style="background:#fff; border:1px solid var(--slate-300); color:var(--navy-900); padding:8px 16px; border-radius:8px; font-size:13px; font-weight:700;">
            تحميل إشعار الطلب PDF
          </button>
        </div>
      </div>

      <!-- Order 2: Delivered -->
      <div class="order-history-card">
        <div class="order-card-header">
          <div>
            <div style="display:flex; align-items:center; gap:12px;">
              <span class="mono" style="font-size:16px; font-weight:900; color:var(--navy-900);">#ORD-8910</span>
              <span class="order-badge-status delivered">✓ تم التوصيل والتحصيل</span>
            </div>
            <div style="font-size:12px; color:var(--slate-500); margin-top:4px;">تاريخ الاستلام: 28 أكتوبر 2026 • الفاتورة الضريبية: <span class="mono">INV-2026-8910</span></div>
          </div>
          <div style="text-align:left;">
            <div class="mono" style="font-size:18px; font-weight:900; color:var(--navy-900);">32,500 ج.م</div>
            <div style="font-size:11.5px; color:#059669; font-weight:700;">تم سداد المبلغ نقداً عند الاستلام</div>
          </div>
        </div>

        <div class="order-item-mini">
          <div class="order-item-mini-img">{SVG_FORTINET}</div>
          <div style="flex:1;">
            <div style="font-size:13.5px; font-weight:800;">جدار حماية فورتينت Fortinet FortiGate 60F Next-Gen Firewall</div>
            <div style="font-size:11.5px; color:#059669;">✓ السيريال: FG60FTK21049210 • الضمان ساري</div>
          </div>
          <div class="mono" style="font-weight:700;">32,500 ج.م</div>
        </div>

        <div style="display:flex; justify-content:flex-end; gap:12px; margin-top:16px; padding-top:14px; border-top:1px solid var(--slate-100);">
          <button style="background:var(--navy-900); color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:13px; font-weight:700; display:inline-flex; align-items:center; gap:6px;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            تحميل الفاتورة الضريبية الرسمية (PDF)
          </button>
          <button style="background:#fff; border:1px solid var(--slate-300); color:var(--navy-900); padding:8px 16px; border-radius:8px; font-size:13px; font-weight:700;">
            إعادة طلب نفس الأصناف
          </button>
        </div>
      </div>
    </main>
  </div>

  {get_footer_html()}
</body>
</html>
"""

# ==============================================================================
# PAGE 13: ADMIN - ADD / EDIT PRODUCT & INVENTORY (Desktop)
# ==============================================================================
PAGE_13_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة تحكم الإدارة - إضافة جهاز ومواصفات تقنية جديدة</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    body {{
      background: #f1f5f9;
      display: flex;
      min-height: 100vh;
    }}

    .admin-sidebar {{
      width: 260px;
      background: var(--navy-950);
      color: #94a3b8;
      display: flex;
      flex-direction: column;
      border-left: 1px solid var(--navy-700);
      flex-shrink: 0;
    }}
    .admin-logo-box {{
      padding: 24px 20px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }}
    .admin-menu-list {{
      list-style: none;
      padding: 16px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      flex: 1;
    }}
    .admin-menu-item a {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 14px;
      border-radius: 8px;
      color: #cbd5e1;
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 600;
    }}
    .admin-menu-item.active a {{
      background: rgba(0, 153, 229, 0.15);
      color: var(--cyan-400);
    }}

    .admin-main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    .admin-topbar {{
      background: #fff;
      padding: 16px 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--slate-200);
    }}

    .admin-content-area {{
      padding: 28px 36px;
      max-width: 1400px;
    }}

    .admin-form-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 28px;
    }}

    .admin-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }}
    .admin-card h4 {{
      font-size: 16px;
      font-weight: 800;
      color: var(--navy-900);
      margin-bottom: 18px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--slate-100);
    }}

    .form-group {{ margin-bottom: 16px; }}
    .form-label {{
      display: block;
      font-size: 12.5px;
      font-weight: 700;
      color: var(--navy-900);
      margin-bottom: 6px;
    }}
    .admin-input {{
      width: 100%;
      border: 1.5px solid var(--slate-300);
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 13.5px;
      outline: none;
    }}
    .admin-input:focus {{
      border-color: var(--cyan-500);
    }}

    /* Drag Drop Box */
    .upload-dropzone {{
      border: 2px dashed #93c5fd;
      background: #eff6ff;
      border-radius: 12px;
      padding: 28px;
      text-align: center;
      cursor: pointer;
    }}

    /* Spec Key-Value Row */
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    .spec-table th {{
      background: #f8fafc;
      padding: 8px 12px;
      text-align: right;
      color: var(--slate-600);
      border-bottom: 1px solid var(--slate-200);
    }}
    .spec-table td {{
      padding: 8px 12px;
      border-bottom: 1px solid var(--slate-100);
    }}
  </style>
</head>
<body>
  <!-- Admin Sidebar -->
  <aside class="admin-sidebar">
    <div class="admin-logo-box">
      <img src="assets/logo_white.png" style="height:38px;" alt="MESS TECH Admin">
      <div style="font-size:11px; color:#38bdf8; font-weight:700; margin-top:6px;">نظام إدارة المتجر والمستودعات</div>
    </div>

    <ul class="admin-menu-list">
      <li class="admin-menu-item"><a href="07_لوحة_التحكم_Admin_Dashboard_Overview.png"><span>📊</span> نظرة عامة والتقارير</a></li>
      <li class="admin-menu-item active"><a href="#"><span>📦</span> إدارة المنتجات والمخزون</a></li>
      <li class="admin-menu-item"><a href="14_جدول_إدارة_الطلبات_Desktop_Admin_Orders_Table.png"><span>🛒</span> إدارة الطلبات والتوريدات</a></li>
      <li class="admin-menu-item"><a href="#"><span>🏢</span> العملاء والشركات</a></li>
      <li class="admin-menu-item"><a href="#"><span>⚙️</span> إعدادات المتجر</a></li>
    </ul>

    <div style="padding:16px 20px; border-top:1px solid rgba(255,255,255,0.06); font-size:12px; color:#94a3b8;">
      المسؤول: <b>م. أحمد رشاد (Admin)</b>
    </div>
  </aside>

  <!-- Admin Main -->
  <main class="admin-main">
    <div class="admin-topbar">
      <div>
        <h2 style="font-size:19px; font-weight:900; color:var(--navy-900);">إضافة جهاز تقني / منتج جديد إلى الكتالوج</h2>
        <div style="font-size:12.5px; color:var(--slate-500);">المنتجات > إضافة منتج جديد • يظهر فوراً في المتجر بعد النشر</div>
      </div>
      <div style="display:flex; gap:12px;">
        <button style="background:#fff; border:1.5px solid var(--slate-300); padding:9px 18px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;">
          حفظ كمسودة
        </button>
        <button style="background:var(--cyan-600); color:#fff; border:none; padding:9px 22px; border-radius:8px; font-size:13px; font-weight:800; cursor:pointer;">
          ✓ نشر المنتج في المتجر
        </button>
      </div>
    </div>

    <div class="admin-content-area">
      <div class="admin-form-grid">
        <!-- Left: Form inputs -->
        <div>
          <!-- Basic Info -->
          <div class="admin-card">
            <h4>المعلومات الأساسية للجهاز</h4>
            <div class="form-group">
              <label class="form-label">اسم المنتج بالعربية (كما يظهر للعميل)</label>
              <input type="text" class="admin-input" value="سويتش سيسكو Cisco Catalyst 3850 Series 24 Port Gigabit PoE+ 4x10G Uplink">
            </div>

            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;" class="form-group">
              <div>
                <label class="form-label">الشركة المصنعة (Brand)</label>
                <select class="admin-input">
                  <option selected>Cisco Systems</option>
                  <option>MikroTik</option>
                  <option>Fortinet</option>
                  <option>Ubiquiti UniFi</option>
                  <option>APC Schneider</option>
                </select>
              </div>
              <div>
                <label class="form-label">القسم الرئيسي بالمتجر</label>
                <select class="admin-input">
                  <option selected>سويتشات الشبكات (Switches)</option>
                  <option>راوترات وسيرفرات</option>
                  <option>جدران الحماية Firewalls</option>
                </select>
              </div>
            </div>

            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;" class="form-group">
              <div>
                <label class="form-label">كود الموديل الرسمي (SKU / Part Number)</label>
                <input type="text" class="admin-input mono" value="WS-C3850-24P-L">
              </div>
              <div>
                <label class="form-label">كود الباركود الدولي (UPC / EAN)</label>
                <input type="text" class="admin-input mono" value="0882658532412">
              </div>
            </div>
          </div>

          <!-- Pricing & Stock -->
          <div class="admin-card">
            <h4>التسعير والمخزون الفعلي بالمستودع</h4>
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:16px;" class="form-group">
              <div>
                <label class="form-label">سعر البيع الأساسي (ج.م)</label>
                <input type="text" class="admin-input mono" value="38,000">
              </div>
              <div>
                <label class="form-label">سعر العرض المخفض (ج.م)</label>
                <input type="text" class="admin-input mono" value="34,900">
              </div>
              <div>
                <label class="form-label">سعر تكلفة التوريد (ج.م)</label>
                <input type="text" class="admin-input mono" value="28,200">
              </div>
            </div>

            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
              <div>
                <label class="form-label">الكمية الفعلية بالمخزن (قطعة)</label>
                <input type="number" class="admin-input mono" value="18">
              </div>
              <div>
                <label class="form-label">حد تنبيه انخفاض المخزون</label>
                <input type="number" class="admin-input mono" value="3">
              </div>
            </div>
          </div>

          <!-- Technical Specs Table -->
          <div class="admin-card">
            <h4>جدول المواصفات التقنية (Tech Specs Matrix)</h4>
            <table class="spec-table">
              <thead>
                <tr>
                  <th>خاصية المواصفة</th>
                  <th>القيمة الفنية الدقيقة</th>
                  <th style="width:50px;">حذف</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><b>منافذ الشبكة الرئيسية:</b></td>
                  <td>24 Port 10/100/1000 Gigabit Ethernet with PoE+</td>
                  <td style="color:#ef4444; text-align:center; cursor:pointer;">✕</td>
                </tr>
                <tr>
                  <td><b>منافذ الأبلينك السريعة:</b></td>
                  <td>4x 10 Gigabit SFP+ Network Module</td>
                  <td style="color:#ef4444; text-align:center; cursor:pointer;">✕</td>
                </tr>
                <tr>
                  <td><b>ميزانية طاقة PoE:</b></td>
                  <td>435W PoE Budget (Supports IP Phones & APs)</td>
                  <td style="color:#ef4444; text-align:center; cursor:pointer;">✕</td>
                </tr>
                <tr>
                  <td><b>سعة التبديل الكلية:</b></td>
                  <td>92 Gbps Switching Capacity</td>
                  <td style="color:#ef4444; text-align:center; cursor:pointer;">✕</td>
                </tr>
              </tbody>
            </table>
            <button style="margin-top:12px; background:#f8fafc; border:1px dashed var(--slate-300); width:100%; padding:8px; border-radius:6px; font-size:12.5px; font-weight:700; color:var(--cyan-600); cursor:pointer;">
              + إضافة بند مواصفة فنية جديد
            </button>
          </div>
        </div>

        <!-- Right Side: Images & Status -->
        <div>
          <!-- Image Upload -->
          <div class="admin-card">
            <h4>صور الجهاز وكتيب Datasheet</h4>
            <div class="upload-dropzone">
              <div style="font-size:28px; margin-bottom:8px;">📁</div>
              <div style="font-size:13.5px; font-weight:800; color:var(--navy-900);">اسحب وأفلت صور المنتج هنا</div>
              <div style="font-size:11.5px; color:var(--slate-500); margin-top:4px;">يدعم PNG, JPG حتى 5MB بجودة عالية</div>
            </div>

            <!-- Uploaded Preview -->
            <div style="margin-top:16px; border:1px solid var(--slate-200); border-radius:8px; padding:10px; display:flex; align-items:center; gap:12px;">
              <div style="width:60px; height:40px; background:#f8fafc; border-radius:4px; display:flex; align-items:center; justify-content:center;">
                {SVG_CISCO_SWITCH}
              </div>
              <div style="flex:1;">
                <div style="font-size:12px; font-weight:700;">cisco-3850-front.png</div>
                <div style="font-size:11px; color:#059669;">الصورة الرئيسية ✓</div>
              </div>
            </div>
          </div>

          <!-- Publishing Settings -->
          <div class="admin-card">
            <h4>إعدادات الظهور والوسوم</h4>
            <div style="margin-bottom:12px;">
              <label style="display:flex; align-items:center; gap:8px; font-size:13px; font-weight:700; cursor:pointer;">
                <input type="checkbox" checked style="accent-color:var(--cyan-500);">
                عرض المنتج ضمن "العروض الحالية"
              </label>
            </div>
            <div style="margin-bottom:12px;">
              <label style="display:flex; align-items:center; gap:8px; font-size:13px; font-weight:700; cursor:pointer;">
                <input type="checkbox" checked style="accent-color:var(--cyan-500);">
                توفر الشحن الفوري خلال 24 ساعة
              </label>
            </div>
            <div>
              <label style="display:flex; align-items:center; gap:8px; font-size:13px; font-weight:700; cursor:pointer;">
                <input type="checkbox" checked style="accent-color:var(--cyan-500);">
                أجهزة أصلية معتمدة 100%
              </label>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</body>
</html>
"""

# ==============================================================================
# PAGE 14: ADMIN - ORDERS MANAGEMENT TABLE (Desktop)
# ==============================================================================
PAGE_14_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | جدول إدارة ومتابعة الطلبات والتوريدات - لوحة التحكم</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    body {{
      background: #f1f5f9;
      display: flex;
      min-height: 100vh;
    }}

    .admin-sidebar {{
      width: 260px;
      background: var(--navy-950);
      color: #94a3b8;
      display: flex;
      flex-direction: column;
      border-left: 1px solid var(--navy-700);
      flex-shrink: 0;
    }}
    .admin-logo-box {{
      padding: 24px 20px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }}
    .admin-menu-list {{
      list-style: none;
      padding: 16px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      flex: 1;
    }}
    .admin-menu-item a {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 14px;
      border-radius: 8px;
      color: #cbd5e1;
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 600;
    }}
    .admin-menu-item.active a {{
      background: rgba(0, 153, 229, 0.15);
      color: var(--cyan-400);
    }}

    .admin-main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    .admin-topbar {{
      background: #fff;
      padding: 16px 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--slate-200);
    }}

    .admin-content-area {{
      padding: 28px 36px;
      max-width: 1440px;
    }}

    /* Stat Cards */
    .stat-ribbon {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-bottom: 24px;
    }}
    .stat-box {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 12px;
      padding: 18px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .stat-num {{
      font-size: 26px;
      font-weight: 900;
      color: var(--navy-900);
      font-family: 'JetBrains Mono';
    }}

    /* Filter & Table Bar */
    .filter-actions-bar {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 12px;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-bottom: 20px;
    }}
    .filter-search-input {{
      flex: 1;
      max-width: 380px;
      border: 1.5px solid var(--slate-300);
      border-radius: 8px;
      padding: 8px 14px;
      font-size: 13px;
      outline: none;
    }}

    /* Orders Table */
    .orders-table-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }}
    .orders-data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    .orders-data-table th {{
      background: #f8fafc;
      padding: 14px 16px;
      text-align: right;
      color: var(--slate-600);
      font-weight: 800;
      border-bottom: 1.5px solid var(--slate-200);
    }}
    .orders-data-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid var(--slate-100);
      vertical-align: middle;
    }}
    .orders-data-table tr:hover {{
      background: #f8fafc;
    }}

    /* Badges */
    .badge-status {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 11.5px;
      font-weight: 800;
    }}
    .badge-status.new {{
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fde68a;
    }}
    .badge-status.transit {{
      background: #eff6ff;
      color: #1d4ed8;
      border: 1px solid #bfdbfe;
    }}
    .badge-status.delivered {{
      background: #ecfdf5;
      color: #047857;
      border: 1px solid #a7f3d0;
    }}
    .badge-status.prep {{
      background: #f3e8ff;
      color: #7e22ce;
      border: 1px solid #e9d5ff;
    }}
  </style>
</head>
<body>
  <!-- Admin Sidebar -->
  <aside class="admin-sidebar">
    <div class="admin-logo-box">
      <img src="assets/logo_white.png" style="height:38px;" alt="MESS TECH Admin">
      <div style="font-size:11px; color:#38bdf8; font-weight:700; margin-top:6px;">نظام إدارة المتجر والمستودعات</div>
    </div>

    <ul class="admin-menu-list">
      <li class="admin-menu-item"><a href="07_لوحة_التحكم_Admin_Dashboard_Overview.png"><span>📊</span> نظرة عامة والتقارير</a></li>
      <li class="admin-menu-item"><a href="13_إضافة_وتعديل_منتج_Desktop_Admin_Add_Product.png"><span>📦</span> إدارة المنتجات والمخزون</a></li>
      <li class="admin-menu-item active"><a href="#"><span>🛒</span> إدارة الطلبات والتوريدات</a></li>
      <li class="admin-menu-item"><a href="#"><span>🏢</span> العملاء والشركات</a></li>
      <li class="admin-menu-item"><a href="#"><span>⚙️</span> إعدادات المتجر</a></li>
    </ul>

    <div style="padding:16px 20px; border-top:1px solid rgba(255,255,255,0.06); font-size:12px; color:#94a3b8;">
      المسؤول: <b>م. أحمد رشاد (Admin)</b>
    </div>
  </aside>

  <!-- Admin Main -->
  <main class="admin-main">
    <div class="admin-topbar">
      <div>
        <h2 style="font-size:19px; font-weight:900; color:var(--navy-900);">إدارة ومتابعة طلبات التوريد المباشرة</h2>
        <div style="font-size:12.5px; color:var(--slate-500);">تحكم كامل في حالات الطلب، تعيين المناديب، وتحصيل الدفع عند الاستلام (COD)</div>
      </div>
      <div>
        <button style="background:var(--navy-900); color:#fff; border:none; padding:9px 18px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;">
          تصدير التقرير (Excel / CSV)
        </button>
      </div>
    </div>

    <div class="admin-content-area">
      <!-- 4 Stat Boxes -->
      <div class="stat-ribbon">
        <div class="stat-box">
          <div>
            <div style="font-size:12px; color:var(--slate-500);">إجمالي طلبات اليوم:</div>
            <div class="stat-num">28</div>
          </div>
          <div style="font-size:26px;">📦</div>
        </div>

        <div class="stat-box">
          <div>
            <div style="font-size:12px; color:#b45309;">طلبات جديدة بحاجة لتأكيد:</div>
            <div class="stat-num" style="color:#b45309;">6</div>
          </div>
          <div style="font-size:26px;">⏳</div>
        </div>

        <div class="stat-box">
          <div>
            <div style="font-size:12px; color:#1d4ed8;">شحنات في الطريق مع المناديب:</div>
            <div class="stat-num" style="color:#1d4ed8;">14</div>
          </div>
          <div style="font-size:26px;">🚚</div>
        </div>

        <div class="stat-box">
          <div>
            <div style="font-size:12px; color:#047857;">تم التسليم والتحصيل اليوم:</div>
            <div class="stat-num" style="color:#047857;">8</div>
          </div>
          <div style="font-size:26px;">💵</div>
        </div>
      </div>

      <!-- Filters -->
      <div class="filter-actions-bar">
        <input type="text" class="filter-search-input" placeholder="ابحث برقم الطلب، اسم العميل، الهاتف أو كود SKU...">

        <div style="display:flex; gap:10px;">
          <select class="filter-search-input" style="max-width:180px;">
            <option>جميع الحالات</option>
            <option>طلب جديد</option>
            <option>قيد التجهيز</option>
            <option>مع المندوب</option>
            <option>تم التسليم</option>
          </select>

          <select class="filter-search-input" style="max-width:160px;">
            <option>جميع المحافظات</option>
            <option>القاهرة الكبرى</option>
            <option>الجيزة</option>
            <option>الإسكندرية</option>
          </select>
        </div>
      </div>

      <!-- Orders Table -->
      <div class="orders-table-card">
        <table class="orders-data-table">
          <thead>
            <tr>
              <th>رقم الطلب</th>
              <th>العميل / الشركة</th>
              <th>الأصناف المطلوبة</th>
              <th>الإجمالي والتحصيل</th>
              <th>حالة الطلب</th>
              <th>مندوب التوصيل</th>
              <th style="text-align:center;">الإجراءات</th>
            </tr>
          </thead>
          <tbody>
            <!-- Row 1 -->
            <tr>
              <td>
                <div class="mono" style="font-weight:900; color:var(--navy-900);">#ORD-9824</div>
                <div style="font-size:11px; color:var(--slate-500);">اليوم 10:15 ص</div>
              </td>
              <td>
                <div style="font-weight:800; color:var(--navy-900);">م. مصطفى الشافعي</div>
                <div style="font-size:11px; color:var(--slate-500);">شركة الأفق • التجمع الخامس</div>
              </td>
              <td>
                <div>سويتش Cisco 2960X + راوتر CCR2004</div>
                <div style="font-size:11.5px; color:var(--slate-500);">3 أصناف • أجهزة أصلية معتمدة 100%</div>
              </td>
              <td>
                <div class="mono" style="font-weight:900; font-size:14.5px; color:var(--navy-900);">37,950 ج.م</div>
                <div style="font-size:11px; color:#2563eb; font-weight:700;">الدفع عند الاستلام (COD)</div>
              </td>
              <td>
                <span class="badge-status transit">🚚 مع المندوب بالطريق</span>
              </td>
              <td>
                <div style="font-weight:700;">كابتن أحمد محمود</div>
                <div class="mono" style="font-size:11px; color:var(--slate-500);">01123456789</div>
              </td>
              <td style="text-align:center;">
                <button style="background:var(--cyan-500); color:#fff; border:none; padding:6px 14px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
                  تحديث الحالة
                </button>
              </td>
            </tr>

            <!-- Row 2 -->
            <tr>
              <td>
                <div class="mono" style="font-weight:900; color:var(--navy-900);">#ORD-9823</div>
                <div style="font-size:11px; color:var(--slate-500);">اليوم 11:40 ص</div>
              </td>
              <td>
                <div style="font-weight:800; color:var(--navy-900);">شركة النيل للنظم السحابية</div>
                <div style="font-size:11px; color:var(--slate-500);">القرية الذكية • الجيزة</div>
              </td>
              <td>
                <div>فورتينت FortiGate 60F Firewall</div>
                <div style="font-size:11.5px; color:var(--slate-500);">قطعة واحدة + رخصة حماية</div>
              </td>
              <td>
                <div class="mono" style="font-weight:900; font-size:14.5px; color:var(--navy-900);">32,500 ج.م</div>
                <div style="font-size:11px; color:#2563eb; font-weight:700;">الدفع عند الاستلام (COD)</div>
              </td>
              <td>
                <span class="badge-status prep">⚙️ قيد الفحص والتجهيز</span>
              </td>
              <td>
                <span style="color:var(--slate-400); font-size:12px;">جاري التعيين...</span>
              </td>
              <td style="text-align:center;">
                <button style="background:#0284c7; color:#fff; border:none; padding:6px 14px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
                  تعيين مندوب
                </button>
              </td>
            </tr>

            <!-- Row 3 -->
            <tr>
              <td>
                <div class="mono" style="font-weight:900; color:var(--navy-900);">#ORD-9822</div>
                <div style="font-size:11px; color:var(--slate-500);">اليوم 12:05 م</div>
              </td>
              <td>
                <div style="font-weight:800; color:var(--navy-900);">م. كريم هشام</div>
                <div style="font-size:11px; color:var(--slate-500);">المعادي الجديدة • القاهرة</div>
              </td>
              <td>
                <div>4x Ubiquiti UniFi U6-Pro Access Point</div>
                <div style="font-size:11.5px; color:var(--slate-500);">4 قطع بالكرتونة الرسمية</div>
              </td>
              <td>
                <div class="mono" style="font-weight:900; font-size:14.5px; color:var(--navy-900);">23,200 ج.م</div>
                <div style="font-size:11px; color:#2563eb; font-weight:700;">الدفع عند الاستلام (COD)</div>
              </td>
              <td>
                <span class="badge-status new">⭐ طلب جديد (يتطلب تأكيد)</span>
              </td>
              <td>
                <span style="color:var(--slate-400); font-size:12px;">-</span>
              </td>
              <td style="text-align:center;">
                <button style="background:#059669; color:#fff; border:none; padding:6px 14px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
                  تأكيد وحجز الأجهزة
                </button>
              </td>
            </tr>

            <!-- Row 4 -->
            <tr>
              <td>
                <div class="mono" style="font-weight:900; color:var(--navy-900);">#ORD-9821</div>
                <div style="font-size:11px; color:var(--slate-500);">اليوم 09:00 ص</div>
              </td>
              <td>
                <div style="font-weight:800; color:var(--navy-900);">مستشفى السلام التخصصي</div>
                <div style="font-size:11px; color:var(--slate-500);">مصر الجديدة • القاهرة</div>
              </td>
              <td>
                <div>وحدة مغذي طاقة APC Smart-UPS 3000VA</div>
                <div style="font-size:11.5px; color:var(--slate-500);">قطعة واحدة معتمدة</div>
              </td>
              <td>
                <div class="mono" style="font-weight:900; font-size:14.5px; color:var(--navy-900);">45,000 ج.م</div>
                <div style="font-size:11px; color:#059669; font-weight:700;">تم التحصيل نقداً COD</div>
              </td>
              <td>
                <span class="badge-status delivered">✓ تم التسليم والتحصيل</span>
              </td>
              <td>
                <div style="font-weight:700;">كابتن حسام علي</div>
              </td>
              <td style="text-align:center;">
                <button style="background:#fff; border:1px solid var(--slate-300); color:var(--navy-900); padding:6px 12px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
                  عرض الفاتورة
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</body>
</html>
"""

def generate_desktop_pages_2():
    print("Generating Desktop Pages 11, 12, 13, 14...")

    # Page 11
    p11_html = os.path.join(DESIGNS_DIR, "page_11_customer_profile.html")
    p11_png = os.path.join(DESIGNS_DIR, "11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png")
    with open(p11_html, "w", encoding="utf-8") as f:
        f.write(PAGE_11_HTML)
    render_html_to_png(p11_html, p11_png, height=1550)

    # Page 12
    p12_html = os.path.join(DESIGNS_DIR, "page_12_order_history.html")
    p12_png = os.path.join(DESIGNS_DIR, "12_سجل_الطلبات_السابقة_Desktop_Order_History.png")
    with open(p12_html, "w", encoding="utf-8") as f:
        f.write(PAGE_12_HTML)
    render_html_to_png(p12_html, p12_png, height=1500)

    # Page 13
    p13_html = os.path.join(DESIGNS_DIR, "page_13_admin_add_product.html")
    p13_png = os.path.join(DESIGNS_DIR, "13_إضافة_وتعديل_منتج_Desktop_Admin_Add_Product.png")
    with open(p13_html, "w", encoding="utf-8") as f:
        f.write(PAGE_13_HTML)
    render_html_to_png(p13_html, p13_png, height=1650)

    # Page 14
    p14_html = os.path.join(DESIGNS_DIR, "page_14_admin_orders_table.html")
    p14_png = os.path.join(DESIGNS_DIR, "14_جدول_إدارة_الطلبات_Desktop_Admin_Orders_Table.png")
    with open(p14_html, "w", encoding="utf-8") as f:
        f.write(PAGE_14_HTML)
    render_html_to_png(p14_html, p14_png, height=1400)

if __name__ == "__main__":
    generate_desktop_pages_2()
