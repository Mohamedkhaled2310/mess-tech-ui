# -*- coding: utf-8 -*-
import os
import subprocess
import json

DESIGNS_DIR = r"E:\mess\designs"
ASSETS_DIR = os.path.join(DESIGNS_DIR, "assets")

# Ensure directories exist
os.makedirs(DESIGNS_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

SHARED_CSS = """
:root {
  --navy-950: #070d18;
  --navy-900: #0b1120;
  --navy-850: #0f172a;
  --navy-800: #172136;
  --navy-700: #1e293b;
  --navy-600: #334155;
  --navy-500: #475569;
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
body { background: var(--bg-page); color: var(--navy-900); direction: rtl; text-align: right; }
.mono { font-family: 'JetBrains Mono', monospace; direction: ltr; display: inline-block; }

/* Top Header Bar */
.top-notice-bar {
  background: var(--navy-950);
  color: var(--slate-400);
  font-size: 12.5px;
  padding: 8px 48px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}
.badge-notice-header {
  background: rgba(0, 153, 229, 0.15);
  color: #38bdf8;
  border: 1px solid rgba(0, 153, 229, 0.35);
  padding: 3px 12px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 11.5px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}

/* Main Navbar */
.main-nav {
  background: var(--navy-900);
  padding: 16px 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 28px;
  border-bottom: 2px solid var(--navy-700);
}
.brand-logo-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}
.brand-logo-img {
  height: 48px;
  width: auto;
  object-fit: contain;
}

/* Search Bar */
.search-wrapper {
  flex: 1;
  max-width: 680px;
  position: relative;
}
.search-input-box {
  display: flex;
  align-items: center;
  background: var(--navy-800);
  border: 1.5px solid #2d3b55;
  border-radius: 10px;
  padding: 3px 6px;
  transition: all 0.2s;
}
.search-input-box:focus-within {
  border-color: var(--cyan-500);
  box-shadow: 0 0 0 3px rgba(0, 153, 229, 0.2);
}
.search-category-dd {
  background: transparent;
  border: none;
  border-left: 1px solid #2d3b55;
  color: var(--slate-400);
  font-size: 13px;
  font-weight: 600;
  padding: 8px 12px;
  outline: none;
  cursor: pointer;
}
.search-input-field {
  flex: 1;
  background: transparent;
  border: none;
  padding: 10px 14px;
  color: #fff;
  font-size: 14px;
  outline: none;
}
.search-input-field::placeholder { color: var(--slate-500); font-size: 13px; }
.search-submit-btn {
  background: var(--cyan-500);
  color: #fff;
  border: none;
  border-radius: 8px;
  padding: 9px 20px;
  font-size: 13.5px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
}
.search-quick-tags {
  display: flex;
  gap: 8px;
  margin-top: 6px;
  font-size: 11.5px;
  color: var(--slate-400);
}
.quick-tag {
  background: rgba(255,255,255,0.06);
  padding: 1px 8px;
  border-radius: 4px;
  color: var(--cyan-400);
  text-decoration: none;
}

/* Header Action Buttons */
.nav-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}
.nav-pill-btn {
  background: var(--navy-800);
  border: 1px solid #2d3b55;
  color: #fff;
  padding: 9px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  position: relative;
}
.pill-counter {
  background: var(--cyan-500);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  padding: 1px 7px;
  border-radius: 999px;
}
.pill-counter.green { background: var(--emerald-500); }
.whatsapp-direct-btn {
  background: #22c55e;
  color: #fff;
  border: none;
  padding: 9px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(34, 197, 94, 0.25);
}

/* Category Subnav */
.subnav-bar {
  background: var(--navy-850);
  padding: 0 40px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid var(--navy-700);
  white-space: nowrap;
  overflow-x: hidden;
  flex-wrap: nowrap;
}
.all-departments-pill {
  background: var(--cyan-600);
  color: #fff;
  padding: 10px 18px;
  font-size: 13px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-left: 14px;
  cursor: pointer;
  white-space: nowrap;
  flex-shrink: 0;
  border-radius: 6px;
}
.subnav-links {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  list-style: none;
  white-space: nowrap;
  flex-wrap: nowrap;
  margin: 0;
  padding: 0;
}
.subnav-links li {
  display: inline-block;
  flex-shrink: 0;
  white-space: nowrap;
}
.subnav-links a {
  color: #cbd5e1;
  padding: 13px 12px;
  font-size: 12.5px;
  font-weight: 600;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  border-bottom: 2px solid transparent;
  transition: all 0.15s;
  white-space: nowrap;
}
.subnav-links a:hover, .subnav-links a.active {
  color: var(--cyan-400);
  border-bottom-color: var(--cyan-400);
  background: rgba(56, 189, 248, 0.05);
}

/* Footer */
.footer-wrap {
  background: var(--navy-950);
  color: var(--slate-400);
  padding: 56px 48px 24px;
  border-top: 1px solid var(--navy-700);
  margin-top: 70px;
}
.footer-container {
  max-width: 1340px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.3fr;
  gap: 48px;
}
.footer-col h5 {
  color: #fff;
  font-size: 16px;
  font-weight: 800;
  margin-bottom: 20px;
  position: relative;
  padding-bottom: 10px;
}
.footer-col h5::after {
  content: '';
  position: absolute;
  bottom: 0;
  right: 0;
  width: 36px;
  height: 2.5px;
  background: var(--cyan-500);
}
.footer-list { list-style: none; display: flex; flex-direction: column; gap: 11px; font-size: 13.5px; }
.footer-list a { color: var(--slate-400); text-decoration: none; }
.footer-bottom-bar {
  max-width: 1340px;
  margin: 40px auto 0;
  padding-top: 24px;
  border-top: 1px solid rgba(255,255,255,0.08);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
}
"""

def get_header_html(active_cat=""):
    return f"""
    <!-- Top utility bar -->
    <div class="top-notice-bar">
      <div style="display:flex; align-items:center; gap:16px;">
        <span class="badge-notice-header">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          توريد وشحن سريع لكافة محافظات مصر
        </span>
        <span style="color:var(--slate-400);">|</span>
        <span>أجهزة أصلية معتمدة | دعم فني هندسي مخصص للمشروعات</span>
      </div>
      <div style="display:flex; align-items:center; gap:20px;">
        <span>هاتف المبيعات: <b class="mono" style="color:#fff;">0100-MESS-TECH</b></span>
        <span>|</span>
        <a href="#" style="color:var(--cyan-400); text-decoration:none; font-weight:700;">English (LTR)</a>
        <span>|</span>
        <a href="#" style="color:#fff; text-decoration:none;">حسابي / تتبع طلب</a>
      </div>
    </div>

    <!-- Main Header -->
    <header class="main-nav">
      <a href="01_الصفحة_الرئيسية_Desktop_Homepage.png" class="brand-logo-wrap">
        <img src="assets/logo_white.png" class="brand-logo-img" alt="MESS TECH Logo">
      </a>

      <!-- Instant Search by Model/SKU -->
      <div class="search-wrapper">
        <div class="search-input-box">
          <select class="search-category-dd">
            <option>جميع الأقسام</option>
            <option>سويتشات الشبكات</option>
            <option>راوترات وسيرفرات</option>
            <option>جدران الحماية Firewalls</option>
            <option>أجهزة واي فاي وأكسس بوينت</option>
            <option>مغذيات الطاقة UPS</option>
            <option>راكات وكابلات</option>
          </select>
          <input type="text" class="search-input-field" placeholder="ابحث برقم الموديل (مثل WS-C2960X، CCR2004، FG-60F) أو كود SKU...">
          <button class="search-submit-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            بحث فوري
          </button>
        </div>
        <div class="search-quick-tags">
          <span>شائع الآن:</span>
          <a href="#" class="quick-tag">Cisco 24 Port PoE</a>
          <a href="#" class="quick-tag">FortiGate 60F</a>
          <a href="#" class="quick-tag">MikroTik 10G</a>
          <a href="#" class="quick-tag">UniFi U6-Pro</a>
          <a href="#" class="quick-tag">Rack 9U</a>
        </div>
      </div>

      <!-- Actions -->
      <div class="nav-actions">
        <!-- Compare -->
        <a href="#" class="nav-pill-btn" title="مقارنة الموديلات">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
          <span>المقارنة</span>
          <span class="pill-counter">3</span>
        </a>

        <!-- Cart -->
        <a href="#" class="nav-pill-btn" title="سلة المشتريات">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          <span>السلة</span>
          <span class="pill-counter green">2</span>
        </a>

        <!-- WhatsApp Direct Sales -->
        <a href="https://wa.me/201000000000" class="whatsapp-direct-btn" title="تواصل مباشر عبر واتساب">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.592 2.654-.696c1.029.575 1.748.817 2.806.817 3.181 0 5.767-2.587 5.768-5.766.001-3.182-2.585-5.768-5.768-5.768zm0 10.37c-.894 0-1.67-.238-2.427-.69l-.174-.103-1.802.472.48-1.758-.113-.181c-.504-.805-.77-1.524-.769-2.544 0-2.535 2.062-4.597 4.597-4.597 2.536 0 4.598 2.063 4.598 4.598 0 2.535-2.063 4.597-4.597 4.597z"/></svg>
          <span>مبيعات الشركات</span>
        </a>
      </div>
    </header>

    <!-- Subnav -->
    <nav class="subnav-bar">
      <div class="all-departments-pill">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        <span>جميع حلول الشبكات</span>
      </div>
      <ul class="subnav-links">
        <li><a href="#" class="{ 'active' if active_cat=='switches' else '' }">سويتشات (Switches)</a></li>
        <li><a href="#" class="{ 'active' if active_cat=='routers' else '' }">راوترات وسيرفرات</a></li>
        <li><a href="#" class="{ 'active' if active_cat=='firewalls' else '' }">جدران الحماية (Firewalls)</a></li>
        <li><a href="#" class="{ 'active' if active_cat=='wifi' else '' }">أكسس بوينت (Wi-Fi)</a></li>
        <li><a href="#" class="{ 'active' if active_cat=='ups' else '' }">مغذيات الطاقة (UPS)</a></li>
        <li><a href="#" class="{ 'active' if active_cat=='racks' else '' }">راكات وكبائن (Racks)</a></li>
        <li><a href="#" class="{ 'active' if active_cat=='cables' else '' }">كابلات وتوصيلات</a></li>
        <li><a href="#" style="color:#38bdf8; font-weight:800;">🔥 العروض الحالية</a></li>
      </ul>
    </nav>
    """

def get_footer_html():
    return f"""
    <footer class="footer-wrap">
      <div class="footer-container">
        <div class="footer-col">
          <img src="assets/logo_white.png" style="height:44px; margin-bottom:16px;" alt="MESS TECH">
          <p style="font-size:13.5px; line-height:1.8; color:var(--slate-400); margin-bottom:16px;">
            شركة <b>MESS TECH</b> رائدة في توريد وتجهيز حلول الشبكات، البنية التحتية، وأمن المعلومات للمشروعات والشركات. نوفر أحدث الموديلات الأصلية المعتمدة بأسعار تنافسية ودعم فني هندسي متقدم.
          </p>
          <div style="display:flex; align-items:center; gap:12px;">
            <span class="badge-notice-header" style="font-size:12px;">أجهزة أصلية معتمدة 100%</span>
            <span style="color:#fff; font-size:13px;">تواصل مباشر: <b>sales@messtech.com</b></span>
          </div>
        </div>

        <div class="footer-col">
          <h5>أقسام التجهيزات</h5>
          <ul class="footer-list">
            <li><a href="#">سويتشات سيسكو كاتاليست</a></li>
            <li><a href="#">راوترات مايكروتك السحابية</a></li>
            <li><a href="#">أجهزة فايروول فورتينت FortiGate</a></li>
            <li><a href="#">أكسس بوينت Ubiquiti UniFi 6</a></li>
            <li><a href="#">وحدات مغذيات الطاقة APC UPS</a></li>
            <li><a href="#">كبائن وراكات السيرفر 9U - 42U</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>خدمات ومعلومات</h5>
          <ul class="footer-list">
            <li><a href="#">الشحن والتوصيل لجميع المحافظات</a></li>
            <li><a href="#">الاستلام المباشر من مقر الشركة</a></li>
            <li><a href="#">الدعم الفني الهندسي والاستشارات</a></li>
            <li><a href="#">تحميل ملفات Datasheet المعتمدة</a></li>
            <li><a href="#">مقارنة مواصفات الموديلات</a></li>
            <li><a href="#">سياسة الإرجاع والاستبدال</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>الدعم والمبيعات المباشرة</h5>
          <p style="font-size:13px; color:var(--slate-400); margin-bottom:12px;">
            فريق المهندسين متاح للرد الفوري على استفسارات الموديلات والمواصفات الفنية:
          </p>
          <div style="background:var(--navy-800); border:1px solid var(--navy-700); padding:14px; border-radius:10px; margin-bottom:12px;">
            <div style="font-size:12px; color:var(--slate-400);">رقم المبيعات المباشر:</div>
            <div class="mono" style="font-size:18px; font-weight:700; color:var(--cyan-400); margin-top:2px;">+20 100 234 5678</div>
          </div>
          <a href="https://wa.me/201000000000" class="whatsapp-direct-btn" style="justify-content:center;">
            محادثة فورية مع المبيعات عبر واتساب
          </a>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <div>جميع الحقوق محفوظة © 2026 لشركة <b>MESS TECH</b> — Tech Solutions Global.</div>
        <div style="display:flex; gap:20px; align-items:center;">
          <span style="color:#38bdf8;">✓ أجهزة أصلية معتمدة</span>
          <span>✓ فحص ومطابقة الأجهزة والمواصفات</span>
          <span>✓ دعم فني هندسي مخصص</span>
        </div>
      </div>
    </footer>
    """

print("Base layout helpers defined successfully!")

