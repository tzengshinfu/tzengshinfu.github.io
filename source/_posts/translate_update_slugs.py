"""
translate_update_slugs.py

Reads rename_mapping.json, opens Chrome, visits Google Translate for each title,
extracts the translated English text, converts it to a slug-like string,
writes that into the object's "slug" property, and saves the JSON file.

Requirements:
  pip install selenium webdriver-manager

Usage:
  python translate_update_slugs.py

Notes:
  - The script uses webdriver-manager to auto-download the matching chromedriver.
  - If you want to use an existing Chrome installation, ensure Chrome is up-to-date.
"""

import json
import time
import random
import urllib.parse
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

JSON_PATH = Path(r"R:\\tzengshinfu.github.io\\source\\_posts\\rename_mapping.json")


def slugify_from_text(text):
    if not text:
        return ""
    s = text.strip().lower()
    # remove characters except letters, numbers, spaces and hyphen
    import re

    s = re.sub(r"[^a-z0-9\s-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    # keep up to first 5 words
    parts = s.split()
    parts = parts[:100]
    return "-".join(parts)


def main():
    if not JSON_PATH.exists():
        print(f"JSON file not found: {JSON_PATH}")
        return

    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print("Unexpected JSON structure: expected a list of objects.")
        return

    chrome_options = Options()
    # show browser so user can observe; change to True for headless
    chrome_options.headless = False
    chrome_options.add_argument("--start-maximized")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except WebDriverException as e:
        print("Failed to start Chrome webdriver:", e)
        return

    wait = WebDriverWait(driver, 20)

    try:
        for idx, obj in enumerate(data, start=1):
            slug = obj.get("slug", "")
            if slug:
                continue

            title = obj.get("title", "")
            if not title:
                print(f"[{idx}/{len(data)}] empty title, skipping (old={obj.get('old')})")
                continue

            url = "https://translate.google.com/?sl=auto&tl=en&text=" + urllib.parse.quote(title) + "&op=translate"
            print(f"[{idx}/{len(data)}] Navigating to translate: {title}")
            try:
                driver.get(url)
            except WebDriverException as e:
                print("  navigation failed:", e)
                continue

            translated = None
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[jsname="W297wb"]')))
                elem = driver.find_element(By.CSS_SELECTOR, 'span[jsname="W297wb"]')
                translated = elem.text.strip()
            except TimeoutException:
                print("  timeout waiting for translation element")
                # try alternative selector that sometimes holds translation
                try:
                    alt = driver.find_element(By.CSS_SELECTOR, "div.result-shield-container span")
                    translated = alt.text.strip()
                except Exception:
                    translated = None

            if translated:
                slug = slugify_from_text(translated)
                obj["slug"] = slug
                print(f'  -> translated: "{translated}" => slug: "{slug}"')
            else:
                print("  -> no translation extracted, leaving slug unchanged")

            delay = random.uniform(5, 10)
            print(f"  waiting {delay:.2f}s before next")
            time.sleep(delay)
    finally:
        try:
            driver.quit()
        except Exception:
            pass

    # write back
    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Saved updated JSON to", JSON_PATH)


if __name__ == "__main__":
    main()
