# -*- coding: utf-8 -*-
import os

DESIGNS_DIR = r"E:\mess\designs"
ROOT_DIR = r"E:\mess"

FRAMES_DATA = [
    # ==========================
    # 0. DESIGN SYSTEM & COLOR PALETTE
    # ==========================
    {
        "id": "frame-palette",
        "section": "palette",
        "num": "00",
        "title": "دليل الألوان ونظام التصميم (Design System & Color Tokens)",
        "dims": "1440 × 1100",
        "src": "00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png",
        "icon": "🎨"
    },

    # ==========================
    # 1. STOREFRONT & CUSTOMER PORTAL (9 Screens)
    # ==========================
    {
        "id": "frame-0",
        "section": "storefront",
        "num": "01",
        "title": "الصفحة الرئيسية (Desktop Storefront)",
        "dims": "1440 × 2300",
        "src": "01_الصفحة_الرئيسية_Desktop_Homepage.png",
        "icon": "🏠"
    },
    {
        "id": "frame-1",
        "section": "storefront",
        "num": "02",
        "title": "صفحة تفاصيل المنتج والمواصفات (Product Details)",
        "dims": "1440 × 2400",
        "src": "02_صفحة_المنتج_والمواصفات_Desktop_Product_Details.png",
        "icon": "📄"
    },
    {
        "id": "frame-2",
        "section": "storefront",
        "num": "03",
        "title": "الفلاتر والبحث التقني (Catalog & Filters)",
        "dims": "1440 × 2200",
        "src": "03_صفحة_الفلاتر_والبحث_Desktop_Catalog_Filters.png",
        "icon": "🔍"
    },
    {
        "id": "frame-3",
        "section": "storefront",
        "num": "04",
        "title": "جدول مقارنة المواصفات (Comparison Matrix)",
        "dims": "1440 × 2200",
        "src": "04_صفحة_مقارنة_المواصفات_Desktop_Product_Comparison.png",
        "icon": "⚖️"
    },
    {
        "id": "frame-4",
        "section": "storefront",
        "num": "05",
        "title": "السلة وإتمام الطلب COD (One-Step Checkout)",
        "dims": "1440 × 2100",
        "src": "05_صفحة_السلة_واتمام_الطلب_Desktop_Cart_Checkout_COD.png",
        "icon": "🛒"
    },
    {
        "id": "frame-5",
        "section": "storefront",
        "num": "06",
        "title": "صفحة تأكيد واستلام الطلب (Thank You Page)",
        "dims": "1440 × 1350",
        "src": "08_صفحة_نجاح_الطلب_Desktop_Order_Success.png",
        "icon": "✓"
    },
    {
        "id": "frame-6",
        "section": "storefront",
        "num": "07",
        "title": "تسجيل الدخول وبوابة العملاء (Customer Auth)",
        "dims": "1440 × 1150",
        "src": "10_تسجيل_الدخول_وإنشاء_حساب_Desktop_Auth_Login.png",
        "icon": "🔑"
    },
    {
        "id": "frame-7",
        "section": "storefront",
        "num": "08",
        "title": "لوحة حسابي ودفتر العناوين (Customer Profile)",
        "dims": "1440 × 1450",
        "src": "11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png",
        "icon": "👤"
    },
    {
        "id": "frame-8",
        "section": "storefront",
        "num": "09",
        "title": "سجل الطلبات السابقة (Order History)",
        "dims": "1440 × 1400",
        "src": "12_سجل_الطلبات_السابقة_Desktop_Order_History.png",
        "icon": "📦"
    },

    # ==========================
    # 2. COMPLETE ADMIN SUITE (8 Screens)
    # ==========================
    {
        "id": "frame-9",
        "section": "admin",
        "num": "A01",
        "title": "لوحة تحكم الإدارة العامة (Admin Overview)",
        "dims": "1440 × 1100",
        "src": "07_لوحة_التحكم_Admin_Dashboard_Overview.png",
        "icon": "📊"
    },
    {
        "id": "frame-10",
        "section": "admin",
        "num": "A02",
        "title": "إضافة وتعديل منتج بالمستودع (Add/Edit Product)",
        "dims": "1440 × 1650",
        "src": "13_إضافة_وتعديل_منتج_Desktop_Admin_Add_Product.png",
        "icon": "📦"
    },
    {
        "id": "frame-11",
        "section": "admin",
        "num": "A03",
        "title": "جدول إدارة ومتابعة الطلبات (Orders Management Table)",
        "dims": "1440 × 1400",
        "src": "14_جدول_إدارة_الطلبات_Desktop_Admin_Orders_Table.png",
        "icon": "🛒"
    },
    {
        "id": "frame-12",
        "section": "admin",
        "num": "A04",
        "title": "تفاصيل أمر الطلب الفردي (Admin Order Details)",
        "dims": "1440 × 1400",
        "src": "15_تفاصيل_الطلب_إدارة_Desktop_Admin_Order_Details.png",
        "icon": "📋"
    },
    {
        "id": "frame-13",
        "section": "admin",
        "num": "A05",
        "title": "إدارة العملاء والشركات (Customers Management)",
        "dims": "1440 × 1350",
        "src": "16_إدارة_العملاء_والشركات_Desktop_Admin_Customers.png",
        "icon": "👥"
    },
    {
        "id": "frame-14",
        "section": "admin",
        "num": "A06",
        "title": "إدارة الأقسام والتصنيفات (Categories Management)",
        "dims": "1440 × 1300",
        "src": "17_إدارة_الأقسام_والتصنيفات_Desktop_Admin_Categories.png",
        "icon": "📁"
    },
    {
        "id": "frame-15",
        "section": "admin",
        "num": "A07",
        "title": "تقارير المبيعات والتحليلات (Sales & Analytics)",
        "dims": "1440 × 1350",
        "src": "18_تقارير_المبيعات_والتحليلات_Desktop_Admin_Reports.png",
        "icon": "📈"
    },
    {
        "id": "frame-16",
        "section": "admin",
        "num": "A08",
        "title": "إعدادات المتجر والشحن وسياسة COD (Settings)",
        "dims": "1440 × 1400",
        "src": "19_إعدادات_المتجر_والشحن_Desktop_Admin_Settings.png",
        "icon": "⚙️"
    },

    # ==========================
    # 3. MOBILE SCREENS (11 Screens)
    # ==========================
    {
        "id": "frame-17",
        "section": "mobile",
        "num": "M01",
        "title": "الرئيسية بالموبايل (Mobile Homepage)",
        "dims": "390 × 844",
        "src": "Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png",
        "icon": "📱"
    },
    {
        "id": "frame-18",
        "section": "mobile",
        "num": "M02",
        "title": "صفحة تفاصيل المنتج بالموبايل",
        "dims": "390 × 844",
        "src": "Mobile_02_صفحة_المنتج_والمواصفات_Mobile_Product_Details.png",
        "icon": "📱"
    },
    {
        "id": "frame-19",
        "section": "mobile",
        "num": "M03",
        "title": "الفلاتر وتصفح الكتالوج بالموبايل",
        "dims": "390 × 844",
        "src": "Mobile_03_الفلاتر_وتصفح_المنتجات_Mobile_Catalog_Filters.png",
        "icon": "📱"
    },
    {
        "id": "frame-20",
        "section": "mobile",
        "num": "M04",
        "title": "السلة وإتمام الطلب COD بالموبايل",
        "dims": "390 × 844",
        "src": "Mobile_04_السلة_واتمام_الطلب_COD_Mobile_Checkout.png",
        "icon": "📱"
    },
    {
        "id": "frame-21",
        "section": "mobile",
        "num": "M05",
        "title": "مقارنة الموديلات بالسحب بالموبايل",
        "dims": "390 × 844",
        "src": "Mobile_05_مقارنة_الموديلات_Mobile_Product_Comparison.png",
        "icon": "📱"
    },
    {
        "id": "frame-22",
        "section": "mobile",
        "num": "M06",
        "title": "تأكيد واستلام الطلب بالموبايل (Thank You)",
        "dims": "390 × 844",
        "src": "Mobile_06_نجاح_الطلب_Mobile_Order_Success.png",
        "icon": "📱"
    },
    {
        "id": "frame-23",
        "section": "mobile",
        "num": "M07",
        "title": "تسجيل الدخول وبوابة العملاء بالموبايل",
        "dims": "390 × 844",
        "src": "Mobile_08_تسجيل_الدخول_وحساب_جديد_Mobile_Auth_Login.png",
        "icon": "📱"
    },
    {
        "id": "frame-24",
        "section": "mobile",
        "num": "M08",
        "title": "لوحة حسابي ودفتر العناوين بالموبايل",
        "dims": "390 × 844",
        "src": "Mobile_09_لوحة_حسابي_والعناوين_Mobile_Customer_Profile.png",
        "icon": "📱"
    },
    {
        "id": "frame-25",
        "section": "mobile",
        "num": "M09",
        "title": "سجل الطلبات السابقة بالموبايل",
        "dims": "390 × 844",
        "src": "Mobile_10_سجل_طلباتي_السابقة_Mobile_Order_History.png",
        "icon": "📱"
    },
    {
        "id": "frame-26",
        "section": "mobile",
        "num": "M10",
        "title": "لوحة إدارة الطلبات بالموبايل (Admin Mobile)",
        "dims": "390 × 844",
        "src": "Mobile_11_إدارة_الطلبات_والمنتجات_Mobile_Admin_Management.png",
        "icon": "📱"
    },
    {
        "id": "frame-27",
        "section": "mobile",
        "num": "Showcase",
        "title": "بانوراما هواتف الموبايل المجمعة",
        "dims": "1440 × 1100",
        "src": "06_نسخة_الموبايل_Mobile_Screens_Showcase.png",
        "icon": "🖼️"
    }
]

