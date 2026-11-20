# -*- coding: utf-8 -*-
"""
update_figma_board_with_palette.py
Adds Frame 00 (Design System & Color Palette) and interactive Palette Modal to build_final_figma_board.py
"""

import os
import re

BOARD_SCRIPT = r"E:\mess\designs\build_final_figma_board.py"

with open(BOARD_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add Frame 00 at start of FRAMES_DATA
target_frames_start = 'FRAMES_DATA = [\n    # ==========================\n    # 1. STOREFRONT & CUSTOMER PORTAL (9 Screens)\n    # =========================='
replacement_frames_start = '''FRAMES_DATA = [
    # ==========================
    # 0. DESIGN SYSTEM & COLOR PALETTE
    # ==========================
    {
        "id": "frame-palette",
        "section": "storefront",
        "num": "00",
        "title": "دليل الألوان ونظام التصميم (Design System & Color Tokens)",
        "dims": "1440 × 1100",
        "src": "00_دليل_الألوان_وهوية_التصميم_Design_System_Color_Palette.png",
        "icon": "🎨"
    },

    # ==========================
    # 1. STOREFRONT & CUSTOMER PORTAL (9 Screens)
    # =========================='''

if target_frames_start in code:
    code = code.replace(target_frames_start, replacement_frames_start)
    print("Added frame-palette to FRAMES_DATA!")

# 2. Update status and title counts
code = code.replace("28 Frames", "29 Frames (Palette + UI)")
code = code.replace("28 Screens", "29 Frames")

# 3. Add Palette button in top-actions
target_top_actions = '<div class="top-actions">'
replacement_top_actions = '''<div class="top-actions">
      <button class="top-btn" onclick="openPaletteModal();" style="background:rgba(0,153,229,0.15); border:1px solid rgba(0,153,229,0.4); color:#38bdf8; font-weight:700;">
        🎨 لوحة الألوان (Palette)
      </button>'''

if target_top_actions in code and "openPaletteModal" not in code:
    code = code.replace(target_top_actions, replacement_top_actions)
    print("Added Palette button to top-actions!")

# 4. Add Palette Modal HTML right before inspect-modal
target_modal = '  <!-- Fullscreen Inspection Modal -->'
palette_modal_html = '''  <!-- Interactive Color Palette Modal -->
  <div class="inspect-modal" id="palette-modal" onclick="closePaletteModal()">
    <div class="modal-top-bar" onclick="event.stopPropagation()">
      <div class="modal-title-box">
        <span style="font-size:18px;">🎨</span>
        <h2>لوحة ألوان متجر MESS TECH الرسمية (Design System Palette)</h2>
      </div>
      <div class="modal-actions">
        <span style="font-size:12px; color:#94a3b8;">اضغط على أي كود لنسخه</span>
        <button class="top-btn" onclick="closePaletteModal()">إغلاق ✕</button>
      </div>
    </div>
    <div class="modal-body" style="padding:30px; display:block; max-width:1100px; margin:0 auto; cursor:default;" onclick="event.stopPropagation()">
      
      <!-- Brand Core -->
      <h3 style="font-size:15px; color:#38bdf8; margin-bottom:14px; font-weight:800; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px;">
        🔷 ألوان العلامة التجارية الأساسية (Brand Core)
      </h3>
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:16px; margin-bottom:28px;">
        
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
      <h3 style="font-size:15px; color:#10b981; margin-bottom:14px; font-weight:800; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px;">
        ⚡ ألوان التفاعل والتجارة الإلكترونية (E-Commerce Accents)
      </h3>
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:16px; margin-bottom:28px;">
        
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
      <h3 style="font-size:15px; color:#94a3b8; margin-bottom:14px; font-weight:800; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:6px;">
        🌫️ الرماديات والأسطح (Surfaces & Neutrals)
      </h3>
      <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:16px;">
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
'''

if target_modal in code and "palette-modal" not in code:
    code = code.replace(target_modal, palette_modal_html + "\n" + target_modal)
    print("Added palette-modal HTML!")

# 5. Add JS functions for opening/closing palette modal
js_functions = '''
    function openPaletteModal() {
      document.getElementById('palette-modal').classList.add('active');
    }
    function closePaletteModal() {
      document.getElementById('palette-modal').classList.remove('active');
    }
'''
if "openPaletteModal" not in code:
    code = code.replace("function openFocusModal(", js_functions + "\n    function openFocusModal(")
    print("Added openPaletteModal JS!")

with open(BOARD_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)
print("Updated build_final_figma_board.py!")
