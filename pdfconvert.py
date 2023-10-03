import pyautogui                        # importeer de package 'pyautogui'
from PIL import Image                   # haal de 'Image' module uit de 'Pillow' package

my_screenshot = pyautogui.screenshot()  # maak een screenshot
screenshot_path = r'C:\Users\Danny\Documents\School\Module 12 - Python\PNG\picture.png' # locatie waar screenshot wordt opgeslagen
my_screenshot.save(screenshot_path)     # slaat screenshot op

image_1 = Image.open(screenshot_path)   # haal screenshot op vanaf de opgegeven bestandslocatie
im_1 = image_1.convert('RGB')           # converteert kleuren naar 'RGB'
pdf_path = r'C:\Users\Danny\Documents\School\Module 12 - Python\PDF_Output\new_pdf01.pdf'   # locatie waar PDF wordt opgeslagen
im_1.save(pdf_path) # slaat PDF op