# -*- coding: utf-8 -*-
import os
import subprocess
from layout_base import SHARED_CSS, get_header_html, get_footer_html
from prepare_svgs import SVG_CISCO_SWITCH, SVG_MIKROTIK, SVG_FORTINET, SVG_UBIQUITI_AP, SVG_RACK_UPS

DESIGNS_DIR = r"E:\mess\designs"

HTML_CONTENT = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
  <meta charset="utf-8">
  <title>MESS TECH | الصفحة الرئيسية - حلول الشبكات والبنية التحتية وأمن المعلومات</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    {SHARED_CSS}

    /* Hero Banner */
    .hero-section {{
      background: radial-gradient(circle at 85% 30%, #172a4d 0%, #0b1120 70%);
      color: #fff;
      padding: 60px 48px;
      position: relative;
      overflow: hidden;
      border-bottom: 1px solid var(--navy-700);
    }}
    .hero-container {{
      max-width: 1340px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      align-items: center;
      gap: 48px;
    }}
    .hero-badge-live {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0, 153, 229, 0.15);
      border: 1px solid rgba(0, 153, 229, 0.4);
      color: var(--cyan-400);
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 20px;
    }}
    .hero-title {{
      font-size: 40px;
      line-height: 1.3;
      font-weight: 900;
      margin-bottom: 18px;
      letter-spacing: -0.5px;
    }}
    .hero-title span {{
      color: var(--cyan-400);
      text-shadow: 0 0 20px rgba(0, 153, 229, 0.4);
    }}
    .hero-subtitle {{
      font-size: 16px;
      line-height: 1.8;
      color: #94a3b8;
      margin-bottom: 28px;
      max-width: 600px;
    }}
    .hero-actions {{
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 32px;
    }}
    .btn-primary-hero {{
      background: var(--cyan-500);
      color: #fff;
      font-size: 15px;
      font-weight: 800;
      padding: 13px 28px;
      border-radius: 10px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 18px rgba(0, 153, 229, 0.35);
    }}
    .btn-secondary-hero {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      font-size: 15px;
      font-weight: 700;
      padding: 13px 24px;
      border-radius: 10px;
      text-decoration: none;
    }}
    .hero-trust-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 24px;
    }}
    .hero-trust-item {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .hero-trust-icon {{
      width: 32px;
      height: 32px;
      background: rgba(0, 153, 229, 0.15);
      color: var(--cyan-400);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
    }}
    .hero-trust-text {{
      font-size: 12.5px;
      font-weight: 700;
      color: #e2e8f0;
      line-height: 1.4;
    }}

    /* Hero Hardware Visual */
    .hero-hardware-box {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.4), inset 0 0 0 1px rgba(255,255,255,0.05);
      position: relative;
    }}
    .hardware-tag {{
      position: absolute;
      top: -12px;
      right: 24px;
      background: #10b981;
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 12px;
      border-radius: 999px;
      box-shadow: 0 2px 8px rgba(16, 185, 129, 0.4);
    }}

    /* Brand Strip */
    .brand-ribbon {{
      background: #fff;
      border-bottom: 1px solid var(--slate-200);
      padding: 24px 48px;
    }}
    .brand-container {{
      max-width: 1340px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }}
    .brand-title-lead {{
      font-size: 13px;
      font-weight: 800;
      color: var(--slate-500);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .brand-logo-item {{
      font-weight: 900;
      font-size: 18px;
      color: #475569;
      opacity: 0.8;
      display: flex;
      align-items: center;
      gap: 6px;
      letter-spacing: 1px;
    }}

    /* Weekly Deals Section with Countdown */
    .weekly-deals-section {{
      max-width: 1340px;
      margin: 48px auto 0;
      padding: 0 48px;
    }}
    .deals-banner-header {{
      background: linear-gradient(90deg, #1e293b 0%, #0f172a 100%);
      border: 1px solid #334155;
      border-radius: 16px;
      padding: 24px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #fff;
      margin-bottom: 24px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    }}
    .deals-title-wrap h3 {{
      font-size: 22px;
      font-weight: 800;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .deals-countdown-box {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .countdown-unit {{
      background: #172136;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 6px 12px;
      text-align: center;
      min-width: 52px;
    }}
    .countdown-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 20px;
      font-weight: 800;
      color: #f59e0b;
      display: block;
      line-height: 1.1;
    }}
    .countdown-label {{
      font-size: 10.5px;
      color: #94a3b8;
    }}

    /* Products Grid */
    .products-grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }}
    .deal-card {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 14px;
      padding: 20px;
      transition: all 0.2s;
      position: relative;
      display: flex;
      flex-direction: column;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}
    .deal-card:hover {{
      border-color: var(--cyan-500);
      box-shadow: 0 8px 24px rgba(0, 153, 229, 0.12);
      transform: translateY(-2px);
    }}
    .badge-discount {{
      position: absolute;
      top: 16px;
      right: 16px;
      background: var(--rose-500);
      color: #fff;
      font-size: 12px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
    }}
    .badge-cod-card {{
      position: absolute;
      top: 16px;
      left: 16px;
      background: rgba(16, 185, 129, 0.12);
      color: #059669;
      border: 1px solid rgba(16, 185, 129, 0.3);
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
    }}
    .card-img-wrap {{
      height: 150px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 20px 0 12px;
      background: #f8fafc;
      border-radius: 10px;
      padding: 10px;
    }}
    .card-brand-model {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}
    .card-brand {{
      font-size: 12px;
      font-weight: 700;
      color: var(--cyan-600);
      text-transform: uppercase;
    }}
    .card-model-sku {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      color: #334155;
      background: #f1f5f9;
      padding: 2px 8px;
      border-radius: 4px;
    }}
    .card-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--navy-900);
      line-height: 1.5;
      margin-bottom: 12px;
      height: 44px;
      overflow: hidden;
    }}
    .specs-pill-strip {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 16px;
    }}
    .specs-pill {{
      background: #f1f5f9;
      color: #475569;
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .deal-progress-bar-wrap {{
      margin-bottom: 16px;
    }}
    .deal-progress-label {{
      display: flex;
      justify-content: space-between;
      font-size: 11.5px;
      color: #64748b;
      margin-bottom: 4px;
      font-weight: 600;
    }}
    .progress-track {{
      height: 6px;
      background: #e2e8f0;
      border-radius: 999px;
      overflow: hidden;
    }}
    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, #f59e0b, #ef4444);
      border-radius: 999px;
    }}
    .card-price-row {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-top: auto;
      padding-top: 12px;
      border-top: 1px solid var(--slate-100);
    }}
    .price-current {{
      font-size: 20px;
      font-weight: 900;
      color: var(--navy-900);
    }}
    .price-current small {{
      font-size: 12px;
      font-weight: 600;
      color: #64748b;
    }}
    .price-old {{
      font-size: 13px;
      color: #94a3b8;
      text-decoration: line-through;
    }}
    .card-btn-action {{
      background: var(--cyan-500);
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Solution Categories Grid */
    .categories-section {{
      max-width: 1340px;
      margin: 56px auto 0;
      padding: 0 48px;
    }}
    .section-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 24px;
    }}
    .section-title {{
      font-size: 24px;
      font-weight: 800;
      color: var(--navy-900);
    }}
    .section-subtitle {{
      font-size: 14px;
      color: #64748b;
      margin-top: 4px;
    }}
    .category-grid-6 {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 16px;
    }}
    .cat-box {{
      background: #fff;
      border: 1px solid var(--slate-200);
      border-radius: 12px;
      padding: 20px 14px;
      text-align: center;
      transition: all 0.2s;
      text-decoration: none;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .cat-box:hover {{
      border-color: var(--cyan-500);
      box-shadow: 0 8px 20px rgba(0, 153, 229, 0.1);
      transform: translateY(-3px);
    }}
    .cat-box-icon {{
      width: 52px;
      height: 52px;
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--cyan-600);
      margin-bottom: 12px;
    }}
    .cat-box-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--navy-900);
      margin-bottom: 4px;
    }}
    .cat-box-count {{
      font-size: 12px;
      color: #64748b;
      font-weight: 500;
    }}

    /* Value Proposition Strip */
    .value-strip {{
      max-width: 1340px;
      margin: 60px auto 0;
      padding: 0 48px;
    }}
    .value-strip-container {{
      background: #0f172a;
      border-radius: 16px;
      padding: 36px 40px;
      color: #fff;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 32px;
      border: 1px solid #1e293b;
    }}
    .value-item {{
      display: flex;
      gap: 14px;
      align-items: flex-start;
    }}
    .value-icon-circle {{
      width: 44px;
      height: 44px;
      background: rgba(0, 153, 229, 0.15);
      color: var(--cyan-400);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .value-item h4 {{
      font-size: 15px;
      font-weight: 800;
      color: #fff;
      margin-bottom: 4px;
    }}
    .value-item p {{
      font-size: 12.5px;
      color: #94a3b8;
      line-height: 1.6;
    }}
  </style>
</head>
<body>

  {get_header_html(active_cat="")}

  <!-- Hero Banner -->
  <section class="hero-section">
    <div class="hero-container">
      <div>
        <div class="hero-badge-live">
          <span style="display:inline-block; width:8px; height:8px; background:#10b981; border-radius:999px;"></span>
          الموزع المعتمد لحلول الشبكات والأمان للمشروعات والشركات
        </div>
        <h1 class="hero-title">
          تجهيز البنية التحتية والشبكات<br>
          بأعلى معايير <span>Enterprise المعتمدة</span>
        </h1>
        <p class="hero-subtitle">
          نوفر أحدث أجهزة السويتشات، الفايروول، الراوترات وأكسس بوينت لأكبر الماركات العالمية (Cisco, Fortinet, MikroTik, Ubiquiti). توريد فوري مع الدفع كاش عند الاستلام (COD) وضمان استبدال معتمد.
        </p>
        <div class="hero-actions">
          <a href="#" class="btn-primary-hero">
            تصفح السويتشات والمعدات
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
          <a href="#" class="btn-secondary-hero">
            طلب عرض أسعار للشركات (RFQ)
          </a>
        </div>
        <div class="hero-trust-grid">
          <div class="hero-trust-item">
            <div class="hero-trust-icon">✓</div>
            <div class="hero-trust-text">دفع كاش عند الاستلام<br><span style="color:#94a3b8; font-weight:400;">معاينة الأجهزة أولاً</span></div>
          </div>
          <div class="hero-trust-item">
            <div class="hero-trust-icon">PDF</div>
            <div class="hero-trust-text">داتاشيت معتمدة<br><span style="color:#94a3b8; font-weight:400;">مواصفات دقيقة لكل موديل</span></div>
          </div>
          <div class="hero-trust-item">
            <div class="hero-trust-icon">⚡</div>
            <div class="hero-trust-text">شحن سريع للمحافظات<br><span style="color:#94a3b8; font-weight:400;">+ استلام مجاني من الفرع</span></div>
          </div>
        </div>
      </div>

      <!-- Hero Visual Equipment Showcase -->
      <div class="hero-hardware-box">
        <span class="hardware-tag">أحدث وصول للمخزون</span>
        <div style="margin-bottom:12px;">
          <div style="font-size:12px; color:var(--cyan-400); font-weight:700; text-transform:uppercase;">Cisco Systems • Catalyst 2960X</div>
          <div style="font-size:18px; font-weight:800; color:#fff;">WS-C2960X-24TD-L Gigabit PoE+</div>
        </div>
        <div style="height:140px; margin-bottom:14px;">
          {SVG_CISCO_SWITCH}
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; background:#172136; padding:12px 16px; border-radius:10px;">
          <div>
            <div style="font-size:11px; color:#94a3b8;">سعر التوريد النقدي (COD)</div>
            <div style="font-size:18px; font-weight:800; color:#fff;">19,850 <small style="font-size:12px; color:#94a3b8;">ج.م</small></div>
          </div>
          <div style="display:flex; gap:8px;">
            <span style="background:rgba(16,185,129,0.15); color:#34d399; font-size:11px; font-weight:700; padding:6px 12px; border-radius:6px;">متوفر بالمخزون</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Certified Brands -->
  <section class="brand-ribbon">
    <div class="brand-container">
      <div class="brand-title-lead">الماركات المعتمدة:</div>
      <div class="brand-logo-item" style="color:#0284c7;">CISCO</div>
      <div class="brand-logo-item" style="color:#ef4444;">FORTINET</div>
      <div class="brand-logo-item" style="color:#0f172a;">MIKROTIK</div>
      <div class="brand-logo-item" style="color:#0099e5;">UBIQUITI</div>
      <div class="brand-logo-item" style="color:#f97316;">ARUBA</div>
      <div class="brand-logo-item" style="color:#10b981;">SCHNEIDER APC</div>
      <div class="brand-logo-item" style="color:#334155;">RUIJIE</div>
    </div>
  </section>

  <!-- Weekly Deals with Timer -->
  <section class="weekly-deals-section">
    <div class="deals-banner-header">
      <div class="deals-title-wrap">
        <h3>
          <span style="color:#f59e0b;">⚡</span>
          عروض التوريد الأسبوعية الحصرية
        </h3>
        <p style="font-size:13px; color:#94a3b8; margin-top:4px;">أسعار خاصة لفترة محدودة على معدات الشبكات الأصلية مع شحن سريع ودفع عند الاستلام</p>
      </div>
      <div class="deals-countdown-box">
        <span style="font-size:13px; font-weight:700; color:#cbd5e1; margin-left:8px;">ينتهي العرض خلال:</span>
        <div class="countdown-unit">
          <span class="countdown-num">02</span>
          <span class="countdown-label">يوم</span>
        </div>
        <div class="countdown-unit">
          <span class="countdown-num">14</span>
          <span class="countdown-label">ساعة</span>
        </div>
        <div class="countdown-unit">
          <span class="countdown-num">28</span>
          <span class="countdown-label">دقيقة</span>
        </div>
        <div class="countdown-unit">
          <span class="countdown-num">45</span>
          <span class="countdown-label">ثانية</span>
        </div>
      </div>
    </div>

    <!-- 3 Deal Cards -->
    <div class="products-grid-3">
      <!-- Card 1: Cisco Switch -->
      <div class="deal-card">
        <span class="badge-discount">-15%</span>
        <span class="badge-cod-card">دفع عند الاستلام COD</span>
        <div class="card-img-wrap">
          {SVG_CISCO_SWITCH}
        </div>
        <div class="card-brand-model">
          <span class="card-brand">Cisco Systems</span>
          <span class="card-model-sku">WS-C2960X-24TD-L</span>
        </div>
        <h4 class="card-title">سويتش سيسكو كاتاليست 24 بورت جيجابت PoE+ مع 2 منفذ 10G SFP+</h4>
        <div class="specs-pill-strip">
          <span class="specs-pill">24 Ports GbE</span>
          <span class="specs-pill">PoE+ 370W</span>
          <span class="specs-pill">2x 10G Uplink</span>
          <span class="specs-pill">Layer 2/3</span>
        </div>
        <div class="deal-progress-bar-wrap">
          <div class="deal-progress-label">
            <span>تم حجز 74% من الكمية</span>
            <span style="color:#ef4444; font-weight:700;">متبقي 5 قطع</span>
          </div>
          <div class="progress-track"><div class="progress-fill" style="width:74%;"></div></div>
        </div>
        <div class="card-price-row">
          <div>
            <div class="price-current">19,850 <small>ج.م</small></div>
            <div class="price-old">23,200 ج.م</div>
          </div>
          <button class="card-btn-action">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
            أضف للسلة
          </button>
        </div>
      </div>

      <!-- Card 2: MikroTik Router -->
      <div class="deal-card">
        <span class="badge-discount">-12%</span>
        <span class="badge-cod-card">دفع عند الاستلام COD</span>
        <div class="card-img-wrap">
          {SVG_MIKROTIK}
        </div>
        <div class="card-brand-model">
          <span class="card-brand">MikroTik</span>
          <span class="card-model-sku">CRS328-24P-4S+RM</span>
        </div>
        <h4 class="card-title">سويتش مايكروتك كلاود 24 بورت PoE ذكي مع 4 منافذ SFP+ 10G</h4>
        <div class="specs-pill-strip">
          <span class="specs-pill">24 Ports PoE</span>
          <span class="specs-pill">500W Dual PSU</span>
          <span class="specs-pill">4x 10G SFP+</span>
          <span class="specs-pill">RouterOS L5</span>
        </div>
        <div class="deal-progress-bar-wrap">
          <div class="deal-progress-label">
            <span>تم حجز 85% من الكمية</span>
            <span style="color:#ef4444; font-weight:700;">متبقي 3 قطع</span>
          </div>
          <div class="progress-track"><div class="progress-fill" style="width:85%;"></div></div>
        </div>
        <div class="card-price-row">
          <div>
            <div class="price-current">22,400 <small>ج.م</small></div>
            <div class="price-old">25,500 ج.م</div>
          </div>
          <button class="card-btn-action">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
            أضف للسلة
          </button>
        </div>
      </div>

      <!-- Card 3: Fortinet Firewall -->
      <div class="deal-card">
        <span class="badge-discount">-10%</span>
        <span class="badge-cod-card">دفع عند الاستلام COD</span>
        <div class="card-img-wrap">
          {SVG_FORTINET}
        </div>
        <div class="card-brand-model">
          <span class="card-brand" style="color:#ef4444;">Fortinet</span>
          <span class="card-model-sku">FG-60F</span>
        </div>
        <h4 class="card-title">جدار حماية فورتينت FortiGate 60F للأمن السيبراني والشركات</h4>
        <div class="specs-pill-strip">
          <span class="specs-pill">10 Gbps Firewall</span>
          <span class="specs-pill">1 Gbps Threat</span>
          <span class="specs-pill">Dual WAN</span>
          <span class="specs-pill">SD-WAN Built-in</span>
        </div>
        <div class="deal-progress-bar-wrap">
          <div class="deal-progress-label">
            <span>تم حجز 60% من الكمية</span>
            <span style="color:#10b981; font-weight:700;">متوفر بالمخزون</span>
          </div>
          <div class="progress-track"><div class="progress-fill" style="width:60%;"></div></div>
        </div>
        <div class="card-price-row">
          <div>
            <div class="price-current">28,900 <small>ج.م</small></div>
            <div class="price-old">32,000 ج.م</div>
          </div>
          <button class="card-btn-action">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
            أضف للسلة
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Categories Grid -->
  <section class="categories-section">
    <div class="section-head">
      <div>
        <h2 class="section-title">تصفح حلول التجهيزات والشبكات</h2>
        <p class="section-subtitle">أقسام متكاملة تغطي كافة متطلبات الداتا سنتر، غرف السيرفرات، والشبكات السلكية واللاسلكية</p>
      </div>
      <a href="#" style="color:var(--cyan-600); font-weight:700; text-decoration:none; font-size:14px;">عرض جميع الأقسام (7) ←</a>
    </div>

    <div class="category-grid-6">
      <a href="#" class="cat-box">
        <div class="cat-box-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="6" cy="12" r="1.5"/><circle cx="10" cy="12" r="1.5"/><circle cx="14" cy="12" r="1.5"/><circle cx="18" cy="12" r="1.5"/></svg>
        </div>
        <div class="cat-box-title">سويتشات الشبكات</div>
        <div class="cat-box-count">48 موديل معتمد</div>
      </a>

      <a href="#" class="cat-box">
        <div class="cat-box-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
        </div>
        <div class="cat-box-title">راوترات وسيرفرات</div>
        <div class="cat-box-count">26 موديل للمشروعات</div>
      </a>

      <a href="#" class="cat-box">
        <div class="cat-box-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <div class="cat-box-title">جدران الحماية</div>
        <div class="cat-box-count">19 جهاز أمني</div>
      </a>

      <a href="#" class="cat-box">
        <div class="cat-box-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg>
        </div>
        <div class="cat-box-title">أكسس بوينت وواي فاي</div>
        <div class="cat-box-count">34 جهاز UniFi & Aruba</div>
      </a>

      <a href="#" class="cat-box">
        <div class="cat-box-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="16" height="10" rx="2"/><line x1="22" y1="11" x2="22" y2="13"/></svg>
        </div>
        <div class="cat-box-title">مغذيات الطاقة UPS</div>
        <div class="cat-box-count">15 وحدة APC أصلية</div>
      </a>

      <a href="#" class="cat-box">
        <div class="cat-box-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 7h10M7 12h10M7 17h10"/></svg>
        </div>
        <div class="cat-box-title">راكات وكبائن الخوادم</div>
        <div class="cat-box-count">9U إلى 42U معتمدة</div>
      </a>
    </div>
  </section>

  <!-- Value Proposition Strip -->
  <section class="value-strip">
    <div class="value-strip-container">
      <div class="value-item">
        <div class="value-icon-circle">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 12 15 16 10"/></svg>
        </div>
        <div>
          <h4>دفع كاش عند الاستلام (COD)</h4>
          <p>أمان تام للشركات، استلم وافحص معداتك والفاتورة الضريبية ثم ادفع نقداً.</p>
        </div>
      </div>

      <div class="value-item">
        <div class="value-icon-circle">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        </div>
        <div>
          <h4>داتاشيت PDF معتمدة</h4>
          <p>مواصفات فنية تفصيلية وDatasheet رسمية قابلة للتحميل لكل موديل بالموقع.</p>
        </div>
      </div>

      <div class="value-item">
        <div class="value-icon-circle">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
        </div>
        <div>
          <h4>شحن لجميع المحافظات</h4>
          <p>شحن سريع مؤمن لكافة محافظات مصر وخيار الاستلام المباشر من مقر الشركة.</p>
        </div>
      </div>

      <div class="value-item">
        <div class="value-icon-circle">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 14 14"/></svg>
        </div>
        <div>
          <h4>ضمان استبدال معتمد</h4>
          <p>ضمان رسمي حتى سنتين مع دعم فني هندسي متخصص لتشغيل وضبط الشبكات.</p>
        </div>
      </div>
    </div>
  </section>

  {get_footer_html()}

</body>
</html>
"""

html_path = os.path.join(DESIGNS_DIR, "page_01_homepage.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Written: {html_path}")

# Render to PNG
png_path = os.path.join(DESIGNS_DIR, "01_الصفحة_الرئيسية_Desktop_Homepage.png")
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1440,2300",
    "--force-device-scale-factor=1.5",
    "--virtual-time-budget=3000",
    f"--screenshot={png_path}",
    f"file:///{os.path.abspath(html_path).replace(chr(92), '/')}"
]
subprocess.run(cmd, check=True)
print(f"Rendered: {png_path} ({os.path.getsize(png_path)/1024:.1f} KB)")

