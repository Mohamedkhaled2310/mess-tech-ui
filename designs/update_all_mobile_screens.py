# -*- coding: utf-8 -*-
import os
import subprocess
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS

DESIGNS_DIR = r"E:\mess\designs"

FRAME_WRAPPER_CSS = """
:root {
  --navy-950: #070d18;
  --navy-900: #0b1120;
  --navy-850: #0f172a;
  --navy-800: #172136;
  --navy-700: #1e293b;
  --navy-600: #334155;
  --cyan-500: #0099e5;
  --cyan-400: #38bdf8;
  --cyan-600: #0284c7;
  --emerald-500: #10b981;
  --emerald-600: #059669;
  --amber-500: #f59e0b;
  --rose-500: #ef4444;
  --slate-100: #f1f5f9;
  --slate-200: #e2e8f0;
  --slate-400: #94a3b8;
  --slate-500: #64748b;
  --bg-page: #f8fafc;
}

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Cairo', sans-serif; }
body {
  background: radial-gradient(circle at 50% 20%, #172a4d 0%, #070d18 80%);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 30px 20px;
  min-height: 100vh;
}
.mono { font-family: 'JetBrains Mono', monospace; direction: ltr; display: inline-block; }

.phone-device-container {
  width: 420px;
  background: #000;
  border: 10px solid #1e293b;
  border-radius: 46px;
  box-shadow: 0 25px 60px rgba(0,0,0,0.65), 0 0 0 2px rgba(255,255,255,0.1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
  direction: rtl;
  text-align: right;
  background-color: var(--bg-page);
}

.phone-status-bar {
  background: var(--navy-900);
  padding: 10px 20px 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 11px;
  color: #fff;
  position: relative;
  z-index: 50;
  direction: ltr;
}
.phone-dynamic-island {
  position: absolute;
  top: 7px;
  left: 50%;
  transform: translateX(-50%);
  width: 95px;
  height: 22px;
  background: #000;
  border-radius: 20px;
}

.device-header-title {
  text-align: center;
  color: #fff;
  margin-bottom: 20px;
  max-width: 500px;
}
.device-header-tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(0, 153, 229, 0.15);
  border: 1px solid rgba(0, 153, 229, 0.4);
  color: var(--cyan-400);
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 8px;
}
.device-header-title h2 {
  font-size: 22px;
  font-weight: 900;
  color: #fff;
}
.device-header-title p {
  font-size: 12.5px;
  color: #94a3b8;
  margin-top: 4px;
}
"""

