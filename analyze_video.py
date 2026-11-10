import os
import json
import time
import base64
from pathlib import Path

from openai import OpenAI


# =====================================================
# CONFIG
# =====================================================

API_KEY = "xxxxxxx"

BASE_URL = (
    "https://xxxxxx-foundry-tr-resource.services.ai.azure.com/openai/v1"
)

MODEL_NAME = "gpt-4o-apparo"

FRAMES_DIR = r"C:\Users\ATA24292\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\frames"

OUTPUT_DIR = r"C:\Users\ATA24292\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\knowledge"

FAILED_DIR = r"C:\Users\ATA24292\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\failed"

MAX_RETRIES = 3


# =====================================================
# CLIENT
# =====================================================

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


# =====================================================
# PROMPT
# =====================================================

PROMPT = """
You are a senior software architect and reverse engineering expert.

Analyze the application screenshot.

Your goal is to extract information that will help another AI recreate the application.

Return ONLY valid JSON.

Schema:

{
  "screen_name": "",
  "screen_purpose": "",

  "ui_components": [
    {
      "type": "",
      "label": "",
      "required": false,
      "description": ""
    }
  ],

  "navigation": {
    "menus": [],
    "breadcrumbs": [],
    "next_possible_screens": []
  },

  "actions": [
    {
      "name": "",
      "purpose": ""
    }
  ],

  "business_entities": [],

  "business_rules": [],

  "workflow_steps": [],

  "database_candidates": [
    {
      "entity": "",
      "attributes": []
    }
  ],

  "api_candidates": [
    {
      "endpoint_purpose": "",
      "possible_method": ""
    }
  ],

  "developer_notes": []
}

Important:

- Infer business meaning if possible.
- Identify forms, grids, filters and workflows.
- Guess CRUD operations when visible.
- Return ONLY JSON.
"""


# =====================================================
# HELPERS
# =====================================================

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(
            f.read()
        ).decode()


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
                        "image_url":
                            f"data:image/jpeg;base64,{image_b64}"
                    }
                ]
            }
        ]
    )

    return response.output_text.strip()


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

Path(OUTPUT_DIR).mkdir(exist_ok=True)

Path(FAILED_DIR).mkdir(exist_ok=True)


# =====================================================
# LOAD FRAMES
# =====================================================

frames = sorted([
    p for p in Path(FRAMES_DIR).glob("*")
    if p.suffix.lower() in [".jpg", ".jpeg", ".png"]
])

print(f"\nFound {len(frames)} frames\n")


# =====================================================
# LOOP
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

    for attempt in range(MAX_RETRIES):

        try:

            raw_output = analyze_image(
                str(frame_path)
            )

            
            raw_output = raw_output.strip()

            raw_output = raw_output.replace(
                "```json", ""
            )
            
            raw_output = raw_output.replace(
                "```", ""
            )
            
            raw_output = raw_output.strip()
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

        except Exception as e:
        
            print(
                f"[Retry {attempt+1}] "
                f"{frame_path.name}"
            )
        
            print(str(e))
        
            try:
                print("RAW RESPONSE:")
                print(raw_output[:5000])
            except:
                pass

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
                f"Failed: {frame_path.name}"
            )

        print(
            f"[FAILED] {frame_path.name}"
        )


# =====================================================
# SUMMARY
# =====================================================

print("\n")
print("=" * 40)
print("PROCESS FINISHED")
print("=" * 40)

print(f"Processed : {processed}")
print(f"Failed    : {failed}")

print(
    f"JSON files written to: {OUTPUT_DIR}"
)
