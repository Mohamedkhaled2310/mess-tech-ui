# -*- coding: utf-8 -*-
"""
Mobile UI/UX Pages Generator for MESS TECH Store
Edge-to-edge mobile viewport
"""

import os
import subprocess
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS

DESIGNS_DIR = r"E:\mess\designs"
ASSETS_DIR = os.path.join(DESIGNS_DIR, "assets")

MOBILE_COMMON_CSS = """
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

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Cairo', sans-serif; -webkit-tap-highlight-color: transparent; }
html, body {
  width: 100%;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
body {
  background: var(--bg-page);
  color: var(--navy-900);
  direction: rtl;
  text-align: right;
  position: relative;
  min-height: 100vh;
}
.mono { font-family: 'JetBrains Mono', monospace; direction: ltr; display: inline-block; }

/* Mobile Top Announcement */
.m-top-announcement {
  background: var(--navy-950);
  color: #34d399;
  font-size: 11px;
  font-weight: 700;
  padding: 7px 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

/* Mobile Header */
.m-navbar {
  background: var(--navy-900);
  padding: 12px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--navy-700);
  position: sticky;
  top: 0;
  z-index: 50;
}
.m-nav-right {
  display: flex;
  align-items: center;
  gap: 10px;
}
.m-logo {
  height: 32px;
  width: auto;
  object-fit: contain;
}
.m-nav-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}
.m-btn-icon {
  width: 36px;
  height: 36px;
  background: var(--navy-800);
  border: 1px solid var(--navy-700);
  border-radius: 8px;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  position: relative;
}
.m-pill-num {
  position: absolute;
  top: -4px;
  left: -4px;
  background: var(--cyan-500);
  color: #fff;
  font-size: 10px;
  font-weight: 800;
  padding: 1px 5px;
  border-radius: 999px;
}
.m-pill-num.green { background: var(--emerald-500); }

/* Mobile Sticky Bottom Nav */
.m-bottom-nav-bar {
  background: #0b1120;
  border-top: 1px solid #1e293b;
  padding: 8px 10px 14px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: sticky;
  bottom: 0;
  z-index: 60;
  box-shadow: 0 -4px 16px rgba(0,0,0,0.25);
}
.m-bottom-nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  color: #94a3b8;
  font-size: 10px;
  font-weight: 700;
  text-decoration: none;
  position: relative;
}
.m-bottom-nav-item.active { color: var(--cyan-400); }
.m-bottom-nav-item svg { width: 19px; height: 19px; }
.bottom-badge {
  position: absolute;
  top: -2px;
  left: 6px;
  background: var(--emerald-500);
  color: #fff;
  font-size: 9px;
  font-weight: 800;
  padding: 0 4px;
  border-radius: 999px;
}

/* Mobile Search Box */
.m-search-container {
  background: var(--navy-900);
  padding: 0 14px 12px;
  border-bottom: 1px solid var(--navy-700);
}
.m-search-input-wrap {
  display: flex;
  align-items: center;
  background: var(--navy-800);
  border: 1.5px solid #2d3b55;
  border-radius: 10px;
  padding: 2px 6px;
}
.m-search-input-field {
  flex: 1;
  background: transparent;
  border: none;
  padding: 8px 10px;
  color: #fff;
  font-size: 12.5px;
  outline: none;
}
.m-search-input-field::placeholder { color: var(--slate-500); font-size: 12px; }
.m-search-btn-icon {
  background: var(--cyan-500);
  color: #fff;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 7px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Quick Categories Horizontal Scroll */
.m-cats-scroller {
  display: flex;
  gap: 8px;
  padding: 12px 14px;
  overflow-x: auto;
  background: #fff;
  border-bottom: 1px solid var(--slate-200);
  scrollbar-width: none;
}
.m-cats-scroller::-webkit-scrollbar { display: none; }
.m-cat-tag {
  background: #f1f5f9;
  border: 1px solid #cbd5e1;
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 700;
  color: #334155;
  white-space: nowrap;
  text-decoration: none;
}
.m-cat-tag.active {
  background: var(--cyan-500);
  color: #fff;
  border-color: var(--cyan-500);
}
"""

def get_mobile_header(active_nav="home"):
    return f"""
    <!-- Top Announcement -->
    <div class="m-top-announcement">
      <span>✓ الدفع كاش عند الاستلام (COD) فقط لجميع محافظات مصر</span>
      <span style="color:#fff; font-size:10px;">استلام من الفرع مجاناً</span>
    </div>

    <!-- Mobile Header -->
    <header class="m-navbar">
      <div class="m-nav-right">
        <button class="m-btn-icon" title="القائمة">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
        </button>
        <a href="#">
          <img src="assets/logo_white.png" class="m-logo" alt="MESS TECH">
        </a>
      </div>

      <div class="m-nav-actions">
        <!-- Compare -->
        <a href="#" class="m-btn-icon" title="المقارنة">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
          <span class="m-pill-num">3</span>
        </a>
        <!-- Cart -->
        <a href="#" class="m-btn-icon" title="السلة (COD)">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
          <span class="m-pill-num green">2</span>
        </a>
        <!-- WhatsApp -->
        <a href="https://wa.me/201000000000" class="m-btn-icon" style="background:#22c55e; border-color:#22c55e;" title="واتساب المبيعات">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.592 2.654-.696c1.029.575 1.748.817 2.806.817 3.181 0 5.767-2.587 5.768-5.766.001-3.182-2.585-5.768-5.768-5.768zm0 10.37c-.894 0-1.67-.238-2.427-.69l-.174-.103-1.802.472.48-1.758-.113-.181c-.504-.805-.77-1.524-.769-2.544 0-2.535 2.062-4.597 4.597-4.597 2.536 0 4.598 2.063 4.598 4.598 0 2.535-2.063 4.597-4.597 4.597z"/></svg>
        </a>
      </div>
    </header>

    <!-- Search Box -->
    <div class="m-search-container">
      <div class="m-search-input-wrap">
        <input type="text" class="m-search-input-field" placeholder="ابحث برقم الموديل (مثل WS-C2960X، FG-60F) أو كود SKU...">
        <button class="m-search-btn-icon">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        </button>
      </div>
    </div>
    """

def get_mobile_bottom_nav(active="home"):
    return f"""
    <!-- Sticky Mobile Bottom Navigation -->
    <nav class="m-bottom-nav-bar">
      <a href="#" class="m-bottom-nav-item {'active' if active=='home' else ''}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
        <span>الرئيسية</span>
      </a>
      <a href="#" class="m-bottom-nav-item {'active' if active=='categories' else ''}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        <span>الأقسام</span>
      </a>
      <a href="#" class="m-bottom-nav-item {'active' if active=='compare' else ''}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
        <span class="bottom-badge" style="background:var(--cyan-500);">3</span>
        <span>المقارنة</span>
      </a>
      <a href="#" class="m-bottom-nav-item {'active' if active=='cart' else ''}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
        <span class="bottom-badge">2</span>
        <span>السلة (COD)</span>
      </a>
      <a href="#" class="m-bottom-nav-item {'active' if active=='account' else ''}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        <span>حسابي</span>
      </a>
    </nav>
    """

print("Updated mobile framework!")