def render_device(html_path, png_path, height=2200):
    cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size=540,{height}",
        "--force-device-scale-factor=1.5",
        "--virtual-time-budget=3000",
        f"--screenshot={png_path}",
        f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
    ]
    print(f"Rendering Mobile: {html_path} -> {png_path} ({height}h)...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(png_path):
        size_kb = os.path.getsize(png_path) / 1024
        print(f"SUCCESS: {png_path} ({size_kb:.1f} KB)")
        return True
    else:
        print(f"FAILED: {png_path}")
        return False

# ==============================================================================
# MOBILE 06: ORDER SUCCESS (THANK YOU PAGE)
# - No tracking, no tax invoice, no "ماذا يحدث بعد تأكيد الطلب"
# ==============================================================================
def make_mob_06():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | Mobile 06 - نجاح تأكيد الطلب</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">📱 Mobile Screen #06</div>
    <h2>صفحة نجاح الطلب (Thank You Page)</h2>
    <p>تأكيد فوري لاختيار الدفع عند الاستلام والتوصيل المباشر لمقر العمل</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span>9:41</span>
      <div class="phone-dynamic-island"></div>
      <span>5G &nbsp; 100%</span>
    </div>

    <!-- App Bar -->
    <div style="background:var(--navy-900); padding:10px 14px; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #1e293b;">
      <img src="assets/logo_white.png" style="height:26px;">
      <span style="color:#10b981; font-size:11.5px; font-weight:800; display:flex; align-items:center; gap:4px;">
        ✓ تم تأكيد الطلب
      </span>
    </div>

    <!-- Hero Success -->
    <div style="background:linear-gradient(180deg, var(--navy-900) 0%, var(--navy-800) 100%); color:#fff; padding:24px 16px; text-align:center;">
      <div style="width:60px; height:60px; background:#10b981; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 12px; font-size:28px; box-shadow:0 0 25px rgba(16,185,129,0.5);">
        ✓
      </div>
      <h3 style="font-size:17px; font-weight:900; margin-bottom:4px;">تم استلام وتأكيد طلبك بنجاح!</h3>
      <p style="font-size:12px; color:#cbd5e1; margin-bottom:12px;">جاري تجهيز الأجهزة بالمستودع والتوصيل خلال 24-48 ساعة</p>
      
      <div style="background:rgba(0,0,0,0.3); border:1px solid rgba(255,255,255,0.1); border-radius:999px; padding:6px 14px; display:inline-flex; gap:8px; font-size:11.5px;">
        <span>رقم الطلب: <b class="mono" style="color:var(--cyan-400);">#ORD-9824</b></span>
        <span>•</span>
        <span>موعد التوصيل: <b>الثلاثاء 17 نوفمبر</b></span>
      </div>
    </div>

    <div style="padding:14px; flex:1;">
      <!-- COD Payment Highlight -->
      <div style="background:#eff6ff; border:1.5px solid #bfdbfe; border-radius:12px; padding:12px; margin-bottom:14px; display:flex; gap:10px; align-items:flex-start;">
        <span style="font-size:22px;">💵</span>
        <div>
          <div style="font-size:12.5px; font-weight:800; color:#1e40af;">طريقة الدفع: الدفع نقداً عند الاستلام (COD)</div>
          <div style="font-size:11px; color:#3b82f6; margin-top:2px;">
            المبلغ المطلوب سداده: <b class="mono" style="font-size:13.5px; color:#1e3a8a;">37,950 ج.م</b> نقداً مع مندوب التوصيل بعد الفحص والمعاينة.
          </div>
        </div>
      </div>

      <!-- Items Summary -->
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:12px; padding:12px; margin-bottom:14px;">
        <div style="font-size:12.5px; font-weight:800; color:var(--navy-900); margin-bottom:8px; border-bottom:1px solid var(--slate-100); padding-bottom:6px;">
          الأصناف المؤكدة في طلبك (3 أصناف)
        </div>

        <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
          <div style="width:40px; height:30px; background:#f8fafc; border-radius:4px; display:flex; align-items:center; justify-content:center;">{SVG_CISCO_SWITCH}</div>
          <div style="flex:1;">
            <div style="font-size:11.5px; font-weight:800;">سويتش Cisco Catalyst 2960-X</div>
            <div class="mono" style="font-size:10px; color:var(--slate-500);">24 Port PoE+ • كمية: 1</div>
          </div>
          <div class="mono" style="font-size:12px; font-weight:800;">28,500 ج.م</div>
        </div>

        <div style="display:flex; align-items:center; gap:10px;">
          <div style="width:40px; height:30px; background:#f8fafc; border-radius:4px; display:flex; align-items:center; justify-content:center;">{SVG_MIKROTIK}</div>
          <div style="flex:1;">
            <div style="font-size:11.5px; font-weight:800;">راوتر MikroTik CCR2004</div>
            <div class="mono" style="font-size:10px; color:var(--slate-500);">16G-2S+PC • كمية: 1</div>
          </div>
          <div class="mono" style="font-size:12px; font-weight:800;">8,950 ج.م</div>
        </div>
      </div>

      <!-- Address card -->
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:12px; padding:12px; margin-bottom:14px; font-size:11.5px;">
        <div style="color:var(--slate-500); margin-bottom:2px;">عنوان التوصيل المعتمد:</div>
        <div style="font-weight:700; color:var(--navy-900);">مبنى تكنوبوليس الإداري، الدور 4، شارع التسعين الشمالي، التجمع الخامس، القاهرة.</div>
      </div>

      <!-- Buttons -->
      <button style="width:100%; background:var(--cyan-500); color:#fff; border:none; padding:12px; border-radius:8px; font-size:13.5px; font-weight:800; cursor:pointer; margin-bottom:8px; display:flex; align-items:center; justify-content:center; gap:6px;">
        <span>📦</span> عرض سجل طلباتي بالحساب
      </button>

      <button style="width:100%; background:#fff; border:1px solid var(--slate-300); color:var(--navy-900); padding:10px; border-radius:8px; font-size:12px; font-weight:700;">
        تحميل إيصال الطلب (PDF)
      </button>
    </div>

    <!-- Bottom Nav -->
    <div style="background:#0b1120; border-top:1px solid #1e293b; padding:8px 10px 12px; display:flex; justify-content:space-around; align-items:center;">
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🏠</span><span>الرئيسية</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>📁</span><span>الأقسام</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:var(--cyan-400); font-size:10px; font-weight:700;"><span>🛒</span><span>السلة</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>👤</span><span>حسابي</span></div>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_06_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_06_نجاح_الطلب_Mobile_Order_Success.png")
    render_device(html_file, png_file, height=980)

