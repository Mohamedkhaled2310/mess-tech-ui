# -*- coding: utf-8 -*-
import os
import subprocess

DESIGNS_DIR = r"E:\mess\designs"

# 1. Update mobile_02_framed.html (Mobile Product Details)
p2_path = os.path.join(DESIGNS_DIR, "mobile_02_framed.html")
with open(p2_path, "r", encoding="utf-8") as f:
    m2 = f.read()

m2 = m2.replace("مع تحميل الداتاشيت وزر عائم للشراء المباشر عبر واتساب", "مع خيارات الطراز والشراء السريع بنقرة واحدة")

old_ds_m2 = """      <div style="background:#0f172a; color:#fff; padding:10px 12px; border-radius:8px; display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <div>
          <div style="font-size:12px; font-weight:800;">الداتاشيت الرسمية (Datasheet PDF)</div>
          <div style="font-size:10px; color:#94a3b8;">ملف المواصفات المعتمد من سيسكو • 3.4 MB</div>
        </div>
        <span style="background:var(--cyan-500); padding:4px 10px; border-radius:6px; font-size:10.5px; font-weight:800;">تحميل PDF</span>
      </div>"""

new_guarantee_m2 = """      <!-- B2C Confidence & Return Guarantee -->
      <div style="background:#f0fdf4; border:1px solid #86efac; color:#14532d; padding:10px 12px; border-radius:8px; display:flex; flex-direction:column; gap:4px; margin-bottom:10px; font-size:11px;">
        <div style="font-weight:800; display:flex; align-items:center; gap:6px; color:#166534;">
          <span>🛡️</span> ضمان وثقة المشتري:
        </div>
        <div>✓ إرجاع واستبدال مجاني خلال 14 يوماً وفق حماية المستهلك</div>
        <div>✓ فحص ومعاينة الأجهزة قبل السداد نقداً لمندوب التوصيل</div>
      </div>

      <!-- Variants Selector -->
      <div style="margin-bottom:10px;">
        <div style="font-size:11.5px; font-weight:800; color:var(--navy-900); margin-bottom:4px;">اختر سعة المنافذ والطراز:</div>
        <div style="display:flex; gap:6px;">
          <div style="flex:1; background:#f0f9ff; border:1.5px solid var(--cyan-500); border-radius:6px; padding:6px 8px; text-align:center;">
            <div style="font-size:11px; font-weight:800; color:var(--cyan-600);">24 بورت PoE+</div>
            <div style="font-size:9.5px; color:#64748b;">370W • متوفر فوراً</div>
          </div>
          <div style="flex:1; background:#f8fafc; border:1px solid var(--slate-200); border-radius:6px; padding:6px 8px; text-align:center;">
            <div style="font-size:11px; font-weight:700; color:#334155;">48 بورت PoE+</div>
            <div style="font-size:9.5px; color:#64748b;">740W (+14,000 ج.م)</div>
          </div>
        </div>
      </div>"""

if old_ds_m2 in m2:
    m2 = m2.replace(old_ds_m2, new_guarantee_m2)

old_bottom_bar_m2 = """    <!-- Fixed Bottom Sticky Bar -->
    <div style="background:#fff; border-top:1px solid var(--slate-200); padding:10px 14px 14px; display:flex; align-items:center; gap:8px;">
      <button style="flex:1; background:var(--cyan-500); color:#fff; border:none; padding:11px; border-radius:8px; font-size:13px; font-weight:800; cursor:pointer; white-space:nowrap; display:inline-flex; justify-content:center; align-items:center;">
        أضف للسلة
      </button>
      <a href="https://wa.me/201000000000?text=استفسار%20عن%20سيسكو%202960X" style="width:42px; height:42px; background:#22c55e; color:#fff; border-radius:8px; display:flex; align-items:center; justify-content:center; text-decoration:none; font-size:18px;" title="واتساب المبيعات">
        💬
      </a>
    </div>"""

