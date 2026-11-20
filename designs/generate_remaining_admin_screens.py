# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS
from render_helper import render_html_to_png

DESIGNS_DIR = r"E:\mess\designs"

ADMIN_COMMON_HEAD = """
    body {
      background: #f1f5f9;
      display: flex;
      min-height: 100vh;
      color: var(--navy-900);
    }
    .admin-sidebar {
      width: 260px;
      background: var(--navy-950);
      color: #94a3b8;
      display: flex;
      flex-direction: column;
      border-left: 1px solid var(--navy-700);
      flex-shrink: 0;
    }
    .admin-logo-box {
      padding: 24px 20px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    .admin-menu-list {
      list-style: none;
      padding: 16px 12px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      flex: 1;
    }
    .admin-menu-item a {
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
    }
    .admin-menu-item a:hover, .admin-menu-item.active a {
      background: rgba(0, 153, 229, 0.15);
      color: var(--cyan-400);
    }
    .admin-main {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }
    .admin-topbar {
      background: #fff;
      padding: 16px 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--slate-200);
    }
    .admin-content-area {
      padding: 28px 36px;
      max-width: 1440px;
    }
    .admin-card {
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }
    .admin-card h4 {
      font-size: 16px;
      font-weight: 800;
      color: var(--navy-900);
      margin-bottom: 18px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--slate-100);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
"""

def get_admin_sidebar_html(active_item="orders"):
    items = [
        ("overview", "07_لوحة_التحكم_Admin_Dashboard_Overview.png", "📊", "نظرة عامة والتقارير"),
        ("products", "13_إضافة_وتعديل_منتج_Desktop_Admin_Add_Product.png", "📦", "إدارة المنتجات والمخزون"),
        ("orders", "14_جدول_إدارة_الطلبات_Desktop_Admin_Orders_Table.png", "🛒", "إدارة ومتابعة الطلبات"),
        ("order_details", "15_تفاصيل_الطلب_إدارة_Desktop_Admin_Order_Details.png", "📋", "تفاصيل أمر الطلب"),
        ("customers", "16_إدارة_العملاء_والشركات_Desktop_Admin_Customers.png", "🏢", "العملاء والشركات"),
        ("categories", "17_إدارة_الأقسام_والتصنيفات_Desktop_Admin_Categories.png", "📁", "الأقسام والتصنيفات"),
        ("reports", "18_تقارير_المبيعات_والتحليلات_Desktop_Admin_Reports.png", "📈", "تحليلات المبيعات"),
        ("settings", "19_إعدادات_المتجر_والشحن_Desktop_Admin_Settings.png", "⚙️", "إعدادات المتجر والشحن"),
    ]
    menu_html = ""
    for code, link, icon, title in items:
        active_cls = "active" if code == active_item else ""
        menu_html += f'<li class="admin-menu-item {active_cls}"><a href="{link}"><span>{icon}</span> {title}</a></li>\n'
    
    return f"""
    <aside class="admin-sidebar">
      <div class="admin-logo-box">
        <img src="assets/logo_white.png" style="height:38px;" alt="MESS TECH Admin">
        <div style="font-size:11px; color:#38bdf8; font-weight:700; margin-top:6px;">نظام إدارة المتجر والمستودعات</div>
      </div>
      <ul class="admin-menu-list">
        {menu_html}
      </ul>
      <div style="padding:16px 20px; border-top:1px solid rgba(255,255,255,0.06); font-size:12px; color:#94a3b8;">
        المسؤول: <b>م. أحمد رشاد (Super Admin)</b>
      </div>
    </aside>
    """

# ==============================================================================
# SCREEN 15: ADMIN SINGLE ORDER DETAILS
# ==============================================================================
PAGE_15_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة الإدارة - تفاصيل أمر الطلب #ORD-9824</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}
    {ADMIN_COMMON_HEAD}
    .detail-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 24px;
    }}
    .status-select-box {{
      display: flex;
      align-items: center;
      gap: 12px;
      background: #f8fafc;
      border: 1px solid var(--slate-200);
      padding: 12px 18px;
      border-radius: 10px;
      margin-bottom: 20px;
    }}
  </style>
