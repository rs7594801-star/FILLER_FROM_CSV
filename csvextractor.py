# # import csv
# # from playwright.sync_api import sync_playwright
# #
# # # ✅ Change this URL for each website
# # TARGET_URL = "https://www.roboform.com/filling-test-all-fields"
# #
# # # ✅ CSV file with your answers filled in
# # CSV_FILE = "website_structure.csv"
# #
# # # ✅ Screenshot file names
# # SCREENSHOT_FILLED = "form_filled.png"
# # SCREENSHOT_SUBMITTED = "form_submitted.png"
# #
# #
# # def load_answers(filename):
# #     fields = []
# #     with open(filename, newline="", encoding="utf-8") as f:
# #         reader = csv.DictReader(f)
# #         for row in reader:
# #             label = row.get("Field Name", "").strip()
# #             selector = row.get("Selector", "").strip()
# #             field_type = row.get("Type", "text").strip()
# #             answer = row.get("Your Answer", "").strip()
# #             if label and answer:
# #                 fields.append({
# #                     "label": label,
# #                     "selector": selector,
# #                     "type": field_type,
# #                     "answer": answer,
# #                 })
# #     return fields
# #
# #
# # def fill_form(page, fields):
# #     filled = 0
# #     skipped = 0
# #
# #     for field in fields:
# #         selector = field["selector"]
# #         answer = field["answer"]
# #         field_type = field["type"]
# #         label = field["label"]
# #
# #         try:
# #             page.wait_for_selector(selector, timeout=3000)
# #             element = page.locator(selector).first
# #
# #             if field_type == "select":
# #                 element.select_option(label=answer)
# #
# #             elif field_type in ("checkbox", "radio"):
# #                 if answer.lower() in ("yes", "true", "1", "on"):
# #                     element.check()
# #
# #             else:
# #                 element.fill(answer)
# #
# #             print(f"  ✅ Filled '{label}' → '{answer}'")
# #             filled += 1
# #
# #         except Exception as e:
# #             print(f"  ⚠️  Skipped '{label}' → {e}")
# #             skipped += 1
# #
# #     return filled, skipped
# #
# #
# # def main():
# #     fields = load_answers(CSV_FILE)
# #
# #     if not fields:
# #         print("❌ No answers found in CSV. Please fill in the 'Your Answer' column first.")
# #         return
# #
# #     print(f"📋 Loaded {len(fields)} fields with answers from {CSV_FILE}")
# #
# #     with sync_playwright() as p:
# #         print(f"\n🌐 Opening: {TARGET_URL}")
# #         browser = p.chromium.launch(headless=False)  # Set True to run in background
# #         page = browser.new_page()
# #
# #         try:
# #             page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=30_000)
# #             page.wait_for_selector("form, input, select, textarea", timeout=10_000)
# #
# #             print("\n✍️  Filling form...\n")
# #             filled, skipped = fill_form(page, fields)
# #
# #             # Screenshot after filling
# #             page.screenshot(path=SCREENSHOT_FILLED, full_page=True)
# #             print(f"\n📸 Screenshot saved → {SCREENSHOT_FILLED}")
# #
# #             # Submit the form
# #             try:
# #                 submit_btn = page.locator("input[type='submit'], button[type='submit']").first
# #                 submit_btn.click()
# #                 page.wait_for_timeout(2000)
# #                 print("🚀 Form submitted successfully!")
# #
# #                 # Screenshot after submit
# #                 page.screenshot(path=SCREENSHOT_SUBMITTED, full_page=True)
# #                 print(f"📸 Post-submit screenshot saved → {SCREENSHOT_SUBMITTED}")
# #
# #             except Exception:
# #                 print("⚠️  No submit button found — form filled but not submitted.")
# #
# #             print(f"\n🎉 Done! Filled: {filled} | Skipped: {skipped}")
# #
# #         except Exception as e:
# #             print(f"❌ Error: {e}")
# #         finally:
# #             browser.close()
# #
# #
# # if __name__ == "__main__":
# #     main()
#
#
# import csv
# from playwright.sync_api import sync_playwright
#
# # ✅ Change this URL for each website
# TARGET_URL = "https://www.roboform.com/filling-test-all-fields"
#
# # ✅ CSV file with your answers filled in
# CSV_FILE = "website_structure.csv"
#
#
# def load_answers(filename):
#     fields = []
#     with open(filename, newline="", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             label = row.get("Field Name", "").strip()
#             selector = row.get("Selector", "").strip()
#             field_type = row.get("Type", "text").strip()
#             answer = row.get("Your Answer", "").strip()
#             if label and answer:
#                 fields.append({
#                     "label": label,
#                     "selector": selector,
#                     "type": field_type,
#                     "answer": answer,
#                 })
#     return fields
#
#
# def fill_form(page, fields):
#     filled = 0
#     skipped = 0
#
#     for field in fields:
#         selector = field["selector"]
#         answer = field["answer"]
#         field_type = field["type"]
#         label = field["label"]
#
#         try:
#             page.wait_for_selector(selector, timeout=3000)
#             element = page.locator(selector).first
#
#             if field_type == "select":
#                 element.select_option(label=answer)
#             elif field_type in ("checkbox", "radio"):
#                 if answer.lower() in ("yes", "true", "1", "on"):
#                     element.check()
#             else:
#                 element.fill(answer)
#
#             print(f"  ✅ Filled '{label}' → '{answer}'")
#             filled += 1
#
#         except Exception as e:
#             print(f"  ⚠️  Skipped '{label}' → {e}")
#             skipped += 1
#
#     return filled, skipped
#
#
# def main():
#     # Ask how many times to fill the form
#     while True:
#         try:
#             times = int(input("🔢 How many times do you want to fill the form? "))
#             if times < 1:
#                 print("❌ Please enter a number greater than 0.")
#             else:
#                 break
#         except ValueError:
#             print("❌ Invalid input. Please enter a whole number.")
#
#     # Load answers from CSV once — same data used every time
#     fields = load_answers(CSV_FILE)
#
#     if not fields:
#         print("❌ No answers found in CSV. Please fill in the 'Your Answer' column first.")
#         return
#
#     print(f"\n📋 Loaded {len(fields)} fields from {CSV_FILE}")
#     print(f"🔁 Will fill the form {times} time(s)\n")
#
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # Set True to run in background
#
#         for i in range(1, times + 1):
#             print(f"\n{'=' * 40}")
#             print(f"📝 Submission {i} of {times}")
#             print(f"{'=' * 40}")
#
#             page = browser.new_page()
#
#             try:
#                 print(f"🌐 Opening: {TARGET_URL}")
#                 page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=30_000)
#                 page.wait_for_selector("form, input, select, textarea", timeout=10_000)
#
#                 print("\n✍️  Filling form...\n")
#                 filled, skipped = fill_form(page, fields)
#
#                 # Screenshot after filling — numbered per run
#                 screenshot_filled = f"form_filled_{i}.png"
#                 page.screenshot(path=screenshot_filled, full_page=True)
#                 print(f"\n📸 Screenshot saved → {screenshot_filled}")
#
#                 # Submit the form
#                 try:
#                     submit_btn = page.locator("input[type='submit'], button[type='submit']").first
#                     submit_btn.click()
#                     page.wait_for_timeout(2000)
#                     print("🚀 Form submitted successfully!")
#
#                     # Screenshot after submit — numbered per run
#                     screenshot_submitted = f"form_submitted_{i}.png"
#                     page.screenshot(path=screenshot_submitted, full_page=True)
#                     print(f"📸 Post-submit screenshot saved → {screenshot_submitted}")
#
#                 except Exception:
#                     print("⚠️  No submit button found — form filled but not submitted.")
#
#                 print(f"\n✅ Run {i} done! Filled: {filled} | Skipped: {skipped}")
#
#             except Exception as e:
#                 print(f"❌ Error on run {i}: {e}")
#
#             finally:
#                 page.close()  # Close page after each run, reopen fresh next time
#
#         browser.close()
#         print(f"\n🎉 All {times} submissions completed!")
#
#
# if __name__ == "__main__":
#     main()


