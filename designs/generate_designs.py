# -*- coding: utf-8 -*-
"""
Generator for MESS TECH E-Commerce UI/UX Mockups
Faithful to Technical Specifications PDF:
- Logo integration
- Enterprise IT & Networking focus (Switches, Routers, Firewalls, Wi-Fi, UPS, Racks, Cables)
- Fast Model / SKU Search
- Advanced Technical Filters (Ports, PoE, Speed)
- COD Only Checkout (One Step)
- Direct WhatsApp Sales Button (No Business API)
- 4-Model Comparison Matrix
- Mobile Responsive Showcase
- Admin Dashboard
"""

import os
import subprocess

DESIGNS_DIR = r"E:\mess\designs"
ASSETS_DIR = os.path.join(DESIGNS_DIR, "assets")

# Base styles & fonts
COMMON_HEAD = """
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --primary-navy: #0b1120;
  --secondary-navy: #131d33;
  --card-dark: #1e293b;
  --accent-cyan: #0099e5;
  --accent-cyan-hover: #0284c7;
  --accent-cyan-light: #e0f2fe;
  --accent-cyan-glow: rgba(0, 153, 229, 0.25);
  --text-primary: #0f172a;
  --text-muted: #64748b;
  --border-light: #e2e8f0;
  --bg-light: #f8fafc;
  --success-emerald: #10b981;
  --warning-amber: #f59e0b;
  --danger-rose: #ef4444;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Cairo', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

body {
  background-color: var(--bg-light);
  color: var(--text-primary);
  direction: rtl;
  text-align: right;
  -webkit-font-smoothing: antialiased;
}

.mono {
  font-family: 'JetBrains Mono', monospace;
  direction: ltr;
  display: inline-block;
}

/* Header & Navigation Styles */
.top-bar {
  background: #070d18;
  color: #94a3b8;
  font-size: 13px;
  padding: 8px 32px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.top-bar-notice {
  display: flex;
  align-items: center;
  gap: 12px;
}

.badge-cod-top {
  background: rgba(16, 185, 129, 0.15);
  color: #34d399;
  border: 1px solid rgba(16, 185, 129, 0.3);
  padding: 2px 10px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 11px;
}

.main-header {
  background: var(--primary-navy);
  padding: 16px 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 28px;
  border-bottom: 2px solid #1e293b;
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}

.logo-img {
  height: 48px;
  width: auto;
  object-fit: contain;
}

.search-box-wrapper {
  flex: 1;
  max-width: 680px;
  position: relative;
}

.search-input-group {
  display: flex;
  align-items: center;
  background: #172136;
  border: 1.5px solid #2d3b55;
  border-radius: 10px;
  padding: 2px 8px;
  transition: all 0.2s;
}

.search-input-group:focus-within {
  border-color: var(--accent-cyan);
  box-shadow: 0 0 0 3px var(--accent-cyan-glow);
}

.search-category-select {
  background: transparent;
  border: none;
  border-left: 1px solid #2d3b55;
  color: #94a3b8;
  font-size: 13px;
  padding: 8px 12px;
  outline: none;
  cursor: pointer;
}

.search-input {
  flex: 1;
  background: transparent;
  border: none;
  padding: 10px 14px;
  color: #f8fafc;
  font-size: 14px;
  outline: none;
}

.search-input::placeholder {
  color: #64748b;
  font-size: 13px;
}

.search-btn {
  background: var(--accent-cyan);
  border: none;
  color: #fff;
  border-radius: 8px;
  padding: 8px 20px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.action-pill-btn {
  background: #172136;
  border: 1px solid #2d3b55;
  color: #f1f5f9;
  padding: 8px 14px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  text-decoration: none;
  font-weight: 600;
  position: relative;
}

.action-badge {
  background: var(--accent-cyan);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  padding: 1px 6px;
  border-radius: 999px;
}

.action-badge.green {
  background: var(--success-emerald);
}

.whatsapp-sales-btn {
  background: #22c55e;
  color: #fff;
  border: none;
  padding: 9px 18px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  text-decoration: none;
}

/* Category Subnav */
.category-subnav {
  background: #0f172a;
  padding: 0 32px;
  display: flex;
  align-items: center;
  gap: 4px;
  border-bottom: 1px solid #1e293b;
  overflow-x: auto;
}

.nav-cat-item {
  color: #cbd5e1;
  padding: 12px 16px;
  font-size: 13.5px;
  font-weight: 600;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 2px solid transparent;
  white-space: nowrap;
}

.nav-cat-item:hover, .nav-cat-item.active {
  color: #38bdf8;
  border-bottom-color: #38bdf8;
  background: rgba(56, 189, 248, 0.05);
}

.all-cats-btn {
  background: var(--accent-cyan);
  color: #fff;
  font-weight: 700;
  padding: 10px 18px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: 12px;
  font-size: 13.5px;
}

/* Footer */
.main-footer {
  background: #070d18;
  color: #94a3b8;
  padding: 48px 32px 24px;
  border-top: 1px solid #1e293b;
  margin-top: 60px;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 40px;
  max-width: 1360px;
  margin: 0 auto 36px;
}

.footer-col h4 {
  color: #f8fafc;
  font-size: 16px;
  font-weight: 800;
  margin-bottom: 18px;
  position: relative;
  padding-bottom: 8px;
}

.footer-col h4::after {
  content: '';
  position: absolute;
  bottom: 0;
  right: 0;
  width: 32px;
  height: 2px;
  background: var(--accent-cyan);
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 13.5px;
}

.footer-links a {
  color: #94a3b8;
  text-decoration: none;
}

.footer-bottom {
  border-top: 1px solid #1e293b;
  padding-top: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  max-width: 1360px;
  margin: 0 auto;
}

/* COD Assurance Banner */
.cod-guarantee-strip {
  background: linear-gradient(90deg, #064e3b 0%, #065f46 100%);
  border: 1px solid #10b981;
  color: #ecfdf5;
  padding: 14px 24px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 16px rgba(16, 185, 129, 0.15);
}
</style>
"""

print("Common template defined!")

