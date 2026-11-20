# -*- coding: utf-8 -*-
"""
apply_b2c_transformations.py
Executes the strategic B2C transformations across all desktop and mobile screens:
1. Cleans up Datasheet download, B2B company fields, and engineer/contractor phrasing.
2. Adds standard E-Commerce elements: Promo Code, Wishlist (❤️), Buy Now button, 14-day return policy, Product Variants, and Free Shipping Progress Bar.
3. Re-renders all impacted screens and synchronizes the Figma canvas.
"""

import os
import re
import subprocess
import shutil

DESIGNS_DIR = r"E:\mess\designs"
ROOT_DIR = r"E:\mess"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(">>> Starting B2C Transformations...")

# ==============================================================================
# 1. UPDATE make_page_01.py
# ==============================================================================
print("Updating make_page_01.py...")
p1_code = read_file(os.path.join(DESIGNS_DIR, "make_page_01.py"))

# Replace title & hero sub
p1_code = p1_code.replace("الموزع المعتمد لحلول الشبكات والأمان للمشروعات والشركات", "متجركم الأول لأحدث أجهزة الشبكات والإلكترونيات وأنظمة المراقبة الذكية")
p1_code = p1_code.replace("سعر التوريد (شامل الضريبة)", "السعر الحالي شامل الضريبة")
p1_code = p1_code.replace("للأمن السيبراني والشركات", "للأمن السيبراني وحماية الشبكات")
p1_code = p1_code.replace("فريق مهندسي شبكات لمساعدتك في اختيار الموديل وضبط التكوينات والإعدادات.", "فريق خدمة العملاء جاهز لمساعدتكم في اختيار ومطابقة أنسب الأجهزة طوال الأسبوع.")
p1_code = p1_code.replace("تصفح حلول التجهيزات والشبكات", "تصفح أحدث أجهزة الشبكات والمراقبة")
p1_code = p1_code.replace("توريد", "طلب")

# Update hero trust items
old_trust = """    .hero-trust-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 24px;
    }"""
new_trust_css = """    .hero-trust-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 24px;
    }
    .card-wishlist-btn {
      position: absolute;
      top: 12px;
      left: 12px;
      width: 34px;
      height: 34px;
      background: #fff;
      border: 1px solid #e2e8f0;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #f43f5e;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
      z-index: 5;
    }"""
if old_trust in p1_code and ".card-wishlist-btn" not in p1_code:
    p1_code = p1_code.replace(old_trust, new_trust_css)

write_file(os.path.join(DESIGNS_DIR, "make_page_01.py"), p1_code)

# ==============================================================================
# 2. UPDATE make_page_02.py (Product Details: Variants, Buy Now, Wishlist, No Datasheet)
# ==============================================================================
print("Updating make_page_02.py...")
p2_code = read_file(os.path.join(DESIGNS_DIR, "make_page_02.py"))

# Clean up datasheet callout in HTML
old_ds_html = """      <!-- Datasheet Download Callout -->
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
      </div>"""

new_confidence_html = """      <!-- B2C Confidence & Return Guarantee Box -->
      <div style="margin-top:20px; background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border:1px solid #334155; border-radius:12px; padding:18px 20px; color:#fff; display:flex; flex-direction:column; gap:12px;">
        <div style="font-size:13.5px; font-weight:800; color:var(--cyan-400); border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:8px; display:flex; align-items:center; gap:8px;">
          <span>🛡️</span> ضمان وثقة المشتري مع MESS TECH
        </div>
        <div style="display:flex; align-items:center; gap:10px; font-size:12.5px;">
          <span style="color:#10b981; font-weight:800;">✓</span>
          <span><b>إرجاع واستبدال مجاني خلال 14 يوماً:</b> وفق حماية المستهلك مع استرداد نقدي كامل.</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px; font-size:12.5px;">
          <span style="color:#38bdf8; font-weight:800;">✓</span>
          <span><b>شحن سريع لباب المنزل:</b> توصيل خلال 24 إلى 48 ساعة لكافة محافظات مصر.</span>
        </div>
        <div style="display:flex; align-items:center; gap:10px; font-size:12.5px;">
          <span style="color:#f59e0b; font-weight:800;">✓</span>
          <span><b>معاينة قبل الدفع:</b> افتح الشحنة وافحص جهازك ومشتملاته قبل سداد الكاش للمندوب.</span>
        </div>
      </div>"""

