# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS, get_header_html, get_footer_html
from prepare_svgs import SVG_CISCO_SWITCH

DESIGNS_DIR = r"E:\mess\designs"

HTML_CONTENT = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | السلة وإتمام الطلب في خطوة واحدة - الدفع كاش عند الاستلام COD</title>
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

    /* One-Step Checkout Grid */
    .checkout-layout {{
      max-width: 1340px;
      margin: 24px auto 0;
      padding: 0 48px;
      display: grid;
      grid-template-columns: 1.25fr 0.95fr;
      gap: 36px;
      align-items: start;
    }}

    /* Form Column (Right in RTL) */
    .checkout-form-column {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    .step-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 24px 28px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }}
    .step-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--slate-100);
    }}
    .step-number-badge {{
      width: 32px;
      height: 32px;
      background: var(--navy-900);
      color: var(--cyan-400);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 14px;
    }}
    .step-title {{
      font-size: 17px;
      font-weight: 800;
      color: var(--navy-900);
    }}

    /* Inputs */
    .form-grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }}
    .form-group {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .form-label {{
      font-size: 13px;
      font-weight: 700;
      color: #334155;
    }}
    .form-input {{
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: 9px;
      padding: 11px 14px;
      font-size: 13.5px;
      color: var(--navy-900);
      outline: none;
      transition: all 0.2s;
    }}
    .form-input:focus {{
      border-color: var(--cyan-500);
      background: #fff;
      box-shadow: 0 0 0 3px rgba(0, 153, 229, 0.15);
    }}

    /* Delivery Option Pills */
    .delivery-options-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 18px;
    }}
    .delivery-radio-card {{
      border: 2px solid var(--slate-200);
      border-radius: 12px;
      padding: 16px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: all 0.2s;
      background: #f8fafc;
    }}
    .delivery-radio-card.active {{
      border-color: var(--cyan-500);
      background: #f0f9ff;
    }}
    .delivery-title-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 14px;
      font-weight: 800;
      color: var(--navy-900);
    }}
    .delivery-desc {{
      font-size: 12px;
      color: #64748b;
      line-height: 1.4;
    }}

    /* COD Locked Payment Box */
    .cod-payment-card {{
      background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
      border: 2px solid #10b981;
      border-radius: 12px;
      padding: 20px;
      position: relative;
    }}
    .cod-badge-selected {{
      position: absolute;
      top: 16px;
      left: 16px;
      background: #10b981;
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .cod-header-line {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 8px;
    }}
    .cod-title {{
      font-size: 16px;
      font-weight: 800;
      color: #065f46;
    }}
    .cod-info-text {{
      font-size: 13px;
      color: #166534;
      line-height: 1.6;
    }}

    /* Summary Column (Left in RTL) */
    .order-summary-column {{
      position: sticky;
      top: 24px;
    }}
    .summary-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 4px 18px rgba(0,0,0,0.04);
    }}
    .summary-title {{
      font-size: 18px;
      font-weight: 800;
      color: var(--navy-900);
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--slate-100);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    /* Cart Items list */
    .cart-items-list {{
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-bottom: 20px;
    }}
    .cart-item-row {{
      display: flex;
      gap: 12px;
      align-items: center;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--slate-100);
    }}
    .cart-item-thumb {{
      width: 60px;
      height: 60px;
      background: #f8fafc;
      border: 1px solid var(--slate-200);
      border-radius: 8px;
      padding: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .cart-item-info {{ flex: 1; }}
    .cart-item-title {{
      font-size: 13px;
      font-weight: 700;
      color: var(--navy-900);
      line-height: 1.4;
    }}
    .cart-item-model {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--slate-500);
    }}
    .cart-item-price-qty {{
      font-size: 13px;
      font-weight: 800;
      color: var(--navy-900);
      margin-top: 4px;
    }}

    /* Coupon Box */
    .coupon-box {{
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
    }}
    .coupon-input {{
      flex: 1;
      background: #f8fafc;
      border: 1.5px dashed #cbd5e1;
      border-radius: 8px;
      padding: 8px 12px;
      font-size: 13px;
      text-transform: uppercase;
      font-family: 'JetBrains Mono', monospace;
    }}
    .btn-apply-coupon {{
      background: var(--navy-900);
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
    }}

    /* Calculations breakdown */
    .calc-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 20px;
      font-size: 13.5px;
    }}
    .calc-row {{
      display: flex;
      justify-content: space-between;
      color: #475569;
    }}
    .calc-row.highlight-free {{
      color: #059669;
      font-weight: 700;
    }}
    .calc-row.total-due {{
      border-top: 2px solid var(--slate-200);
      padding-top: 14px;
      font-size: 20px;
      font-weight: 900;
      color: var(--navy-900);
    }}

    /* Place Order CTA */
    .btn-place-order-cod {{
      width: 100%;
      background: linear-gradient(135deg, var(--cyan-600) 0%, var(--cyan-500) 100%);
      color: #fff;
      border: none;
      padding: 16px;
      border-radius: 12px;
      font-size: 16px;
      font-weight: 900;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      white-space: nowrap;
      box-shadow: 0 4px 20px rgba(0, 153, 229, 0.4);
    }}
    .trust-footer-strip {{
      margin-top: 16px;
      display: flex;
      justify-content: center;
      gap: 16px;
      font-size: 11.5px;
      color: #64748b;
    }}
  </style>
