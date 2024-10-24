import tempfile
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Union

from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager  # Import webdriver_manager for automatic driver installation
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver

DOWNLOAD_PATH = tempfile.TemporaryDirectory().name

user_agents = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
]

@dataclass
class Delay:
    small: int = 3
    medium: int = 10
    large: int = 30
    xlarge: int = 200


def get_webdriver(download_path: Union[Path, str] = DOWNLOAD_PATH, headless: bool = True) -> Chrome:
    """Get the Chrome WebDriver with custom download directory and options"""
    options = ChromeOptions()
    prefs = {"download.default_directory": str(download_path)}
    options.add_experimental_option("prefs", prefs)
    if headless:
        options.add_argument("--headless")
    options.add_argument(f"user-agent={random.choice(user_agents)}")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    service = Service(ChromeDriverManager().install())
    
    webdriver = Chrome(service=service, options=options)
    setattr(webdriver, "download_dir_path", str(download_path))
    return webdriver