if old_ds_html in p2_code:
    p2_code = p2_code.replace(old_ds_html, new_confidence_html)

# Add Product Variants selector before Key Specs
old_specs_target = """        <!-- Key Specs Matrix -->
        <div class="key-specs-grid">"""

new_variants_and_specs = """        <!-- Product Options / Variants -->
        <div style="margin-bottom:18px;">
          <div style="font-size:13px; font-weight:800; color:var(--navy-900); margin-bottom:8px;">اختر سعة المنافذ والموديل:</div>
          <div style="display:flex; gap:12px;">
            <div style="background:#f0f9ff; border:2px solid var(--cyan-500); border-radius:10px; padding:10px 16px; cursor:pointer; flex:1;">
              <div style="font-size:13.5px; font-weight:800; color:var(--cyan-600);">24 بورت Gigabit PoE+</div>
              <div style="font-size:11.5px; color:#64748b;">طاقة 370W • متوفر بالمخزون</div>
            </div>
            <div style="background:#f8fafc; border:1.5px solid var(--slate-200); border-radius:10px; padding:10px 16px; cursor:pointer; flex:1;">
              <div style="font-size:13.5px; font-weight:700; color:#334155;">48 بورت Gigabit PoE+</div>
              <div style="font-size:11.5px; color:#64748b;">طاقة 740W (+14,000 ج.م)</div>
            </div>
          </div>
        </div>

        <!-- Key Specs Matrix -->
        <div class="key-specs-grid">"""

if old_specs_target in p2_code:
    p2_code = p2_code.replace(old_specs_target, new_variants_and_specs)

# Replace action buttons with Buy Now + Add to Cart + Wishlist
old_actions_block = """          <div class="action-row-main">
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
          </a>"""

new_actions_block = """          <div class="action-row-main" style="display:flex; gap:10px; align-items:center;">
            <div class="qty-picker">
              <button class="qty-btn">-</button>
              <div class="qty-display">1</div>
              <button class="qty-btn">+</button>
            </div>

            <!-- Add to Cart -->
            <button class="btn-add-cart-primary" style="flex:1; white-space:nowrap; display:inline-flex; align-items:center; justify-content:center; gap:8px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
              <span>أضف للسلة</span>
            </button>

            <!-- Buy Now Direct -->
            <a href="05_صفحة_السلة_واتمام_الطلب_Desktop_Cart_Checkout_COD.png" style="background:linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color:#fff; padding:13px 22px; border-radius:10px; font-size:14.5px; font-weight:800; text-decoration:none; display:inline-flex; align-items:center; gap:8px; box-shadow:0 4px 14px rgba(245,158,11,0.35); white-space:nowrap;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              <span>شراء الآن</span>
            </a>

            <!-- Wishlist Button -->
            <button title="إضافة إلى المفضلة" style="width:48px; height:48px; background:#fff; border:1.5px solid #fecdd3; border-radius:10px; display:inline-flex; align-items:center; justify-content:center; cursor:pointer; color:#f43f5e; box-shadow:0 2px 8px rgba(244,63,94,0.15);">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="#f43f5e" stroke="#f43f5e" stroke-width="1"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
            </button>
          </div>"""

if old_actions_block in p2_code:
    p2_code = p2_code.replace(old_actions_block, new_actions_block)

# Replace reviews & terms
p2_code = p2_code.replace("(24 تقييم مهندسي شبكات ومشروعات)", "(4.9 ★ • 24 تقييم مشتري معتمد)")
p2_code = p2_code.replace("تقييمات مهندسي المشروعات (24)", "تقييمات ومراجعات المشترين (24)")
p2_code = p2_code.replace('أو خيار "اطلب للتوريد" للكميات الكبيرة', '✓ توصيل سريع لباب المنزل مع المعاينة قبل الدفع')
p2_code = p2_code.replace("توريد", "طلب")

