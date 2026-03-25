# import csv
# from bs4 import BeautifulSoup
# from playwright.sync_api import sync_playwright
#
# TARGET_URL = "https://www.roboform.com/filling-test-all-fields"
#
#
# def save_to_csv(data, filename="website_structure.csv"):
#     with open(filename, "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(["Field Name"])
#         for label in data:
#             writer.writerow([label])
#     print(f"\n✅ Saved {len(data)} fields to {filename}")
#
#
# def get_preceding_label(field, soup):
#     """Walk backwards through the DOM to find the nearest label-like text."""
#
#     # Strategy 1: <label for="id">
#     field_id = field.get("id")
#     if field_id:
#         tag = soup.find("label", attrs={"for": field_id})
#         if tag:
#             return tag.get_text(strip=True)
#
#     # Strategy 2: Parent <label>
#     parent = field.find_parent("label")
#     if parent:
#         return parent.get_text(strip=True)
#
#     # Strategy 3: Look at the parent container's text nodes / siblings
#     parent = field.parent
#     if parent:
#         # Grab all text that comes BEFORE this field inside the parent
#         text_before = []
#         for sibling in parent.children:
#             if sibling == field:
#                 break
#             if hasattr(sibling, 'get_text'):
#                 t = sibling.get_text(strip=True)
#                 if t:
#                     text_before.append(t)
#             elif isinstance(sibling, str):
#                 t = sibling.strip()
#                 if t:
#                     text_before.append(t)
#         if text_before:
#             return text_before[-1]  # closest text before the field
#
#     # Strategy 4: Go up one more level and try again
#     grandparent = field.parent.parent if field.parent else None
#     if grandparent:
#         for sibling in grandparent.children:
#             if sibling == field.parent:
#                 break
#             if hasattr(sibling, 'get_text'):
#                 t = sibling.get_text(strip=True)
#                 if t:
#                     return t
#
#     # Strategy 5: Fallback to aria-label or placeholder
#     return (
#         field.get("aria-label")
#         or field.get("placeholder")
#         or None
#     )
#
#
# def extract_fields(html):
#     soup = BeautifulSoup(html, "html.parser")
#     seen = set()
#     labels = []
#
#     skip_types = {"hidden", "submit", "button", "reset", "image"}
#
#     for field in soup.find_all(["input", "select", "textarea"]):
#         if field.get("type") in skip_types:
#             continue
#
#         label = get_preceding_label(field, soup)
#
#         if not label or label in seen:
#             continue
#
#         seen.add(label)
#         labels.append(label)
#
#     return labels
#
#
# def main():
#     with sync_playwright() as p:
#         print(f"🌐 Opening: {TARGET_URL}")
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
#         try:
#             page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=30_000)
#             page.wait_for_selector("form, input, select, textarea", timeout=10_000)
#
#             print("🔍 Extracting field names...")
#             data = extract_fields(page.content())
#             save_to_csv(data)
#
#             print("\n📋 Fields found:")
#             for i, label in enumerate(data, 1):
#                 print(f"  {i}. {label}")
#
#         except Exception as e:
#             print(f"❌ Error: {e}")
#         finally:
#             browser.close()
#
#
# if __name__ == "__main__":
#     main()


import csv
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

TARGET_URL = "https://www.digitalunite.com/practice-webform-learners"


def save_to_csv(data, filename="website_structure.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Field Name", "Selector", "Type", "Your Answer"])
        for item in data:
            writer.writerow([item["label"], item["selector"], item["type"], ""])
    print(f"\n✅ Saved {len(data)} fields to {filename}")
    print("📝 Now open website_structure.csv and fill in the 'Your Answer' column!")


def get_preceding_label(field, soup):
    field_id = field.get("id")
    if field_id:
        tag = soup.find("label", attrs={"for": field_id})
        if tag:
            return tag.get_text(strip=True)

    parent = field.find_parent("label")
    if parent:
        return parent.get_text(strip=True)

    parent = field.parent
    if parent:
        text_before = []
        for sibling in parent.children:
            if sibling == field:
                break
            if hasattr(sibling, "get_text"):
                t = sibling.get_text(strip=True)
                if t:
                    text_before.append(t)
            elif isinstance(sibling, str):
                t = sibling.strip()
                if t:
                    text_before.append(t)
        if text_before:
            return text_before[-1]

    grandparent = field.parent.parent if field.parent else None
    if grandparent:
        for sibling in grandparent.children:
            if sibling == field.parent:
                break
            if hasattr(sibling, "get_text"):
                t = sibling.get_text(strip=True)
                if t:
                    return t

    return field.get("aria-label") or field.get("placeholder") or None


def extract_fields(html):
    soup = BeautifulSoup(html, "html.parser")
    seen = set()
    fields = []

    skip_types = {"hidden", "submit", "button", "reset", "image"}

    for field in soup.find_all(["input", "select", "textarea"]):
        if field.get("type") in skip_types:
            continue

        label = get_preceding_label(field, soup)

        if not label or label in seen:
            continue

        seen.add(label)

        field_id = field.get("id")
        field_name = field.get("name")
        field_type = field.name if field.name != "input" else field.get("type", "text")

        fields.append({
            "label": label,
            "selector": f"#{field_id}" if field_id else f"[name='{field_name}']",
            "type": field_type,
        })

    return fields


def main():
    with sync_playwright() as p:
        print(f"🌐 Opening: {TARGET_URL}")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=30_000)
            page.wait_for_selector("form, input, select, textarea", timeout=10_000)

            print("🔍 Extracting field names...")
            data = extract_fields(page.content())
            save_to_csv(data)

            print("\n📋 Fields found:")
            for i, item in enumerate(data, 1):
                print(f"  {i}. {item['label']}")

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            browser.close()


if __name__ == "__main__":
    main()