def generate_index():
    palette_frames = ""
    storefront_frames = ""
    admin_frames = ""
    mobile_frames = ""
    
    sidebar_palette = ""
    sidebar_storefront = ""
    sidebar_admin = ""
    sidebar_mobile = ""

    for idx, item in enumerate(FRAMES_DATA):
        sec = item["section"]
        is_desktop = sec in ["palette", "storefront", "admin"]
        frame_cls = "desktop-frame" if is_desktop else ("showcase-frame" if item["num"] == "Showcase" else "mobile-frame")
        selected_cls = "selected" if idx == 0 else ""
        active_sidebar = "active" if idx == 0 else ""

        frame_markup = f"""
          <!-- Frame {idx}: {item['num']} -->
          <div class="figma-frame {frame_cls} {selected_cls}" data-frame-index="{idx}" id="{item['id']}">
            <div class="frame-label">
              <span class="frame-hash">#</span>
              <span>{item['num']} · {item['title']}</span>
              <span class="frame-dims">{item['dims']}</span>
            </div>
            <div class="frame-card">
              <div class="handle tl"></div><div class="handle tr"></div><div class="handle bl"></div><div class="handle br"></div>
              <div class="frame-hover-actions">
                <button class="frame-btn" onclick="openFocusModal({idx}); event.stopPropagation();">👁️ تكبير</button>
                <a href="{item['src']}" download class="frame-btn" onclick="event.stopPropagation();">⬇️ تحميل</a>
              </div>
              <img src="{item['src']}" alt="{item['num']} {item['title']}" loading="{'eager' if idx < 4 else 'lazy'}">
            </div>
          </div>
        """

        sidebar_markup = f"""
          <li class="sidebar-item {active_sidebar}" data-index="{idx}">
            <span class="item-icon">{item['icon']}</span>
            <span class="item-title">{item['num']} · {item['title']}</span>
          </li>
        """

        if sec == "palette":
            palette_frames += frame_markup
            sidebar_palette += sidebar_markup
        elif sec == "storefront":
            storefront_frames += frame_markup
            sidebar_storefront += sidebar_markup
        elif sec == "admin":
            admin_frames += frame_markup
            sidebar_admin += sidebar_markup
        else:
            mobile_frames += frame_markup
            sidebar_mobile += sidebar_markup

    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | لوحة التصاميم التفاعلية (Figma Canvas Showcase)</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --figma-bg: #1e1e1e;
      --figma-canvas-dot: #333333;
      --figma-panel-bg: #2c2c2c;
      --figma-panel-border: #3c3c3c;
      --figma-text-primary: #ffffff;
      --figma-text-secondary: #999999;
      --figma-text-muted: #666666;
      --figma-blue: #0d99ff;
      --figma-blue-hover: #007be5;
      --figma-accent: #0099e5;
      --figma-card-bg: #141414;
      --figma-hover-bg: #383838;
      --font-cairo: 'Cairo', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: var(--font-cairo);
      -webkit-user-select: none;
      user-select: none;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      overflow: hidden;
      background: var(--figma-bg);
      color: var(--figma-text-primary);
      position: relative;
    }}

    .mono {{
      font-family: var(--font-mono);
      direction: ltr;
      display: inline-block;
    }}

    #viewport {{
      position: absolute;
      top: 48px;
      left: 0;
      right: 0;
      bottom: 0;
      overflow: hidden;
      cursor: grab;
      touch-action: none;
      background-color: var(--figma-bg);
      background-image: radial-gradient(var(--figma-canvas-dot) 1.2px, transparent 1.2px);
      background-size: 24px 24px;
      z-index: 1;
    }}

    #viewport.dragging {{
      cursor: grabbing !important;
    }}

    #canvas-world {{
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      display: flex;
      flex-direction: column;
      gap: 120px;
      padding: 120px 100px 300px 100px;
      will-change: transform;
    }}

    .board-section {{
      display: flex;
      flex-direction: column;
      gap: 32px;
    }}

    .section-header-tag {{
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: rgba(44, 44, 44, 0.85);
      border: 1px solid var(--figma-panel-border);
      backdrop-filter: blur(10px);
      padding: 10px 22px;
      border-radius: 12px;
      width: fit-content;
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }}

    .section-header-tag .title {{
      font-size: 18px;
      font-weight: 800;
      color: #fff;
    }}

    .section-header-tag .meta {{
      font-family: var(--font-mono);
      font-size: 13px;
      color: var(--figma-blue);
      background: rgba(13, 153, 255, 0.12);
      padding: 3px 10px;
      border-radius: 6px;
    }}

    .frames-row {{
      display: flex;
      flex-direction: row;
      gap: 60px;
      align-items: flex-start;
    }}

    .figma-frame {{
      display: flex;
      flex-direction: column;
      position: relative;
      cursor: pointer;
      transition: filter 0.2s ease;
    }}

    .frame-label {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 12px;
      font-size: 14px;
      font-weight: 700;
      color: var(--figma-text-secondary);
      direction: rtl;
      transition: color 0.15s ease;
    }}

    .frame-label .frame-hash {{
      color: var(--figma-blue);
      font-family: var(--font-mono);
      font-weight: 800;
      font-size: 15px;
    }}

    .frame-label .frame-dims {{
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: var(--figma-text-muted);
      background: rgba(255,255,255,0.06);
      padding: 2px 7px;
      border-radius: 4px;
    }}

    .figma-frame:hover .frame-label,
    .figma-frame.selected .frame-label {{
      color: #fff;
    }}

    .frame-card {{
      background: #000;
      border-radius: 8px;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.65), 0 0 0 1px rgba(255, 255, 255, 0.08);
      position: relative;
      transition: box-shadow 0.2s ease, transform 0.2s ease;
      overflow: hidden;
    }}

    .figma-frame.selected .frame-card {{
      box-shadow: 0 0 0 3px var(--figma-blue), 0 25px 60px rgba(0,0,0,0.8);
    }}

    .frame-card .handle {{
      position: absolute;
      width: 10px;
      height: 10px;
      background: #fff;
      border: 1.5px solid var(--figma-blue);
      border-radius: 2px;
      opacity: 0;
      pointer-events: none;
      z-index: 10;
      transition: opacity 0.15s ease;
    }}
    .figma-frame.selected .handle {{ opacity: 1; }}
    .handle.tl {{ top: -5px; left: -5px; }}
    .handle.tr {{ top: -5px; right: -5px; }}
    .handle.bl {{ bottom: -5px; left: -5px; }}
    .handle.br {{ bottom: -5px; right: -5px; }}

    .desktop-frame .frame-card {{
      width: 1440px;
    }}
    .desktop-frame img {{
      width: 1440px;
      height: auto;
      display: block;
    }}

    .mobile-frame .frame-card {{
      width: 440px;
      border-radius: 46px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.12);
    }}
    .mobile-frame img {{
      width: 440px;
      height: auto;
      display: block;
    }}

    .showcase-frame .frame-card {{
      width: 1440px;
    }}
    .showcase-frame img {{
      width: 1440px;
      height: auto;
      display: block;
    }}

    .frame-hover-actions {{
      position: absolute;
      top: 14px;
      left: 14px;
      display: flex;
      gap: 8px;
      z-index: 15;
      opacity: 0;
      transform: translateY(-4px);
      transition: all 0.2s ease;
    }}
    .figma-frame:hover .frame-hover-actions {{
      opacity: 1;
      transform: translateY(0);
    }}
    .frame-btn {{
      background: rgba(30, 30, 30, 0.85);
      border: 1px solid rgba(255,255,255,0.15);
      color: #fff;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      backdrop-filter: blur(8px);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      box-shadow: 0 4px 12px rgba(0,0,0,0.4);
      transition: background 0.15s;
    }}
    .frame-btn:hover {{
      background: var(--figma-blue);
      border-color: var(--figma-blue);
    }}

    /* ========================================================= */
    /* UPGRADED AUTHENTIC FIGMA TOPBAR                           */
    /* ========================================================= */
    .figma-top-bar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 48px;
      background: var(--figma-panel-bg);
      border-bottom: 1px solid var(--figma-panel-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 14px;
      z-index: 100;
      box-shadow: 0 4px 16px rgba(0,0,0,0.3);
      direction: ltr;
    }}

    /* LEFT ZONE: Brand & Project */
    .top-left-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .figma-brand-mark {{
      width: 32px;
      height: 32px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .figma-brand-mark:hover {{
      background: var(--figma-hover-bg);
      border-color: rgba(255, 255, 255, 0.15);
    }}
    .file-info-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .file-name {{
      font-size: 13px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}
    .file-dropdown-icon {{
      font-size: 10px;
      color: var(--figma-text-secondary);
    }}
    .file-badge-version {{
      font-size: 10.5px;
      font-weight: 700;
      color: #34d399;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 2px 8px;
      border-radius: 999px;
    }}
    .file-badge-frames {{
      font-size: 10.5px;
      font-weight: 700;
      color: #94a3b8;
      background: rgba(255, 255, 255, 0.06);
      padding: 2px 8px;
      border-radius: 999px;
    }}

    /* CENTER ZONE: Segmented Section Switcher */
    .top-nav-switcher {{
      display: flex;
      align-items: center;
      background: rgba(0, 0, 0, 0.4);
      border: 1px solid var(--figma-panel-border);
      border-radius: 8px;
      padding: 3px;
      gap: 3px;
    }}
    .switcher-tab {{
      background: transparent;
      border: none;
      color: var(--figma-text-secondary);
      font-size: 12px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 5px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .switcher-tab:hover {{
      background: rgba(255, 255, 255, 0.06);
      color: #fff;
    }}
    .switcher-tab.active {{
      background: var(--figma-hover-bg);
      color: #fff;
      font-weight: 700;
      box-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }}
    .tab-count {{
      font-size: 10px;
      font-family: var(--font-mono);
      background: rgba(255, 255, 255, 0.12);
      padding: 1px 6px;
      border-radius: 4px;
      color: #cbd5e1;
    }}

    /* RIGHT ZONE: Pro Figma Tools */
    .top-right-tools {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .top-tool-btn {{
      background: transparent;
      border: 1px solid var(--figma-panel-border);
      color: var(--figma-text-primary);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }}
    .top-tool-btn:hover {{
      background: var(--figma-hover-bg);
      border-color: rgba(255,255,255,0.2);
    }}
    .top-tool-btn.palette-btn {{
      background: rgba(0, 153, 229, 0.12);
      border-color: rgba(0, 153, 229, 0.35);
      color: #38bdf8;
      font-weight: 700;
    }}
    .top-tool-btn.palette-btn:hover {{
      background: rgba(0, 153, 229, 0.22);
      border-color: var(--figma-blue);
    }}
    .palette-swatch-dots {{
      display: inline-flex;
      gap: 3px;
      align-items: center;
    }}
    .palette-swatch-dots span {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
    }}

    .top-present-btn {{
      background: var(--figma-blue);
      color: #fff;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
      box-shadow: 0 2px 8px rgba(13, 153, 255, 0.35);
    }}
    .top-present-btn:hover {{
      background: var(--figma-blue-hover);
    }}

    /* Floating Canvas Help Badge (Bottom Left) */
    .canvas-help-badge {{
      position: fixed;
      bottom: 22px;
      left: 24px;
      background: rgba(35, 35, 35, 0.9);
      backdrop-filter: blur(10px);
      border: 1px solid var(--figma-panel-border);
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 11.5px;
      color: var(--figma-text-secondary);
      display: flex;
      align-items: center;
      gap: 8px;
      z-index: 80;
      pointer-events: none;
      box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    }}
    .canvas-help-badge kbd {{
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 1px 6px;
      border-radius: 4px;
    }}

    /* Sidebar */
    .figma-sidebar {{
      position: fixed;
      top: 48px;
      right: 0;
      width: 330px;
      bottom: 0;
      background: var(--figma-panel-bg);
      border-left: 1px solid var(--figma-panel-border);
      z-index: 90;
      display: flex;
      flex-direction: column;
      transform: translateX(0);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: -6px 0 24px rgba(0,0,0,0.3);
      direction: rtl;
    }}

    .figma-sidebar.collapsed {{
      transform: translateX(100%);
    }}

    .sidebar-header {{
      padding: 14px 16px;
      border-bottom: 1px solid var(--figma-panel-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .sidebar-header h3 {{
      font-size: 13px;
      font-weight: 800;
      color: #fff;
      letter-spacing: 0.3px;
    }}
    .count-badge {{
      background: rgba(255,255,255,0.08);
      font-size: 11px;
      font-family: var(--font-mono);
      padding: 2px 7px;
      border-radius: 4px;
      color: var(--figma-text-secondary);
    }}

    .sidebar-list {{
      flex: 1;
      overflow-y: auto;
      padding: 8px;
      list-style: none;
    }}
    .sidebar-group-title {{
      font-size: 11px;
      font-weight: 800;
      color: var(--figma-text-muted);
      text-transform: uppercase;
      padding: 12px 10px 6px;
      letter-spacing: 0.5px;
    }}
    .sidebar-item {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 10px;
      border-radius: 6px;
      cursor: pointer;
      color: var(--figma-text-secondary);
      font-size: 12.5px;
      font-weight: 600;
      transition: all 0.12s;
    }}
    .sidebar-item:hover {{
      background: var(--figma-hover-bg);
      color: #fff;
    }}
    .sidebar-item.active {{
      background: rgba(13, 153, 255, 0.12);
      color: var(--figma-blue);
      font-weight: 700;
    }}
    .item-icon {{ font-size: 14px; }}
    .item-title {{ flex: 1; }}

    /* Floating Toolbar (Dock) */
    .figma-toolbar {{
      position: fixed;
      bottom: 22px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--figma-panel-bg);
      border: 1px solid var(--figma-panel-border);
      border-radius: 999px;
      height: 44px;
      padding: 0 8px;
      display: flex;
      align-items: center;
      gap: 4px;
      z-index: 100;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      direction: ltr;
    }}
    .tool-btn {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: transparent;
      border: none;
      color: var(--figma-text-secondary);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .tool-btn:hover {{
      background: var(--figma-hover-bg);
      color: #fff;
    }}
    .tool-btn.active {{
      background: var(--figma-blue);
      color: #fff;
    }}
    .toolbar-divider {{
      width: 1px;
      height: 20px;
      background: var(--figma-panel-border);
      margin: 0 4px;
    }}
    .zoom-readout {{
      font-size: 12px;
      font-weight: 700;
      color: #fff;
      padding: 4px 8px;
      border-radius: 4px;
      cursor: pointer;
      min-width: 52px;
      text-align: center;
    }}
    .zoom-readout:hover {{
      background: var(--figma-hover-bg);
    }}

    /* Inspect & Palette Modals */
    .inspect-modal {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(10, 10, 10, 0.94);
      backdrop-filter: blur(12px);
      z-index: 200;
      display: none;
      flex-direction: column;
    }}
    .inspect-modal.active {{ display: flex; }}
    .modal-top-bar {{
      height: 52px;
      background: rgba(30, 30, 30, 0.95);
      border-bottom: 1px solid var(--figma-panel-border);
      padding: 0 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      direction: ltr;
    }}
    .modal-title-box {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .modal-title-box h2 {{
      font-size: 14.5px;
      font-weight: 800;
      color: #fff;
    }}
    .modal-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .modal-body {{
      flex: 1;
      overflow: auto;
      padding: 40px;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      cursor: zoom-out;
    }}
    .modal-body img {{
      max-width: 100%;
      height: auto;
      border-radius: 10px;
      box-shadow: 0 25px 80px rgba(0,0,0,0.8);
      border: 1px solid rgba(255,255,255,0.15);
      cursor: default;
    }}

    @media (max-width: 1024px) {{
      .top-nav-switcher {{ display: none; }}
      .canvas-help-badge {{ display: none; }}
      .figma-sidebar {{
        width: 100%;
        transform: translateX(100%);
      }}
    }}
  </style>
</head>
<body>

  <!-- UPGRADED FIGMA TOPBAR -->
  <header class="figma-top-bar">
    
    <!-- LEFT: Figma Brand & Project Info -->
    <div class="top-left-brand">
      <div class="figma-brand-mark" title="Figma UI Experience">
        <!-- Official Figma Logo Icon -->
        <svg width="15" height="22" viewBox="0 0 38 57" fill="none">
          <path d="M19 28.5C19 23.2533 23.2533 19 28.5 19C33.7467 19 38 23.2533 38 28.5C38 33.7467 33.7467 38 28.5 38C23.2533 38 19 33.7467 19 28.5Z" fill="#1ABCFE"/>
          <path d="M0 47.5C0 42.2533 4.25329 38 9.5 38H19V47.5C19 52.7467 14.7467 57 9.5 57C4.25329 57 0 52.7467 0 47.5Z" fill="#0ACF83"/>
          <path d="M19 0V19H28.5C33.7467 19 38 14.7467 38 9.5C38 4.25329 33.7467 0 28.5 0H19Z" fill="#FF7262"/>
          <path d="M0 9.5C0 14.7467 4.25329 19 9.5 19H19V0H9.5C4.25329 0 0 4.25329 0 9.5Z" fill="#F24E1E"/>
          <path d="M0 28.5C0 33.7467 4.25329 38 9.5 38H19V19H9.5C4.25329 19 0 23.2533 0 28.5Z" fill="#A259FF"/>
        </svg>
      </div>

      <div class="file-info-group">
        <span class="file-name" title="اسم الملف والمشروع">
          MESS TECH E-Commerce
          <span class="file-dropdown-icon">▾</span>
        </span>
        <span class="file-badge-version">v2.4 Ready</span>
        <span class="file-badge-frames">29 Frames</span>
      </div>
    </div>

    <!-- CENTER: Segmented Section Switcher (Fast Jump) -->
    <nav class="top-nav-switcher">
      <button class="switcher-tab" data-target="palette" onclick="jumpToSection('palette')">
        <span>🎨</span>
        <span>الهوية والألوان</span>
      </button>
      <button class="switcher-tab active" data-target="storefront" onclick="jumpToSection('storefront')">
        <span>💻</span>
        <span>المتجر والعميل</span>
        <span class="tab-count">9</span>
      </button>
      <button class="switcher-tab" data-target="admin" onclick="jumpToSection('admin')">
        <span>🛠️</span>
        <span>لوحة الإدارة</span>
        <span class="tab-count">8</span>
      </button>
      <button class="switcher-tab" data-target="mobile" onclick="jumpToSection('mobile')">
        <span>📱</span>
        <span>شاشات الموبايل</span>
        <span class="tab-count">11</span>
      </button>
    </nav>

    <!-- RIGHT: Pro Figma Tools -->
    <div class="top-right-tools">
      <!-- Color Palette Modal Trigger -->
      <button class="top-tool-btn palette-btn" onclick="openPaletteModal();" title="فتح لوحة الألوان الرسمية ورموز Hex">
        <span class="palette-swatch-dots">
          <span style="background:#0099e5;"></span>
          <span style="background:#10b981;"></span>
          <span style="background:#f59e0b;"></span>
        </span>
        <span>الألوان</span>
      </button>

      <!-- Fit Screen -->
      <button class="top-tool-btn" id="btn-fit-screen" title="احتواء كامل الكانفاس في الشاشة (Fit All)">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
        <span>احتواء</span>
      </button>

      <!-- Present Mode (Full Screen Preview) -->
      <button class="top-present-btn" onclick="openFocusModal(activeFrameIdx)" title="معاينة الشاشة بملء العرض (Present Mode)">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        <span>معاينة (Present)</span>
      </button>

      <!-- Layers Sidebar Toggle -->
      <button class="top-tool-btn" id="toggle-sidebar" title="إظهار / إخفاء قائمة الطبقات والشاشات (Layers)">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg>
        <span>الطبقات</span>
      </button>
    </div>
  </header>

  <!-- Left Sidebar (Layers Navigator) -->
  <aside class="figma-sidebar" id="sidebar">
    <div class="sidebar-header">
      <h3>الطبقات والشاشات (Layers)</h3>
      <span class="count-badge">29 Frames</span>
    </div>

    <ul class="sidebar-list">
      <div class="sidebar-group-title">🎨 دليل الألوان ونظام التصميم (Design System)</div>
      {sidebar_palette}

      <div class="sidebar-group-title">💻 شاشات المتجر وتجربة العميل (Desktop - 9)</div>
      {sidebar_storefront}

      <div class="sidebar-group-title">🛠️ شاشات لوحة تحكم الإدارة الكاملة (Admin Suite - 8)</div>
      {sidebar_admin}

      <div class="sidebar-group-title">📱 شاشات الهواتف الذكية (Mobile iOS - 11)</div>
      {sidebar_mobile}
    </ul>
  </aside>

  <!-- Floating Canvas Help Badge -->
  <div class="canvas-help-badge">
    <span>🖱️ اسحب للتحريك (Pan)</span>
    <span>•</span>
    <span>بكرة الماوس للتكبير والتصغير (Zoom)</span>
    <span>•</span>
    <span><kbd>Space</kbd> + سحب</span>
  </div>

  <!-- Interactive Infinite Canvas Viewport -->
  <div id="viewport">
    <div id="canvas-world">

      <!-- SECTION 0: DESIGN SYSTEM & PALETTE -->
      <section class="board-section" id="section-palette">
        <div class="section-header-tag">
          <span style="font-size:20px;">🎨</span>
          <span class="title">دليل الألوان ونظام التصميم (Design System & Color Tokens)</span>
          <span class="meta">Visual Style Guide</span>
        </div>

        <div class="frames-row">
          {palette_frames}
        </div>
      </section>

      <!-- SECTION 1: STOREFRONT & CUSTOMER PORTAL -->
      <section class="board-section" id="section-storefront">
        <div class="section-header-tag">
          <span style="font-size:20px;">💻</span>
          <span class="title">شاشات المتجر وتجربة العميل (Desktop Storefront & Customer Portal — 9 شاشات)</span>
          <span class="meta">1440px Grid</span>
        </div>

        <div class="frames-row">
          {storefront_frames}
        </div>
      </section>

      <!-- SECTION 2: COMPLETE ADMIN SUITE -->
      <section class="board-section" id="section-admin">
        <div class="section-header-tag">
          <span style="font-size:20px;">🛠️</span>
          <span class="title">شاشات لوحة تحكم الإدارة الكاملة (Desktop Admin Dashboard Suite — 8 شاشات)</span>
          <span class="meta">Full Enterprise Admin</span>
        </div>

        <div class="frames-row">
          {admin_frames}
        </div>
      </section>

      <!-- SECTION 3: MOBILE SCREENS -->
      <section class="board-section" id="section-mobile">
        <div class="section-header-tag">
          <span style="font-size:20px;">📱</span>
          <span class="title">شاشات وتجربة الهواتف الذكية (Mobile iOS Screens — iPhone 15 Pro — 11 شاشة)</span>
          <span class="meta">390 × 844 px (Retina 3x)</span>
        </div>

        <div class="frames-row">
          {mobile_frames}
        </div>
      </section>

    </div>
  </div>

  <!-- Figma Floating Toolbar (Dock) -->
  <div class="figma-toolbar">
    <button class="tool-btn active" id="tool-hand" title="أداة التحريك والسحب (Hand Tool - H)">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v6M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8M6 14.5a4.5 4.5 0 0 0 9 0V11a2 2 0 0 1 2-2v0a2 2 0 0 1 2 2v3.5a8.5 8.5 0 0 1-17 0v-2"/></svg>
    </button>

    <div class="toolbar-divider"></div>

    <button class="tool-btn" id="tool-zoom-out" title="تصغير (Zoom Out)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/></svg>
    </button>

    <div class="zoom-readout mono" id="zoom-text" title="انقر لإعادة الضبط إلى 100%">20%</div>

    <button class="tool-btn" id="tool-zoom-in" title="تكبير (Zoom In)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
    </button>

    <div class="toolbar-divider"></div>

    <button class="tool-btn" id="tool-fit" title="احتواء الكل في الشاشة (Fit All)">
      <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
    </button>

    <button class="tool-btn" id="tool-reset" title="حجم طبيعي 100% (Reset 100%)">
      <span class="mono" style="font-size:11px; font-weight:800;">1:1</span>
    </button>
  </div>

  <!-- Interactive Color Palette Modal -->
  <div class="inspect-modal" id="palette-modal" onclick="closePaletteModal()">
    <div class="modal-top-bar" onclick="event.stopPropagation()">
      <div class="modal-title-box">
        <span style="font-size:18px;">🎨</span>
        <h2>لوحة ألوان متجر MESS TECH الرسمية (Design System Palette)</h2>
      </div>
      <div class="modal-actions">
        <span style="font-size:12px; color:#94a3b8;">انقر على أي كود لنسخه فوراً</span>
        <button class="top-tool-btn" onclick="closePaletteModal()">إغلاق ✕</button>
      </div>
    </div>
    <div class="modal-body" style="padding:30px; display:block; max-width:1100px; margin:0 auto; cursor:default;" onclick="event.stopPropagation()">
      
      <!-- Brand Core -->
      <h3 style="font-size:15px; color:#38bdf8; margin-bottom:14px; font-weight:800; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px; text-align:right;">
        🔷 ألوان العلامة التجارية الأساسية (Brand Core)
      </h3>
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:16px; margin-bottom:28px; text-align:right;">
        
        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; overflow:hidden;">
          <div style="height:60px; background:#0099e5;"></div>
          <div style="padding:10px 12px;">
            <div style="font-size:13px; font-weight:800; color:#fff;">Electric Cyan (رئيسي)</div>
            <div style="font-size:11px; color:#94a3b8; margin:2px 0 6px;">أزرار البحث، التحديدات، وأضف للسلة</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px;">
              <code style="color:#38bdf8; font-weight:700;">#0099E5</code>
              <button onclick="navigator.clipboard.writeText('#0099E5'); alert('تم نسخ: #0099E5');" style="background:#1e293b; color:#fff; border:none; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">نسخ</button>
            </div>
          </div>
        </div>

        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; overflow:hidden;">
          <div style="height:60px; background:#38bdf8;"></div>
          <div style="padding:10px 12px;">
            <div style="font-size:13px; font-weight:800; color:#fff;">Sky Glow (مضيء)</div>
            <div style="font-size:11px; color:#94a3b8; margin:2px 0 6px;">النصوص المميزة والروابط النشطة</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px;">
              <code style="color:#38bdf8; font-weight:700;">#38BDF8</code>
              <button onclick="navigator.clipboard.writeText('#38BDF8'); alert('تم نسخ: #38BDF8');" style="background:#1e293b; color:#fff; border:none; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">نسخ</button>
            </div>
          </div>
        </div>

        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; overflow:hidden;">
          <div style="height:60px; background:#0b1120; border-bottom:1px solid #334155;"></div>
          <div style="padding:10px 12px;">
            <div style="font-size:13px; font-weight:800; color:#fff;">Deep Navy (كحلي تكنولوجي)</div>
            <div style="font-size:11px; color:#94a3b8; margin:2px 0 6px;">الهيدر، العناوين، وبطاقات الديسكتوب</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px;">
              <code style="color:#38bdf8; font-weight:700;">#0B1120</code>
              <button onclick="navigator.clipboard.writeText('#0B1120'); alert('تم نسخ: #0B1120');" style="background:#1e293b; color:#fff; border:none; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">نسخ</button>
            </div>
          </div>
        </div>

        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; overflow:hidden;">
          <div style="height:60px; background:#070d18; border-bottom:1px solid #334155;"></div>
          <div style="padding:10px 12px;">
            <div style="font-size:13px; font-weight:800; color:#fff;">Midnight Black (الفوتر)</div>
            <div style="font-size:11px; color:#94a3b8; margin:2px 0 6px;">الفوتر، الشريط العلوي، وإطار الآيفون</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px;">
              <code style="color:#38bdf8; font-weight:700;">#070D18</code>
              <button onclick="navigator.clipboard.writeText('#070D18'); alert('تم نسخ: #070D18');" style="background:#1e293b; color:#fff; border:none; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">نسخ</button>
            </div>
          </div>
        </div>

      </div>

      <!-- Functional Accents -->
      <h3 style="font-size:15px; color:#10b981; margin-bottom:14px; font-weight:800; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px; text-align:right;">
        ⚡ ألوان التفاعل والتجارة الإلكترونية (E-Commerce Accents)
      </h3>
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:16px; margin-bottom:28px; text-align:right;">
        
        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; overflow:hidden;">
          <div style="height:60px; background:#10b981;"></div>
          <div style="padding:10px 12px;">
            <div style="font-size:13px; font-weight:800; color:#fff;">Emerald Green (الدفع والاستلام)</div>
            <div style="font-size:11px; color:#94a3b8; margin:2px 0 6px;">الدفع عند الاستلام COD وشارات التوفر</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px;">
              <code style="color:#34d399; font-weight:700;">#10B981</code>
              <button onclick="navigator.clipboard.writeText('#10B981'); alert('تم نسخ: #10B981');" style="background:#1e293b; color:#fff; border:none; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">نسخ</button>
            </div>
          </div>
        </div>

        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; overflow:hidden;">
          <div style="height:60px; background:#f59e0b;"></div>
          <div style="padding:10px 12px;">
            <div style="font-size:13px; font-weight:800; color:#fff;">Warm Amber (شراء الآن)</div>
            <div style="font-size:11px; color:#94a3b8; margin:2px 0 6px;">زر الشراء السريع ونجوم التقييم</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px;">
              <code style="color:#fbbf24; font-weight:700;">#F59E0B</code>
              <button onclick="navigator.clipboard.writeText('#F59E0B'); alert('تم نسخ: #F59E0B');" style="background:#1e293b; color:#fff; border:none; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">نسخ</button>
            </div>
          </div>
        </div>

        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; overflow:hidden;">
          <div style="height:60px; background:#f43f5e;"></div>
          <div style="padding:10px 12px;">
            <div style="font-size:13px; font-weight:800; color:#fff;">Crimson Rose (المفضلة)</div>
            <div style="font-size:11px; color:#94a3b8; margin:2px 0 6px;">أيقونة المفضلة وشارات الخصومات</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px;">
              <code style="color:#fb7185; font-weight:700;">#F43F5E</code>
              <button onclick="navigator.clipboard.writeText('#F43F5E'); alert('تم نسخ: #F43F5E');" style="background:#1e293b; color:#fff; border:none; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">نسخ</button>
            </div>
          </div>
        </div>

        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; overflow:hidden;">
          <div style="height:60px; background:#ffffff;"></div>
          <div style="padding:10px 12px;">
            <div style="font-size:13px; font-weight:800; color:#fff;">Pure White (كروت المنتجات)</div>
            <div style="font-size:11px; color:#94a3b8; margin:2px 0 6px;">خلفيات الكروت البيضاء والقوائم</div>
            <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px;">
              <code style="color:#fff; font-weight:700;">#FFFFFF</code>
              <button onclick="navigator.clipboard.writeText('#FFFFFF'); alert('تم نسخ: #FFFFFF');" style="background:#1e293b; color:#fff; border:none; padding:2px 6px; border-radius:4px; font-size:10px; cursor:pointer;">نسخ</button>
            </div>
          </div>
        </div>

      </div>

      <!-- Neutrals -->
      <h3 style="font-size:15px; color:#94a3b8; margin-bottom:14px; font-weight:800; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px; text-align:right;">
        🌫️ الرماديات والأسطح (Surfaces & Neutrals)
      </h3>
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:16px; text-align:right;">
        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:8px; padding:10px;">
          <div style="height:30px; background:#f8fafc; border-radius:4px; margin-bottom:6px;"></div>
          <div style="font-size:12px; font-weight:700; color:#fff;">خلفية الصفحات</div>
          <code style="font-size:11px; color:#94a3b8;">#F8FAFC</code>
        </div>
        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:8px; padding:10px;">
          <div style="height:30px; background:#e2e8f0; border-radius:4px; margin-bottom:6px;"></div>
          <div style="font-size:12px; font-weight:700; color:#fff;">الحدود والفواصل</div>
          <code style="font-size:11px; color:#94a3b8;">#E2E8F0</code>
        </div>
        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:8px; padding:10px;">
          <div style="height:30px; background:#64748b; border-radius:4px; margin-bottom:6px;"></div>
          <div style="font-size:12px; font-weight:700; color:#fff;">النصوص الثانوية</div>
          <code style="font-size:11px; color:#94a3b8;">#64748B</code>
        </div>
        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:8px; padding:10px;">
          <div style="height:30px; background:#1e293b; border-radius:4px; margin-bottom:6px;"></div>
          <div style="font-size:12px; font-weight:700; color:#fff;">فواصل الثيم الداكن</div>
          <code style="font-size:11px; color:#94a3b8;">#1E293B</code>
        </div>
      </div>

    </div>
  </div>

  <!-- Fullscreen Inspection Modal -->
  <div class="inspect-modal" id="inspect-modal" onclick="closeFocusModal()">
    <div class="modal-top-bar" onclick="event.stopPropagation()">
      <div class="modal-title-box">
        <span class="mono" style="color:var(--figma-blue); font-weight:800; font-size:16px;">#</span>
        <h2 id="modal-frame-title">اسم الشاشة</h2>
      </div>
      <div class="modal-actions">
        <a id="modal-download-link" href="#" download class="top-present-btn">تحميل الصورة بدقة Full HD ⬇️</a>
        <button class="top-tool-btn" onclick="closeFocusModal()">إغلاق ✕</button>
      </div>
    </div>
    <div class="modal-body" id="modal-body">
      <img id="modal-img" src="" alt="Full Preview" onclick="event.stopPropagation()">
    </div>
  </div>

  <!-- Figma Interactive Pan, Zoom & Navigation Script -->
  <script>
    let panX = 60;
    let panY = 70;
    let scale = 0.16;
    let isDragging = false;
    let startX = 0;
    let startY = 0;
    let activeFrameIdx = 0;

    const viewport = document.getElementById('viewport');
    const world = document.getElementById('canvas-world');
    const zoomText = document.getElementById('zoom-text');
    const sidebar = document.getElementById('sidebar');
    const toggleSidebar = document.getElementById('toggle-sidebar');
    const frames = document.querySelectorAll('.figma-frame');
    const sidebarItems = document.querySelectorAll('.sidebar-item');

    // Frames metadata
    const framesMeta = {str(list(map(lambda x: {"id": x["id"], "title": f"{x['num']} · {x['title']}", "src": x["src"]}, FRAMES_DATA)))};

    function applyTransform() {{
      scale = Math.min(Math.max(scale, 0.03), 2.2);
      world.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{scale}})`;
      zoomText.textContent = `${{Math.round(scale * 100)}}%`;
    }}

    function selectFrame(index, centerOnIt = true) {{
      activeFrameIdx = index;
      frames.forEach((f, i) => {{
        f.classList.toggle('selected', i === index);
      }});
      sidebarItems.forEach((item, i) => {{
        item.classList.toggle('active', i === index);
      }});

      if (centerOnIt) {{
        const targetFrame = frames[index];
        if (targetFrame) {{
          const worldRect = world.getBoundingClientRect();
          const frameRect = targetFrame.getBoundingClientRect();
          
          const frameWorldX = (frameRect.left - worldRect.left) / scale;
          const frameWorldY = (frameRect.top - worldRect.top) / scale;
          const frameW = frameRect.width / scale;
          const frameH = frameRect.height / scale;

          const viewW = window.innerWidth;
          const viewH = window.innerHeight;

          let targetScale = Math.min(
            (viewW - 140) / frameW,
            (viewH - 140) / frameH
          );
          targetScale = Math.min(Math.max(targetScale, 0.25), 0.75);

          const targetPanX = (viewW / 2) - ((frameWorldX + frameW / 2) * targetScale);
          const targetPanY = (viewH / 2) - ((frameWorldY + frameH / 2) * targetScale);

          animateCamera(targetPanX, targetPanY, targetScale);
        }}
      }}
    }}

    function animateCamera(targetX, targetY, targetScale, duration = 380) {{
      const startX = panX;
      const startY = panY;
      const startScale = scale;
      const startTime = performance.now();

      function step(now) {{
        const progress = Math.min((now - startTime) / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);

        panX = startX + (targetX - startX) * ease;
        panY = startY + (targetY - startY) * ease;
        scale = startScale + (targetScale - startScale) * ease;
        applyTransform();

        if (progress < 1) {{
          requestAnimationFrame(step);
        }}
      }}
      requestAnimationFrame(step);
    }}

    // Jump to section smoothly
    function jumpToSection(target) {{
      document.querySelectorAll('.switcher-tab').forEach(tab => {{
        tab.classList.toggle('active', tab.dataset.target === target);
      }});

      let elId = 'section-storefront';
      if (target === 'palette') elId = 'section-palette';
      else if (target === 'admin') elId = 'section-admin';
      else if (target === 'mobile') elId = 'section-mobile';

      const secEl = document.getElementById(elId);
      if (!secEl) return;

      const worldRect = world.getBoundingClientRect();
      const secRect = secEl.getBoundingClientRect();

      const secWorldX = (secRect.left - worldRect.left) / scale;
      const secWorldY = (secRect.top - worldRect.top) / scale;
      const secW = secRect.width / scale;
      const secH = secRect.height / scale;

      const viewW = window.innerWidth;
      const viewH = window.innerHeight;

      let targetScale = Math.min((viewW - 160) / secW, (viewH - 160) / secH);
      targetScale = Math.min(Math.max(targetScale, 0.08), 0.35);

      const targetPanX = (viewW / 2) - ((secWorldX + secW / 2) * targetScale);
      const targetPanY = (viewH / 2) - ((secWorldY + secH / 2) * targetScale);

      animateCamera(targetPanX, targetPanY, targetScale, 420);
    }}

    // Mouse drag
    viewport.addEventListener('mousedown', (e) => {{
      if (e.target.closest('.frame-hover-actions') || e.target.closest('.figma-toolbar') || e.target.closest('.figma-sidebar') || e.target.closest('.figma-top-bar')) return;
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
      viewport.classList.add('dragging');
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      applyTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isDragging = false;
      viewport.classList.remove('dragging');
    }});

    // Wheel zoom
    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const zoomFactor = e.ctrlKey ? 1.05 : 1.15;
      const delta = e.deltaY < 0 ? zoomFactor : 1 / zoomFactor;

      const mouseX = e.clientX;
      const mouseY = e.clientY;

      const newScale = Math.min(Math.max(scale * delta, 0.03), 2.2);

      panX = mouseX - (mouseX - panX) * (newScale / scale);
      panY = mouseY - (mouseY - panY) * (newScale / scale);
      scale = newScale;

      applyTransform();
    }}, {{ passive: false }});

    // Frame click
    frames.forEach((f, idx) => {{
      f.addEventListener('click', (e) => {{
        selectFrame(idx, true);
      }});
    }});

    // Sidebar item click
    sidebarItems.forEach((item, idx) => {{
      item.addEventListener('click', () => {{
        selectFrame(idx, true);
        if (window.innerWidth <= 768) {{
          sidebar.classList.add('collapsed');
        }}
      }});
    }});

    // Fit view
    function fitAll() {{
      const viewW = window.innerWidth;
      const viewH = window.innerHeight;
      const worldW = 14500;
      const worldH = 6500;

      let targetScale = Math.min((viewW - 120) / worldW, (viewH - 120) / worldH);
      targetScale = Math.min(Math.max(targetScale, 0.04), 0.16);

      animateCamera(40, 50, targetScale, 450);
    }}

    document.getElementById('tool-fit').addEventListener('click', fitAll);
    document.getElementById('btn-fit-screen').addEventListener('click', fitAll);

    document.getElementById('tool-reset').addEventListener('click', () => {{
      animateCamera(window.innerWidth / 4, 100, 1.0, 300);
    }});
    zoomText.addEventListener('click', () => {{
      animateCamera(window.innerWidth / 4, 100, 1.0, 300);
    }});

    document.getElementById('tool-zoom-in').addEventListener('click', () => {{
      const newScale = Math.min(scale * 1.3, 2.2);
      animateCamera(panX, panY, newScale, 200);
    }});
    document.getElementById('tool-zoom-out').addEventListener('click', () => {{
      const newScale = Math.max(scale / 1.3, 0.03);
      animateCamera(panX, panY, newScale, 200);
    }});

    // Toggle sidebar
    toggleSidebar.addEventListener('click', () => {{
      sidebar.classList.toggle('collapsed');
      toggleSidebar.classList.toggle('active', !sidebar.classList.contains('collapsed'));
    }});

    // Modal Focus
    function openFocusModal(idx) {{
      const item = framesMeta[idx];
      if (!item) return;
      document.getElementById('modal-frame-title').textContent = item.title;
      document.getElementById('modal-img').src = item.src;
      document.getElementById('modal-download-link').href = item.src;
      document.getElementById('inspect-modal').classList.add('active');
    }}

    function closeFocusModal() {{
      document.getElementById('inspect-modal').classList.remove('active');
    }}

    // Palette Modal
    function openPaletteModal() {{
      document.getElementById('palette-modal').classList.add('active');
    }}
    function closePaletteModal() {{
      document.getElementById('palette-modal').classList.remove('active');
    }}

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        closeFocusModal();
        closePaletteModal();
      }} else if (e.key === 'f' || e.key === 'F') {{
        if (!e.ctrlKey && !e.metaKey && document.activeElement.tagName !== 'INPUT') {{
          fitAll();
        }}
      }} else if (e.key === 'p' || e.key === 'P') {{
        if (!e.ctrlKey && !e.metaKey && document.activeElement.tagName !== 'INPUT') {{
          openFocusModal(activeFrameIdx);
        }}
      }} else if (e.key === 'ArrowRight') {{
        if (activeFrameIdx > 0) selectFrame(activeFrameIdx - 1, true);
      }} else if (e.key === 'ArrowLeft') {{
        if (activeFrameIdx < frames.length - 1) selectFrame(activeFrameIdx + 1, true);
      }}
    }});

    // Init
    applyTransform();
    selectFrame(0, false);
  </script>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    html_out = generate_index()
    
    root_file = os.path.join(ROOT_DIR, "index.html")
    with open(root_file, "w", encoding="utf-8") as f:
        f.write(html_out)
    print("Updated root index.html")

    designs_file = os.path.join(DESIGNS_DIR, "index.html")
    with open(designs_file, "w", encoding="utf-8") as f:
        f.write(html_out)
    print("Updated designs/index.html")
