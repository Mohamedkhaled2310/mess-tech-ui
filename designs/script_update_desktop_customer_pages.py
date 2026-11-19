# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS, get_header_html, get_footer_html
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS
from render_helper import render_html_to_png

DESIGNS_DIR = r"E:\mess\designs"

# ==============================================================================
# PAGE 08: ORDER SUCCESS / THANK YOU PAGE (Cleaned Desktop)
# - Removed "ماذا يحدث بعد تأكيد الطلب"
# - Removed "تتبع مسار الطلب"
# - Removed "الفواتير الضريبية"
# - Used "طلب" instead of "توريد"
# ==============================================================================
PAGE_08_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | تم تأكيد طلبك بنجاح - شكراً لتسوقكم</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    .success-hero {{
      background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
      color: #fff;
      padding: 44px 48px;
      text-align: center;
      border-bottom: 2px solid var(--navy-700);
      position: relative;
    }}
    .success-check-circle {{
      width: 76px;
      height: 76px;
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 18px;
      box-shadow: 0 0 35px rgba(16, 185, 129, 0.45);
      border: 4px solid rgba(255, 255, 255, 0.2);
    }}
    .success-hero h1 {{
      font-size: 28px;
      font-weight: 900;
      margin-bottom: 8px;
      color: #fff;
    }}
    .success-hero p {{
      color: #cbd5e1;
      font-size: 15px;
      max-width: 600px;
      margin: 0 auto 20px;
      line-height: 1.6;
    }}
    .order-meta-pills {{
      display: inline-flex;
      gap: 16px;
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 10px 24px;
      border-radius: 999px;
      font-size: 13.5px;
    }}
    .order-meta-pills b {{ color: var(--cyan-400); }}

    .success-layout {{
      max-width: 1200px;
      margin: 36px auto;
      padding: 0 32px;
      display: grid;
      grid-template-columns: 1.3fr 0.85fr;
      gap: 32px;
      align-items: start;
    }}

    .success-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 26px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.03);
      margin-bottom: 24px;
    }}
    .success-card h3 {{
      font-size: 18px;
      font-weight: 800;
      color: var(--navy-900);
      margin-bottom: 18px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--slate-100);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .cod-highlight-box {{
      background: #eff6ff;
      border: 1.5px solid #bfdbfe;
      border-radius: 12px;
      padding: 16px 20px;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      margin-bottom: 20px;
    }}
    .cod-highlight-icon {{
      width: 40px;
      height: 40px;
      background: #3b82f6;
      color: #fff;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      font-size: 20px;
    }}

    .item-row {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 14px 0;
      border-bottom: 1px solid var(--slate-100);
    }}
    .item-row:last-child {{ border-bottom: none; }}
    .item-thumb {{
      width: 70px;
      height: 50px;
      background: #f8fafc;
      border: 1px solid var(--slate-200);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4px;
      flex-shrink: 0;
    }}

    .btn-action-primary {{
      background: var(--cyan-500);
      color: #fff;
      font-size: 15px;
      font-weight: 800;
      padding: 14px 24px;
      border-radius: 10px;
      text-decoration: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(0, 153, 229, 0.3);
      width: 100%;
    }}
    .btn-action-secondary {{
      background: #fff;
      color: var(--navy-900);
      font-size: 14px;
      font-weight: 700;
      padding: 12px 20px;
      border-radius: 10px;
      text-decoration: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      border: 1.5px solid var(--slate-300);
      cursor: pointer;
      width: 100%;
      margin-top: 10px;
    }}
  </style>