new_bottom_bar_m2 = """    <!-- Fixed Bottom Sticky Bar: Buy Now + Add to Cart + Wishlist -->
    <div style="background:#fff; border-top:1px solid var(--slate-200); padding:10px 14px 14px; display:flex; align-items:center; gap:8px;">
      <button style="flex:1; background:var(--cyan-500); color:#fff; border:none; padding:11px; border-radius:8px; font-size:12.5px; font-weight:800; cursor:pointer; white-space:nowrap; display:inline-flex; justify-content:center; align-items:center;">
        أضف للسلة
      </button>
      <a href="Mobile_04_السلة_واتمام_الطلب_COD_Mobile_Checkout.png" style="flex:1; background:linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color:#fff; padding:11px; border-radius:8px; font-size:12.5px; font-weight:800; text-decoration:none; display:inline-flex; justify-content:center; align-items:center; white-space:nowrap; box-shadow:0 3px 10px rgba(245,158,11,0.3);">
        شراء الآن
      </a>
      <button title="إضافة للمفضلة" style="width:40px; height:40px; background:#fff; border:1.5px solid #fecdd3; border-radius:8px; display:flex; align-items:center; justify-content:center; color:#f43f5e; cursor:pointer;">
        ❤️
      </button>
    </div>"""

if old_bottom_bar_m2 in m2:
    m2 = m2.replace(old_bottom_bar_m2, new_bottom_bar_m2)

with open(p2_path, "w", encoding="utf-8") as f:
    f.write(m2)
print("Updated mobile_02_framed.html!")

# 2. Update mobile_04_framed.html (Mobile Checkout)
p4_path = os.path.join(DESIGNS_DIR, "mobile_04_framed.html")
with open(p4_path, "r", encoding="utf-8") as f:
    m4 = f.read()

m4 = m4.replace('value="م. أحمد فتحي (شركة دلتا)"', 'value="أحمد فتحي الكردي"')
m4 = m4.replace('value="ahmed.fathi@deltatech.com"', 'value="ahmed.fathi@gmail.com"')
m4 = m4.replace('value="المعادي الجديدة، شارع النصر، عمارة 14"', 'value="المعادي الجديدة، شارع النصر، عمارة 14، شقة 5"')

# Remove branch pickup
old_shipping_options = """      <div style="display:flex; gap:6px; margin-bottom:8px;">
        <div style="flex:1; border:1.5px solid var(--cyan-500); background:#f0f9ff; color:var(--cyan-600); border-radius:6px; padding:6px; text-align:center; font-size:11px; font-weight:700;">
          توصيل لمقر الشركة
        </div>
        <div style="flex:1; border:1.5px solid var(--slate-200); background:#f8fafc; color:#64748b; border-radius:6px; padding:6px; text-align:center; font-size:11px; font-weight:700;">
          استلام من الفرع (مجاناً)
        </div>
      </div>"""

new_shipping_options = """      <div style="border:1.5px solid var(--cyan-500); background:#f0f9ff; color:var(--cyan-600); border-radius:6px; padding:7px 10px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
        <span style="font-size:11.5px; font-weight:800;">توصيل وشحن سريع لباب المنزل</span>
        <span style="background:#10b981; color:#fff; font-size:9.5px; font-weight:800; padding:2px 6px; border-radius:4px;">شحن مجاني</span>
      </div>"""

if old_shipping_options in m4:
    m4 = m4.replace(old_shipping_options, new_shipping_options)

with open(p4_path, "w", encoding="utf-8") as f:
    f.write(m4)
print("Updated mobile_04_framed.html!")

# Render both to PNG
def render(html_name, png_name):
    h_path = os.path.join(DESIGNS_DIR, html_name)
    p_path = os.path.join(DESIGNS_DIR, png_name)
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=540,1100",
        "--force-device-scale-factor=1.5",
        "--virtual-time-budget=3000",
        f"--screenshot={p_path}",
        f"file:///{os.path.abspath(h_path).replace(chr(92), '/')}"
    ]
    subprocess.run(cmd, check=True)
    size_kb = os.path.getsize(p_path) / 1024
    print(f"Rendered: {png_name} ({size_kb:.1f} KB)")
    # copy to root
    shutil_dst = os.path.join(r"E:\mess", png_name)
    with open(p_path, "rb") as sf, open(shutil_dst, "wb") as df:
        df.write(sf.read())

render("mobile_02_framed.html", "Mobile_02_صفحة_المنتج_والمواصفات_Mobile_Product_Details.png")
render("mobile_04_framed.html", "Mobile_04_السلة_واتمام_الطلب_COD_Mobile_Checkout.png")
print("Finished Mobile 02 and 04 updates!")