write_file(os.path.join(DESIGNS_DIR, "make_page_02.py"), p2_code)

# ==============================================================================
# 3. UPDATE make_page_03.py (Catalog)
# ==============================================================================
print("Updating make_page_03.py...")
p3_code = read_file(os.path.join(DESIGNS_DIR, "make_page_03.py"))
p3_code = p3_code.replace("سويتشات الشبكات المعتمدة للشركات والمشروعات", "سويتشات وأجهزة الشبكات الأصلية المعتمدة")
p3_code = p3_code.replace("اطلب للتوريد (مشروعات)", "أضف للسلة")
p3_code = p3_code.replace("اطلب للتوريد المباشر", "طلب سريع")
p3_code = p3_code.replace("الأكثر طلباً وتوريداً", "الأكثر مبيعاً وتقييماً")
p3_code = p3_code.replace("توريد", "طلب")
write_file(os.path.join(DESIGNS_DIR, "make_page_03.py"), p3_code)

# ==============================================================================
# 4. UPDATE make_page_04.py (Comparison)
# ==============================================================================
print("Updating make_page_04.py...")
p4_code = read_file(os.path.join(DESIGNS_DIR, "make_page_04.py"))
p4_code = p4_code.replace("حالة التوريد والاعتماد", "حالة التوفر والضمان")
p4_code = p4_code.replace("توريد", "طلب")
write_file(os.path.join(DESIGNS_DIR, "make_page_04.py"), p4_code)

# ==============================================================================
# 5. UPDATE make_page_05.py (Cart & Checkout: Coupon, Free Shipping Bar, Clean Fields)
# ==============================================================================
print("Updating make_page_05.py...")
p5_code = read_file(os.path.join(DESIGNS_DIR, "make_page_05.py"))

# Clean Step 1 inputs (remove company)
old_step1_inputs = """        <div class="form-grid-2">
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
        </div>"""

new_step1_inputs = """        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">الاسم بالكامل (الاسم الأول واسم العائلة) *</label>
            <input type="text" class="form-input" value="أحمد فتحي الكردي">
          </div>
          <div class="form-group">
            <label class="form-label">رقم الهاتف الأساسي (للتواصل والتوصيل) *</label>
            <input type="text" class="form-input mono" value="0100 234 5678">
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">البريد الإلكتروني (لتأكيد استلام الطلب)</label>
            <input type="email" class="form-input mono" value="ahmed.fathi@gmail.com">
          </div>
          <div class="form-group">
            <label class="form-label">رقم هاتف بديل (اختياري)</label>
            <input type="text" class="form-input mono" placeholder="0110 000 0000">
          </div>
        </div>"""

if old_step1_inputs in p5_code:
    p5_code = p5_code.replace(old_step1_inputs, new_step1_inputs)

# Delivery address and text
p5_code = p5_code.replace("توصيل وشحن سريع للمقر أو العنوان", "توصيل وشحن سريع لباب المنزل")
p5_code = p5_code.replace("تسليم عبر أسطول مندوبي MESS TECH خلال 24 إلى 48 ساعة لكافة محافظات مصر مع الفحص والمعاينة.", "تسليم سريع حتى باب المنزل خلال 24-48 ساعة لكافة محافظات مصر مع الفحص والمعاينة قبل السداد.")
p5_code = p5_code.replace('value="شارع النصر، عمارة 14، الدور الخامس، مقر الشركة"', 'value="شارع النصر، عمارة 14، شقة 5، المعادي الجديدة"')

