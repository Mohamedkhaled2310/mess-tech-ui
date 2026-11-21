# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

DESIGNS_DIR = r"E:\mess\designs"
ROOT_DIR = r"E:\mess"
ASSETS_DIR = r"E:\mess\designs\assets"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# ==============================================================================
# 1. GENERATE DESKTOP HOMEPAGE (page_01_homepage.html)
# ==============================================================================
HOMEPAGE_HTML = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | المتجر التقني الأول لأجهزة الشبكات والاتصالات والإلكترونيات الأصلية</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      /* Extra Lightened Fresh Petrol Marine Palette (Never Black) */
      --petrol-950: #0a3658; /* Luminous deep marine petrol */
      --petrol-900: #0e4c77; /* Primary vibrant petrol */
      --petrol-850: #125c90; /* Marine blue */
      --petrol-800: #176ea9; /* Fresh petrol */
      --petrol-750: #1c80c2;
      --petrol-700: #2b92d4;
      --petrol-500: #0099e5; /* Signature electric cyan */
      --petrol-400: #38bdf8; /* Bright cyan highlight */
      --petrol-100: #e0f2fe;
      --petrol-50:  #f0f9ff;
      --cyan-500: #0099e5;
      --cyan-400: #38bdf8;
      --cyan-600: #0284c7;
      --emerald-500: #10b981;
      --amber-500: #f59e0b;
      --rose-500: #ef4444;
      --slate-100: #f1f5f9;
      --slate-200: #e2e8f0;
      --slate-400: #94a3b8;
      --slate-500: #64748b;
      --bg-page: #f6fafd;
      --text-main: #0c3352;
      --text-muted: #4e6b87;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Cairo', sans-serif; }
    body { background: var(--bg-page); color: var(--text-main); direction: rtl; text-align: right; }
    .mono { font-family: 'JetBrains Mono', monospace; direction: ltr; display: inline-block; }

    /* Top Notice Bar */
    .top-notice-bar {
      background: #082d49;
      color: #bae6fd;
      font-size: 13.5px;
      font-weight: 600;
      padding: 10px 48px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255,255,255,0.12);
    }
    .badge-notice-header {
      background: rgba(0, 153, 229, 0.25);
      color: #38bdf8;
      border: 1px solid rgba(0, 153, 229, 0.5);
      padding: 3px 12px;
      border-radius: 999px;
      font-weight: 800;
      font-size: 12.5px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* Main Navbar */
    .main-nav {
      background: linear-gradient(135deg, #0e5282 0%, #0a3d64 100%);
      padding: 18px 48px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 28px;
      border-bottom: 2px solid #08304f;
    }
    .brand-logo-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }
    .brand-logo-img {
      height: 50px;
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
      background: #093c62;
      border: 1.5px solid #1a6499;
      border-radius: 10px;
      padding: 4px 6px;
      transition: all 0.2s;
    }
    .search-input-box:focus-within {
      border-color: var(--cyan-400);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.3);
    }
    .search-category-dd {
      background: transparent;
      border: none;
      border-left: 1px solid #1a6499;
      color: #e0f2fe;
      font-size: 14px;
      font-weight: 700;
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
      font-size: 15px;
      outline: none;
    }
    .search-input-field::placeholder { color: #93c5fd; font-size: 14px; }
    .search-submit-btn {
      background: linear-gradient(135deg, var(--cyan-600) 0%, var(--cyan-500) 100%);
      color: #fff;
      border: none;
      border-radius: 8px;
      padding: 10px 24px;
      font-size: 14.5px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
    }
    .search-quick-tags {
      display: flex;
      gap: 8px;
      margin-top: 7px;
      font-size: 12.5px;
      color: #bae6fd;
    }
    .quick-tag {
      background: rgba(255,255,255,0.1);
      padding: 2px 10px;
      border-radius: 4px;
      color: #e0f2fe;
      text-decoration: none;
      font-weight: 600;
    }

    /* Actions */
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .nav-pill-btn {
      background: #093c62;
      border: 1.5px solid #1a6499;
      color: #fff;
      padding: 10px 16px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      position: relative;
    }
    .pill-counter {
      background: var(--cyan-500);
      color: #fff;
      font-size: 11.5px;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 999px;
    }
    .pill-counter.green { background: var(--emerald-500); }

    /* Subnav */
    .subnav-bar {
      background: #0c456f;
      padding: 0 48px;
      display: flex;
      align-items: center;
      border-bottom: 1.5px solid #08304f;
      white-space: nowrap;
    }
    .all-departments-pill {
      background: var(--cyan-600);
      color: #fff;
      padding: 12px 22px;
      font-size: 14.5px;
      font-weight: 800;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-left: 16px;
      cursor: pointer;
      border-radius: 6px;
    }
    .subnav-links {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      list-style: none;
    }
    .subnav-links a {
      color: #f0f9ff;
      padding: 14px 16px;
      font-size: 14px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border-bottom: 2.5px solid transparent;
      transition: all 0.2s;
    }
    .subnav-links a:hover, .subnav-links a.active {
      color: #38bdf8;
      border-bottom-color: #38bdf8;
    }

    /* ========================================================================
       HERO CAROUSEL BANNER (Full 16:9 / Panoramic Slider like PETA)
       ======================================================================== */
    .hero-carousel-wrap {
      max-width: 1380px;
      margin: 24px auto 0;
      padding: 0 24px;
      position: relative;
    }
    .carousel-slider-box {
      position: relative;
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 12px 35px rgba(14, 82, 130, 0.16);
      border: 1.5px solid #bfdbfe;
      background: #fff;
      height: 380px;
    }
    .carousel-banner-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
      display: block;
    }
    .carousel-overlay-cta {
      position: absolute;
      bottom: 24px;
      right: 32px;
      background: rgba(10, 54, 88, 0.88);
      backdrop-filter: blur(8px);
      border: 1.5px solid rgba(255, 255, 255, 0.2);
      padding: 12px 24px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      gap: 16px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.25);
    }
    .carousel-overlay-text {
      color: #fff;
      font-size: 14.5px;
      font-weight: 800;
    }
    .carousel-overlay-btn {
      background: linear-gradient(135deg, var(--cyan-600) 0%, var(--cyan-500) 100%);
      color: #fff;
      padding: 8px 20px;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 800;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .carousel-arrow {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 46px;
      height: 46px;
      background: rgba(255, 255, 255, 0.92);
      border: 1px solid #bfdbfe;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: var(--petrol-950);
      box-shadow: 0 4px 14px rgba(0,0,0,0.15);
      z-index: 10;
      font-size: 20px;
      font-weight: 800;
    }
    .carousel-arrow.prev { right: 20px; }
    .carousel-arrow.next { left: 20px; }
    .carousel-dots {
      position: absolute;
      bottom: 16px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      gap: 8px;
      z-index: 10;
    }
    .carousel-dot {
      width: 10px;
      height: 10px;
      border-radius: 999px;
      background: rgba(14, 82, 130, 0.35);
      cursor: pointer;
      transition: all 0.3s;
    }
    .carousel-dot.active {
      width: 30px;
      background: var(--cyan-600);
    }

    /* ========================================================================
       TRUST STRIP
       ======================================================================== */
    .trust-strip-wrap {
      max-width: 1380px;
      margin: 22px auto 0;
      padding: 0 24px;
    }
    .trust-strip-grid {
      background: #fff;
      border: 1.5px solid #bfdbfe;
      border-radius: 14px;
      padding: 16px 28px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      box-shadow: 0 4px 15px rgba(14, 82, 130, 0.05);
    }
    .trust-strip-item {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .trust-strip-icon {
      width: 48px;
      height: 48px;
      background: #eff6ff;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      flex-shrink: 0;
      border: 1px solid #dbeafe;
    }
    .trust-strip-title {
      font-size: 14.5px;
      font-weight: 800;
      color: var(--petrol-950);
      margin-bottom: 2px;
    }
    .trust-strip-desc {
      font-size: 12.5px;
      color: var(--slate-500);
      font-weight: 600;
    }

    /* ========================================================================
       SECTIONS & CATEGORY BANNERS (Like PETA Store)
       ======================================================================== */
    .section-wrap {
      max-width: 1380px;
      margin: 36px auto 0;
      padding: 0 24px;
    }
    .section-header-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 20px;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 12px;
    }
    .section-title-main {
      font-size: 25px;
      font-weight: 900;
      color: var(--petrol-950);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .section-view-more {
      font-size: 14.5px;
      font-weight: 800;
      color: var(--cyan-600);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .cat-banners-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 22px;
      margin-bottom: 24px;
    }
    .cat-banner-card {
      background: #fff;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 6px 20px rgba(14, 82, 130, 0.12);
      position: relative;
      display: block;
      text-decoration: none;
      transition: transform 0.2s, box-shadow 0.2s;
      border: 1.5px solid #bfdbfe;
    }
    .cat-banner-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(14, 82, 130, 0.2);
    }
    .cat-banner-img {
      width: 100%;
      height: 160px;
      object-fit: cover;
      display: block;
    }

    /* ========================================================================
       PRODUCT SHOWCASE GRID (Refined comfortable fonts)
       ======================================================================== */
    .products-showcase-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-bottom: 36px;
    }
    .product-box {
      background: #fff;
      border: 1.5px solid #e2e8f0;
      border-radius: 14px;
      padding: 18px;
      position: relative;
      display: flex;
      flex-direction: column;
      transition: all 0.2s;
    }
    .product-box:hover {
      border-color: var(--cyan-500);
      box-shadow: 0 8px 24px rgba(0, 153, 229, 0.12);
    }
    .product-badge-discount {
      position: absolute;
      top: 14px;
      right: 14px;
      background: #ef4444;
      color: #fff;
      font-size: 12px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      z-index: 2;
    }
    .product-badge-hot {
      position: absolute;
      top: 14px;
      left: 14px;
      background: #f59e0b;
      color: #fff;
      font-size: 11.5px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      z-index: 2;
    }
    .product-img-wrap {
      height: 165px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 10px;
      margin-bottom: 12px;
      background: #f8fafc;
      border-radius: 10px;
    }
    .product-img-wrap img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }
    .product-brand-tag {
      font-size: 12.5px;
      font-weight: 800;
      color: var(--cyan-600);
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .product-name-title {
      font-size: 15px;
      font-weight: 800;
      color: var(--petrol-950);
      line-height: 1.5;
      margin-bottom: 8px;
      flex: 1;
    }
    .product-specs-list {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }
    .spec-pill {
      background: #f1f5f9;
      color: #475569;
      font-size: 11.5px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }
    .product-price-action-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 12px;
      border-top: 1px solid #f1f5f9;
      margin-top: auto;
    }
    .price-value-now {
      font-size: 21px;
      font-weight: 900;
      color: var(--cyan-600);
    }
    .price-value-now small {
      font-size: 13.5px;
      color: #64748b;
      font-weight: 700;
    }
    .price-value-before {
      font-size: 13px;
      color: #94a3b8;
      text-decoration: line-through;
    }
    .btn-add-cart {
      background: linear-gradient(135deg, var(--cyan-600) 0%, var(--cyan-500) 100%);
      color: #fff;
      border: none;
      padding: 9px 18px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Flash Deals Section */
    .flash-deals-box {
      background: linear-gradient(135deg, #0e5282 0%, #0a3d64 100%);
      border-radius: 18px;
      padding: 26px 32px;
      color: #fff;
      margin-bottom: 36px;
      box-shadow: 0 10px 30px rgba(14, 82, 130, 0.16);
    }
    .deals-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 22px;
    }
    .deals-timer-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .timer-unit {
      background: #093455;
      border: 1px solid #1c5e90;
      padding: 6px 14px;
      border-radius: 8px;
      text-align: center;
    }
    .timer-val { font-size: 18px; font-weight: 900; color: #38bdf8; display: block; }
    .timer-lbl { font-size: 11px; color: #bae6fd; font-weight: 700; }

    /* Certified Brands Ribbon */
    .brands-ribbon {
      background: #fff;
      border-top: 1.5px solid #bfdbfe;
      border-bottom: 1.5px solid #bfdbfe;
      padding: 24px 48px;
      margin-top: 40px;
    }
    .brands-container {
      max-width: 1380px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      flex-wrap: wrap;
    }
    .brand-name {
      font-size: 19px;
      font-weight: 900;
      color: #475569;
      letter-spacing: 0.5px;
    }

    /* Footer */
    .footer-wrap {
      background: linear-gradient(180deg, #0a3658 0%, #07253d 100%);
      color: #cbd5e1;
      padding: 56px 48px 24px;
      border-top: 3.5px solid var(--cyan-500);
      margin-top: 50px;
    }
    .footer-container {
      max-width: 1380px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr 1.2fr;
      gap: 40px;
      margin-bottom: 40px;
    }
    .footer-col h5 {
      color: #fff;
      font-size: 16.5px;
      font-weight: 800;
      margin-bottom: 18px;
      position: relative;
      padding-bottom: 8px;
    }
    .footer-col h5::after {
      content: '';
      position: absolute;
      bottom: 0;
      right: 0;
      width: 32px;
      height: 2px;
      background: var(--cyan-400);
    }
    .footer-list { list-style: none; }
    .footer-list li { margin-bottom: 10px; }
    .footer-list a {
      color: #94a3b8;
      text-decoration: none;
      font-size: 14px;
      transition: color 0.2s;
    }
    .footer-list a:hover { color: #38bdf8; }
    .footer-bottom-bar {
      max-width: 1380px;
      margin: 0 auto;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13.5px;
      color: #94a3b8;
    }
  </style>
</head>
<body>

  <!-- Top Notice Bar -->
  <div class="top-notice-bar">
    <div style="display:flex; align-items:center; gap:16px;">
      <span class="badge-notice-header">معاينة وفحص قبل الدفع</span>
      <span>جميع الأجهزة التقنية أصلية 100% بالضمان مع إمكانية الفحص الكامل عند الاستلام (COD)</span>
    </div>
    <div style="display:flex; align-items:center; gap:18px;">
      <span>خدمة العملاء والدعم المباشر: <b class="mono" style="color:#fff;">19824</b></span>
      <span style="color:#64748b;">|</span>
      <a href="11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png" style="color:#fff; text-decoration:none; font-weight:700;">حسابي / طلباتي</a>
    </div>
  </div>

  <!-- Main Header -->
  <header class="main-nav">
    <a href="01_الصفحة_الرئيسية_Desktop_Homepage.png" class="brand-logo-wrap">
      <img src="assets/logo_white.png" class="brand-logo-img" alt="MESS TECH Logo">
    </a>

    <!-- Instant Search -->
    <div class="search-wrapper">
      <div class="search-input-box">
        <select class="search-category-dd">
          <option>جميع الأقسام</option>
          <option>سويتشات الشبكات</option>
          <option>حلول الواي فاي</option>
          <option>وحدات التخزين NAS</option>
          <option>مغذيات الطاقة UPS</option>
          <option>كبائن وراكات</option>
        </select>
        <input type="text" class="search-input-field" placeholder="ابحث باسم الجهاز، الموديل (WS-C2960X، U6-Pro) أو كود SKU...">
        <button class="search-submit-btn">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          بحث فوري
        </button>
      </div>
      <div class="search-quick-tags">
        <span>الأكثر طلباً:</span>
        <a href="#" class="quick-tag">سويتش سيسكو 24 بورت</a>
        <a href="#" class="quick-tag">أكسس بوينت Wi-Fi 6</a>
        <a href="#" class="quick-tag">سيرفر تخزين Synology</a>
        <a href="#" class="quick-tag">مغذي طاقة UPS 1000VA</a>
      </div>
    </div>

    <!-- Actions -->
    <div class="nav-actions">
      <!-- Wishlist -->
      <a href="#" class="nav-pill-btn" title="قائمة المفضلة">
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#f43f5e" stroke-width="2.2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
        <span>المفضلة</span>
        <span class="pill-counter" style="background:#f43f5e;">4</span>
      </a>

      <!-- Compare -->
      <a href="04_صفحة_مقارنة_المواصفات_Desktop_Product_Comparison.png" class="nav-pill-btn" title="مقارنة المنتجات">
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
        <span>المقارنة</span>
        <span class="pill-counter">2</span>
      </a>

      <!-- Cart -->
      <a href="05_صفحة_السلة_واتمام_الطلب_Desktop_Cart_Checkout_COD.png" class="nav-pill-btn" title="سلة المشتريات">
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
        <span>السلة</span>
        <span class="pill-counter green">2</span>
      </a>

      <!-- Profile -->
      <a href="11_لوحة_حسابي_ودفتر_العناوين_Desktop_Customer_Profile.png" class="nav-pill-btn" style="background:#0c416a; border-color:var(--cyan-400);" title="حسابي">
        <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
        <span>حسابي</span>
      </a>
    </div>
  </header>

  <!-- Subnav -->
  <nav class="subnav-bar">
    <div class="all-departments-pill">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      <span>جميع أقسام المتجر</span>
    </div>
    <ul class="subnav-links">
      <li><a href="#" class="active">سويتشات الشبكات</a></li>
      <li><a href="#">راوترات وسيرفرات</a></li>
      <li><a href="#">كاميرات ومراقبة IP</a></li>
      <li><a href="#">أكسس بوينت Wi-Fi 6 & 7</a></li>
      <li><a href="#">مغذيات الطاقة UPS</a></li>
      <li><a href="#">راكات وكبائن السيرفرات</a></li>
      <li><a href="#">كابلات وإكسسوارات الشبكة</a></li>
      <li><a href="#" style="color:#38bdf8; font-weight:800;">🔥 العروض والتخفيضات</a></li>
    </ul>
  </nav>

  <!-- ========================================================================
       HERO CAROUSEL SLIDER (Panoramic 16:9 Banner)
       ======================================================================== -->
  <section class="hero-carousel-wrap">
    <div class="carousel-slider-box">
      <img src="assets/banner_huawei_ekit.jpg" alt="Huawei eKit Smart Networking Solutions" class="carousel-banner-img">

      <!-- Overlay CTA for Quick Shopping -->
      <div class="carousel-overlay-cta">
        <span class="carousel-overlay-text">⚡ عروض حصرية على أجهزة الشبكات وسويتشات Gigabit & PoE</span>
        <a href="#switches-showcase" class="carousel-overlay-btn">
          تسوق الآن
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
        </a>
      </div>

      <!-- Controls -->
      <div class="carousel-arrow prev">›</div>
      <div class="carousel-arrow next">‹</div>
      <div class="carousel-dots">
        <span class="carousel-dot active"></span>
        <span class="carousel-dot"></span>
        <span class="carousel-dot"></span>
        <span class="carousel-dot"></span>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       TRUST STRIP
       ======================================================================== -->
  <section class="trust-strip-wrap">
    <div class="trust-strip-grid">
      <div class="trust-strip-item">
        <div class="trust-strip-icon">💵</div>
        <div>
          <div class="trust-strip-title">الدفع عند الاستلام (COD)</div>
          <div class="trust-strip-desc">معاينة وفحص المنتج قبل السداد</div>
        </div>
      </div>
      <div class="trust-strip-item">
        <div class="trust-strip-icon">🚚</div>
        <div>
          <div class="trust-strip-title">شحن سريع ومؤمّن</div>
          <div class="trust-strip-desc">توصيل لكافة المحافظات خلال 24-48 ساعة</div>
        </div>
      </div>
      <div class="trust-strip-item">
        <div class="trust-strip-icon">🔄</div>
        <div>
          <div class="trust-strip-title">استبدال واسترجاع 14 يوماً</div>
          <div class="trust-strip-desc">سياسة إرجاع مرنة ومجانية للمستهلك</div>
        </div>
      </div>
      <div class="trust-strip-item">
        <div class="trust-strip-icon">🛡️</div>
        <div>
          <div class="trust-strip-title">أجهزة أصلية 100% معتمدة</div>
          <div class="trust-strip-desc">بالكرتونة الأصلية مع ضمان التوريد</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       SECTION 1: CATEGORY FEATURE BANNERS (Switches, WiFi, Storage)
       ======================================================================== -->
  <section class="section-wrap" id="switches-showcase">
    <div class="section-header-row">
      <div class="section-title-main">
        <span>📁</span>
        <span>الأقسام الرئيسية الأكثر طلباً</span>
      </div>
      <a href="#" class="section-view-more">عرض كل الأقسام ←</a>
    </div>

    <!-- 3 Category Banner Cards (PETA Layout) -->
    <div class="cat-banners-grid-3">
      <a href="#" class="cat-banner-card">
        <img src="assets/cat_banner_switches.jpg" alt="Switches" class="cat-banner-img">
      </a>
      <a href="#" class="cat-banner-card">
        <img src="assets/cat_banner_wifi.jpg" alt="WIFI Solutions" class="cat-banner-img">
      </a>
      <a href="#" class="cat-banner-card">
        <img src="assets/cat_banner_storage.jpg" alt="Storage" class="cat-banner-img">
      </a>
    </div>

    <!-- Product Showcase Under Category: Switches -->
    <div class="section-header-row" style="margin-top:10px;">
      <div class="section-title-main" style="font-size:20px;">
        <span style="color:var(--cyan-600);">🔌</span>
        <span>سويتشات الشبكات وموزعات البيانات (Gigabit & PoE+)</span>
      </div>
      <a href="#" class="section-view-more">تسوق المزيد من السويتشات (24 موديل) ←</a>
    </div>

    <div class="products-showcase-grid">
      <!-- Product 1 -->
      <div class="product-box">
        <span class="product-badge-discount">-17%</span>
        <span class="product-badge-hot">HOT</span>
        <div class="product-img-wrap">
          <img src="assets/prod_cisco_sw.jpg" alt="Cisco Catalyst 2960X">
        </div>
        <div class="product-brand-tag">Cisco Systems</div>
        <div class="product-name-title">سويتش سيسكو كاتاليست 2960X بورت جيجابت + 2 منفذ 10G SFP</div>
        <div class="product-specs-list">
          <span class="spec-pill">24 Ports GbE</span>
          <span class="spec-pill">PoE+ 370W</span>
          <span class="spec-pill">10G Uplink</span>
        </div>
        <div class="product-price-action-row">
          <div>
            <div class="price-value-now">18,480 <small>ج.م</small></div>
            <div class="price-value-before">22,170 ج.م</div>
          </div>
          <button class="btn-add-cart">أضف للسلة</button>
        </div>
      </div>

      <!-- Product 2 -->
      <div class="product-box">
        <span class="product-badge-discount">-17%</span>
        <div class="product-img-wrap">
          <img src="assets/prod_poe_sw.jpg" alt="MikroTik CRS328">
        </div>
        <div class="product-brand-tag">MikroTik RouterOS</div>
        <div class="product-name-title">راوتر وسويتش مايكروتك CRS328 ذكي 24 بورت PoE مع 4 منافذ SFP+</div>
        <div class="product-specs-list">
          <span class="spec-pill">24 PoE Out</span>
          <span class="spec-pill">4x 10G SFP+</span>
          <span class="spec-pill">Dual Boot</span>
        </div>
        <div class="product-price-action-row">
          <div>
            <div class="price-value-now">12,346 <small>ج.م</small></div>
            <div class="price-value-before">14,815 ج.م</div>
          </div>
          <button class="btn-add-cart">أضف للسلة</button>
        </div>
      </div>

      <!-- Product 3 -->
      <div class="product-box">
        <div class="product-img-wrap">
          <img src="assets/prod_cisco_sw.jpg" alt="Cisco Catalyst 48 Port">
        </div>
        <div class="product-brand-tag">Cisco Systems</div>
        <div class="product-name-title">سويتش سيسكو إنتربرايز 48 بورت جيجابت مع تغذية PoE كاملة</div>
        <div class="product-specs-list">
          <span class="spec-pill">48 Ports PoE</span>
          <span class="spec-pill">740W Power</span>
          <span class="spec-pill">Stackable</span>
        </div>
        <div class="product-price-action-row">
          <div>
            <div class="price-value-now">27,940 <small>ج.م</small></div>
            <div class="price-value-before">33,520 ج.م</div>
          </div>
          <button class="btn-add-cart">أضف للسلة</button>
        </div>
      </div>

      <!-- Product 4 -->
      <div class="product-box">
        <span class="product-badge-discount">-20%</span>
        <div class="product-img-wrap">
          <img src="assets/prod_poe_sw.jpg" alt="Ruijie Reyee Switch">
        </div>
        <div class="product-brand-tag">Ruijie Reyee</div>
        <div class="product-name-title">سويتش رويجي سحابي 16 بورت جيجابت مع إدارة كاملة عبر الموبايل</div>
        <div class="product-specs-list">
          <span class="spec-pill">16 GbE</span>
          <span class="spec-pill">Cloud App</span>
          <span class="spec-pill">Surge 6KV</span>
        </div>
        <div class="product-price-action-row">
          <div>
            <div class="price-value-now">6,750 <small>ج.م</small></div>
            <div class="price-value-before">8,450 ج.م</div>
          </div>
          <button class="btn-add-cart">أضف للسلة</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       SECTION 2: SECONDARY CATEGORY BANNERS (UPS, Attendance, Interactive)
       ======================================================================== -->
  <section class="section-wrap">
    <!-- 3 Category Banner Cards -->
    <div class="cat-banners-grid-3">
      <a href="#" class="cat-banner-card">
        <img src="assets/cat_banner_ups.jpg" alt="UPS Power" class="cat-banner-img">
      </a>
      <a href="#" class="cat-banner-card">
        <img src="assets/cat_banner_attendance.jpg" alt="Attendance" class="cat-banner-img">
      </a>
      <a href="#" class="cat-banner-card">
        <img src="assets/cat_banner_screen.jpg" alt="Interactive Screens" class="cat-banner-img">
      </a>
    </div>

    <!-- Product Showcase Under Category: WiFi & Storage -->
    <div class="section-header-row" style="margin-top:10px;">
      <div class="section-title-main" style="font-size:20px;">
        <span style="color:var(--cyan-600);">📡</span>
        <span>أجهزة الواي فاي وسيرفرات التخزين السحابية (Wi-Fi 6 & NAS)</span>
      </div>
      <a href="#" class="section-view-more">تسوق المزيد من حلول الواي فاي والتخزين ←</a>
    </div>

    <div class="products-showcase-grid">
      <!-- Product 5 -->
      <div class="product-box">
        <span class="product-badge-discount">-17%</span>
        <span class="product-badge-hot">HOT</span>
        <div class="product-img-wrap">
          <img src="assets/prod_wifi_ap1.jpg" alt="Grandstream GWN7664">
        </div>
        <div class="product-brand-tag">Grandstream</div>
        <div class="product-name-title">أكسس بوينت جراند ستريم GWN7664 Wi-Fi 6 سقفية فائقة التغطية</div>
        <div class="product-specs-list">
          <span class="spec-pill">Wi-Fi 6 AX3500</span>
          <span class="spec-pill">512 Clients</span>
          <span class="spec-pill">PoE+</span>
        </div>
        <div class="product-price-action-row">
          <div>
            <div class="price-value-now">4,289 <small>ج.م</small></div>
            <div class="price-value-before">5,147 ج.م</div>
          </div>
          <button class="btn-add-cart">أضف للسلة</button>
        </div>
      </div>

      <!-- Product 6 -->
      <div class="product-box">
        <span class="product-badge-discount">-12%</span>
        <div class="product-img-wrap">
          <img src="assets/prod_wifi_ap2.jpg" alt="Ubiquiti U6-Pro">
        </div>
        <div class="product-brand-tag">Ubiquiti UniFi</div>
        <div class="product-name-title">أكسس بوينت يوبيكويتي UniFi U6-Pro بسرعات جيجابت مضاعفة</div>
        <div class="product-specs-list">
          <span class="spec-pill">5.3 Gbps</span>
          <span class="spec-pill">300+ Clients</span>
          <span class="spec-pill">IP54</span>
        </div>
        <div class="product-price-action-row">
          <div>
            <div class="price-value-now">5,890 <small>ج.م</small></div>
            <div class="price-value-before">6,700 ج.م</div>
          </div>
          <button class="btn-add-cart">أضف للسلة</button>
        </div>
      </div>

      <!-- Product 7 -->
      <div class="product-box">
        <div class="product-img-wrap">
          <img src="assets/prod_nas_5bay.jpg" alt="Synology DS620slim">
        </div>
        <div class="product-brand-tag">Synology NAS</div>
        <div class="product-name-title">سيرفر تخزين سحابي سينولوجي DiskStation 6-Bay صغير الحجم</div>
        <div class="product-specs-list">
          <span class="spec-pill">6-Bay SSD/HDD</span>
          <span class="spec-pill">RAID Support</span>
          <span class="spec-pill">Private Cloud</span>
        </div>
        <div class="product-price-action-row">
          <div>
            <div class="price-value-now">8,599 <small>ج.م</small></div>
            <div class="price-value-before">9,200 ج.م</div>
          </div>
          <button class="btn-add-cart">أضف للسلة</button>
        </div>
      </div>

      <!-- Product 8 -->
      <div class="product-box">
        <span class="product-badge-discount">-15%</span>
        <div class="product-img-wrap">
          <img src="assets/prod_nas_6bay.jpg" alt="Synology DS923+">
        </div>
        <div class="product-brand-tag">Synology NAS</div>
        <div class="product-name-title">سيرفر تخزين سينولوجي DS923+ عالي الأداء للمكاتب والنسخ الاحتياطي</div>
        <div class="product-specs-list">
          <span class="spec-pill">4-Bay Hot Swap</span>
          <span class="spec-pill">NVMe Cache</span>
          <span class="spec-pill">10GbE Ready</span>
        </div>
        <div class="product-price-action-row">
          <div>
            <div class="price-value-now">21,505 <small>ج.م</small></div>
            <div class="price-value-before">25,000 ج.م</div>
          </div>
          <button class="btn-add-cart">أضف للسلة</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       FLASH DEALS / العروض الحالية
       ======================================================================== -->
  <section class="section-wrap">
    <div class="flash-deals-box">
      <div class="deals-header">
        <div>
          <div style="display:flex; align-items:center; gap:8px; font-size:25px; font-weight:900;">
            <span style="color:#f59e0b;">⚡</span>
            <span>العروض الحالية والتخفيضات الأسبوعية</span>
          </div>
          <p style="font-size:14.5px; color:#bae6fd; margin-top:4px;">
            أسعار خاصة محدودة الكمية على أجهزة الشبكات ومغذيات الطاقة مع توصيل سريع لجميع المحافظات
          </p>
        </div>
        <div class="deals-timer-wrap">
          <span style="font-size:14px; font-weight:700; color:#bae6fd;">ينتهي العرض خلال:</span>
          <div class="timer-unit">
            <span class="timer-val mono">02</span>
            <span class="timer-lbl">يوم</span>
          </div>
          <div class="timer-unit">
            <span class="timer-val mono">14</span>
            <span class="timer-lbl">ساعة</span>
          </div>
          <div class="timer-unit">
            <span class="timer-val mono">38</span>
            <span class="timer-lbl">دقيقة</span>
          </div>
          <div class="timer-unit">
            <span class="timer-val mono">50</span>
            <span class="timer-lbl">ثانية</span>
          </div>
        </div>
      </div>

      <!-- 3 Featured Deals in Flash Deals -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:20px;">
        <!-- Deal 1: UPS -->
        <div style="background:#fff; color:var(--text-main); border-radius:14px; padding:18px; display:flex; gap:16px; align-items:center;">
          <div style="width:110px; height:110px; background:#f8fafc; border-radius:10px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
            <img src="assets/prod_ups_tower.jpg" style="max-width:90%; max-height:90%; object-fit:contain;" alt="APC UPS">
          </div>
          <div>
            <span style="background:#ef4444; color:#fff; font-size:11.5px; font-weight:800; padding:2px 7px; border-radius:4px;">خصم 20%</span>
            <div style="font-size:15px; font-weight:800; color:var(--petrol-950); margin:6px 0 4px; line-height:1.4;">مغذي طاقة ذكي APC Easy UPS 1000VA لحماية السيرفرات</div>
            <div style="font-size:19px; font-weight:900; color:var(--cyan-600);">7,450 <small style="font-size:12px; color:#64748b;">ج.م</small> <span style="font-size:12.5px; color:#94a3b8; text-decoration:line-through;">9,300 ج.م</span></div>
          </div>
        </div>

        <!-- Deal 2: Powerstation -->
        <div style="background:#fff; color:var(--text-main); border-radius:14px; padding:18px; display:flex; gap:16px; align-items:center;">
          <div style="width:110px; height:110px; background:#f8fafc; border-radius:10px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
            <img src="assets/prod_ups_powerstation.jpg" style="max-width:90%; max-height:90%; object-fit:contain;" alt="Portable Powerstation">
          </div>
          <div>
            <span style="background:#f59e0b; color:#fff; font-size:11.5px; font-weight:800; padding:2px 7px; border-radius:4px;">الأكثر طلباً</span>
            <div style="font-size:15px; font-weight:800; color:var(--petrol-950); margin:6px 0 4px; line-height:1.4;">محطة طاقة محمولة Powerstation 600W للراوترات والعمل الميداني</div>
            <div style="font-size:19px; font-weight:900; color:var(--cyan-600);">13,800 <small style="font-size:12px; color:#64748b;">ج.م</small> <span style="font-size:12.5px; color:#94a3b8; text-decoration:line-through;">16,200 ج.م</span></div>
          </div>
        </div>

        <!-- Deal 3: Interactive Screen -->
        <div style="background:#fff; color:var(--text-main); border-radius:14px; padding:18px; display:flex; gap:16px; align-items:center;">
          <div style="width:110px; height:110px; background:#f8fafc; border-radius:10px; display:flex; align-items:center; justify-content:center; flex-shrink:0;">
            <img src="assets/prod_interactive_screen.jpg" style="max-width:90%; max-height:90%; object-fit:contain;" alt="Interactive Screen">
          </div>
          <div>
            <span style="background:#10b981; color:#fff; font-size:11.5px; font-weight:800; padding:2px 7px; border-radius:4px;">معاينة عند الاستلام</span>
            <div style="font-size:15px; font-weight:800; color:var(--petrol-950); margin:6px 0 4px; line-height:1.4;">شاشة اجتماعات تفاعلية 65 بوصة 4K تعمل باللمس بنظامين</div>
            <div style="font-size:19px; font-weight:900; color:var(--cyan-600);">34,900 <small style="font-size:12px; color:#64748b;">ج.م</small> <span style="font-size:12.5px; color:#94a3b8; text-decoration:line-through;">39,500 ج.م</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================================
       CERTIFIED BRANDS RIBBON
       ======================================================================== -->
  <section class="brands-ribbon">
    <div class="brands-container">
      <div style="font-size:15.5px; font-weight:800; color:var(--petrol-900);">الماركات الأصلية المعتمدة:</div>
      <div class="brand-name" style="color:#0284c7;">CISCO</div>
      <div class="brand-name" style="color:#ef4444;">HUAWEI</div>
      <div class="brand-name" style="color:#0f172a;">MIKROTIK</div>
      <div class="brand-name" style="color:#0099e5;">UBIQUITI</div>
      <div class="brand-name" style="color:#f97316;">GRANDSTREAM</div>
      <div class="brand-name" style="color:#10b981;">SYNOLOGY</div>
      <div class="brand-name" style="color:#334155;">SCHNEIDER APC</div>
      <div class="brand-name" style="color:#2563eb;">FORTINET</div>
    </div>
  </section>

  <!-- ========================================================================
       FOOTER
       ======================================================================== -->
  <footer class="footer-wrap">
    <div class="footer-container">
      <div class="footer-col">
        <img src="assets/logo_white.png" style="height:44px; margin-bottom:16px;" alt="MESS TECH">
        <p style="font-size:14px; line-height:1.8; color:#cbd5e1; margin-bottom:16px;">
          متجر <b>MESS TECH</b> وجهتكم الأولى لأحدث الأجهزة التقنية، مستلزمات الشبكات، أنظمة المراقبة والإلكترونيات الأصلية المعتمدة بأفضل الأسعار، مع ميزة الفحص والمعاينة قبل الدفع عند الاستلام.
        </p>
        <div style="display:flex; align-items:center; gap:12px;">
          <span class="badge-notice-header" style="font-size:12.5px;">منتجات أصلية معتمدة 100%</span>
          <span style="color:#fff; font-size:13.5px;">الدعم: <b>support@messtech.com</b></span>
        </div>
      </div>

      <div class="footer-col">
        <h5>أقسام المتجر</h5>
        <ul class="footer-list">
          <li><a href="#">سويتشات الشبكات Gigabit & PoE</a></li>
          <li><a href="#">أجهزة الراوتر والواي فاي Wi-Fi 6</a></li>
          <li><a href="#">كاميرات المراقبة وأجهزة التسجيل</a></li>
          <li><a href="#">وحدات التخزين السحابية NAS</a></li>
          <li><a href="#">مغذيات الطاقة الذكية UPS</a></li>
          <li><a href="#">كبائن وراكات السيرفرات وملحقاتها</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h5>خدمات المشترين</h5>
        <ul class="footer-list">
          <li><a href="#">الشحن والتوصيل لكافة المحافظات</a></li>
          <li><a href="#">سياسة الإرجاع والاستبدال (14 يوماً)</a></li>
          <li><a href="#">خدمة الدفع نقداً عند الاستلام (COD)</a></li>
          <li><a href="#">الأسئلة الشائعة ومساعدة العملاء</a></li>
          <li><a href="#">الشروط والأحكام والضمان التجاري</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h5>خدمة العملاء والدعم الفني</h5>
        <p style="font-size:13.5px; color:#cbd5e1; margin-bottom:12px;">
          فريق خدمة العملاء جاهز للرد على استفساراتكم ومساعدتكم طوال أيام الأسبوع:
        </p>
        <div style="background:#093455; border:1px solid #1c5e90; padding:14px; border-radius:10px; margin-bottom:12px;">
          <div style="font-size:12px; color:#94a3b8;">الخط الساخن المباشر:</div>
          <div class="mono" style="font-size:19px; font-weight:800; color:#38bdf8; margin-top:2px;">19824 • 0100 234 5678</div>
        </div>
        <div style="font-size:12.5px; color:#94a3b8; display:flex; align-items:center; gap:6px;">
          <span style="color:#10b981;">●</span> متاح يومياً من 9 صباحاً حتى 10 مساءً
        </div>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div>جميع الحقوق محفوظة © 2026 لمتجر <b>MESS TECH</b> — للتجارة الإلكترونية والتقنية.</div>
      <div style="display:flex; gap:20px; align-items:center;">
        <span style="color:#38bdf8;">✓ منتجات أصلية 100%</span>
        <span>✓ استرجاع واستبدال مجاني 14 يوماً</span>
        <span>✓ فحص ومعاينة قبل الدفع</span>
      </div>
    </div>
  </footer>

</body>
</html>
"""

p01_html_path = os.path.join(DESIGNS_DIR, "page_01_homepage.html")
with open(p01_html_path, "w", encoding="utf-8") as f:
    f.write(HOMEPAGE_HTML)
print("Updated page_01_homepage.html")

# Render Desktop Homepage
p01_png_path = os.path.join(DESIGNS_DIR, "01_الصفحة_الرئيسية_Desktop_Homepage.png")
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,2480",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=3000",
    f"--screenshot={p01_png_path}",
    f"file:///{os.path.abspath(p01_html_path).replace(chr(92), '/')}"
]
subprocess.run(cmd, check=True)
root_p01_png = os.path.join(ROOT_DIR, "01_الصفحة_الرئيسية_Desktop_Homepage.png")
shutil.copy2(p01_png_path, root_p01_png)
print("Rendered and copied 01_الصفحة_الرئيسية_Desktop_Homepage.png")

# ==============================================================================
# 2. UPDATE DESIGN SYSTEM PALETTE (page_00_design_system_palette.html)
# ==============================================================================
p00_path = os.path.join(DESIGNS_DIR, "page_00_design_system_palette.html")
if os.path.exists(p00_path):
    with open(p00_path, "r", encoding="utf-8") as f:
        p00_content = f.read()

    # Update swatches to reflect new lightened petrol
    p00_content = p00_content.replace("#070d18", "#0a3658")
    p00_content = p00_content.replace("#0b1120", "#0e4c77")
    p00_content = p00_content.replace("#0f172a", "#125c90")
    p00_content = p00_content.replace("#172136", "#176ea9")
    p00_content = p00_content.replace("Dark Navy 950", "Deep Marine Petrol")
    p00_content = p00_content.replace("Dark Navy 900", "Primary Vibrant Petrol")
    p00_content = p00_content.replace("Navy 850", "Luminous Petrol Blue")

    with open(p00_path, "w", encoding="utf-8") as f:
        f.write(p00_content)

    p00_png = os.path.join(DESIGNS_DIR, "00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png")
    cmd_00 = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1440,1650",
        "--force-device-scale-factor=1.5",
        "--virtual-time-budget=2500",
        f"--screenshot={p00_png}",
        f"file:///{os.path.abspath(p00_path).replace(chr(92), '/')}"
    ]
    subprocess.run(cmd_00, check=True)
    shutil.copy2(p00_png, os.path.join(ROOT_DIR, "00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png"))
    print("Rendered and copied 00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png")

# ==============================================================================
# 3. UPDATE MOBILE HOMEPAGE (mobile_01_framed.html)
# ==============================================================================
mob01_path = os.path.join(DESIGNS_DIR, "mobile_01_framed.html")
if os.path.exists(mob01_path):
    with open(mob01_path, "r", encoding="utf-8") as f:
        mob_content = f.read()

    # Update mobile colors and hero banner
    mob_content = mob_content.replace("#070d18", "#0a3658")
    mob_content = mob_content.replace("#0b1120", "#0e4c77")
    mob_content = mob_content.replace("#172a4d", "#125c90")

    with open(mob01_path, "w", encoding="utf-8") as f:
        f.write(mob_content)

    mob01_png = os.path.join(DESIGNS_DIR, "Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png")
    cmd_mob = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=540,1200",
        "--force-device-scale-factor=1.5",
        "--virtual-time-budget=2500",
        f"--screenshot={mob01_png}",
        f"file:///{os.path.abspath(mob01_path).replace(chr(92), '/')}"
    ]
    subprocess.run(cmd_mob, check=True)
    shutil.copy2(mob01_png, os.path.join(ROOT_DIR, "Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png"))
    print("Rendered and copied Mobile_01_الصفحة_الرئيسية_Mobile_Homepage.png")

print("\nAll 3 main screens successfully updated and rendered!")
