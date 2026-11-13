# -*- coding: utf-8 -*-
import os
import subprocess

DESIGNS_DIR = r"E:\mess\designs"
ASSETS_DIR = os.path.join(DESIGNS_DIR, "assets")

# Check logo files
clean_logo = "assets/logo_clean.png"
white_logo = "assets/logo_white.png"

# SVG Icons
ICON_SEARCH = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>'''
ICON_CART = '''<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>'''
ICON_COMPARE = '''<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>'''
ICON_WHATSAPP = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.592 2.654-.696c1.029.575 1.748.817 2.806.817 3.181 0 5.767-2.587 5.768-5.766.001-3.182-2.585-5.768-5.768-5.768zm0 10.37c-.894 0-1.67-.238-2.427-.69l-.174-.103-1.802.472.48-1.758-.113-.181c-.504-.805-.77-1.524-.769-2.544 0-2.535 2.062-4.597 4.597-4.597 2.536 0 4.598 2.063 4.598 4.598 0 2.535-2.063 4.597-4.597 4.597z"/></svg>'''
ICON_SHIELD = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><path d="m9 12 2 2 4-4"></path></svg>'''
ICON_TRUCK = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>'''
ICON_DOWNLOAD = '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>'''
ICON_CHECK = '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>'''
ICON_CLOCK = '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'''

# Product Hardware SVGs (Crisp realistic vector equipment)
SVG_CISCO_SWITCH = '''
<svg viewBox="0 0 400 160" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sw-body" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2d3748"/>
      <stop offset="50%" stop-color="#1a202c"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="metal" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="50%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
  </defs>
  <!-- 1U Chassis -->
  <rect x="20" y="35" width="360" height="90" rx="4" fill="url(#sw-body)" stroke="#475569" stroke-width="1.5"/>
  <!-- Rack Ears -->
  <rect x="8" y="35" width="12" height="90" rx="2" fill="url(#metal)"/>
  <circle cx="14" cy="45" r="2.5" fill="#1e293b"/>
  <circle cx="14" cy="115" r="2.5" fill="#1e293b"/>
  <rect x="380" y="35" width="12" height="90" rx="2" fill="url(#metal)"/>
  <circle cx="386" cy="45" r="2.5" fill="#1e293b"/>
  <circle cx="386" cy="115" r="2.5" fill="#1e293b"/>
  <!-- Cisco Badge & Model -->
  <rect x="35" y="48" width="50" height="14" rx="2" fill="#0284c7" opacity="0.8"/>
  <text x="60" y="58" font-size="8" font-family="sans-serif" font-weight="900" fill="#ffffff" text-anchor="middle">CISCO</text>
  <text x="35" y="72" font-size="7" font-family="monospace" fill="#94a3b8">WS-C2960X-24TD-L</text>
  <!-- System LEDs -->
  <circle cx="38" cy="88" r="2" fill="#10b981"/>
  <circle cx="46" cy="88" r="2" fill="#10b981"/>
  <circle cx="54" cy="88" r="2" fill="#10b981"/>
  <circle cx="62" cy="88" r="2" fill="#38bdf8"/>
  <text x="35" y="98" font-size="6" font-family="monospace" fill="#64748b">STAT  RPS  MAST  PoE</text>
  <!-- 24 Ports Grid (2 rows of 12) -->
  <g transform="translate(105, 52)">
    <rect x="-4" y="-4" width="205" height="52" rx="3" fill="#0f172a" stroke="#334155"/>
''' + "".join([f'''
    <rect x="{i*16}" y="0" width="12" height="18" rx="2" fill="#1e293b" stroke="#475569" stroke-width="0.8"/>
    <rect x="{i*16+2}" y="2" width="8" height="5" fill="#0284c7" opacity="0.3"/>
    <circle cx="{i*16+6}" cy="21" r="1.5" fill="{"#10b981" if i%2==0 else "#0284c7"}"/>
    <rect x="{i*16}" y="26" width="12" height="18" rx="2" fill="#1e293b" stroke="#475569" stroke-width="0.8"/>
    <rect x="{i*16+2}" y="28" width="8" height="5" fill="#0284c7" opacity="0.3"/>
    <circle cx="{i*16+6}" cy="47" r="1.5" fill="{"#10b981" if (i+1)%3!=0 else "#64748b"}"/>
''' for i in range(12)]) + '''
  </g>
  <!-- 2x 10G SFP+ Uplink Slots -->
  <g transform="translate(322, 54)">
    <rect x="-4" y="-4" width="45" height="48" rx="3" fill="#0f172a" stroke="#334155"/>
    <rect x="0" y="2" width="16" height="38" rx="2" fill="#334155" stroke="#94a3b8"/>
    <rect x="20" y="2" width="16" height="38" rx="2" fill="#334155" stroke="#94a3b8"/>
    <circle cx="8" cy="44" r="1.5" fill="#38bdf8"/>
    <circle cx="28" cy="44" r="1.5" fill="#38bdf8"/>
    <text x="18" y="-7" font-size="6" font-family="monospace" fill="#38bdf8" text-anchor="middle">10G SFP+</text>
  </g>
</svg>
'''

