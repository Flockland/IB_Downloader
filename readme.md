# IB Resources Scraper

This project is a Python script that scrapes a site with IB resources for school and downloads them to a folder selected by the user. The program uses **Python**, **Selenium**, **Chromedriver**, **Tkinter**, and **shutil**.

## Prerequisites

- Python 3.7 or higher
- **Selenium** WebDriver
- **Chromedriver** version `133.0.6943.98` (Official Build) (64-bit) (cohort: M133 Rollout)
- **Tkinter** and **shutil** for the graphical interface and file handling

---

## Installation

### For Technical Users:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Flockland/IB_Downloader.git
    cd IB_Downloader
    ```

2. **Activate the Virtual Environment**:
    Since the `venv` folder is included in this repository, users can skip the virtual environment creation steps. Simply run the following `.bat` script to activate the `venv`:

    On **Windows**, run the `activate_venv.bat` script:
    ```bash
    activate_venv.bat
    ```

    This will activate the `venv` folder and set up the environment for your project.

3. **Run the Script**:
    With the virtual environment activated, you can start using the project. Run the `main.py` script:
    ```bash
    python main.py
    ```

---

### For Non-Technical Users:

If you're not familiar with coding or using the command line, follow these steps:

1. **Download the ZIP Folder**:
    - Go to the repository page and click **Download ZIP** (or download the ZIP from this link: `https://github.com/Flockland/IB_Downloader/archive/refs/heads/main.zip`).
    - Once downloaded, **extract** the ZIP file to any folder on your computer.

2. **Activate the Virtual Environment**:

    - Open the folder where you extracted the ZIP file.
    - Find the `activate_venv.bat` file in the folder and double-click it.
    - This will open a **Command Prompt window** and automatically activate the virtual environment. You should see `(venv)` at the beginning of the command prompt.

3. **Run the Program**:
    - In the same Command Prompt window, run the program by typing:
      ```bash
      python main.py
      ```

    - The program will open a window where you can select a folder to download the files and choose which file types to download.

---

## How to Use

### 1. Check Your Version of Chrome

To use this project, you'll need **Chrome** and **Chromedriver**. Make sure you have **Chrome version 133.0.6943.98** or compatible.

**To check your Chrome version:**

1. Open Chrome and click the three dots in the top-right corner.
2. Go to **Help > About Google Chrome**.
3. Your version will be displayed there.

**To update Chrome:**

1. On the same page (Help > About Google Chrome), Chrome will check for updates automatically.
2. If an update is available, it will install and prompt you to restart Chrome.

### 2. Download or Install Chromedriver

You will need the matching version of **Chromedriver**. 
The provided version of ChromeDriver is **Chromedriver** version `133.0.6943.98` (Official Build) (64-bit) (cohort: M133 Rollout).
If you have chrome updated to that version you do not need the following steps.

Follow these steps:

1. Go to the [Chromedriver Downloads page](https://sites.google.com/a/chromium.org/chromedriver/downloads).
2. Download the version that matches your **Chrome version**.
3. **Install Chromedriver** by extracting the downloaded file and placing it in the project directory or setting it in your system’s PATH.

---

## License

MIT License
