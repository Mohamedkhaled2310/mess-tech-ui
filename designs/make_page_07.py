# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS

DESIGNS_DIR = r"E:\mess\designs"

HTML_CONTENT = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة تحكم الإدارة (Admin Dashboard) - إدارة الأوردرات والمخزون والتوريد</title>
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

    /* Admin Sidebar (Right in RTL) */
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
      transition: all 0.15s;
    }}
    .admin-menu-item a:hover, .admin-menu-item.active a {{
      background: rgba(0, 153, 229, 0.15);
      color: var(--cyan-400);
    }}
    .admin-badge-count {{
      background: #ef4444;
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 1px 7px;
      border-radius: 999px;
      margin-right: auto;
    }}
    .admin-user-footer {{
      padding: 16px 20px;
      border-top: 1px solid rgba(255,255,255,0.06);
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .user-avatar {{
      width: 36px;
      height: 36px;
      background: var(--cyan-500);
      color: #fff;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
    }}

    /* Admin Main Content */
    .admin-main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Top Bar */
    .admin-topbar {{
      background: #fff;
      border-bottom: 1px solid var(--slate-200);
      padding: 14px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .topbar-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .btn-action-primary {{
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
    }}
    .btn-action-secondary {{
      background: #f8fafc;
      border: 1px solid var(--slate-200);
      color: #334155;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}

    /* Dashboard Body */
    .admin-body {{
      padding: 28px 32px;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }}

    /* KPI Cards Grid */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }}
    .kpi-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 20px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
      display: flex;
      flex-direction: column;
    }}
    .kpi-title-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
      color: #64748b;
      margin-bottom: 8px;
      font-weight: 700;
    }}
    .kpi-value {{
      font-size: 26px;
      font-weight: 900;
      color: var(--navy-900);
      margin-bottom: 6px;
    }}
    .kpi-delta {{
      font-size: 11.5px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .delta-green {{ color: #059669; }}
    .delta-amber {{ color: #d97706; }}

    /* Layout Split: Orders Table (Left) + Quick Rules (Right) */
    .dashboard-split {{
      display: grid;
      grid-template-columns: 2.3fr 1fr;
      gap: 24px;
      align-items: start;
    }}

    /* Orders Management Table */
    .dashboard-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 24px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }}
    .card-header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }}
    .card-header-title {{
      font-size: 17px;
      font-weight: 900;
      color: var(--navy-900);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .admin-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: right;
    }}
    .admin-table th {{
      background: #f8fafc;
      padding: 12px 14px;
      font-size: 12.5px;
      font-weight: 800;
      color: #475569;
      border-bottom: 1px solid var(--slate-200);
    }}
    .admin-table td {{
      padding: 12px 14px;
      font-size: 13px;
      color: #334155;
      border-bottom: 1px solid var(--slate-100);
    }}
    .status-badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 11.5px;
      font-weight: 800;
    }}
    .status-new {{ background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }}
    .status-confirmed {{ background: #fefce8; color: #a16207; border: 1px solid #fef08a; }}
    .status-shipped {{ background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }}
    .status-delivered {{ background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }}
    .status-cancelled {{ background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; }}

    /* Quick Settings Widget */
    .quick-settings-box {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .setting-item-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--slate-100);
    }}
    .setting-label {{
      font-size: 13px;
      font-weight: 700;
      color: var(--navy-900);
    }}
    .setting-val {{
      font-size: 12.5px;
      color: #64748b;
      font-family: 'JetBrains Mono', sans-serif;
    }}
  </style>