SVG_MIKROTIK = '''
<svg viewBox="0 0 400 160" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect x="25" y="35" width="350" height="90" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="12" y="35" width="13" height="90" fill="#94a3b8" rx="2"/>
  <rect x="375" y="35" width="13" height="90" fill="#94a3b8" rx="2"/>
  <rect x="42" y="50" width="55" height="24" rx="3" fill="#0f172a"/>
  <text x="69" y="66" font-size="9" font-family="monospace" font-weight="700" fill="#38bdf8" text-anchor="middle">RouterOS</text>
  <text x="42" y="86" font-size="8" font-family="sans-serif" font-weight="800" fill="#1e293b">MikroTik</text>
  <text x="42" y="98" font-size="7" font-family="monospace" fill="#64748b">CRS328-24P-4S+RM</text>
  <!-- Port cluster -->
  <g transform="translate(125, 52)">
    <rect x="-4" y="-4" width="180" height="52" rx="3" fill="#e2e8f0" stroke="#94a3b8"/>
''' + "".join([f'''
    <rect x="{i*14}" y="2" width="11" height="18" rx="1.5" fill="#1e293b" stroke="#64748b"/>
    <circle cx="{i*14+5}" cy="22" r="1.2" fill="#10b981"/>
    <rect x="{i*14}" y="26" width="11" height="18" rx="1.5" fill="#1e293b" stroke="#64748b"/>
    <circle cx="{i*14+5}" cy="46" r="1.2" fill="#10b981"/>
''' for i in range(12)]) + '''
  </g>
  <!-- 4 SFP+ cages -->
  <g transform="translate(315, 52)">
    <rect x="0" y="4" width="10" height="38" rx="1.5" fill="#334155" stroke="#0099e5"/>
    <rect x="13" y="4" width="10" height="38" rx="1.5" fill="#334155" stroke="#0099e5"/>
    <rect x="26" y="4" width="10" height="38" rx="1.5" fill="#334155" stroke="#0099e5"/>
    <rect x="39" y="4" width="10" height="38" rx="1.5" fill="#334155" stroke="#0099e5"/>
    <text x="25" y="-5" font-size="7" font-family="monospace" fill="#0284c7" text-anchor="middle">4x SFP+ 10G</text>
  </g>
</svg>
'''