</head>
<body>
  {get_admin_sidebar_html("order_details")}

  <main class="admin-main">
    <div class="admin-topbar">
      <div>
        <div style="display:flex; align-items:center; gap:10px;">
          <h2 style="font-size:19px; font-weight:900; color:var(--navy-900);">أمر طلب رقم: <span class="mono" style="color:var(--cyan-600);">#ORD-9824</span></h2>
          <span style="background:#eff6ff; color:#1d4ed8; font-size:11.5px; font-weight:800; padding:3px 10px; border-radius:999px;">🚚 مع المندوب - قيد التوصيل</span>
        </div>
        <div style="font-size:12.5px; color:var(--slate-500); margin-top:2px;">تاريخ تسجيل الطلب: 15 نوفمبر 2026 - 10:15 ص • طريقة الدفع: الدفع نقداً عند الاستلام (COD)</div>
      </div>
      <div style="display:flex; gap:10px;">
        <button style="background:#fff; border:1.5px solid var(--slate-300); padding:8px 16px; border-radius:8px; font-size:12.5px; font-weight:700; cursor:pointer;">
          طباعة إيصال الاستلام
        </button>
        <button style="background:var(--cyan-500); color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:12.5px; font-weight:800; cursor:pointer;">
          حفظ التغييرات
        </button>
      </div>
    </div>

    <div class="admin-content-area">
      <!-- Status Changer Line -->
      <div class="status-select-box">
        <span style="font-size:13px; font-weight:800; color:var(--navy-900);">تحديث حالة الطلب:</span>
        <select style="border:1.5px solid var(--slate-300); border-radius:6px; padding:6px 12px; font-size:13px; font-weight:700; outline:none; background:#fff;">
          <option>طلب جديد (جديد)</option>
          <option>قيد الفحص والتجهيز بالمستودع</option>
          <option selected>مع مندوب التوصيل (قيد التوصيل الآن)</option>
          <option>تم التسليم وتحصيل المبلغ بنجاح</option>
          <option>طلب ملغي / مسترجع</option>
        </select>
        <span style="color:var(--slate-400); margin:0 8px;">|</span>
        <span style="font-size:13px; font-weight:800; color:var(--navy-900);">تعيين مندوب التوصيل:</span>
        <select style="border:1.5px solid var(--slate-300); border-radius:6px; padding:6px 12px; font-size:13px; font-weight:700; outline:none; background:#fff;">
          <option selected>كابتن أحمد محمود (فان 842 جمرك)</option>
          <option>كابتن حسام علي (فان 319)</option>
          <option>كابتن طارق سعيد</option>
        </select>
      </div>

      <div class="detail-grid">
        <!-- Left: Products Table & Notes -->
        <div>
          <div class="admin-card">
            <h4>الأصناف والمعدات المطلوبة (3 أصناف)</h4>
            <table style="width:100%; border-collapse:collapse; font-size:13px;">
              <thead>
                <tr style="background:#f8fafc; border-bottom:1.5px solid var(--slate-200); text-align:right;">
                  <th style="padding:10px;">المنتج</th>
                  <th style="padding:10px;">كود SKU</th>
                  <th style="padding:10px;">سعر الوحدة</th>
                  <th style="padding:10px;">الكمية</th>
                  <th style="padding:10px;">الإجمالي</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--slate-100);">
                  <td style="padding:12px 10px; display:flex; align-items:center; gap:10px;">
                    <div style="width:50px; height:35px; background:#f8fafc; border:1px solid var(--slate-200); border-radius:4px; display:flex; align-items:center; justify-content:center;">{SVG_CISCO_SWITCH}</div>
                    <div>
                      <div style="font-weight:800;">سويتش سيسكو Cisco Catalyst 2960-X</div>
                      <div style="font-size:11px; color:#059669;">24 Port PoE+ • أجهزة أصلية معتمدة</div>
                    </div>
                  </td>
                  <td style="padding:10px;" class="mono">WS-C2960X-24TD-L</td>
                  <td style="padding:10px;" class="mono">28,500 ج.م</td>
                  <td style="padding:10px; font-weight:800;">1</td>
                  <td style="padding:10px;" class="mono"><b>28,500 ج.م</b></td>
                </tr>
                <tr style="border-bottom:1px solid var(--slate-100);">
                  <td style="padding:12px 10px; display:flex; align-items:center; gap:10px;">
                    <div style="width:50px; height:35px; background:#f8fafc; border:1px solid var(--slate-200); border-radius:4px; display:flex; align-items:center; justify-content:center;">{SVG_MIKROTIK}</div>
                    <div>
                      <div style="font-weight:800;">راوتر كلاود مايكروتك MikroTik CCR2004</div>
                      <div style="font-size:11px; color:#059669;">16G-2S+PC Dual PSU</div>
                    </div>
                  </td>
                  <td style="padding:10px;" class="mono">CCR2004-16G</td>
                  <td style="padding:10px;" class="mono">8,950 ج.م</td>
                  <td style="padding:10px; font-weight:800;">1</td>
                  <td style="padding:10px;" class="mono"><b>8,950 ج.م</b></td>
                </tr>
                <tr>
                  <td style="padding:12px 10px; display:flex; align-items:center; gap:10px;">
                    <div style="width:50px; height:35px; background:#f8fafc; border:1px solid var(--slate-200); border-radius:4px; display:flex; align-items:center; justify-content:center;">{SVG_UBIQUITI_AP}</div>
                    <div>
                      <div style="font-weight:800;">بكرة كابلات شبكات Schneider Cat6 UTP</div>
                      <div style="font-size:11px; color:#059669;">305 متر نحاس نقي</div>
                    </div>
                  </td>
                  <td style="padding:10px;" class="mono">VDI2414002</td>
                  <td style="padding:10px;" class="mono">500 ج.م</td>
                  <td style="padding:10px; font-weight:800;">1</td>
                  <td style="padding:10px;" class="mono"><b>500 ج.م</b></td>
                </tr>
              </tbody>
            </table>

            <div style="background:#f8fafc; border-radius:10px; padding:16px; margin-top:16px; font-size:13px;">
              <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                <span style="color:var(--slate-500);">إجمالي قيمة المنتجات:</span>
                <span class="mono" style="font-weight:700;">37,950 ج.م</span>
              </div>
              <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
                <span style="color:var(--slate-500);">مصاريف الشحن والتوصيل:</span>
                <span style="color:#059669; font-weight:800;">مجاناً (0 ج.م)</span>
              </div>
              <div style="border-top:1.5px dashed var(--slate-300); padding-top:8px; display:flex; justify-content:space-between; font-size:15px; font-weight:900;">
                <span>المبلغ المستحق تحصيله من العميل (COD):</span>
                <span class="mono" style="color:var(--cyan-600); font-size:18px;">37,950 ج.م</span>
              </div>
            </div>
          </div>

          <!-- Internal Admin Notes -->
          <div class="admin-card">
            <h4>الملاحظات الداخلية لإدارة المستودع والشحن</h4>
            <textarea style="width:100%; border:1.5px solid var(--slate-300); border-radius:8px; padding:12px; font-size:13px; outline:none; height:80px; resize:none;">