</head>
<body>
  {get_header_html()}

  <!-- Hero Header -->
  <section class="success-hero">
    <div class="success-check-circle">
      <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
    </div>
    <h1>تم استلام طلبك بنجاح وجاري تجهيزه بالمستودع!</h1>
    <p>شكراً لثقتكم بمتجر <b>MESS TECH</b>. تم تسجيل الطلب بنجاح وسيتواصل معكم فريق العمل لتأكيد موعد التوصيل.</p>
    <div class="order-meta-pills">
      <span>رقم الطلب: <b class="mono">#ORD-9824</b></span>
      <span>•</span>
      <span>التاريخ: <b>15 نوفمبر 2026</b></span>
      <span>•</span>
      <span>موعد التوصيل المتوقع: <b>خلال 24-48 ساعة (الثلاثاء 17 نوفمبر)</b></span>
    </div>
  </section>

  <!-- Content Layout -->
  <main class="success-layout">
    <!-- Main Right Column: Order Details -->
    <div>
      <!-- Payment Highlight -->
      <div class="cod-highlight-box">
        <div class="cod-highlight-icon">💵</div>
        <div>
          <h4 style="font-size:15.5px; font-weight:800; color:#1e40af; margin-bottom:4px;">طريقة الدفع المختارة: الدفع نقداً عند الاستلام (COD)</h4>
          <p style="font-size:13px; color:#3b82f6; line-height:1.6; margin:0;">
            سيتم تحصيل المبلغ الإجمالي البالغ <b class="mono" style="font-size:15px; color:#1e3a8a;">37,950 ج.م</b> نقداً أو عبر بطاقة الدفع (POS) مع مندوب التوصيل بعد معاينة وفحص كراتين الأجهزة واستلام إيصال الاستلام المعتمد.
          </p>
        </div>
      </div>

      <!-- Shipping & Customer Info -->
      <div class="success-card">
        <h3>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          بيانات العميل وعنوان التوصيل
        </h3>
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; font-size:13.5px;">
          <div>
            <div style="color:var(--slate-500); font-size:12px; margin-bottom:4px;">اسم العميل / الشركة:</div>
            <div style="font-weight:800; color:var(--navy-900);">م. مصطفى الشافعي — شركة الأفق للحلول الذكية</div>
          </div>
          <div>
            <div style="color:var(--slate-500); font-size:12px; margin-bottom:4px;">رقم الهاتف المسجل للتوصيل:</div>
            <div class="mono" style="font-weight:800; color:var(--navy-900);">+20 100 123 4567</div>
          </div>
          <div style="grid-column: span 2;">
            <div style="color:var(--slate-500); font-size:12px; margin-bottom:4px;">عنوان التوصيل المعتمد:</div>
            <div style="font-weight:700; color:var(--navy-900);">مبنى تكنوبوليس، الدور الرابع، شارع التسعين الشمالي، التجمع الخامس، القاهرة.</div>
          </div>
        </div>
      </div>

      <!-- Order Items Summary -->
      <div class="success-card">
        <h3>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          الأجهزة والمعدات المؤكدة بالطلب (3 أصناف)
        </h3>

        <div class="item-row">
          <div class="item-thumb">{SVG_CISCO_SWITCH}</div>
          <div style="flex:1;">
            <div style="font-size:14.5px; font-weight:800; color:var(--navy-900);">سويتش سيسكو Cisco Catalyst 2960-X Series</div>
            <div class="mono" style="font-size:12px; color:var(--slate-500);">SKU: WS-C2960X-24TD-L • 24 Port Gigabit + 2x 10G SFP+</div>
            <div style="font-size:11.5px; color:#059669; font-weight:700; margin-top:2px;">✓ أجهزة أصلية معتمدة 100% بالكرتونة والملحقات</div>
          </div>
          <div style="text-align:left;">
            <div style="font-size:12px; color:var(--slate-500);">الكمية: 1</div>
            <div class="mono" style="font-size:16px; font-weight:900; color:var(--navy-900);">28,500 ج.م</div>
          </div>
        </div>

        <div class="item-row">
          <div class="item-thumb">{SVG_MIKROTIK}</div>
          <div style="flex:1;">
            <div style="font-size:14.5px; font-weight:800; color:var(--navy-900);">راوتر كلاود مايكروتك MikroTik CCR2004-16G-2S+PC</div>
            <div class="mono" style="font-size:12px; color:var(--slate-500);">SKU: CCR2004-16G • 16x Gigabit + 2x 10G SFP+ Dual PSU</div>
            <div style="font-size:11.5px; color:#059669; font-weight:700; margin-top:2px;">✓ أجهزة أصلية معتمدة 100%</div>
          </div>
          <div style="text-align:left;">
            <div style="font-size:12px; color:var(--slate-500);">الكمية: 1</div>
            <div class="mono" style="font-size:16px; font-weight:900; color:var(--navy-900);">8,950 ج.م</div>
          </div>
        </div>

        <div class="item-row">
          <div class="item-thumb">{SVG_UBIQUITI_AP}</div>
          <div style="flex:1;">
            <div style="font-size:14.5px; font-weight:800; color:var(--navy-900);">بكرة كابلات شبكات Schneider Actassi Cat6 UTP 305m</div>
            <div class="mono" style="font-size:12px; color:var(--slate-500);">SKU: VDI2414002 • 100% نحاس نقي معتمد</div>
          </div>
          <div style="text-align:left;">
            <div style="font-size:12px; color:var(--slate-500);">الكمية: 1</div>
            <div class="mono" style="font-size:16px; font-weight:900; color:var(--navy-900);">500 ج.م</div>
          </div>
        </div>

        <!-- Bill Totals -->
        <div style="background:#f8fafc; border-radius:10px; padding:16px 20px; margin-top:16px; font-size:13.5px;">
          <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
            <span style="color:var(--slate-500);">المجموع الفرعي للأجهزة:</span>
            <span class="mono" style="font-weight:700;">37,950 ج.م</span>
          </div>
          <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
            <span style="color:var(--slate-500);">الشحن والتوصيل (العروض الحالية):</span>
            <span style="color:#059669; font-weight:800;">مجاناً بالكامل</span>
          </div>
          <div style="border-top:1.5px dashed var(--slate-300); padding-top:10px; margin-top:6px; display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:16px; font-weight:900; color:var(--navy-900);">المبلغ الإجمالي المطلوب تحصيله (COD):</span>
            <span class="mono" style="font-size:22px; font-weight:900; color:var(--cyan-600);">37,950 ج.م</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Side Left Column: Actions & Contact -->
    <div>
      <div class="success-card" style="border: 2px solid #bfdbfe; background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);">
        <h3 style="border-bottom:none; margin-bottom:12px;">إجراءات سريعة لطلبك</h3>
        <p style="font-size:13px; color:var(--slate-500); margin-bottom:20px; line-height:1.6;">
          تم تسجيل طلبك وحجز المنتجات لك مباشرة، وسيتصل بكم مندوب التوصيل قبل التحرك.
        </p>

        <a href="11_سجل_الطلبات_السابقة_Desktop_Order_History.png" class="btn-action-primary">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
          عرض سجل طلباتي في الحساب
        </a>

        <button class="btn-action-secondary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          تحميل إشعار استلام الطلب (PDF)
        </button>

        <button class="btn-action-secondary" style="border-color:transparent; color:var(--slate-500);">
          ← متابعة التسوق وتصفح العروض الحالية
        </button>
      </div>

      <!-- Tech Help Card -->
      <div style="background:#0f172a; border-radius:14px; padding:20px; color:#fff; display:flex; align-items:center; gap:16px;">
        <div style="width:48px; height:48px; background:rgba(0, 153, 229, 0.2); border:1px solid var(--cyan-500); border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--cyan-400)" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        </div>
        <div>
          <div style="font-size:14px; font-weight:800; color:#fff;">هل ترغب بتعديل العنوان أو إضافة أصناف؟</div>
          <div style="font-size:12.5px; color:#94a3b8; margin-top:2px;">اتصل فوراً بخدمة العملاء والمبيعات: <b class="mono" style="color:var(--cyan-400);">0100-MESS-TECH</b></div>
        </div>
      </div>
    </div>
  </main>

  {get_footer_html()}
