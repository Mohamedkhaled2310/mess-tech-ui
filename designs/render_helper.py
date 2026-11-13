import subprocess
import os
import sys

def render_html_to_png(html_path, output_png_path, width=1440, height=2200, scale=1.5, wait_ms=2500):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    abs_html = os.path.abspath(html_path)
    file_url = "file:///" + abs_html.replace("\\", "/")
    
    args = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--force-device-scale-factor={scale}",
        f"--virtual-time-budget={wait_ms}",
        f"--screenshot={output_png_path}",
        file_url
    ]
    
    print(f"Rendering {html_path} -> {output_png_path} ({width}x{height} @ {scale}x)...")
    res = subprocess.run(args, capture_output=True, text=True)
    if os.path.exists(output_png_path):
        size_kb = os.path.getsize(output_png_path) / 1024
        print(f"SUCCESS: {output_png_path} ({size_kb:.1f} KB)")
        return True
    else:
        print(f"FAILED: {output_png_path}")
        print("STDERR:", res.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) > 2:
        render_html_to_png(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python render_helper.py <html_path> <png_path>")