تم فحص الكراتين ومطابقة الأجهزة والتأكد من سلامة التغليف. العميل طلب الاتصال قبل الوصول والتسليم بالدور الرابع بمبنى تكنوبوليس.
            </textarea>
            <button style="margin-top:8px; background:#f1f5f9; border:1px solid var(--slate-300); padding:6px 14px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
              حفظ الملاحظة
            </button>
          </div>
        </div>

        <!-- Right: Customer Info Box -->
        <div>
          <div class="admin-card">
            <h4>بيانات العميل</h4>
            <div style="font-size:14.5px; font-weight:800; color:var(--navy-900); margin-bottom:4px;">م. مصطفى الشافعي</div>
            <div style="font-size:12px; color:var(--slate-500); margin-bottom:12px;">شركة الأفق للحلول الرقمية</div>

            <div style="font-size:12.5px; color:var(--slate-600); line-height:1.8;">
              <div>الهاتف: <b class="mono" style="color:var(--navy-900);">01001234567</b></div>
              <div>البريد: <span class="mono">m.elshafei@alofok-tech.com</span></div>
              <div>كود العميل: <span class="mono">MST-4402</span> (حساب مشتري موثق)</div>
            </div>
          </div>

          <div class="admin-card">
            <h4>عنوان التوصيل المعتمد</h4>
            <div style="font-size:13px; font-weight:700; color:var(--navy-900); line-height:1.6; margin-bottom:10px;">
              مبنى تكنوبوليس الإداري، الدور الرابع، شارع التسعين الشمالي، التجمع الخامس، القاهرة.
            </div>
            <div style="font-size:12px; color:var(--slate-500);">
              مندوب الشحن المكلف: <b>كابتن أحمد محمود</b> (01123456789)
            </div>
          </div>

          <div class="admin-card" style="border:1.5px solid #bfdbfe; background:#eff6ff;">
            <h4 style="color:#1e40af; border-bottom-color:#bfdbfe;">طريقة الدفع والتحصيل</h4>
            <div style="font-size:13px; font-weight:800; color:#1e3a8a; margin-bottom:4px;">الدفع نقداً عند الاستلام (COD)</div>
            <div style="font-size:12px; color:#3b82f6; line-height:1.5;">
              يتم تحصيل 37,950 ج.م نقداً أو بفيزا المندوب عند تسليم الأجهزة للعميل مباشرة.
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
# SCREEN 16: ADMIN CUSTOMERS & CLIENTS MANAGEMENT TABLE
# ==============================================================================
PAGE_16_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة الإدارة - إدارة العملاء والشركات</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}
    {ADMIN_COMMON_HEAD}
    .customers-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    .customers-table th {{
      background: #f8fafc;
      padding: 12px 14px;
      text-align: right;
      color: var(--slate-600);
      font-weight: 800;
      border-bottom: 1.5px solid var(--slate-200);
    }}
    .customers-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--slate-100);
      vertical-align: middle;
    }}
    .customers-table tr:hover {{
      background: #f8fafc;
    }}
  </style>