</body>
</html>
"""

# ==============================================================================
# PAGE 10: AUTHENTICATION / LOGIN / REGISTER (Cleaned Desktop)
# - Removed OTP Box completely
# - Removed "فواتير ضريبية"
# - Replaced "توريد" with "طلب"
# ==============================================================================
PAGE_10_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | تسجيل الدخول وإنشاء حساب العملاء والشركات</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    body {{
      background: radial-gradient(circle at 75% 25%, #172a4d 0%, #070d18 70%);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    .auth-page-container {{
      max-width: 1100px;
      margin: 48px auto;
      padding: 0 40px;
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 56px;
      align-items: center;
      flex: 1;
    }}

    .auth-brand-side {{
      color: #fff;
    }}
    .auth-brand-logo {{
      height: 52px;
      margin-bottom: 24px;
    }}
    .auth-brand-side h1 {{
      font-size: 32px;
      font-weight: 900;
      line-height: 1.4;
      margin-bottom: 16px;
    }}
    .auth-brand-side p {{
      color: #94a3b8;
      font-size: 15px;
      line-height: 1.8;
      margin-bottom: 28px;
    }}
    .feature-pill-row {{
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .feature-pill {{
      display: flex;
      align-items: center;
      gap: 14px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 12px 18px;
      border-radius: 12px;
    }}
    .feature-pill-icon {{
      width: 36px;
      height: 36px;
      background: rgba(0, 153, 229, 0.15);
      border: 1px solid rgba(0, 153, 229, 0.4);
      color: var(--cyan-400);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
    }}

    .auth-card {{
      background: #ffffff;
      border-radius: 20px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      padding: 36px 40px;
      border: 1px solid var(--slate-200);
    }}

    .auth-tabs {{
      display: flex;
      background: #f1f5f9;
      border-radius: 10px;
      padding: 4px;
      margin-bottom: 28px;
    }}
    .auth-tab-btn {{
      flex: 1;
      text-align: center;
      padding: 10px;
      font-size: 14px;
      font-weight: 800;
      color: var(--slate-500);
      background: transparent;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .auth-tab-btn.active {{
      background: #fff;
      color: var(--navy-900);
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }}

    .form-group {{
      margin-bottom: 18px;
    }}
    .form-label {{
      display: block;
      font-size: 13px;
      font-weight: 700;
      color: var(--navy-900);
      margin-bottom: 6px;
    }}
    .form-control-input {{
      width: 100%;
      border: 1.5px solid var(--slate-300);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 14px;
      outline: none;
      transition: all 0.2s;
    }}
    .form-control-input:focus {{
      border-color: var(--cyan-500);
      box-shadow: 0 0 0 3px rgba(0, 153, 229, 0.15);
    }}

    .btn-submit-auth {{
      width: 100%;
      background: var(--navy-900);
      color: #fff;
      font-size: 15px;
      font-weight: 800;
      padding: 13px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      margin-top: 8px;
      box-shadow: 0 4px 12px rgba(11, 17, 32, 0.25);
    }}
  </style>
</head>
<body>
  {get_header_html()}

  <div class="auth-page-container">
    <!-- Left Showcase -->
    <div class="auth-brand-side">
      <img src="assets/logo_white.png" class="auth-brand-logo" alt="MESS TECH Logo">
      <h1>بوابة العملاء والشركات<br><span style="color:var(--cyan-400);">لطلب حلول وتجهيزات الشبكات</span></h1>
      <p>
        سجل دخولك الآن للوصول إلى أسعار المنتجات الخاصة، مراجعة طلباتك السابقة، وحفظ عناوين الشحن لتسريع عمليات الشراء القادمة.
      </p>

      <div class="feature-pill-row">
        <div class="feature-pill">
          <div class="feature-pill-icon">✓</div>
          <div>
            <div style="font-weight:800; font-size:14px;">أجهزة أصلية معتمدة 100%</div>
            <div style="font-size:12px; color:#94a3b8;">سيسكو، مايكروتك، فورتينت، يوبيكويتي، وAPC من المصادر الرسمية.</div>
          </div>
        </div>

        <div class="feature-pill">
          <div class="feature-pill-icon">⚡</div>
          <div>
            <div style="font-weight:800; font-size:14px;">إتمام سريع للطلب في خطوة واحدة</div>
            <div style="font-size:12px; color:#94a3b8;">تأكيد فوري للطلب مع خيار الدفع نقداً عند الاستلام.</div>
          </div>
        </div>

        <div class="feature-pill">
          <div class="feature-pill-icon">🚚</div>
          <div>
            <div style="font-weight:800; font-size:14px;">شحن وتوصيل سريع ومؤمن</div>
            <div style="font-size:12px; color:#94a3b8;">توصيل مباشر لمقر عملك أو موقع مشروعك خلال 24-48 ساعة.</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Right Login Card -->
    <div class="auth-card">
      <div class="auth-tabs">
        <button class="auth-tab-btn active">تسجيل الدخول</button>
        <button class="auth-tab-btn">إنشاء حساب جديد</button>
      </div>

      <div>
        <div class="form-group">
          <label class="form-label">البريد الإلكتروني أو رقم الهاتف</label>
          <input type="text" class="form-control-input mono" value="m.elshafei@alofok-tech.com" placeholder="name@company.com أو 010xxxxxxxx">
        </div>

        <div class="form-group">
          <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
            <label class="form-label" style="margin-bottom:0;">كلمة المرور</label>
            <a href="#" style="font-size:12px; color:var(--cyan-600); text-decoration:none; font-weight:700;">نسيت كلمة المرور؟</a>
          </div>
          <input type="password" class="form-control-input mono" value="••••••••••••" placeholder="أدخل كلمة المرور">
        </div>

        <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:20px; font-size:13px;">
          <label style="display:flex; align-items:center; gap:8px; cursor:pointer; color:var(--slate-600);">
            <input type="checkbox" checked style="accent-color:var(--cyan-500); width:16px; height:16px;">
            تذكر بيانات الدخول على هذا الجهاز
          </label>
        </div>

        <button class="btn-submit-auth">تسجيل الدخول لحسابي</button>

        <div style="margin-top:24px; text-align:center; font-size:13px; color:var(--slate-500);">
          ليس لديك حساب بعد؟ <a href="#" style="color:var(--cyan-600); font-weight:800; text-decoration:none;">سجل حساب جديد الآن</a>
        </div>
      </div>
    </div>
  </div>

  {get_footer_html()}
</body>
</html>
"""

