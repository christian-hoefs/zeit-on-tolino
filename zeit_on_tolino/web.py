import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Union

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.firefox.webdriver import WebDriver

DOWNLOAD_PATH = tempfile.TemporaryDirectory().name

@dataclass
class Delay:
    small: int = 3
    medium: int = 10
    large: int = 30
    xlarge: int = 200


def get_webdriver(download_path: Union[Path, str] = DOWNLOAD_PATH) -> WebDriver:
    options = ChromeOptions()
    prefs = {"download.default_directory" : f"{download_path}/"}
    options.add_experimental_option("prefs",prefs)
    options.add_argument("--headless")
    options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1")
    webdriver = Chrome(options=options)
    setattr(webdriver, "download_dir_path", str(download_path))
    return webdriver
