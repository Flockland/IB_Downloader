from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Made by Flockland

folder_path = ""
selected_extensions = []

def save_selection():
    global selected_extensions
    selected_extensions = [ext for ext, var in checkboxes.items() if var.get()]
    select_folder()

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path = folder_path.replace("/", "\\")
        root.destroy()

# Get options from user.
root = tk.Tk()
root.title("Select File Types & Folder")
root.geometry("400x300")
tk.Label(root, text="Select file types to download:").pack(pady=5)
file_types = [".pdf", ".png", ".jpg", ".html", ".css", ".zip"]
checkboxes = {ext: tk.BooleanVar() for ext in file_types}
for ext, var in checkboxes.items():
    tk.Checkbutton(root, text=ext, variable=var).pack(anchor="w")
btn = tk.Button(root, text="Select Folder to Download to", command=save_selection)
btn.pack(pady=10)

root.mainloop()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
prefs = {
    "download.default_directory": folder_path,  
    "download.prompt_for_download": False,      
    "download.directory_upgrade": True,         
    "safebrowsing.enabled": True                
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=Service(), options=options)

url = 'https://repo.pirateib.xyz/'
driver.get(url)


time.sleep(3)  

rows = driver.find_elements(By.CSS_SELECTOR, '#main-table tbody tr')
urls = []

dirs = {"https://repo.pirateib.xyz" : {}}
current = "https://repo.pirateib.xyz"
baseUrl = "https://repo.pirateib.xyz"

downloaded = []

past = ["https://repo.pirateib.xyz/?p=","https://repo.pirateib.xyz"]
# Recursively navigate through website downloading wanted files.
def populate(url,dir2,cur_path):
    try:
        # Attempt to create folder structure
        os.makedirs(folder_path+"\\"+'\\'.join(cur_path))
    except Exception as e:
        pass
    driver.get(url)
    rows = driver.find_elements(By.CSS_SELECTOR, '#main-table tbody tr')
    i = 0
    while i < len(rows):
        try:
            row = rows[i]
            # Find the link in the last cell (Actions)
            link = row.find_element(By.CSS_SELECTOR, 'td:first-child a')
            folder = row.text.split("\n")[0]
            #Extract the query part from the href
            query_part = link.get_attribute('href').split('?')[1] if '?' in link.get_attribute('href') else None
            newUrl = baseUrl+"/?"+query_part
            if newUrl in past:
                # Skip urls already visited ( such as return url )
                i+=1
                continue
            flag = False

            for ext in selected_extensions:
                if newUrl.endswith(ext):
                    flg = True
                    break

            if flag and not newUrl in downloaded:
                driver.get(newUrl)
                button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download')]")
                button.click()
                new_path = cur_path.copy()
                new_path.append(folder)
                
                # Move the downloaded file into its correct place.
                source = ""
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)
                    if os.path.isfile(file_path):
                        print(file_path)
                        source = file_path
                        break
                shutil.move(source, folder_path+"\\"+'\\'.join(new_path))
                downloaded.append(newUrl)
                past.append(newUrl)
                driver.get(url)
                # Refresh stale element
                rows = driver.find_elements(By.CSS_SELECTOR, '#main-table tbody tr')
                i+=1
                continue
            # Enter new sub directory recursively
            new_path = cur_path.copy()
            new_path.append(folder)
            dir2[newUrl] = {}
            past.append(newUrl)
            populate(newUrl,dir2[newUrl],new_path)
            driver.get(url)
            urls.append(newUrl)
            rows = driver.find_elements(By.CSS_SELECTOR, '#main-table tbody tr')
            
        except Exception as e:
            print(f"Error extracting URL: {e}")
        i+=1
    else:
        pass
    # Return to previous page once done with current.
    driver.get(url)
    return
path = []
populate("https://repo.pirateib.xyz",dirs["https://repo.pirateib.xyz"],path)
input("Done. ( Probably )\nPress Enter to terminate the program.")


driver.quit()