</head>
<body>
  {get_admin_sidebar_html("customers")}

  <main class="admin-main">
    <div class="admin-topbar">
      <div>
        <h2 style="font-size:19px; font-weight:900; color:var(--navy-900);">إدارة ومتابعة حسابات العملاء والشركات</h2>
        <div style="font-size:12.5px; color:var(--slate-500);">إجمالي العملاء المسجلين: 420 عميل وشركة تقنية</div>
      </div>
      <div>
        <button style="background:var(--navy-900); color:#fff; border:none; padding:8px 16px; border-radius:8px; font-size:12.5px; font-weight:700; cursor:pointer;">
          + إضافة عميل يدوياً
        </button>
      </div>
    </div>

    <div class="admin-content-area">
      <!-- 3 Metrics -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:20px; margin-bottom:24px;">
        <div class="admin-card" style="margin-bottom:0; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:12px; color:var(--slate-500);">إجمالي العملاء:</div>
            <div class="mono" style="font-size:24px; font-weight:900;">420</div>
          </div>
          <span style="font-size:28px;">👥</span>
        </div>
        <div class="admin-card" style="margin-bottom:0; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:12px; color:#059669;">عملاء نشطين هذا الشهر:</div>
            <div class="mono" style="font-size:24px; font-weight:900; color:#059669;">185</div>
          </div>
          <span style="font-size:28px;">⚡</span>
        </div>
        <div class="admin-card" style="margin-bottom:0; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:12px; color:#2563eb;">عملاء متكررو الشراء:</div>
            <div class="mono" style="font-size:24px; font-weight:900; color:#2563eb;">48</div>
          </div>
          <span style="font-size:28px;">🔁</span>
        </div>
      </div>

      <!-- Filter bar -->
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:12px; padding:14px 18px; margin-bottom:20px; display:flex; justify-content:space-between; align-items:center;">
        <input type="text" placeholder="ابحث باسم العميل، الهاتف، أو اسم الشركة..." style="width:360px; border:1.5px solid var(--slate-300); border-radius:8px; padding:8px 14px; font-size:13px; outline:none;">
        <div style="display:flex; gap:10px;">
          <select style="border:1.5px solid var(--slate-300); border-radius:8px; padding:8px 12px; font-size:12.5px; outline:none;">
            <option>جميع المحافظات</option>
            <option>القاهرة</option>
            <option>الجيزة</option>
            <option>الإسكندرية</option>
          </select>
          <select style="border:1.5px solid var(--slate-300); border-radius:8px; padding:8px 12px; font-size:12.5px; outline:none;">
            <option>جميع الحالات</option>
            <option>حساب نشط</option>
            <option>حساب جديد</option>
          </select>
        </div>
      </div>

      <!-- Customers Table -->
      <div class="admin-card" style="padding:0; overflow:hidden;">
        <table class="customers-table">
          <thead>
            <tr>
              <th>اسم العميل</th>
              <th>بيانات الاتصال</th>
              <th>المحافظة</th>
              <th>عدد الطلبات</th>
              <th>إجمالي المشتريات</th>
              <th>تاريخ آخر طلب</th>
              <th>حالة الحساب</th>
              <th style="text-align:center;">الإجراءات</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <div style="font-weight:800;">م. مصطفى الشافعي</div>
                <div style="font-size:11px; color:var(--slate-500);">شركة الأفق للحلول الرقمية</div>
              </td>
              <td>
                <div class="mono" style="font-weight:700;">01001234567</div>
                <div class="mono" style="font-size:11px; color:var(--slate-500);">m.elshafei@alofok-tech.com</div>
              </td>
              <td>القاهرة (التجمع)</td>
              <td class="mono" style="font-weight:800;">16 طلب</td>
              <td class="mono" style="font-weight:900; color:var(--cyan-600);">148,500 ج.م</td>
              <td style="font-size:12px;">15 نوفمبر 2026</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">حساب نشط ✓</span></td>
              <td style="text-align:center;">
                <button style="background:var(--cyan-500); color:#fff; border:none; padding:5px 12px; border-radius:6px; font-size:11.5px; font-weight:700; cursor:pointer;">عرض الطلبات</button>
              </td>
            </tr>

            <tr>
              <td>
                <div style="font-weight:800;">شركة النيل للنظم السحابية</div>
                <div style="font-size:11px; color:var(--slate-500);">مسؤول المشتريات: أ. سامح</div>
              </td>
              <td>
                <div class="mono" style="font-weight:700;">01229876543</div>
                <div class="mono" style="font-size:11px; color:var(--slate-500);">proc@nilesys.eg</div>
              </td>
              <td>الجيزة (القرية الذكية)</td>
              <td class="mono" style="font-weight:800;">8 طلبات</td>
              <td class="mono" style="font-weight:900; color:var(--cyan-600);">89,200 ج.م</td>
              <td style="font-size:12px;">15 نوفمبر 2026</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">حساب نشط ✓</span></td>
              <td style="text-align:center;">
                <button style="background:var(--cyan-500); color:#fff; border:none; padding:5px 12px; border-radius:6px; font-size:11.5px; font-weight:700; cursor:pointer;">عرض الطلبات</button>
              </td>
            </tr>

            <tr>
              <td>
                <div style="font-weight:800;">م. كريم هشام</div>
                <div style="font-size:11px; color:var(--slate-500);">مهندس شبكات حر</div>
              </td>
              <td>
                <div class="mono" style="font-weight:700;">01156781234</div>
                <div class="mono" style="font-size:11px; color:var(--slate-500);">karim.net@gmail.com</div>
              </td>
              <td>القاهرة (المعادي)</td>
              <td class="mono" style="font-weight:800;">4 طلبات</td>
              <td class="mono" style="font-weight:900; color:var(--cyan-600);">46,800 ج.م</td>
              <td style="font-size:12px;">15 نوفمبر 2026</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">حساب نشط ✓</span></td>
              <td style="text-align:center;">
                <button style="background:var(--cyan-500); color:#fff; border:none; padding:5px 12px; border-radius:6px; font-size:11.5px; font-weight:700; cursor:pointer;">عرض الطلبات</button>
              </td>
            </tr>

            <tr>
              <td>
                <div style="font-weight:800;">مستشفى السلام التخصصي</div>
                <div style="font-size:11px; color:var(--slate-500);">إدارة نظم المعلومات IT</div>
              </td>
              <td>
                <div class="mono" style="font-weight:700;">01099887766</div>
                <div class="mono" style="font-size:11px; color:var(--slate-500);">it@salamhosp.org</div>
              </td>
              <td>القاهرة (مصر الجديدة)</td>
              <td class="mono" style="font-weight:800;">12 طلب</td>
              <td class="mono" style="font-weight:900; color:var(--cyan-600);">210,000 ج.م</td>
              <td style="font-size:12px;">15 نوفمبر 2026</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">حساب نشط ✓</span></td>
              <td style="text-align:center;">
                <button style="background:var(--cyan-500); color:#fff; border:none; padding:5px 12px; border-radius:6px; font-size:11.5px; font-weight:700; cursor:pointer;">عرض الطلبات</button>
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

# ==============================================================================
# SCREEN 17: ADMIN CATEGORIES & CATALOG MANAGEMENT
# ==============================================================================
PAGE_17_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة الإدارة - إدارة الأقسام والتصنيفات</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}
    {ADMIN_COMMON_HEAD}
    .cat-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    .cat-table th {{
      background: #f8fafc;
      padding: 12px 16px;
      text-align: right;
      color: var(--slate-600);
      font-weight: 800;
      border-bottom: 1.5px solid var(--slate-200);
    }}
    .cat-table td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--slate-100);
      vertical-align: middle;
    }}
  </style>
