%%time

import json
import time
import base64
import traceback
from pathlib import Path

from openai import OpenAI


# =====================================================
# CONFIG
# =====================================================

API_KEY = "xxxxx"

BASE_URL = "https://xxxxx-foundry-tr-resource.services.ai.azure.com/openai/v1"

MODEL_NAME = "gpt-4o-apparo"

FRAMES_DIR = r"C:\Users\ATA24292\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\frames"

OUTPUT_DIR = r"C:\Users\ATA24292\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\knowledge"

FAILED_DIR = r"C:\Users\ATA24292\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\failed"

MAX_RETRIES = 3

REQUEST_TIMEOUT = 180


# =====================================================
# CLIENT
# =====================================================

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
    timeout=REQUEST_TIMEOUT
)


# =====================================================
# PROMPT
# =====================================================

PROMPT = """
You are a software reverse engineering analyst.

Analyze the screenshot and extract ONLY information that is directly visible in the user interface.

DO NOT guess:
- backend architecture
- database schema
- API endpoints
- implementation details
- hidden business logic
- technical stack

DO NOT invent entities, fields, workflows or rules that are not clearly visible.

Your only goal is to describe the visible user interface.

Return ONLY valid JSON.

Schema:

{
  "screen_title": "",
  "screen_type": "",
  "screen_description": "",

  "visible_text": [],

  "navigation_elements": [
    {
      "label": "",
      "type": ""
    }
  ],

  "buttons": [
    {
      "label": "",
      "state": ""
    }
  ],

  "links": [],

  "tabs": [],

  "checkboxes": [
    {
      "label": "",
      "checked": false
    }
  ],

  "radio_buttons": [],

  "dropdowns": [
    {
      "label": "",
      "selected_value": ""
    }
  ],

  "input_fields": [
    {
      "label": "",
      "value": "",
      "read_only": false
    }
  ],

  "tables": [
    {
      "name": "",
      "columns": []
    }
  ],

  "filters": [],

  "dialogs": [],

  "notifications": [],

  "images": [],

  "icons": [],

  "observed_features": [],

  "user_can_do": [],

  "screen_observations": []
}

Rules:

- Capture ALL visible labels.
- Preserve original wording whenever possible.
- Capture every visible checkbox label.
- Capture every visible menu item.
- Capture every visible table column.
- Record only what is visible.
- If something is unclear use "unknown".
- Do not infer backend behavior.
- Do not infer APIs.
- Do not infer database tables.
- Do not infer business rules.
- Do not wrap output in markdown.
- Do not use code fences.

Return JSON only.
"""


# =====================================================
# HELPERS
# =====================================================

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(
            f.read()
        ).decode()


def clean_json_output(text):

    if text is None:
        raise Exception("Model returned None")

    text = text.strip()

    if text.startswith("```json"):
        text = text[7:]

    if text.endswith("```"):
        text = text[:-3]

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text.strip()


def analyze_image(image_path):

    image_b64 = encode_image(image_path)

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": PROMPT
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{image_b64}"
                    }
                ]
            }
        ]
    )

    return response.output_text


def save_json(output_file, obj):

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            obj,
            f,
            indent=2,
            ensure_ascii=False
        )


# =====================================================
# FOLDERS
# =====================================================

Path(OUTPUT_DIR).mkdir(
    exist_ok=True
)

Path(FAILED_DIR).mkdir(
    exist_ok=True
)


# =====================================================
# LOAD FRAMES
# =====================================================

frames = sorted([
    p for p in Path(FRAMES_DIR).glob("*")
    if p.suffix.lower() in [".jpg", ".jpeg", ".png"]
])

print(f"\nFound {len(frames)} frames\n")


# =====================================================
# PROCESS
# =====================================================

processed = 0
failed = 0


for frame_path in frames:

    json_path = (
        Path(OUTPUT_DIR)
        / f"{frame_path.stem}.json"
    )

    if json_path.exists():

        print(
            f"[SKIP] {frame_path.name}"
        )

        continue

    print(
        f"\nProcessing: {frame_path.name}"
    )

    success = False

    for attempt in range(
        1,
        MAX_RETRIES + 1
    ):

        raw_output = None

        try:

            raw_output = analyze_image(
                str(frame_path)
            )

            raw_output = clean_json_output(
                raw_output
            )

            parsed = json.loads(
                raw_output
            )

            save_json(
                json_path,
                parsed
            )

            processed += 1
            success = True

            print(
                f"[OK] {frame_path.name}"
            )

            break

        except json.JSONDecodeError:

            print(
                f"[JSON ERROR] {frame_path.name}"
            )

            if raw_output:
                print(raw_output[:3000])

            time.sleep(3)

        except Exception as e:

            print(
                f"[RETRY {attempt}] {frame_path.name}"
            )

            print(
                f"{type(e).__name__}: {str(e)}"
            )

            traceback.print_exc()

            if raw_output:
                print("\nRAW RESPONSE:")
                print(raw_output[:3000])

            time.sleep(5)

    if not success:

        failed += 1

        failed_file = (
            Path(FAILED_DIR)
            / f"{frame_path.stem}.txt"
        )

        with open(
            failed_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                f"Failed: {frame_path.name}\n"
            )

        print(
            f"[FAILED] {frame_path.name}"
        )


# =====================================================
# SUMMARY
# =====================================================

print("\n")
print("=" * 50)
print("PROCESS FINISHED")
print("=" * 50)

print(
    f"Processed : {processed}"
)

print(
    f"Failed    : {failed}"
)

print(
    f"Output    : {OUTPUT_DIR}"
)