SVG_FORTINET = '''
<svg viewBox="0 0 320 160" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect x="30" y="40" width="260" height="80" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
  <rect x="45" y="52" width="70" height="16" rx="2" fill="#ef4444"/>
  <text x="80" y="63" font-size="9" font-family="sans-serif" font-weight="900" fill="#fff" text-anchor="middle">FORTINET</text>
  <text x="45" y="80" font-size="8" font-family="monospace" font-weight="700" fill="#0f172a">FortiGate 60F</text>
  <text x="45" y="92" font-size="7" font-family="sans-serif" fill="#64748b">Next-Gen Firewall</text>
  <!-- Ports -->
  <g transform="translate(140, 56)">
    <rect x="0" y="0" width="14" height="22" rx="2" fill="#1e293b"/>
    <text x="7" y="30" font-size="5" fill="#64748b" text-anchor="middle">WAN1</text>
    <rect x="18" y="0" width="14" height="22" rx="2" fill="#1e293b"/>
    <text x="25" y="30" font-size="5" fill="#64748b" text-anchor="middle">WAN2</text>
    <rect x="36" y="0" width="14" height="22" rx="2" fill="#1e293b"/>
    <text x="43" y="30" font-size="5" fill="#64748b" text-anchor="middle">DMZ</text>
    <rect x="60" y="0" width="14" height="22" rx="2" fill="#0284c7"/>
    <rect x="78" y="0" width="14" height="22" rx="2" fill="#0284c7"/>
    <rect x="96" y="0" width="14" height="22" rx="2" fill="#0284c7"/>
    <rect x="114" y="0" width="14" height="22" rx="2" fill="#0284c7"/>
    <rect x="132" y="0" width="14" height="22" rx="2" fill="#0284c7"/>
    <text x="103" y="30" font-size="6" fill="#0284c7" text-anchor="middle">Internal 1-5 (GbE)</text>
  </g>
</svg>
'''

SVG_UBIQUITI_AP = '''
<svg viewBox="0 0 240 180" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="ap-glow" cx="50%" cy="50%" r="50%">
      <stop offset="70%" stop-color="#ffffff"/>
      <stop offset="90%" stop-color="#f1f5f9"/>
      <stop offset="100%" stop-color="#cbd5e1"/>
    </radialGradient>
  </defs>
  <!-- Outer Dome -->
  <circle cx="120" cy="90" r="70" fill="url(#ap-glow)" stroke="#e2e8f0" stroke-width="2" filter="drop-shadow(0 6px 12px rgba(0,0,0,0.08))"/>
  <!-- Glowing UniFi Cyan Ring -->
  <circle cx="120" cy="90" r="28" fill="none" stroke="#0099e5" stroke-width="3.5" opacity="0.9"/>
  <!-- Center metallic logo notch -->
  <circle cx="120" cy="90" r="24" fill="#f8fafc"/>
  <path d="M115 84 L125 84 L120 96 Z" fill="#0099e5" opacity="0.8"/>
  <text x="120" y="108" font-size="6" font-family="sans-serif" font-weight="700" fill="#64748b" text-anchor="middle">U6-PRO</text>
  <text x="120" y="172" font-size="8" font-family="sans-serif" font-weight="700" fill="#0f172a" text-anchor="middle">UniFi Wi-Fi 6 Pro Access Point</text>
</svg>
'''

SVG_RACK_UPS = '''
<svg viewBox="0 0 240 180" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect x="30" y="20" width="180" height="140" rx="6" fill="#0f172a" stroke="#334155" stroke-width="2"/>
  <rect x="45" y="35" width="150" height="30" rx="3" fill="#1e293b"/>
  <!-- LCD -->
  <rect x="55" y="42" width="50" height="16" rx="2" fill="#0284c7" opacity="0.3"/>
  <text x="80" y="53" font-size="7" font-family="monospace" fill="#38bdf8" text-anchor="middle">230V / 100%</text>
  <circle cx="120" cy="50" r="4" fill="#10b981"/>
  <rect x="45" y="75" width="150" height="70" rx="3" fill="#1e293b"/>
  <line x1="55" y1="90" x2="185" y2="90" stroke="#475569" stroke-dasharray="4 2"/>
  <line x1="55" y1="110" x2="185" y2="110" stroke="#475569" stroke-dasharray="4 2"/>
  <line x1="55" y1="130" x2="185" y2="130" stroke="#475569" stroke-dasharray="4 2"/>
  <text x="120" y="165" font-size="7" font-family="monospace" fill="#94a3b8" text-anchor="middle">APC Smart-UPS RT 3000VA</text>
</svg>
'''

print("SVGs prepared successfully!")