</head>
<body>
  {get_admin_sidebar_html("categories")}

  <main class="admin-main">
    <div class="admin-topbar">
      <div>
        <h2 style="font-size:19px; font-weight:900; color:var(--navy-900);">إدارة أقسام المتجر والتصنيفات التقنية</h2>
        <div style="font-size:12.5px; color:var(--slate-500);">ترتيب الأقسام، التحكم في ظهورها بالمتجر، وإضافة تصنيفات فرعية</div>
      </div>
      <div>
        <button style="background:var(--cyan-600); color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:13px; font-weight:800; cursor:pointer;">
          + إضافة قسم رئيسي جديد
        </button>
      </div>
    </div>

    <div class="admin-content-area">
      <div class="admin-card" style="padding:0; overflow:hidden;">
        <table class="cat-table">
          <thead>
            <tr>
              <th>الترتيب</th>
              <th>اسم القسم</th>
              <th>الاسم اللاتيني (Slug)</th>
              <th>عدد المنتجات النشطة</th>
              <th>حالة الظهور بالمتجر</th>
              <th style="text-align:center;">الإجراءات</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="mono" style="font-weight:800;">1</td>
              <td>
                <div style="font-weight:800; font-size:14px;">سويتشات الشبكات (Switches)</div>
                <div style="font-size:11px; color:var(--slate-500);">سيسكو، مايكروتك، يوبيكويتي (Managed / PoE)</div>
              </td>
              <td class="mono">switches</td>
              <td class="mono" style="font-weight:800;">42 جهاز</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">مفعل ظاهرياً ✓</span></td>
              <td style="text-align:center;">
                <button style="background:#fff; border:1px solid var(--slate-300); padding:5px 10px; border-radius:6px; font-size:12px; font-weight:700;">تعديل</button>
              </td>
            </tr>

            <tr>
              <td class="mono" style="font-weight:800;">2</td>
              <td>
                <div style="font-weight:800; font-size:14px;">راوترات وسيرفرات (Routers & Servers)</div>
                <div style="font-size:11px; color:var(--slate-500);">Cloud Core Routers، راوترات سحابية</div>
              </td>
              <td class="mono">routers-servers</td>
              <td class="mono" style="font-weight:800;">28 جهاز</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">مفعل ظاهرياً ✓</span></td>
              <td style="text-align:center;">
                <button style="background:#fff; border:1px solid var(--slate-300); padding:5px 10px; border-radius:6px; font-size:12px; font-weight:700;">تعديل</button>
              </td>
            </tr>

            <tr>
              <td class="mono" style="font-weight:800;">3</td>
              <td>
                <div style="font-weight:800; font-size:14px;">جدران الحماية (Firewalls & Security)</div>
                <div style="font-size:11px; color:var(--slate-500);">Fortinet FortiGate، حماية أمن شبكات</div>
              </td>
              <td class="mono">firewalls</td>
              <td class="mono" style="font-weight:800;">18 جهاز</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">مفعل ظاهرياً ✓</span></td>
              <td style="text-align:center;">
                <button style="background:#fff; border:1px solid var(--slate-300); padding:5px 10px; border-radius:6px; font-size:12px; font-weight:700;">تعديل</button>
              </td>
            </tr>

            <tr>
              <td class="mono" style="font-weight:800;">4</td>
              <td>
                <div style="font-weight:800; font-size:14px;">أجهزة واي فاي وأكسس بوينت (Wi-Fi APs)</div>
                <div style="font-size:11px; color:var(--slate-500);">UniFi 6، حلول تغطية الفنادق والشركات</div>
              </td>
              <td class="mono">wifi-access-points</td>
              <td class="mono" style="font-weight:800;">34 جهاز</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">مفعل ظاهرياً ✓</span></td>
              <td style="text-align:center;">
                <button style="background:#fff; border:1px solid var(--slate-300); padding:5px 10px; border-radius:6px; font-size:12px; font-weight:700;">تعديل</button>
              </td>
            </tr>

            <tr>
              <td class="mono" style="font-weight:800;">5</td>
              <td>
                <div style="font-weight:800; font-size:14px;">مغذيات الطاقة المنقطعة (UPS Systems)</div>
                <div style="font-size:11px; color:var(--slate-500);">APC Schneider Smart-UPS</div>
              </td>
              <td class="mono">ups-power</td>
              <td class="mono" style="font-weight:800;">15 وحدة</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">مفعل ظاهرياً ✓</span></td>
              <td style="text-align:center;">
                <button style="background:#fff; border:1px solid var(--slate-300); padding:5px 10px; border-radius:6px; font-size:12px; font-weight:700;">تعديل</button>
              </td>
            </tr>

            <tr>
              <td class="mono" style="font-weight:800;">6</td>
              <td>
                <div style="font-weight:800; font-size:14px;">كبائن وراكات السيرفر (Server Racks & Cabinets)</div>
                <div style="font-size:11px; color:var(--slate-500);">راكات حائطية وأرضية 9U - 42U</div>
              </td>
              <td class="mono">racks-cabinets</td>
              <td class="mono" style="font-weight:800;">22 كابينة</td>
              <td><span style="background:#ecfdf5; color:#059669; font-size:11px; font-weight:800; padding:2px 8px; border-radius:4px;">مفعل ظاهرياً ✓</span></td>
              <td style="text-align:center;">
                <button style="background:#fff; border:1px solid var(--slate-300); padding:5px 10px; border-radius:6px; font-size:12px; font-weight:700;">تعديل</button>
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

