import subprocess

html_test = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="utf-8">
<style>
body { margin: 0; background: #070d18; display: flex; justify-content: center; padding: 24px 0; }
.phone-canvas { width: 414px; background: #fff; border-radius: 36px; overflow: hidden; box-shadow: 0 16px 50px rgba(0,0,0,0.6); border: 8px solid #1e293b; }
.header { background: #0b1120; color: #fff; padding: 14px; text-align: center; font-family: sans-serif; font-weight: bold; }
.content { padding: 16px; font-family: sans-serif; }
</style>
</head>
<body>
<div class="phone-canvas">
  <div class="header">MESS TECH MOBILE TEST</div>
  <div class="content"><h3>سويتش سيسكو كاتاليست</h3><p>دفع عند الاستلام COD</p></div>
</div>
</body>
</html>"""

with open('designs/test_mob.html', 'w', encoding='utf-8') as f:
    f.write(html_test)

cmd = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=500,600',
    '--force-device-scale-factor=2.0',
    '--screenshot=designs/test_mob.png',
    'file:///E:/mess/designs/test_mob.html'
]
subprocess.run(cmd, check=True)
print('Test mob rendered successfully!')