# ==============================================================================
# MOBILE 08: AUTH LOGIN (Cleaned - NO OTP)
# ==============================================================================
def make_mob_08():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | Mobile 08 - الدخول وحساب العملاء</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">📱 Mobile Screen #07</div>
    <h2>تسجيل الدخول وبوابة العملاء</h2>
    <p>دخول فوري بحساب الشركات أو الحساب الشخصي لطلب المنتجات مباشرة</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span>9:41</span>
      <div class="phone-dynamic-island"></div>
      <span>5G &nbsp; 100%</span>
    </div>

    <!-- Header -->
    <div style="background:var(--navy-900); padding:24px 20px 20px; text-align:center; border-bottom:1px solid #1e293b;">
      <img src="assets/logo_white.png" style="height:32px; margin-bottom:8px;">
      <div style="color:var(--cyan-400); font-size:12px; font-weight:800;">بوابة العملاء والشركات المعتمدة</div>
    </div>

    <div style="padding:20px; flex:1;">
      <!-- Tab toggle -->
      <div style="display:flex; background:#f1f5f9; border-radius:8px; padding:3px; margin-bottom:20px;">
        <button style="flex:1; background:#fff; border:none; padding:8px; border-radius:6px; font-weight:800; font-size:12.5px; color:var(--navy-900); box-shadow:0 1px 3px rgba(0,0,0,0.1);">تسجيل الدخول</button>
        <button style="flex:1; background:transparent; border:none; padding:8px; border-radius:6px; font-weight:700; font-size:12.5px; color:var(--slate-500);">حساب جديد</button>
      </div>

      <!-- Inputs -->
      <div style="margin-bottom:14px;">
        <label style="font-size:11.5px; font-weight:700; color:var(--navy-900); display:block; margin-bottom:4px;">البريد الإلكتروني أو رقم الهاتف</label>
        <input type="text" class="mono" value="m.elshafei@alofok-tech.com" style="width:100%; border:1.5px solid var(--slate-300); border-radius:8px; padding:10px; font-size:12.5px; outline:none;">
      </div>

      <div style="margin-bottom:16px;">
        <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
          <label style="font-size:11.5px; font-weight:700; color:var(--navy-900);">كلمة المرور</label>
          <a href="#" style="font-size:11px; color:var(--cyan-600); font-weight:700; text-decoration:none;">نسيت كلمة المرور؟</a>
        </div>
        <input type="password" value="••••••••••••" style="width:100%; border:1.5px solid var(--slate-300); border-radius:8px; padding:10px; font-size:12.5px; outline:none;">
      </div>

      <button style="width:100%; background:var(--navy-900); color:#fff; border:none; padding:12px; border-radius:8px; font-size:13.5px; font-weight:800; cursor:pointer; margin-bottom:16px;">
        تسجيل الدخول لحسابي
      </button>

      <!-- Trust benefits list -->
      <div style="background:#f8fafc; border:1px solid var(--slate-200); border-radius:10px; padding:14px; font-size:11.5px;">
        <div style="font-weight:800; color:var(--navy-900); margin-bottom:8px;">مميزات الحساب لدى MESS TECH:</div>
        <div style="display:flex; align-items:center; gap:6px; color:#059669; margin-bottom:6px;">✓ أجهزة أصلية معتمدة 100% بالكرتونة</div>
        <div style="display:flex; align-items:center; gap:6px; color:#059669; margin-bottom:6px;">✓ الدفع عند الاستلام مع المعاينة</div>
        <div style="display:flex; align-items:center; gap:6px; color:#059669;">✓ حفظ العناوين لسرعة الشراء وتكرار الطلب</div>
      </div>
    </div>

    <!-- Bottom Nav -->
    <div style="background:#0b1120; border-top:1px solid #1e293b; padding:8px 10px 12px; display:flex; justify-content:space-around; align-items:center;">
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🏠</span><span>الرئيسية</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>📁</span><span>الأقسام</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🛒</span><span>السلة</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:var(--cyan-400); font-size:10px; font-weight:700;"><span>👤</span><span>حسابي</span></div>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_08_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_08_تسجيل_الدخول_وحساب_جديد_Mobile_Auth_Login.png")
    render_device(html_file, png_file, height=980)