# COD Box text
old_cod_desc = """            حرصاً على أمان وموثوقية التعامل مع الشركات والمشروعات: <b>لا يتطلب المتجر أي بطاقات دفع إلكتروني أو فيزا</b>. ستقوم بمعاينة الأجهزة، التأكد من سريال الموديلات والفاتورة الضريبية، ثم سداد المبلغ نقداً لمندوب التسليم."""
new_cod_desc = """            حرصاً على راحتك وأمان مشترياتك: <b>لا يتطلب المتجر أي بطاقات بنكية مسبقة أو دفع إلكتروني</b>. استلم شحنتك أولاً وافحص أجهزتك عند باب منزلك، ثم قم بسداد المبلغ نقداً لمندوب التوصيل."""
if old_cod_desc in p5_code:
    p5_code = p5_code.replace(old_cod_desc, new_cod_desc)

# Summary: Add Free Shipping Progress Bar & Coupon Box
old_summary_header = """        <div class="summary-title">
          <span>ملخص الأوردر (منتجين)</span>
          <a href="#" style="font-size:12px; color:var(--cyan-600); text-decoration:none;">تعديل السلة</a>
        </div>"""

new_summary_header = """        <div class="summary-title">
          <span>ملخص الأوردر (منتجين)</span>
          <a href="#" style="font-size:12px; color:var(--cyan-600); text-decoration:none;">تعديل السلة</a>
        </div>

        <!-- Free Shipping Progress Bar -->
        <div style="background:#ecfdf5; border:1px solid #a7f3d0; border-radius:10px; padding:12px 14px; margin-bottom:18px;">
          <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:800; color:#065f46; margin-bottom:6px;">
            <span>🚚 شحن منزلي مجاني لكافة طلباتك</span>
            <span>مؤهل 100%</span>
          </div>
          <div style="height:6px; background:#d1fae5; border-radius:999px; overflow:hidden;">
            <div style="width:100%; height:100%; background:#10b981;"></div>
          </div>
          <div style="font-size:11.5px; color:#047857; margin-top:5px;">🎉 رائع! طلبك مؤهل للشحن السريع المجاني لباب المنزل.</div>
        </div>"""

if old_summary_header in p5_code and "Free Shipping Progress Bar" not in p5_code:
    p5_code = p5_code.replace(old_summary_header, new_summary_header)

# Coupon box with promo code discount
old_coupon_box = """        <!-- Coupon Box -->
        <div class="coupon-box">
          <input type="text" class="coupon-input" placeholder="كود الخصم (إن وجد)">
          <button class="btn-apply-coupon">تطبيق</button>
        </div>"""

new_coupon_box = """        <!-- Coupon Box -->
        <div style="margin-bottom:18px;">
          <div style="font-size:12px; font-weight:700; color:#475569; margin-bottom:6px;">هل لديك كود خصم أو بروموكود؟</div>
          <div class="coupon-box" style="margin-bottom:6px;">
            <input type="text" class="coupon-input" value="MESSTECH10" style="border-color:#0099e5; color:var(--cyan-600); font-weight:800;">
            <button class="btn-apply-coupon" style="background:#0099e5;">مُطبّق ✓</button>
          </div>
          <div style="font-size:11.5px; color:#059669; font-weight:700;">تم تطبيق خصم ترويجي 10% (وفرت 1,500 ج.م)</div>
        </div>"""

if old_coupon_box in p5_code:
    p5_code = p5_code.replace(old_coupon_box, new_coupon_box)

write_file(os.path.join(DESIGNS_DIR, "make_page_05.py"), p5_code)

# ==============================================================================
# 6. UPDATE script_update_desktop_customer_pages.py (08, 10, 11, 12)
# ==============================================================================
print("Updating script_update_desktop_customer_pages.py...")
pc_code = read_file(os.path.join(DESIGNS_DIR, "script_update_desktop_customer_pages.py"))