</head>
<body>

  <!-- Admin Sidebar -->
  <aside class="admin-sidebar">
    <div class="admin-logo-box">
      <img src="assets/logo_white.png" style="height:36px;" alt="MESS TECH">
      <div style="font-size:11px; color:var(--cyan-400); font-weight:700; margin-top:4px;">لوحة تحكم المتجر والمخزون</div>
    </div>

    <ul class="admin-menu-list">
      <li class="admin-menu-item active">
        <a href="#">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          <span>نظرة عامة وإحصائيات</span>
        </a>
      </li>
      <li class="admin-menu-item">
        <a href="#">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          <span>الطلبات والأوردرات</span>
          <span class="admin-badge-count">14</span>
        </a>
      </li>
      <li class="admin-menu-item">
        <a href="#">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="6" cy="12" r="1.5"/><circle cx="10" cy="12" r="1.5"/><circle cx="14" cy="12" r="1.5"/><circle cx="18" cy="12" r="1.5"/></svg>
          <span>المنتجات والمواصفات</span>
        </a>
      </li>
      <li class="admin-menu-item">
        <a href="#">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          <span>قاعدة بيانات العملاء</span>
        </a>
      </li>
      <li class="admin-menu-item">
        <a href="#">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
          <span>أسعار الشحن للمحافظات</span>
        </a>
      </li>
      <li class="admin-menu-item">
        <a href="#">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
          <span>تقارير المبيعات (Excel)</span>
        </a>
      </li>
      <li class="admin-menu-item">
        <a href="#">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
          <span>الإعدادات والصلاحيات</span>
        </a>
      </li>
    </ul>

    <div class="admin-user-footer">
      <div class="user-avatar">م</div>
      <div>
        <div style="font-size:13px; font-weight:800; color:#fff;">م. كريم السعيد</div>
        <div style="font-size:11px; color:#64748b;">مدير النظام (Super Admin)</div>
      </div>
    </div>
  </aside>

  <!-- Admin Main -->
  <main class="admin-main">
    <!-- Topbar -->
    <header class="admin-topbar">
      <div style="display:flex; align-items:center; gap:16px;">
        <h2 style="font-size:18px; font-weight:900; color:var(--navy-900);">نظرة عامة على المتجر ومتابعة الأوردرات</h2>
        <span style="background:#ecfdf5; color:#047857; font-size:11.5px; font-weight:700; padding:2px 10px; border-radius:999px;">
          المتجر يعمل بكفاءة 100%
        </span>
      </div>

      <div class="topbar-actions">
        <button class="btn-action-secondary">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
          رفع منتجات Excel / CSV
        </button>
        <button class="btn-action-primary">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          إضافة منتج جديد
        </button>
      </div>
    </header>

    <div class="admin-body">
      <!-- 4 KPI Cards -->
      <section class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-title-row">
            <span>تحصيل مبيعات اليوم (COD)</span>
            <span>💰</span>
          </div>
          <div class="kpi-value">128,450 <small style="font-size:14px; color:#64748b;">ج.م</small></div>
          <div class="kpi-delta delta-green">↑ +14.2% مقارنة بالأسبوع الماضي</div>
        </div>

        <div class="kpi-card">
          <div class="kpi-title-row">
            <span>أوردرات اليوم الجديدة</span>
            <span>📦</span>
          </div>
          <div class="kpi-value">14 <small style="font-size:14px; color:#64748b;">أوردر</small></div>
          <div class="kpi-delta delta-green">✓ 9 تم تأكيدهم هاتفياً مع العملاء</div>
        </div>

        <div class="kpi-card">
          <div class="kpi-title-row">
            <span>تنبيهات المخزون المنخفض</span>
            <span>⚠️</span>
          </div>
          <div class="kpi-value" style="color:#d97706;">4 <small style="font-size:14px; color:#64748b;">موديلات</small></div>
          <div class="kpi-delta delta-amber">تحت الحد الأدنى (أقل من 3 قطع)</div>
        </div>

        <div class="kpi-card">
          <div class="kpi-title-row">
            <span>نسبة تحويل الزوار لأوردرات</span>
            <span>📈</span>
          </div>
          <div class="kpi-value">4.8%</div>
          <div class="kpi-delta delta-green">↑ متفوق على متوسط متاجر الـ B2B</div>
        </div>
      </section>

      <!-- Main Section: Orders Table & Settings -->
      <div class="dashboard-split">
        <!-- Table -->
        <div class="dashboard-card">
          <div class="card-header-bar">
            <div class="card-header-title">
              <span>أحدث الطلبات وحالات التوريد والتحصيل (COD)</span>
            </div>
            <div style="display:flex; gap:8px;">
              <button class="btn-action-secondary" style="font-size:12px; padding:6px 12px;">طباعة بوليصات الشحن</button>
              <button class="btn-action-secondary" style="font-size:12px; padding:6px 12px;">تصدير Excel</button>
            </div>
          </div>

          <table class="admin-table">
            <thead>
              <tr>
                <th>رقم الطلب</th>
                <th>العميل والشركة</th>
                <th>المحافظة</th>
                <th>الموديل والكمية</th>
                <th>المبلغ المطلوب (COD)</th>
                <th>حالة الطلب</th>
                <th>الإجراءات</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b class="mono" style="color:var(--cyan-600);">#ORD-2026-1048</b></td>
                <td>
                  <b>م. أحمد فتحي</b>
                  <div style="font-size:11px; color:#64748b;">شركة دلتا للحلول المتكاملة</div>
                </td>
                <td>القاهرة (المعادي)</td>
                <td><span class="mono">WS-C2960X-24TD-L (x2)</span></td>
                <td><b>42,200 ج.م</b></td>
                <td><span class="status-badge status-new">جديد بانتظار التأكيد</span></td>
                <td><button style="background:none; border:none; color:var(--cyan-600); font-weight:700; cursor:pointer;">تأكيد هاتفياً</button></td>
              </tr>

              <tr>
                <td><b class="mono" style="color:var(--cyan-600);">#ORD-2026-1047</b></td>
                <td>
                  <b>م. إبراهيم خليل</b>
                  <div style="font-size:11px; color:#64748b;">مستشفى الصفوة التخصصي</div>
                </td>
                <td>الجيزة (الدقي)</td>
                <td><span class="mono">FortiGate FG-60F (x1)</span></td>
                <td><b>28,900 ج.م</b></td>
                <td><span class="status-badge status-confirmed">تم التأكيد هاتفياً</span></td>
                <td><button style="background:none; border:none; color:var(--cyan-600); font-weight:700; cursor:pointer;">طباعة البوليصة</button></td>
              </tr>

              <tr>
                <td><b class="mono" style="color:var(--cyan-600);">#ORD-2026-1046</b></td>
                <td>
                  <b>م. سامح عزيز</b>
                  <div style="font-size:11px; color:#64748b;">مركز النيل للحاسبات</div>
                </td>
                <td>الإسكندرية (سموحة)</td>
                <td><span class="mono">CRS328-24P-4S+RM (x1)</span></td>
                <td><b>22,550 ج.م</b></td>
                <td><span class="status-badge status-shipped">تم الشحن مع المندوب</span></td>
                <td><button style="background:none; border:none; color:var(--cyan-600); font-weight:700; cursor:pointer;">تتبع السائق</button></td>
              </tr>

              <tr>
                <td><b class="mono" style="color:var(--cyan-600);">#ORD-2026-1045</b></td>
                <td>
                  <b>م. محمود رضوان</b>
                  <div style="font-size:11px; color:#64748b;">المجموعة الهندسية</div>
                </td>
                <td>القاهرة (التجمع الخامس)</td>
                <td><span class="mono">UniFi U6-Pro (x4)</span></td>
                <td><b>34,800 ج.م</b></td>
                <td><span class="status-badge status-delivered">تم التسليم والتحصيل COD</span></td>
                <td><span style="color:#059669; font-weight:800; font-size:12px;">تم التوريد ✓</span></td>
              </tr>

              <tr>
                <td><b class="mono" style="color:var(--cyan-600);">#ORD-2026-1044</b></td>
                <td>
                  <b>شركة الأهرام للبرمجيات</b>
                  <div style="font-size:11px; color:#64748b;">استلام من الفرع</div>
                </td>
                <td>فرع المعادي</td>
                <td><span class="mono">APC UPS 3000VA (x1)</span></td>
                <td><b>31,000 ج.م</b></td>
                <td><span class="status-badge status-delivered">تم الاستلام والتحصيل</span></td>
                <td><span style="color:#059669; font-weight:800; font-size:12px;">تم التوريد ✓</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Quick Settings & Governorate Shipping Widget -->
        <div class="quick-settings-box">
          <h3 style="font-size:16px; font-weight:900; color:var(--navy-900); padding-bottom:8px; border-bottom:1px solid var(--slate-100);">
            إعدادات الشحن والتواصل
          </h3>

          <div class="setting-item-row">
            <div>
              <div class="setting-label">شحن مجاني فوق مبلغ:</div>
              <div style="font-size:11.5px; color:#64748b;">يتم تفعيله آلياً في السلة</div>
            </div>
            <div class="setting-val" style="color:#059669; font-weight:800;">20,000 ج.م</div>
          </div>

          <div class="setting-item-row">
            <div>
              <div class="setting-label">شحن القاهرة والجيزة:</div>
              <div style="font-size:11.5px; color:#64748b;">توصيل خلال 24 ساعة</div>
            </div>
            <div class="setting-val">100 ج.م</div>
          </div>

          <div class="setting-item-row">
            <div>
              <div class="setting-label">شحن الإسكندرية والوجه البحري:</div>
              <div style="font-size:11.5px; color:#64748b;">توصيل 48 ساعة</div>
            </div>
            <div class="setting-val">150 ج.م</div>
          </div>

          <div class="setting-item-row">
            <div>
              <div class="setting-label">شحن الصعيد والمحافظات البعيدة:</div>
              <div style="font-size:11.5px; color:#64748b;">توصيل 48-72 ساعة</div>
            </div>
            <div class="setting-val">200 ج.م</div>
          </div>

          <div class="setting-item-row" style="border-bottom:none;">
            <div>
              <div class="setting-label">رقم واتساب المبيعات المباشر:</div>
              <div style="font-size:11.5px; color:#64748b;">يرتبط تلقائياً بصفحات المنتجات</div>
            </div>
            <div class="setting-val" style="color:#22c55e; font-weight:800;">+20 100 234 5678</div>
          </div>

          <button class="btn-action-primary" style="justify-content:center; width:100%; font-size:12.5px; padding:9px;">
            تحديث إعدادات الشحن والمبيعات
          </button>
        </div>
      </div>
    </div>
  </main>

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "page_07_admin_dashboard.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "07_لوحة_التحكم_Admin_Dashboard_Overview.png")
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