# ==============================================================================
# PAGE 11: CUSTOMER PROFILE & ADDRESS BOOK (Cleaned Desktop)
# - Removed "الفواتير الضريبية"
# - Removed "أجهزتي وسيريالات الضمان"
# - Replaced "توريد" with "طلب"
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
    <!-- Sidebar (Cleaned) -->
    <aside class="portal-sidebar">
      <div class="user-profile-summary">
        <div class="user-avatar-circle">م ش</div>
        <h3 style="font-size:16px; font-weight:800; margin-bottom:2px;">م. مصطفى الشافعي</h3>
        <div style="font-size:12px; color:#94a3b8; margin-bottom:8px;">حساب شركة معتمد</div>
        <div style="display:inline-block; background:rgba(0, 153, 229, 0.2); border:1px solid rgba(0, 153, 229, 0.4); color:var(--cyan-400); padding:3px 10px; border-radius:999px; font-size:11px; font-weight:700;">
          كود العميل: <span class="mono">MST-4402</span>
        </div>
      </div>

      <ul class="portal-nav-list">
        <li class="portal-nav-item active"><a href="#"><span>📊</span> نظرة عامة وبيانات الحساب</a></li>
        <li class="portal-nav-item"><a href="09_سجل_الطلبات_السابقة_Desktop_Order_History.png"><span>📦</span> سجل طلباتي (16 طلب)</a></li>
        <li class="portal-nav-item"><a href="#"><span>📍</span> دفتر العناوين المحفوظة</a></li>
        <li class="portal-nav-item"><a href="#"><span>⚙️</span> إعدادات الحساب وكلمة المرور</a></li>
      </ul>
    </aside>

    <!-- Main Content -->
    <main>
      <!-- Metric Cards -->
      <div class="metric-grid">
        <div class="metric-card">
          <div class="metric-icon" style="background:#eff6ff; color:#2563eb;">🚚</div>
          <div>
            <div style="font-size:12px; color:var(--slate-500);">الطلبات قيد التوصيل:</div>
            <div style="font-size:20px; font-weight:900; color:var(--navy-900);">طلب واحد نشط</div>
          </div>
        </div>

        <div class="metric-card">
          <div class="metric-icon" style="background:#ecfdf5; color:#059669;">✓</div>
          <div>
            <div style="font-size:12px; color:var(--slate-500);">الطلبات المكتملة والمستلمة:</div>
            <div style="font-size:20px; font-weight:900; color:var(--navy-900);">15 طلب مكتمل</div>
          </div>
        </div>

        <div class="metric-card">
          <div class="metric-icon" style="background:#fef3c7; color:#d97706;">🏢</div>
          <div>
            <div style="font-size:12px; color:var(--slate-500);">حالة العضوية:</div>
            <div style="font-size:20px; font-weight:900; color:var(--navy-900);">عميل مميز (VIP)</div>
          </div>
        </div>
      </div>

      <!-- Account Info Section -->
      <div class="section-card">
        <h3>
          <span>بيانات الحساب الشخصية</span>
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
            <label style="font-size:12px; font-weight:700; color:var(--navy-900); display:block; margin-bottom:6px;">اسم الشركة / المؤسسة (اختياري)</label>
            <input type="text" class="portal-input" value="شركة الأفق للحلول الرقمية">
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
      </div>

      <!-- Address Book Section -->
      <div class="section-card">
        <h3>
          <span>دفتر عناوين التوصيل المحفوظة</span>
          <button style="background:#fff; color:var(--cyan-600); border:1.5px solid var(--cyan-500); padding:6px 14px; border-radius:6px; font-size:12.5px; font-weight:800; cursor:pointer;">
            + إضافة عنوان جديد
          </button>
        </h3>

        <div class="address-grid">
          <!-- Default Address -->
          <div class="address-card default">
            <span class="address-badge default">المقر الرئيسي (الافتراضي للتسليم)</span>
            <div style="font-size:14px; font-weight:800; color:var(--navy-900); margin-bottom:4px;">مبنى تكنوبوليس الإداري - الدور 4</div>
            <div style="font-size:13px; color:var(--slate-600); line-height:1.6; margin-bottom:12px;">
              شارع التسعين الشمالي، مجمع البنوك، التجمع الخامس، القاهرة.
            </div>
            <div style="font-size:12px; color:var(--slate-500); display:flex; justify-content:space-between; align-items:center; border-top:1px solid #bfdbfe; padding-top:8px;">
              <span>المستلم: م. مصطفى الشافعي</span>
              <span class="mono" style="font-weight:700;">01001234567</span>
            </div>
          </div>

          <!-- Second Address -->
          <div class="address-card">
            <span class="address-badge" style="background:#f1f5f9; color:var(--slate-600);">عنوان فرعي</span>
            <div style="font-size:14px; font-weight:800; color:var(--navy-900); margin-bottom:4px;">مستودع مدينة العبور - قطعة 14</div>
            <div style="font-size:13px; color:var(--slate-600); line-height:1.6; margin-bottom:12px;">
              مدينة العبور، المنطقة الصناعية الأولى، القاهرة.
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
# PAGE 12: ORDER HISTORY (Cleaned Desktop)
# - Removed "تتبع الشحنة" (tracking page removed)
# - Removed "الفواتير الضريبية"
# - Replaced "توريد" with "طلب"
# ==============================================================================
PAGE_12_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | سجل الطلبات السابقة وإيصالات الاستلام</title>
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
        <li class="portal-nav-item"><a href="08_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png"><span>📊</span> نظرة عامة وبيانات الحساب</a></li>
        <li class="portal-nav-item active"><a href="#"><span>📦</span> طلباتي السابقة (16)</a></li>
        <li class="portal-nav-item"><a href="#"><span>📍</span> دفتر العناوين المحفوظة</a></li>
        <li class="portal-nav-item"><a href="#"><span>⚙️</span> إعدادات الحساب وكلمة المرور</a></li>
      </ul>
    </aside>

    <!-- Main Content -->
    <main>
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">
        <h2 style="font-size:22px; font-weight:900; color:var(--navy-900);">سجل الطلبات السابقة</h2>
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
            <div style="font-size:11.5px; color:var(--slate-500);">شامل الشحن بالكامل</div>
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
          <button style="background:var(--cyan-500); color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer;">
            عرض تفاصيل الطلب
          </button>
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
              <span class="order-badge-status delivered">✓ تم التسليم والتحصيل</span>
            </div>
            <div style="font-size:12px; color:var(--slate-500); margin-top:4px;">تاريخ الاستلام: 28 أكتوبر 2026 • إيصال الاستلام: <span class="mono">RCP-2026-8910</span></div>
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
            <div style="font-size:11.5px; color:#059669;">✓ جهاز أصلي معتمد 100%</div>
          </div>
          <div class="mono" style="font-weight:700;">32,500 ج.م</div>
        </div>

        <div style="display:flex; justify-content:flex-end; gap:12px; margin-top:16px; padding-top:14px; border-top:1px solid var(--slate-100);">
          <button style="background:var(--navy-900); color:#fff; border:none; padding:8px 18px; border-radius:8px; font-size:13px; font-weight:700; display:inline-flex; align-items:center; gap:6px;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            تحميل إيصال الاستلام (PDF)
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