import csv
from playwright.sync_api import sync_playwright

# ✅ Change this URL for each website
TARGET_URL = "https://www.digitalunite.com/practice-webform-learners"

# ✅ CSV file with your answers filled in
CSV_FILE = "website_structure.csv"


def load_answers(filename):
    fields = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            label = row.get("Field Name", "").strip()
            selector = row.get("Selector", "").strip()
            field_type = row.get("Type", "text").strip()
            answer = row.get("Your Answer", "").strip()
            if label and answer:
                fields.append({
                    "label": label,
                    "selector": selector,
                    "type": field_type,
                    "answer": answer,
                })
    return fields


def fill_form(page, fields):
    filled = 0
    skipped = 0

    for field in fields:
        selector = field["selector"]
        answer = field["answer"]
        field_type = field["type"]
        label = field["label"]

        try:
            page.wait_for_selector(selector, timeout=3000)
            element = page.locator(selector).first

            if field_type == "select":
                element.select_option(label=answer)
            elif field_type in ("checkbox", "radio"):
                if answer.lower() in ("yes", "true", "1", "on"):
                    element.check()
            else:
                element.fill(answer)

            print(f"  ✅ Filled '{label}' → '{answer}'")
            filled += 1

        except Exception as e:
            print(f"  ⚠️  Skipped '{label}' → {e}")
            skipped += 1

    return filled, skipped