# ==============================================================================
# SCREEN 18: ADMIN SALES REPORTS & ANALYTICS
# ==============================================================================
PAGE_18_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة الإدارة - تقارير المبيعات والأداء</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}
    {ADMIN_COMMON_HEAD}
    .chart-bar-container {{
      height: 180px;
      display: flex;
      align-items: flex-end;
      gap: 20px;
      padding: 10px 0;
      border-bottom: 1.5px solid var(--slate-200);
      margin-top: 16px;
    }}
    .chart-col {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      height: 100%;
      justify-content: flex-end;
    }}
    .chart-bar {{
      width: 100%;
      background: linear-gradient(180deg, var(--cyan-500) 0%, var(--cyan-600) 100%);
      border-radius: 6px 6px 0 0;
      position: relative;
    }}
    .chart-bar:hover {{
      background: var(--cyan-400);
    }}
  </style>
</head>
<body>
  {get_admin_sidebar_html("reports")}

  <main class="admin-main">
    <div class="admin-topbar">
      <div>
        <h2 style="font-size:19px; font-weight:900; color:var(--navy-900);">تقارير المبيعات وتحليلات أداء المتجر</h2>
        <div style="font-size:12.5px; color:var(--slate-500);">تحليلات الإيرادات الشهرية، متوسط قيمة السلة، والمنتجات الأكثر طلباً</div>
      </div>
      <div style="display:flex; gap:8px;">
        <button style="background:#fff; border:1px solid var(--slate-300); padding:6px 14px; border-radius:6px; font-size:12px; font-weight:700;">هذا الشهر</button>
        <button style="background:var(--navy-900); color:#fff; border:none; padding:6px 14px; border-radius:6px; font-size:12px; font-weight:700;">تصدير تقرير PDF</button>
      </div>
    </div>

    <div class="admin-content-area">
      <!-- 4 KPI Ribbon -->
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:20px; margin-bottom:24px;">
        <div class="admin-card" style="margin-bottom:0;">
          <div style="font-size:12px; color:var(--slate-500);">إجمالي مبيعات الشهر:</div>
          <div class="mono" style="font-size:24px; font-weight:900; color:var(--cyan-600); margin:4px 0;">1,280,000 ج.م</div>
          <div style="font-size:11px; color:#059669; font-weight:700;">+18.4% نمو عن الشهر السابق</div>
        </div>

        <div class="admin-card" style="margin-bottom:0;">
          <div style="font-size:12px; color:var(--slate-500);">إجمالي عدد الطلبات:</div>
          <div class="mono" style="font-size:24px; font-weight:900; color:var(--navy-900); margin:4px 0;">248 طلب</div>
          <div style="font-size:11px; color:#059669; font-weight:700;">28 طلب خلال الـ 24 ساعة الماضية</div>
        </div>

        <div class="admin-card" style="margin-bottom:0;">
          <div style="font-size:12px; color:var(--slate-500);">متوسط قيمة الطلب (AOV):</div>
          <div class="mono" style="font-size:24px; font-weight:900; color:var(--navy-900); margin:4px 0;">5,160 ج.م</div>
          <div style="font-size:11px; color:var(--slate-500);">شامل معدات المشاريع الكبرى</div>
        </div>

        <div class="admin-card" style="margin-bottom:0;">
          <div style="font-size:12px; color:var(--slate-500);">نسبة نجاح التسليم والتحصيل:</div>
          <div class="mono" style="font-size:24px; font-weight:900; color:#059669; margin:4px 0;">97.2%</div>
          <div style="font-size:11px; color:#059669; font-weight:700;">أعلى نسبة التزام بالمواعيد</div>
        </div>
      </div>

      <!-- Chart Card -->
      <div class="admin-card">
        <h4>نمو المبيعات خلال الـ 6 أشهر الماضية</h4>
        <div class="chart-bar-container">
          <div class="chart-col">
            <span class="mono" style="font-size:11px; font-weight:700;">640K</span>
            <div class="chart-bar" style="height:50%;"></div>
            <span style="font-size:11px; color:var(--slate-500);">يونيو</span>
          </div>
          <div class="chart-col">
            <span class="mono" style="font-size:11px; font-weight:700;">720K</span>
            <div class="chart-bar" style="height:58%;"></div>
            <span style="font-size:11px; color:var(--slate-500);">يوليو</span>
          </div>
          <div class="chart-col">
            <span class="mono" style="font-size:11px; font-weight:700;">850K</span>
            <div class="chart-bar" style="height:68%;"></div>
            <span style="font-size:11px; color:var(--slate-500);">أغسطس</span>
          </div>
          <div class="chart-col">
            <span class="mono" style="font-size:11px; font-weight:700;">990K</span>
            <div class="chart-bar" style="height:78%;"></div>
            <span style="font-size:11px; color:var(--slate-500);">سبتمبر</span>
          </div>
          <div class="chart-col">
            <span class="mono" style="font-size:11px; font-weight:700;">1.08M</span>
            <div class="chart-bar" style="height:86%;"></div>
            <span style="font-size:11px; color:var(--slate-500);">أكتوبر</span>
          </div>
          <div class="chart-col">
            <span class="mono" style="font-size:11px; font-weight:900; color:var(--cyan-600);">1.28M</span>
            <div class="chart-bar" style="height:100%; background:linear-gradient(180deg, #10b981 0%, #059669 100%);"></div>
            <span style="font-size:11px; font-weight:800; color:var(--navy-900);">نوفمبر (الحالي)</span>
          </div>
        </div>
      </div>

      <!-- Top Selling Products Table -->
      <div class="admin-card">
        <h4>أعلى الأجهزة تحقيقاً للإيرادات (Top Products)</h4>
        <table style="width:100%; border-collapse:collapse; font-size:13px;">
          <thead>
            <tr style="background:#f8fafc; text-align:right; border-bottom:1.5px solid var(--slate-200);">
              <th style="padding:10px;">الجهاز التقني</th>
              <th style="padding:10px;">الماركة</th>
              <th style="padding:10px;">الكمية المباعة</th>
              <th style="padding:10px;">إجمالي المبيعات</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--slate-100);">
              <td style="padding:10px; font-weight:800;">سويتش سيسكو Cisco Catalyst 2960-X</td>
              <td style="padding:10px;">Cisco Systems</td>
              <td style="padding:10px;" class="mono">24 قطعة</td>
              <td style="padding:10px;" class="mono"><b>684,000 ج.م</b></td>
            </tr>
            <tr style="border-bottom:1px solid var(--slate-100);">
              <td style="padding:10px; font-weight:800;">جدار حماية فورتينت FortiGate 60F Firewall</td>
              <td style="padding:10px;">Fortinet</td>
              <td style="padding:10px;" class="mono">12 قطعة</td>
              <td style="padding:10px;" class="mono"><b>390,000 ج.م</b></td>
            </tr>
            <tr>
              <td style="padding:10px; font-weight:800;">راوتر كلاود مايكروتك CCR2004-16G</td>
              <td style="padding:10px;">MikroTik</td>
              <td style="padding:10px;" class="mono">18 قطعة</td>
              <td style="padding:10px;" class="mono"><b>161,100 ج.م</b></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</body>