def generate_cleaned_customer_pages():
    print("Generating Cleaned Customer Desktop Pages (08, 10, 11, 12)...")

    # Page 08 - Success
    p08_html = os.path.join(DESIGNS_DIR, "page_08_order_success.html")
    p08_png = os.path.join(DESIGNS_DIR, "08_صفحة_نجاح_الطلب_Desktop_Order_Success.png")
    with open(p08_html, "w", encoding="utf-8") as f:
        f.write(PAGE_08_HTML)
    render_html_to_png(p08_html, p08_png, height=1350)

    # Page 10 - Auth Login
    p10_html = os.path.join(DESIGNS_DIR, "page_10_auth_login.html")
    p10_png = os.path.join(DESIGNS_DIR, "10_تسجيل_الدخول_وإنشاء_حساب_Desktop_Auth_Login.png")
    with open(p10_html, "w", encoding="utf-8") as f:
        f.write(PAGE_10_HTML)
    render_html_to_png(p10_html, p10_png, height=1150)

    # Page 11 - Customer Profile
    p11_html = os.path.join(DESIGNS_DIR, "page_11_customer_profile.html")
    p11_png = os.path.join(DESIGNS_DIR, "11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png")
    with open(p11_html, "w", encoding="utf-8") as f:
        f.write(PAGE_11_HTML)
    render_html_to_png(p11_html, p11_png, height=1450)

    # Page 12 - Order History
    p12_html = os.path.join(DESIGNS_DIR, "page_12_order_history.html")
    p12_png = os.path.join(DESIGNS_DIR, "12_سجل_الطلبات_السابقة_Desktop_Order_History.png")
    with open(p12_html, "w", encoding="utf-8") as f:
        f.write(PAGE_12_HTML)
    render_html_to_png(p12_html, p12_png, height=1400)

if __name__ == "__main__":
    generate_cleaned_customer_pages()