</head>
<body>

  {get_header_html(active_cat="")}

  <!-- Breadcrumbs -->
  <div class="breadcrumb-bar">
    <a href="#">الرئيسية</a>
    <span>›</span>
    <a href="#">سلة المشتريات</a>
    <span>›</span>
    <span class="breadcrumb-current">إتمام الطلب في خطوة واحدة (One-Page Checkout)</span>
  </div>

  <main class="checkout-layout">

    <!-- Right Side: Fast 1-Step Form -->
    <div class="checkout-form-column">

      <!-- Step 1: Customer Contact -->
      <div class="step-card">
        <div class="step-header">
          <div class="step-number-badge">1</div>
          <div>
            <div class="step-title">بيانات العميل والتواصل (Customer Information)</div>
            <div style="font-size:12px; color:#64748b;">يمكنك الشراء السريع كضيف دون الحاجة لإنشاء حساب مسبق</div>
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">الاسم بالكامل أو اسم الشركة *</label>
            <input type="text" class="form-input" value="م. أحمد فتحي (شركة دلتا للحلول المتكاملة)">
          </div>
          <div class="form-group">
            <label class="form-label">رقم الهاتف الأساسي (مطلوب للتوصيل) *</label>
            <input type="text" class="form-input mono" value="0100 234 5678">
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">البريد الإلكتروني (لتلقي إشعار وبوليصة الطلب)</label>
            <input type="email" class="form-input mono" value="ahmed.fathi@deltatech.com">
          </div>
          <div class="form-group">
            <label class="form-label">رقم هاتف بديل (اختياري)</label>
            <input type="text" class="form-input mono" placeholder="0110 000 0000">
          </div>
        </div>
      </div>

      <!-- Step 2: Delivery Method -->
      <div class="step-card">
        <div class="step-header">
          <div class="step-number-badge">2</div>
          <div>
            <div class="step-title">طريقة الاستلام وعنوان التوصيل (Delivery Address)</div>
            <div style="font-size:12px; color:#64748b;">تحديد وجهة الشحن لحساب تكلفة الشحن آلياً للمحافظة</div>
          </div>
        </div>

        <div class="delivery-options-grid">
          <div class="delivery-radio-card active">
            <div class="delivery-title-row">
              <span>توصيل للمقر أو الشركة</span>
              <span style="color:#059669; font-size:12px;">شحن مؤمن</span>
            </div>
            <div class="delivery-desc">تسليم عبر مندوب MESS TECH خلال 24 إلى 48 ساعة لكافة محافظات مصر.</div>
          </div>

          <div class="delivery-radio-card">
            <div class="delivery-title-row">
              <span>استلام مباشر من الفرع</span>
              <span style="color:var(--cyan-600); font-size:12px;">مجاناً (0 ج.م)</span>
            </div>
            <div class="delivery-desc">استلام فوري من مقر الشركة (فرع المعادي / القاهرة) ومعاينة الأجهزة فوراً.</div>
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">المحافظة (لحساب الشحن) *</label>
            <select class="form-input" style="cursor:pointer; font-weight:700;">
              <option selected>القاهرة (شحن مجاني للطلبات فوق 20,000 ج.م)</option>
              <option>الجيزة (شحن مجاني)</option>
              <option>الإسكندرية</option>
              <option>الدلتا والوجه البحري</option>
              <option>مدن القناة</option>
              <option>محافظات الصعيد</option>
            </select>
          </div>
          <div class="form-group">
            <label class="form-label">المدينة / الحي *</label>
            <input type="text" class="form-input" value="المعادي الجديدة">
          </div>
        </div>

        <div class="form-group" style="margin-bottom:16px;">
          <label class="form-label">العنوان التفصيلي (الشارع، رقم المبنى، الدور) *</label>
          <input type="text" class="form-input" value="شارع النصر، عمارة 14، الدور الخامس، مقر الشركة">
        </div>

        <div class="form-group">
          <label class="form-label">ملاحظات لمندوب الشحن ومواعيد التواجد</label>
          <input type="text" class="form-input" placeholder="مثال: التواجد متاح من 9 صباحاً حتى 5 مساءً...">
        </div>
      </div>

      <!-- Step 3: Payment Method (COD Only) -->
      <div class="step-card">
        <div class="step-header">
          <div class="step-number-badge">3</div>
          <div>
            <div class="step-title">طريقة الدفع (Payment Method)</div>
            <div style="font-size:12px; color:#64748b;">نظام الدفع المعتمد في متجر MESS TECH</div>
          </div>
        </div>

        <div class="cod-payment-card">
          <span class="cod-badge-selected">محدد تلقائياً</span>
          <div class="cod-header-line">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 12 15 16 10"/></svg>
            <div class="cod-title">الدفع نقداً عند الاستلام (Cash on Delivery - COD) فقط</div>
          </div>
          <p class="cod-info-text">
            حرصاً على أمان وموثوقية التعامل مع الشركات والمشروعات: <b>لا يتطلب المتجر أي بطاقات دفع إلكتروني أو فيزا</b>. ستقوم بمعاينة الأجهزة، التأكد من سريال الموديلات والفاتورة الضريبية، ثم سداد المبلغ نقداً لمندوب التسليم.
          </p>
        </div>
      </div>
    </div>

    <!-- Left Side: Order Summary -->
    <aside class="order-summary-column">
      <div class="summary-card">
        <div class="summary-title">
          <span>ملخص الأوردر (منتجين)</span>
          <a href="#" style="font-size:12px; color:var(--cyan-600); text-decoration:none;">تعديل السلة</a>
        </div>

        <!-- Items -->
        <div class="cart-items-list">
          <div class="cart-item-row">
            <div class="cart-item-thumb">{SVG_CISCO_SWITCH}</div>
            <div class="cart-item-info">
              <div class="cart-item-title">سويتش سيسكو كاتاليست 24 بورت PoE+</div>
              <div class="cart-item-model">WS-C2960X-24TD-L • الكمية: 2</div>
              <div class="cart-item-price-qty">39,700 ج.م</div>
            </div>
          </div>

          <div class="cart-item-row">
            <div class="cart-item-thumb">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#334155" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 7h10M7 12h10M7 17h10"/></svg>
            </div>
            <div class="cart-item-info">
              <div class="cart-item-title">كابينة راك 9U جداري معتمدة مع مراوح</div>
              <div class="cart-item-model">RACK-WALL-9U • الكمية: 1</div>
              <div class="cart-item-price-qty">3,500 ج.م</div>
            </div>
          </div>
        </div>

        <!-- Coupon code -->
        <div class="coupon-box">
          <input type="text" class="coupon-input" value="MESS2026" placeholder="كود الخصم">
          <button class="btn-apply-coupon">تم التطبيق ✓</button>
        </div>

        <!-- Totals breakdown -->
        <div class="calc-list">
          <div class="calc-row">
            <span>المجموع الفرعي:</span>
            <span>43,200 ج.م</span>
          </div>
          <div class="calc-row highlight-free">
            <span>الشحن للمحافظة (القاهرة):</span>
            <span>مجاني (تجاوز 20,000 ج.م)</span>
          </div>
          <div class="calc-row" style="color:var(--rose-500); font-weight:700;">
            <span>خصم الكوبون (MESS2026):</span>
            <span>- 1,000 ج.م</span>
          </div>
          <div class="calc-row total-due">
            <span>الإجمالي المستحق عند الاستلام (COD):</span>
            <span style="color:var(--cyan-600);">42,200 <small style="font-size:14px; font-weight:600; color:#64748b;">ج.م</small></span>
          </div>
        </div>

        <!-- Place Order Button -->
        <button class="btn-place-order-cod">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          تأكيد الطلب الآن - الدفع عند الاستلام
        </button>

        <div class="trust-footer-strip">
          <span>✓ فاتورة ضريبية رسمية</span>
          <span>✓ فحص ومعاينة قبل الدفع</span>
          <span>✓ أجهزة أصلية معتمدة 100%</span>
        </div>
      </div>
    </aside>
  </main>

  {get_footer_html()}

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "page_05_cart_checkout.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "05_صفحة_السلة_واتمام_الطلب_Desktop_Cart_Checkout_COD.png")
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,2100",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=3000",
    f"--screenshot={png_path}",
    f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
]
subprocess.run(cmd, check=True)
print(f"Rendered: {png_path} ({os.path.getsize(png_path)/1024:.1f} KB)")