# ==============================================================================
# MOBILE 09: CUSTOMER PROFILE (Cleaned)
# ==============================================================================
def make_mob_09():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | Mobile 09 - لوحة حسابي ودفتر العناوين</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">📱 Mobile Screen #08</div>
    <h2>لوحة حساب العميل ودفتر العناوين</h2>
    <p>إدارة بيانات الحساب الشخصية، العناوين المحفوظة، وتسهيل الشراء</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span>9:41</span>
      <div class="phone-dynamic-island"></div>
      <span>5G &nbsp; 100%</span>
    </div>

    <!-- User Header -->
    <div style="background:var(--navy-900); color:#fff; padding:20px 16px; display:flex; align-items:center; gap:14px; border-bottom:1px solid #1e293b;">
      <div style="width:52px; height:52px; background:linear-gradient(135deg, var(--cyan-500), #0284c7); border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:18px;">
        م ش
      </div>
      <div>
        <div style="font-size:15px; font-weight:800;">م. مصطفى الشافعي</div>
        <div style="font-size:11.5px; color:#94a3b8;">شركة الأفق للحلول الرقمية</div>
        <div style="display:inline-block; background:rgba(0,153,229,0.2); color:var(--cyan-400); font-size:10px; font-weight:700; padding:1px 6px; border-radius:4px; margin-top:2px;">
          كود العميل: <span class="mono">MST-4402</span>
        </div>
      </div>
    </div>

    <!-- Quick stats strip -->
    <div style="background:#fff; border-bottom:1px solid var(--slate-200); padding:10px 16px; display:flex; justify-content:space-around; text-align:center;">
      <div>
        <div class="mono" style="font-size:15px; font-weight:900; color:var(--cyan-600);">1</div>
        <div style="font-size:10.5px; color:var(--slate-500);">طلب قيد التوصيل</div>
      </div>
      <div style="width:1px; height:24px; background:var(--slate-200);"></div>
      <div>
        <div class="mono" style="font-size:15px; font-weight:900; color:#059669;">15</div>
        <div style="font-size:10.5px; color:var(--slate-500);">طلب مستلم</div>
      </div>
      <div style="width:1px; height:24px; background:var(--slate-200);"></div>
      <div>
        <div class="mono" style="font-size:15px; font-weight:900; color:var(--navy-900);">2</div>
        <div style="font-size:10.5px; color:var(--slate-500);">عناوين مسجلة</div>
      </div>
    </div>

    <div style="padding:14px; flex:1;">
      <!-- Saved Addresses -->
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <span style="font-size:13px; font-weight:800; color:var(--navy-900);">دفتر عناوين التوصيل المحفوظة</span>
        <span style="font-size:11px; color:var(--cyan-600); font-weight:800; cursor:pointer;">+ إضافة عنوان</span>
      </div>

      <!-- Address 1 -->
      <div style="background:#f0f9ff; border:1.5px solid #bfdbfe; border-radius:10px; padding:12px; margin-bottom:10px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span style="background:var(--cyan-500); color:#fff; font-size:9.5px; font-weight:800; padding:1px 6px; border-radius:4px;">الافتراضي</span>
          <span style="font-size:11px; color:var(--slate-500);">تعديل</span>
        </div>
        <div style="font-size:12.5px; font-weight:800; color:var(--navy-900);">المقر الرئيسي - مبنى تكنوبوليس</div>
        <div style="font-size:11px; color:var(--slate-600); margin-top:2px;">شارع التسعين الشمالي، التجمع الخامس، القاهرة.</div>
        <div class="mono" style="font-size:11px; color:var(--cyan-700); font-weight:700; margin-top:4px;">01001234567</div>
      </div>

      <!-- Address 2 -->
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:12px; margin-bottom:16px;">
        <div style="font-size:12.5px; font-weight:800; color:var(--navy-900);">مستودع مدينة العبور</div>
        <div style="font-size:11px; color:var(--slate-600); margin-top:2px;">المنطقة الصناعية الأولى، مدينة العبور.</div>
        <div class="mono" style="font-size:11px; color:var(--slate-500); margin-top:4px;">01123456788</div>
      </div>

      <!-- Menu Links -->
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:12px; overflow:hidden;">
        <div style="padding:12px 14px; border-bottom:1px solid var(--slate-100); display:flex; justify-content:space-between; align-items:center; font-size:12.5px; font-weight:700;">
          <span>📦 سجل طلباتي السابقة (16)</span>
          <span style="color:var(--slate-400);">←</span>
        </div>
        <div style="padding:12px 14px; display:flex; justify-content:space-between; align-items:center; font-size:12.5px; font-weight:700; color:#ef4444;">
          <span>🚪 تسجيل الخروج</span>
          <span>←</span>
        </div>
      </div>
    </div>

    <!-- Bottom Nav -->
    <div style="background:#0b1120; border-top:1px solid #1e293b; padding:8px 10px 12px; display:flex; justify-content:space-around; align-items:center;">
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🏠</span><span>الرئيسية</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>📁</span><span>الأقسام</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🛒</span><span>السلة</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:var(--cyan-400); font-size:10px; font-weight:700;"><span>👤</span><span>حسابي</span></div>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_09_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_09_لوحة_حسابي_والعناوين_Mobile_Customer_Profile.png")
    render_device(html_file, png_file, height=980)