</html>
"""

# ==============================================================================
# SCREEN 19: ADMIN STORE SETTINGS & SHIPPING
# ==============================================================================
PAGE_19_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة الإدارة - إعدادات المتجر والشحن</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}
    {ADMIN_COMMON_HEAD}
    .settings-tab-bar {{
      display: flex;
      gap: 10px;
      margin-bottom: 24px;
      border-bottom: 2px solid var(--slate-200);
      padding-bottom: 2px;
    }}
    .settings-tab {{
      padding: 10px 18px;
      font-size: 13.5px;
      font-weight: 800;
      color: var(--slate-500);
      cursor: pointer;
      border-bottom: 3px solid transparent;
      margin-bottom: -4px;
    }}
    .settings-tab.active {{
      color: var(--cyan-600);
      border-bottom-color: var(--cyan-600);
    }}
  </style>
</head>
<body>
  {get_admin_sidebar_html("settings")}

  <main class="admin-main">
    <div class="admin-topbar">
      <div>
        <h2 style="font-size:19px; font-weight:900; color:var(--navy-900);">إعدادات المتجر والشحن وسياسات الدفع</h2>
        <div style="font-size:12.5px; color:var(--slate-500);">التحكم في تكاليف الشحن بالمحافظات، شروط الدفع عند الاستلام، ومدراء النظام</div>
      </div>
      <div>
        <button style="background:var(--cyan-500); color:#fff; border:none; padding:8px 22px; border-radius:8px; font-size:13px; font-weight:800; cursor:pointer;">
          حفظ كافة الإعدادات
        </button>
      </div>
    </div>

    <div class="admin-content-area">
      <!-- Tabs -->
      <div class="settings-tab-bar">
        <div class="settings-tab active">الشحن وسياسة التوصيل</div>
        <div class="settings-tab">شروط الدفع عند الاستلام (COD)</div>
        <div class="settings-tab">بيانات المتجر والتواصل</div>
        <div class="settings-tab">مدراء النظام والصلاحيات</div>
      </div>

      <!-- Card 1: Shipping Rules -->
      <div class="admin-card">
        <h4>قواعد وتكاليف الشحن للمحافظات</h4>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; margin-bottom:16px;">
          <div>
            <label style="font-size:12.5px; font-weight:700; display:block; margin-bottom:6px;">مدة التوصيل القياسية لكافة المحافظات</label>
            <input type="text" value="خلال 24 إلى 48 ساعة عمل" style="width:100%; border:1.5px solid var(--slate-300); border-radius:8px; padding:10px; font-size:13px; outline:none;">
          </div>
          <div>
            <label style="font-size:12.5px; font-weight:700; display:block; margin-bottom:6px;">الحد الأدنى للشحن المجاني (ج.م)</label>
            <input type="text" class="mono" value="20,000" style="width:100%; border:1.5px solid var(--slate-300); border-radius:8px; padding:10px; font-size:13px; outline:none;">
          </div>
        </div>

        <div style="font-size:13px; font-weight:800; margin-bottom:8px;">تكلفة الشحن الثابتة للطلبات تحت الحد الأدنى:</div>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:16px;">
          <div style="background:#f8fafc; border:1px solid var(--slate-200); border-radius:8px; padding:12px;">
            <div style="font-size:12px; font-weight:700;">القاهرة والجيزة:</div>
            <div class="mono" style="font-size:16px; font-weight:900; color:var(--navy-900); margin-top:4px;">100 ج.م</div>
          </div>
          <div style="background:#f8fafc; border:1px solid var(--slate-200); border-radius:8px; padding:12px;">
            <div style="font-size:12px; font-weight:700;">الإسكندرية والوجه البحري:</div>
            <div class="mono" style="font-size:16px; font-weight:900; color:var(--navy-900); margin-top:4px;">150 ج.م</div>
          </div>
          <div style="background:#f8fafc; border:1px solid var(--slate-200); border-radius:8px; padding:12px;">
            <div style="font-size:12px; font-weight:700;">محافظات الصعيد والقناة:</div>
            <div class="mono" style="font-size:16px; font-weight:900; color:var(--navy-900); margin-top:4px;">200 ج.م</div>
          </div>
        </div>
      </div>

      <!-- Card 2: COD Rules -->
      <div class="admin-card">
        <h4>سياسة الدفع عند الاستلام (COD Policy)</h4>
        <div style="margin-bottom:12px;">
          <label style="display:flex; align-items:center; gap:8px; font-size:13px; font-weight:700; cursor:pointer;">
            <input type="checkbox" checked style="accent-color:var(--cyan-500); width:16px; height:16px;">
            تفعيل الدفع نقداً عند الاستلام كطريقة الدفع الحصرية بالمتجر
          </label>
        </div>
        <div style="margin-bottom:12px;">
          <label style="display:flex; align-items:center; gap:8px; font-size:13px; font-weight:700; cursor:pointer;">
            <input type="checkbox" checked style="accent-color:var(--cyan-500); width:16px; height:16px;">
            إتاحة الدفع عبر بطاقة الدفع (POS) مع مندوب التوصيل
          </label>
        </div>
        <div>
          <label style="display:flex; align-items:center; gap:8px; font-size:13px; font-weight:700; cursor:pointer;">
            <input type="checkbox" checked style="accent-color:var(--cyan-500); width:16px; height:16px;">
            السماح للعميل بمعاينة وفحص كراتين الأجهزة قبل سداد المبلغ
          </label>
        </div>
      </div>

      <!-- Card 3: Admins Table -->
      <div class="admin-card">
        <h4>مدراء النظام وصلاحيات الوصول</h4>
        <table style="width:100%; border-collapse:collapse; font-size:13px;">
          <thead>
            <tr style="background:#f8fafc; text-align:right; border-bottom:1.5px solid var(--slate-200);">
              <th style="padding:10px;">الاسم</th>
              <th style="padding:10px;">البريد الإلكتروني</th>
              <th style="padding:10px;">الدور والصلاحية</th>
              <th style="padding:10px;">الحالة</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--slate-100);">
              <td style="padding:10px; font-weight:800;">م. أحمد رشاد</td>
              <td style="padding:10px;" class="mono">a.rashad@messtech.com</td>
              <td style="padding:10px;"><span style="background:#fef3c7; color:#b45309; font-weight:800; font-size:11px; padding:2px 8px; border-radius:4px;">مدير عام (Super Admin)</span></td>
              <td style="padding:10px; color:#059669; font-weight:800;">نشط ✓</td>
            </tr>
            <tr style="border-bottom:1px solid var(--slate-100);">
              <td style="padding:10px; font-weight:800;">م. سارة علي</td>
              <td style="padding:10px;" class="mono">sara.ali@messtech.com</td>
              <td style="padding:10px;"><span style="background:#eff6ff; color:#1d4ed8; font-weight:800; font-size:11px; padding:2px 8px; border-radius:4px;">إدارة المخزون والمنتجات</span></td>
              <td style="padding:10px; color:#059669; font-weight:800;">نشط ✓</td>
            </tr>
            <tr>
              <td style="padding:10px; font-weight:800;">كابتن طارق سعيد</td>
              <td style="padding:10px;" class="mono">dispatch@messtech.com</td>
              <td style="padding:10px;"><span style="background:#f3e8ff; color:#7e22ce; font-weight:800; font-size:11px; padding:2px 8px; border-radius:4px;">مسؤول الشحن والتوزيع</span></td>
              <td style="padding:10px; color:#059669; font-weight:800;">نشط ✓</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</body>
</html>
"""