# Clean up Page 10 header (Auth Login)
pc_code = pc_code.replace("بوابة العملاء والشركات<br><span style=\"color:var(--cyan-400);\">لطلب حلول وتجهيزات الشبكات</span>", "تسجيل الدخول إلى حسابك<br><span style=\"color:var(--cyan-400);\">أهلاً بك مجدداً في متجر MESS TECH</span>")
pc_code = pc_code.replace("م. مصطفى الشافعي — شركة الأفق للحلول الذكية", "مصطفى كمال الشافعي — حساب شخصي")
pc_code = pc_code.replace("م. مصطفى الشافعي", "مصطفى الشافعي")
pc_code = pc_code.replace("اسم الشركة / المؤسسة (اختياري)", "المدينة / الحي السكني")
pc_code = pc_code.replace("توريد", "طلب")

# Add Wishlist in Customer Profile sidebar
old_profile_nav = """        <li class="portal-menu-item active"><a href="11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png"><span>👤</span> بياناتي وعناويني</a></li>
        <li class="portal-menu-item"><a href="12_سجل_الطلبات_السابقة_Desktop_Order_History.png"><span>🛒</span> سجل طلباتي</a></li>
        <li class="portal-menu-item"><a href="10_تسجيل_الدخول_وإنشاء_حساب_Desktop_Auth_Login.png"><span>🚪</span> تسجيل الخروج</a></li>"""

new_profile_nav = """        <li class="portal-menu-item active"><a href="11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png"><span>👤</span> بياناتي وعناويني</a></li>
        <li class="portal-menu-item"><a href="12_سجل_الطلبات_السابقة_Desktop_Order_History.png"><span>🛒</span> سجل طلباتي</a></li>
        <li class="portal-menu-item"><a href="#"><span>❤️</span> قائمة المفضلة (4 منتجات)</a></li>
        <li class="portal-menu-item"><a href="10_تسجيل_الدخول_وإنشاء_حساب_Desktop_Auth_Login.png"><span>🚪</span> تسجيل الخروج</a></li>"""

if old_profile_nav in pc_code:
    pc_code = pc_code.replace(old_profile_nav, new_profile_nav)

write_file(os.path.join(DESIGNS_DIR, "script_update_desktop_customer_pages.py"), pc_code)

# ==============================================================================
# 7. UPDATE page_14_admin_orders_table.html
# ==============================================================================
print("Updating page_14_admin_orders_table.html...")
p14_path = os.path.join(DESIGNS_DIR, "page_14_admin_orders_table.html")
p14_code = read_file(p14_path)
p14_code = p14_code.replace("والتوريدات", "")
p14_code = p14_code.replace("طلبات التوريد المباشرة", "الطلبات والمبيعات المباشرة")
p14_code = p14_code.replace("توريد", "طلب")
write_file(p14_path, p14_code)

# ==============================================================================
# 8. UPDATE page_16_admin_customers.html
# ==============================================================================
print("Updating page_16_admin_customers.html...")
p16_path = os.path.join(DESIGNS_DIR, "page_16_admin_customers.html")
p16_code = read_file(p16_path)
p16_code = p16_code.replace("إدارة ومتابعة حسابات العملاء والشركات", "إدارة ومتابعة بيانات العملاء والمشترين")
p16_code = p16_code.replace("<span>🏢</span> العملاء والشركات", "<span>👥</span> إدارة العملاء")
p16_code = p16_code.replace("حسابات شركات معتمدة:", "عملاء متكررو الشراء:")
p16_code = p16_code.replace("شركة تقنية", "مشتري")
p16_code = p16_code.replace("العميل / الشركة", "اسم العميل")
p16_code = p16_code.replace("حساب شركة", "حساب نشط ✓")
write_file(p16_path, p16_code)

# ==============================================================================
# 9. UPDATE update_all_mobile_screens.py (Mobile screens)
# ==============================================================================
print("Updating update_all_mobile_screens.py...")
mob_code = read_file(os.path.join(DESIGNS_DIR, "update_all_mobile_screens.py"))
mob_code = mob_code.replace("لمقر العمل", "لباب المنزل")
mob_code = mob_code.replace("توريد", "طلب")
write_file(os.path.join(DESIGNS_DIR, "update_all_mobile_screens.py"), mob_code)

print(">>> Code adjustments completed! Now executing re-renders...")
