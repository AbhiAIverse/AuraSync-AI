import pystray
from PIL import Image, ImageDraw
import subprocess
import sys
import os

def create_image():
    """Generates a dynamic tray icon."""
    image = Image.new('RGB', (64, 64), color=(74, 144, 226))
    dc = ImageDraw.Draw(image)
    dc.rectangle((16, 16, 48, 48), fill=(255, 255, 255))
    return image

def run_main_script(icon, item):
    subprocess.Popen([sys.executable, "main.py"])

def run_dashboard(icon, item):
    subprocess.Popen(["streamlit", "run", "dashboard/app.py"])

def on_quit(icon, item):
    icon.stop()

def setup_tray():
    icon = pystray.Icon("AuraSyncAI", create_image(), "AuraSync AI Wellness Monitor", menu=pystray.Menu(
        pystray.MenuItem("Start AI Monitor", run_main_script),
        pystray.MenuItem("Open Streamlit Dashboard", run_dashboard),
        pystray.MenuItem("Quit", on_quit)
    ))
    icon.run()

if __name__ == "__main__":
    setup_tray()