def generate_admin_screens():
    print("Generating Admin Screens 15, 16, 17, 18, 19...")

    # Screen 15 - Order Details
    p15_html = os.path.join(DESIGNS_DIR, "page_15_admin_order_details.html")
    p15_png = os.path.join(DESIGNS_DIR, "15_تفاصيل_الطلب_إدارة_Desktop_Admin_Order_Details.png")
    with open(p15_html, "w", encoding="utf-8") as f:
        f.write(PAGE_15_HTML)
    render_html_to_png(p15_html, p15_png, height=1400)

    # Screen 16 - Customers
    p16_html = os.path.join(DESIGNS_DIR, "page_16_admin_customers.html")
    p16_png = os.path.join(DESIGNS_DIR, "16_إدارة_العملاء_والشركات_Desktop_Admin_Customers.png")
    with open(p16_html, "w", encoding="utf-8") as f:
        f.write(PAGE_16_HTML)
    render_html_to_png(p16_html, p16_png, height=1350)

    # Screen 17 - Categories
    p17_html = os.path.join(DESIGNS_DIR, "page_17_admin_categories.html")
    p17_png = os.path.join(DESIGNS_DIR, "17_إدارة_الأقسام_والتصنيفات_Desktop_Admin_Categories.png")
    with open(p17_html, "w", encoding="utf-8") as f:
        f.write(PAGE_17_HTML)
    render_html_to_png(p17_html, p17_png, height=1300)

    # Screen 18 - Reports
    p18_html = os.path.join(DESIGNS_DIR, "page_18_admin_reports.html")
    p18_png = os.path.join(DESIGNS_DIR, "18_تقارير_المبيعات_والتحليلات_Desktop_Admin_Reports.png")
    with open(p18_html, "w", encoding="utf-8") as f:
        f.write(PAGE_18_HTML)
    render_html_to_png(p18_html, p18_png, height=1350)

    # Screen 19 - Settings
    p19_html = os.path.join(DESIGNS_DIR, "page_19_admin_settings.html")
    p19_png = os.path.join(DESIGNS_DIR, "19_إعدادات_المتجر_والشحن_Desktop_Admin_Settings.png")
    with open(p19_html, "w", encoding="utf-8") as f:
        f.write(PAGE_19_HTML)
    render_html_to_png(p19_html, p19_png, height=1400)

if __name__ == "__main__":
    generate_admin_screens()
