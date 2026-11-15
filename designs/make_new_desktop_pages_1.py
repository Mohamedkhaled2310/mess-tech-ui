# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS, get_header_html, get_footer_html
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS
from render_helper import render_html_to_png

DESIGNS_DIR = r"E:\mess\designs"

# ==============================================================================
# PAGE 08: ORDER SUCCESS / THANK YOU PAGE (Desktop)
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
      max-width: 1340px;
      margin: 36px auto;
      padding: 0 48px;
      display: grid;
      grid-template-columns: 1.25fr 0.9fr;
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

    /* COD Notice Banner in Success Page */
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

    .timeline-steps {{
      display: flex;
      flex-direction: column;
      gap: 20px;
      position: relative;
      padding-right: 18px;
    }}
    .timeline-steps::before {{
      content: '';
      position: absolute;
      top: 14px;
      bottom: 14px;
      right: 5px;
      width: 2px;
      background: var(--slate-200);
    }}
    .timeline-step-item {{
      display: flex;
      align-items: flex-start;
      gap: 14px;
      position: relative;
    }}
    .step-dot {{
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--slate-300);
      border: 2px solid #fff;
      position: absolute;
      right: -18px;
      top: 4px;
      box-shadow: 0 0 0 2px var(--slate-200);
    }}
    .step-dot.active {{
      background: var(--cyan-500);
      box-shadow: 0 0 0 3px rgba(0, 153, 229, 0.35);
    }}
    .step-dot.done {{
      background: var(--emerald-500);
      box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.35);
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
    <p>شكراً لثقتكم بشركة <b>MESS TECH</b>. تم تأكيد الطلب وتعيين كود الشحنة للبدء فوراً في الفحص الفني للأجهزة قبل التوصيل.</p>
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
            سيتم تحصيل المبلغ الإجمالي البالغ <b class="mono" style="font-size:15px; color:#1e3a8a;">37,950 ج.م</b> نقداً أو عبر بطاقة الدفع (POS) مع مندوب التوصيل بعد فحص ومطابقة كراتين الأجهزة واستلام الفاتورة الضريبية الرسمية.
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
            <div style="font-weight:700; color:var(--navy-900);">مبنى تكنوبوليس الإداري، الدور الرابع، شارع التسعين الشمالي، التجمع الخامس، القاهرة الجديدة.</div>
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
            <div class="mono" style="font-size:12px; color:var(--slate-500);">SKU: VDI2414002 • 100% نحاس نقي معتمد للمشروعات</div>
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
          <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
            <span style="color:var(--slate-500);">ضريبة القيمة المضافة (14% فواتير رسمية):</span>
            <span style="color:var(--slate-500); font-size:12px;">مشمولة ومفصلة بالفاتورة</span>
          </div>
          <div style="border-top:1.5px dashed var(--slate-300); padding-top:10px; margin-top:6px; display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:16px; font-weight:900; color:var(--navy-900);">المبلغ الإجمالي المطلوب تحصيله (COD):</span>
            <span class="mono" style="font-size:22px; font-weight:900; color:var(--cyan-600);">37,950 ج.م</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Side Left Column: Next Steps & Tracking Action -->
    <div>
      <!-- Action Buttons Card -->
      <div class="success-card" style="border: 2px solid #bfdbfe; background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);">
        <h3 style="border-bottom:none; margin-bottom:12px;">إجراءات سريعة لطلبك</h3>
        <p style="font-size:13px; color:var(--slate-500); margin-bottom:20px; line-height:1.6;">
          يمكنك تتبع خط سير المندوب لحظياً حتى وصول الشحنة، أو تحميل نسخة أولية من أمر التوريد.
        </p>

        <a href="09_صفحة_تتبع_الطلب_Desktop_Order_Tracking.png" class="btn-action-primary">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          تتبع مسار وحالة الطلب الآن
        </a>

        <button class="btn-action-secondary">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          تحميل إشعار استلام الطلب (PDF)
        </button>

        <button class="btn-action-secondary" style="border-color:transparent; color:var(--slate-500);">
          ← متابعة التسوق وتصفح العروض الحالية
        </button>
      </div>

      <!-- What Happens Next? Timeline -->
      <div class="success-card">
        <h3>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          ماذا يحدث بعد تأكيد الطلب؟
        </h3>

        <div class="timeline-steps">
          <div class="timeline-step-item">
            <span class="step-dot done"></span>
            <div>
              <div style="font-size:14px; font-weight:800; color:var(--navy-900);">1. استلام وتأكيد الطلب الفوري</div>
              <div style="font-size:12.5px; color:var(--slate-500); margin-top:2px;">تم حجز الأجهزة في مستودع MESS TECH بنجاح وتوليد أمر التوريد الداخلي.</div>
            </div>
          </div>

          <div class="timeline-step-item">
            <span class="step-dot active"></span>
            <div>
              <div style="font-size:14px; font-weight:800; color:var(--cyan-600);">2. الفحص الفني ومطابقة السيريال (الآن)</div>
              <div style="font-size:12.5px; color:var(--slate-500); margin-top:2px;">يقوم مهندس الجودة بمطابقة الأرقام التسلسلية والتأكد من سلامة التغليف المصنعي.</div>
            </div>
          </div>

          <div class="timeline-step-item">
            <span class="step-dot"></span>
            <div>
              <div style="font-size:14px; font-weight:800; color:var(--navy-900);">3. اتصال التأكيد والتحرك للموقع</div>
              <div style="font-size:12.5px; color:var(--slate-500); margin-top:2px;">يتواصل معك مسؤول الشحن قبل التحرك لتأكيد موعد استلام الشحنة بمقركم.</div>
            </div>
          </div>

          <div class="timeline-step-item">
            <span class="step-dot"></span>
            <div>
              <div style="font-size:14px; font-weight:800; color:var(--navy-900);">4. الاستلام والفحص والدفع نقداً</div>
              <div style="font-size:12.5px; color:var(--slate-500); margin-top:2px;">معاينة الكراتين واستلام الفاتورة وسداد المبلغ نقداً عند الاستلام.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Tech Help Card -->
      <div style="background:#0f172a; border-radius:14px; padding:20px; color:#fff; display:flex; align-items:center; gap:16px;">
        <div style="width:48px; height:48px; background:rgba(0, 153, 229, 0.2); border:1px solid var(--cyan-500); border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--cyan-400)" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        </div>
        <div>
          <div style="font-size:14px; font-weight:800; color:#fff;">هل ترغب بتعديل العنوان أو إضافة أصناف؟</div>
          <div style="font-size:12.5px; color:#94a3b8; margin-top:2px;">اتصل فوراً بقسم الدعم والتوريد: <b class="mono" style="color:var(--cyan-400);">0100-MESS-TECH</b></div>
        </div>
      </div>
    </div>
  </main>

  {get_footer_html()}
</body>
</html>
"""

# ==============================================================================
# PAGE 09: ORDER TRACKING & STATUS (Desktop)
# ==============================================================================
PAGE_09_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | تتبع حالة ومسار الطلب - Live Order Tracking</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    .tracking-header-wrap {{
      background: var(--navy-900);
      color: #fff;
      padding: 32px 48px;
      border-bottom: 2px solid var(--navy-700);
    }}
    .tracking-header-container {{
      max-width: 1340px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .search-tracking-box {{
      display: flex;
      align-items: center;
      background: var(--navy-800);
      border: 1.5px solid var(--navy-700);
      border-radius: 10px;
      padding: 4px;
      width: 440px;
    }}
    .search-tracking-box input {{
      flex: 1;
      background: transparent;
      border: none;
      color: #fff;
      padding: 8px 14px;
      font-size: 13.5px;
      outline: none;
    }}
    .search-tracking-box button {{
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 8px 18px;
      border-radius: 7px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
    }}

    .tracking-main-layout {{
      max-width: 1340px;
      margin: 32px auto;
      padding: 0 48px;
      display: grid;
      grid-template-columns: 1.35fr 0.85fr;
      gap: 32px;
      align-items: start;
    }}

    .tracking-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 28px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.03);
      margin-bottom: 24px;
    }}

    /* Horizontal Stepper */
    .stepper-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
      margin: 36px 10px 48px;
    }}
    .stepper-progress-bg {{
      position: absolute;
      top: 24px;
      left: 30px;
      right: 30px;
      height: 4px;
      background: var(--slate-200);
      z-index: 1;
    }}
    .stepper-progress-active {{
      position: absolute;
      top: 24px;
      right: 30px;
      width: 65%;
      height: 4px;
      background: linear-gradient(90deg, var(--cyan-500), #10b981);
      z-index: 2;
    }}
    .step-node {{
      position: relative;
      z-index: 5;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      width: 120px;
      text-align: center;
    }}
    .node-icon-circle {{
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: #fff;
      border: 3px solid var(--slate-300);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      color: var(--slate-400);
      box-shadow: 0 3px 10px rgba(0,0,0,0.05);
      transition: all 0.2s;
    }}
    .node-icon-circle.done {{
      background: #10b981;
      border-color: #059669;
      color: #fff;
    }}
    .node-icon-circle.current {{
      background: var(--cyan-500);
      border-color: #0284c7;
      color: #fff;
      box-shadow: 0 0 0 6px rgba(0, 153, 229, 0.25);
      animation: pulse 2s infinite;
    }}
    .node-title {{
      font-size: 13px;
      font-weight: 800;
      color: var(--navy-900);
    }}
    .node-time {{
      font-size: 11px;
      color: var(--slate-500);
      margin-top: -4px;
    }}

    /* Live Status Badge */
    .status-banner-live {{
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #fff;
      padding: 20px 24px;
      border-radius: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 28px;
    }}

    /* Activity log */
    .log-item {{
      display: flex;
      gap: 18px;
      padding: 14px 0;
      border-bottom: 1px solid var(--slate-100);
    }}
    .log-time {{
      font-family: 'JetBrains Mono';
      font-size: 12px;
      color: var(--slate-500);
      width: 130px;
      flex-shrink: 0;
      text-align: left;
      direction: ltr;
    }}
    .log-content h5 {{
      font-size: 14px;
      font-weight: 800;
      color: var(--navy-900);
      margin-bottom: 3px;
    }}
    .log-content p {{
      font-size: 12.5px;
      color: var(--slate-500);
      margin: 0;
    }}
  </style>
</head>
<body>
  {get_header_html()}

  <!-- Tracking Top Header -->
  <div class="tracking-header-wrap">
    <div class="tracking-header-container">
      <div>
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
          <span class="badge-notice-header" style="background:#0284c7; color:#fff;">بث مباشر للشحنة</span>
          <span style="color:#94a3b8; font-size:13px;">تحديث قبل دقيقتين</span>
        </div>
        <h1 style="font-size:24px; font-weight:900;">تتبع مسار شحنة المعدات: <span class="mono" style="color:var(--cyan-400);">#ORD-9824</span></h1>
      </div>

      <div class="search-tracking-box">
        <input type="text" value="ORD-9824" placeholder="أدخل رقم طلب آخر لتتبعه...">
        <button>تتبع</button>
      </div>
    </div>
  </div>

  <main class="tracking-main-layout">
    <!-- Main Left: Status, Stepper, & Logs -->
    <div>
      <div class="tracking-card">
        <!-- Live Alert Banner -->
        <div class="status-banner-live">
          <div style="display:flex; align-items:center; gap:16px;">
            <div style="width:48px; height:48px; background:rgba(255,255,255,0.2); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:24px;">
              🚚
            </div>
            <div>
              <div style="font-size:12px; color:#e0f2fe; font-weight:700;">الحالة الحالية للشحنة:</div>
              <div style="font-size:19px; font-weight:900;">الشحنة مع مندوب التوصيل — في الطريق إلى موقعكم</div>
            </div>
          </div>
          <div style="text-align:left; background:rgba(0,0,0,0.25); padding:10px 16px; border-radius:8px;">
            <div style="font-size:11px; color:#bae6fd;">موعد الوصول المقدر:</div>
            <div style="font-size:16px; font-weight:900; color:#fff;">اليوم 03:30 م - 05:00 م</div>
          </div>
        </div>

        <!-- 5-Step Horizontal Stepper -->
        <div class="stepper-bar">
          <div class="stepper-progress-bg"></div>
          <div class="stepper-progress-active"></div>

          <!-- Step 1 -->
          <div class="step-node">
            <div class="node-icon-circle done">✓</div>
            <div class="node-title">تم استلام الطلب</div>
            <div class="node-time mono">15 Nov - 10:15 AM</div>
          </div>

          <!-- Step 2 -->
          <div class="step-node">
            <div class="node-icon-circle done">✓</div>
            <div class="node-title">الفحص والتجهيز</div>
            <div class="node-time mono">15 Nov - 02:45 PM</div>
          </div>

          <!-- Step 3 -->
          <div class="step-node">
            <div class="node-icon-circle done">✓</div>
            <div class="node-title">تم التحميل للسيارة</div>
            <div class="node-time mono">16 Nov - 09:30 AM</div>
          </div>

          <!-- Step 4 (Current) -->
          <div class="step-node">
            <div class="node-icon-circle current">🚚</div>
            <div class="node-title" style="color:var(--cyan-600);">مع المندوب بالطريق</div>
            <div class="node-time mono">16 Nov - 01:20 PM</div>
          </div>

          <!-- Step 5 -->
          <div class="step-node">
            <div class="node-icon-circle">🏠</div>
            <div class="node-title" style="color:var(--slate-400);">التسليم والتحصيل</div>
            <div class="node-time mono">متوقع اليوم</div>
          </div>
        </div>

        <!-- Live Activity Detailed Log -->
        <h4 style="font-size:16px; font-weight:800; color:var(--navy-900); margin:32px 0 16px; padding-bottom:10px; border-bottom:1px solid var(--slate-100);">
          سجل تحركات الشحنة بالتفصيل (Detailed Audit Log)
        </h4>

        <div class="log-item">
          <div class="log-time">16 Nov • 01:20 PM</div>
          <div class="log-content">
            <h5 style="color:var(--cyan-600);">الشحنة خرجت للتسليم بصحبة الكابتن أحمد محمود</h5>
            <p>السيارة متجهة الآن إلى منطقة التجمع الخامس - شارع التسعين الشمالي.</p>
          </div>
        </div>

        <div class="log-item">
          <div class="log-time">16 Nov • 09:30 AM</div>
          <div class="log-content">
            <h5>تم فحص وتحميل الأجهزة بسيارة النقل المجهزة ضد الصدمات</h5>
            <p>مستودع MESS TECH الرئيسي - المنطقة الصناعية بالعبور.</p>
          </div>
        </div>

        <div class="log-item">
          <div class="log-time">15 Nov • 02:45 PM</div>
          <div class="log-content">
            <h5>مطابقة الأرقام التسلسلية (Serial Numbers) وإصدار الفاتورة</h5>
            <p>فحص وتغليف سويتش سيسكو WS-C2960X وراوتر مايكروتك والتأكد من مطابقة المواصفات 100%.</p>
          </div>
        </div>

        <div class="log-item">
          <div class="log-time">15 Nov • 10:15 AM</div>
          <div class="log-content">
            <h5>تم تأكيد الطلب إلكترونياً بنظام الدفع عند الاستلام (COD)</h5>
            <p>تم إشعار إدارة المستودع بحجز الأصناف فوراً.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Side Right Column: Driver & Destination Info -->
    <div>
      <!-- Driver Card -->
      <div class="tracking-card" style="border: 1.5px solid #bae6fd; background:#f0f9ff;">
        <h4 style="font-size:16px; font-weight:800; color:#0369a1; margin-bottom:16px; display:flex; align-items:center; gap:8px;">
          <span>👤</span> مسؤول التوصيل والشحن
        </h4>
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:16px;">
          <div style="width:56px; height:56px; background:#0284c7; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:22px; font-weight:900;">
            أ م
          </div>
          <div>
            <div style="font-size:16px; font-weight:800; color:var(--navy-900);">كابتن أحمد محمود</div>
            <div style="font-size:12.5px; color:var(--slate-500);">مندوب أسطول النقل المعتمد لـ MESS TECH</div>
            <div style="font-size:12px; color:#059669; font-weight:700; margin-top:2px;">سيارة فان مجهزة ومغلقة ضد الأتربة</div>
          </div>
        </div>

        <div style="background:#fff; border:1px solid #bfdbfe; border-radius:10px; padding:12px; margin-bottom:14px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:11.5px; color:var(--slate-500);">الاتصال بالمندوب مباشرة:</div>
            <div class="mono" style="font-size:16px; font-weight:800; color:#0284c7;">0112-345-6789</div>
          </div>
          <button style="background:#0284c7; color:#fff; border:none; padding:8px 14px; border-radius:8px; font-size:12.5px; font-weight:700; cursor:pointer;">
            اتصال فوري
          </button>
        </div>
      </div>

      <!-- Payment & Receipt Info -->
      <div class="tracking-card">
        <h4 style="font-size:16px; font-weight:800; color:var(--navy-900); margin-bottom:14px;">
          ملخص التحصيل والاستلام
        </h4>
        <div style="font-size:13px; line-height:1.7; color:var(--slate-600); margin-bottom:16px;">
          <div>طريقة الدفع: <b style="color:#1d4ed8;">الدفع نقداً عند الاستلام (COD)</b></div>
          <div>المبلغ المطلوب تجهيزه: <b class="mono" style="font-size:16px; color:var(--navy-900);">37,950 ج.م</b></div>
          <div>العنوان: <b>تكنوبوليس، شارع التسعين الشمالي، التجمع الخامس</b></div>
        </div>

        <button style="width:100%; background:var(--navy-900); color:#fff; border:none; padding:12px; border-radius:8px; font-size:13.5px; font-weight:700; display:flex; align-items:center; justify-content:center; gap:8px; cursor:pointer;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          معاينة وتنزيل أمر التوريد المبدئي
        </button>
      </div>
    </div>
  </main>

  {get_footer_html()}
</body>
</html>
"""

# ==============================================================================
# PAGE 10: AUTHENTICATION / LOGIN / REGISTER / OTP (Desktop)
# ==============================================================================
PAGE_10_HTML = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | تسجيل الدخول وإنشاء حساب الشركات والمهندسين</title>
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
      max-width: 1200px;
      margin: 48px auto;
      padding: 0 40px;
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: 56px;
      align-items: center;
      flex: 1;
    }}

    /* Left Brand Showcase */
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

    /* Right Auth Card */
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

    .otp-demonstrator-box {{
      background: #f8fafc;
      border: 1.5px dashed #0284c7;
      border-radius: 12px;
      padding: 16px;
      margin-top: 18px;
      text-align: center;
    }}
    .otp-boxes {{
      display: flex;
      justify-content: center;
      gap: 12px;
      margin: 12px 0;
    }}
    .otp-digit {{
      width: 48px;
      height: 52px;
      background: #fff;
      border: 2px solid #0284c7;
      border-radius: 10px;
      font-size: 24px;
      font-weight: 900;
      color: var(--navy-900);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'JetBrains Mono';
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
      <h1>بوابة الشركات والمهندسين<br><span style="color:var(--cyan-400);">لتوريد حلول وتجهيزات الشبكات</span></h1>
      <p>
        سجل دخولك الآن للوصول إلى أسعار التوريد الحصرية، تتبع مباشر لطلباتكم ومطابقة أرقام السيريال، وتحميل الفواتير الإلكترونية المعتمدة بضغطة زر.
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
            <div style="font-weight:800; font-size:14px;">تسجيل ومطابقة السيريال في حسابك</div>
            <div style="font-size:12px; color:#94a3b8;">حفظ أرقام السيريال للأجهزة لسهولة إدارة الشبكة ومطابقة الضمان.</div>
          </div>
        </div>

        <div class="feature-pill">
          <div class="feature-pill-icon">📄</div>
          <div>
            <div style="font-weight:800; font-size:14px;">فواتير ضريبية رسمية للشركات</div>
            <div style="font-size:12px; color:#94a3b8;">إصدار فوري للفاتورة الضريبية باسم شركتكم وسجلها التجاري.</div>
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

        <!-- Or OTP Quick Verification Demo -->
        <div class="otp-demonstrator-box">
          <div style="font-size:12px; font-weight:800; color:#0369a1; display:flex; align-items:center; justify-content:center; gap:6px;">
            <span>📱</span> أو تسجيل الدخول برمز التحقق الفوري (SMS OTP)
          </div>
          <div style="font-size:11.5px; color:var(--slate-500); margin-top:2px;">تم إرسال رمز التحقق إلى <b class="mono" style="color:var(--navy-900);">0100****4567</b></div>

          <div class="otp-boxes">
            <div class="otp-digit">4</div>
            <div class="otp-digit">8</div>
            <div class="otp-digit">2</div>
            <div class="otp-digit">1</div>
          </div>

          <div style="font-size:11px; color:#059669; font-weight:700;">
            ✓ تم التحقق بنجاح — جاري الدخول للوحة حسابك...
          </div>
        </div>

        <div style="margin-top:20px; text-align:center; font-size:13px; color:var(--slate-500);">
          ليس لديك حساب بعد؟ <a href="#" style="color:var(--cyan-600); font-weight:800; text-decoration:none;">سجل حساب شركة الآن</a>
        </div>
      </div>
    </div>
  </div>

  {get_footer_html()}
</body>
</html>
"""

def generate_desktop_pages_1():
    print("Generating Desktop Pages 08, 09, 10...")
    
    # Page 08
    p08_html = os.path.join(DESIGNS_DIR, "page_08_order_success.html")
    p08_png = os.path.join(DESIGNS_DIR, "08_صفحة_نجاح_الطلب_Desktop_Order_Success.png")
    with open(p08_html, "w", encoding="utf-8") as f:
        f.write(PAGE_08_HTML)
    render_html_to_png(p08_html, p08_png, height=1850)

    # Page 09
    p09_html = os.path.join(DESIGNS_DIR, "page_09_order_tracking.html")
    p09_png = os.path.join(DESIGNS_DIR, "09_صفحة_تتبع_الطلب_Desktop_Order_Tracking.png")
    with open(p09_html, "w", encoding="utf-8") as f:
        f.write(PAGE_09_HTML)
    render_html_to_png(p09_html, p09_png, height=1700)

    # Page 10
    p10_html = os.path.join(DESIGNS_DIR, "page_10_auth_login.html")
    p10_png = os.path.join(DESIGNS_DIR, "10_تسجيل_الدخول_وإنشاء_حساب_Desktop_Auth_Login.png")
    with open(p10_html, "w", encoding="utf-8") as f:
        f.write(PAGE_10_HTML)
    render_html_to_png(p10_html, p10_png, height=1400)

if __name__ == "__main__":
    generate_desktop_pages_1()