# ==============================================================================
# MOBILE 10: ORDER HISTORY (Cleaned)
# ==============================================================================
def make_mob_10():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | Mobile 10 - سجل طلباتي السابقة</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">📱 Mobile Screen #09</div>
    <h2>سجل الطلبات السابقة وإيصالات الاستلام</h2>
    <p>متابعة الطلبات السابقة والحالية وتفاصيل التكلفة بنقرة واحدة</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span>9:41</span>
      <div class="phone-dynamic-island"></div>
      <span>5G &nbsp; 100%</span>
    </div>

    <!-- App Bar -->
    <div style="background:var(--navy-900); padding:12px 16px; display:flex; justify-content:space-between; align-items:center; color:#fff;">
      <span style="font-size:14px; font-weight:800;">طلباتي السابقة (16)</span>
      <span style="font-size:12px; color:var(--cyan-400);">بحث بالرقم</span>
    </div>

    <!-- Filter chips -->
    <div style="background:#fff; border-bottom:1px solid var(--slate-200); padding:8px 12px; display:flex; gap:8px; overflow-x:auto;">
      <span style="background:var(--navy-900); color:#fff; font-size:11px; font-weight:800; padding:4px 12px; border-radius:999px; white-space:nowrap;">الكل (16)</span>
      <span style="background:#f1f5f9; color:var(--slate-600); font-size:11px; font-weight:700; padding:4px 12px; border-radius:999px; white-space:nowrap;">قيد التوصيل (1)</span>
      <span style="background:#f1f5f9; color:var(--slate-600); font-size:11px; font-weight:700; padding:4px 12px; border-radius:999px; white-space:nowrap;">تم الاستلام (15)</span>
    </div>

    <div style="padding:12px; flex:1;">
      <!-- Order 1: Active In-Transit -->
      <div style="background:#fff; border:1.5px solid #bfdbfe; border-radius:12px; padding:12px; margin-bottom:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; border-bottom:1px solid var(--slate-100); padding-bottom:6px;">
          <span class="mono" style="font-size:13.5px; font-weight:900; color:var(--navy-900);">#ORD-9824</span>
          <span style="background:#eff6ff; color:#2563eb; font-size:10px; font-weight:800; padding:2px 8px; border-radius:999px;">🚚 قيد التوصيل اليوم</span>
        </div>

        <div style="font-size:11px; color:var(--slate-500); margin-bottom:6px;">15 نوفمبر 2026 • الدفع عند الاستلام COD</div>

        <div style="font-size:12px; font-weight:700; color:var(--navy-900); margin-bottom:4px;">
          سويتش Cisco 2960X + راوتر MikroTik CCR2004
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; border-top:1px solid var(--slate-100); padding-top:8px;">
          <div class="mono" style="font-size:14px; font-weight:900; color:var(--cyan-600);">37,950 ج.م</div>
          <button style="background:var(--cyan-500); color:#fff; border:none; padding:6px 12px; border-radius:6px; font-size:11px; font-weight:800; cursor:pointer;">
            تفاصيل الطلب
          </button>
        </div>
      </div>

      <!-- Order 2: Delivered -->
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:12px; padding:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; border-bottom:1px solid var(--slate-100); padding-bottom:6px;">
          <span class="mono" style="font-size:13.5px; font-weight:900; color:var(--navy-900);">#ORD-8910</span>
          <span style="background:#ecfdf5; color:#059669; font-size:10px; font-weight:800; padding:2px 8px; border-radius:999px;">✓ تم الاستلام والتحصيل</span>
        </div>

        <div style="font-size:11px; color:var(--slate-500); margin-bottom:6px;">28 أكتوبر 2026 • إيصال: RCP-8910</div>
        <div style="font-size:12px; font-weight:700; color:var(--navy-900); margin-bottom:4px;">
          فورتينت Fortinet FortiGate 60F Firewall
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; border-top:1px solid var(--slate-100); padding-top:8px;">
          <div class="mono" style="font-size:14px; font-weight:900; color:var(--navy-900);">32,500 ج.م</div>
          <button style="background:var(--navy-900); color:#fff; border:none; padding:6px 10px; border-radius:6px; font-size:11px; font-weight:700;">
            إيصال الاستلام
          </button>
        </div>
      </div>
    </div>

    <!-- Bottom Nav -->
    <div style="background:#0b1120; border-top:1px solid #1e293b; padding:8px 10px 12px; display:flex; justify-content:space-around; align-items:center;">
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>🏠</span><span>الرئيسية</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>📁</span><span>الأقسام</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:var(--cyan-400); font-size:10px; font-weight:700;"><span>📦</span><span>طلباتي</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>👤</span><span>حسابي</span></div>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_10_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_10_سجل_طلباتي_السابقة_Mobile_Order_History.png")
    render_device(html_file, png_file, height=980)