def main():
    # Ask how many times to fill the form
    while True:
        try:
            times = int(input("🔢 How many times do you want to fill the form? "))
            if times < 1:
                print("❌ Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

    # Load answers from CSV once — same data used every time
    fields = load_answers(CSV_FILE)

    if not fields:
        print("❌ No answers found in CSV. Please fill in the 'Your Answer' column first.")
        return

    print(f"\n📋 Loaded {len(fields)} fields from {CSV_FILE}")
    print(f"🔁 Will fill the form {times} time(s)\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set True to run in background

        for i in range(1, times + 1):
            print(f"\n{'=' * 40}")
            print(f"📝 Submission {i} of {times}")
            print(f"{'=' * 40}")

            page = browser.new_page()

            try:
                print(f"🌐 Opening: {TARGET_URL}")
                page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=30_000)
                page.wait_for_selector("form, input, select, textarea", timeout=10_000)

                print("\n✍️  Filling form...\n")
                filled, skipped = fill_form(page, fields)

                # Screenshot after filling — numbered per run
                screenshot_filled = f"form_filled_{i}.png"
                page.screenshot(path=screenshot_filled, full_page=True)
                print(f"\n📸 Screenshot saved → {screenshot_filled}")

                # Submit the form
                try:
                    submit_btn = page.locator("input[type='submit'], button[type='submit']").first
                    submit_btn.click()
                    page.wait_for_timeout(2000)
                    print("🚀 Form submitted successfully!")

                    # Screenshot after submit — numbered per run
                    screenshot_submitted = f"form_submitted_{i}.png"
                    page.screenshot(path=screenshot_submitted, full_page=True)
                    print(f"📸 Post-submit screenshot saved → {screenshot_submitted}")

                except Exception:
                    print("⚠️  No submit button found — form filled but not submitted.")

                print(f"\n✅ Run {i} done! Filled: {filled} | Skipped: {skipped}")

            except Exception as e:
                print(f"❌ Error on run {i}: {e}")

            finally:
                page.close()  # Close page after each run, reopen fresh next time

        browser.close()
        print(f"\n🎉 All {times} submissions completed!")


if __name__ == "__main__":
    main()