# ==============================================================================
# MOBILE 11: ADMIN MOBILE MANAGEMENT
# ==============================================================================
def make_mob_11():
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | Mobile 11 - إدارة الطلبات والمستودع موبايل</title>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>{FRAME_WRAPPER_CSS}</style>
</head>
<body>
  <div class="device-header-title">
    <div class="device-header-tag">📱 Mobile Screen #10</div>
    <h2>لوحة تحكم الإدارة السريعة (Admin Mobile)</h2>
    <p>متابعة فورية للطلبات الواردة وتعيين المناديب وتحديث المخزون من الهاتف</p>
  </div>

  <div class="phone-device-container">
    <div class="phone-status-bar">
      <span>9:41</span>
      <div class="phone-dynamic-island"></div>
      <span>5G &nbsp; 100%</span>
    </div>

    <!-- Admin Mobile App Bar -->
    <div style="background:var(--navy-950); padding:12px 16px; display:flex; justify-content:space-between; align-items:center; color:#fff; border-bottom:1px solid var(--navy-800);">
      <div style="display:flex; align-items:center; gap:8px;">
        <img src="assets/logo_white.png" style="height:24px;">
        <span style="font-size:11px; background:#ef4444; color:#fff; font-weight:800; padding:1px 6px; border-radius:999px;">Admin</span>
      </div>
      <span style="font-size:12px; color:var(--slate-400);">م. أحمد رشاد</span>
    </div>

    <!-- Quick stats 3 boxes -->
    <div style="background:var(--navy-900); padding:12px 14px; display:flex; gap:10px;">
      <div style="flex:1; background:var(--navy-800); border:1px solid var(--navy-700); border-radius:8px; padding:8px 10px; text-align:center;">
        <div class="mono" style="font-size:16px; font-weight:900; color:#fff;">28</div>
        <div style="font-size:10px; color:#94a3b8;">طلبات اليوم</div>
      </div>
      <div style="flex:1; background:var(--navy-800); border:1px solid var(--navy-700); border-radius:8px; padding:8px 10px; text-align:center;">
        <div class="mono" style="font-size:16px; font-weight:900; color:#f59e0b;">6</div>
        <div style="font-size:10px; color:#f59e0b;">جديدة للتأكيد</div>
      </div>
      <div style="flex:1; background:var(--navy-800); border:1px solid var(--navy-700); border-radius:8px; padding:8px 10px; text-align:center;">
        <div class="mono" style="font-size:16px; font-weight:900; color:#38bdf8;">14</div>
        <div style="font-size:10px; color:#38bdf8;">مع المناديب</div>
      </div>
    </div>

    <div style="padding:14px; flex:1;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <span style="font-size:13px; font-weight:800; color:var(--navy-900);">الطلبات الواردة التي تتطلب إجراء</span>
        <span style="font-size:11px; color:var(--cyan-600); font-weight:700;">عرض الكل</span>
      </div>

      <!-- Action Card 1 -->
      <div style="background:#fff; border:1px solid var(--slate-200); border-radius:10px; padding:12px; margin-bottom:10px;">
        <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
          <span class="mono" style="font-size:12.5px; font-weight:900; color:var(--navy-900);">#ORD-9824</span>
          <span style="background:#eff6ff; color:#1d4ed8; font-size:9.5px; font-weight:800; padding:1px 6px; border-radius:4px;">مع المندوب</span>
        </div>
        <div style="font-size:12px; font-weight:700;">م. مصطفى الشافعي • شركة الأفق</div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; border-top:1px solid var(--slate-100); padding-top:6px;">
          <span class="mono" style="font-size:13px; font-weight:900;">37,950 ج.م COD</span>
          <button style="background:var(--cyan-500); color:#fff; border:none; padding:4px 10px; border-radius:4px; font-size:10.5px; font-weight:800;">تحديث حالة</button>
        </div>
      </div>

      <!-- Action Card 2 -->
      <div style="background:#fff; border:1.5px solid #fde68a; border-radius:10px; padding:12px; margin-bottom:10px;">
        <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
          <span class="mono" style="font-size:12.5px; font-weight:900; color:var(--navy-900);">#ORD-9822</span>
          <span style="background:#fef3c7; color:#b45309; font-size:9.5px; font-weight:800; padding:1px 6px; border-radius:4px;">جديد • بحاجة لتأكيد</span>
        </div>
        <div style="font-size:12px; font-weight:700;">م. كريم هشام • 4x UniFi APs</div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; border-top:1px solid var(--slate-100); padding-top:6px;">
          <span class="mono" style="font-size:13px; font-weight:900;">23,200 ج.م COD</span>
          <button style="background:#059669; color:#fff; border:none; padding:4px 10px; border-radius:4px; font-size:10.5px; font-weight:800;">تأكيد فوري ✓</button>
        </div>
      </div>

      <!-- Stock Alert Pill -->
      <div style="background:#fef2f2; border:1px solid #fecaca; border-radius:8px; padding:10px; display:flex; align-items:center; gap:8px;">
        <span style="font-size:16px;">⚠️</span>
        <div style="font-size:11px; color:#991b1b;">
          <b>تنبيه مخزون:</b> سويتش Cisco 3850 قارب على النفاد (متبقي 3 قطع بالمستودع).
        </div>
      </div>
    </div>

    <!-- Admin Bottom Nav -->
    <div style="background:var(--navy-950); border-top:1px solid var(--navy-800); padding:8px 10px 12px; display:flex; justify-content:space-around; align-items:center;">
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:var(--cyan-400); font-size:10px; font-weight:700;"><span>🛒</span><span>الطلبات</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>📦</span><span>المنتجات</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>📊</span><span>التقارير</span></div>
      <div style="display:flex; flex-direction:column; align-items:center; gap:2px; color:#94a3b8; font-size:10px; font-weight:700;"><span>⚙️</span><span>الإعدادات</span></div>
    </div>
  </div>
</body>
</html>
"""
    html_file = os.path.join(DESIGNS_DIR, "mobile_11_framed.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    png_file = os.path.join(DESIGNS_DIR, "Mobile_11_إدارة_الطلبات_والمنتجات_Mobile_Admin_Management.png")
    render_device(html_file, png_file, height=980)

if __name__ == "__main__":
    print("Re-rendering updated mobile screens...")
    make_mob_06()
    make_mob_08()
    make_mob_09()
    make_mob_10()
    make_mob_11()
    print("All mobile screens updated successfully!")
