import json
from pathlib import Path
from collections import defaultdict


# =====================================================
# CONFIG
# =====================================================

KNOWLEDGE_DIR = r"C:\Users\ATA24292\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\knowledge"

OUTPUT_FILE = r"C:\Users\ATA24292\Downloads\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\application_blueprint.md"


# =====================================================
# LOAD FILES
# =====================================================

json_files = sorted(
    Path(KNOWLEDGE_DIR).glob("*.json")
)

print(f"Found {len(json_files)} json files")


# =====================================================
# COLLECT SCREENS
# =====================================================

screens = {}

all_features = set()
all_navigation = set()
all_buttons = set()
all_checkboxes = set()
all_tabs = set()
all_user_actions = set()


for file in json_files:

    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

    except Exception as e:

        print(f"Cannot read {file.name}")
        continue

    screen_title = (
        data.get("screen_title")
        or "Unknown Screen"
    )

    if screen_title not in screens:

        screens[screen_title] = {
            "type": data.get(
                "screen_type",
                ""
            ),
            "description": data.get(
                "screen_description",
                ""
            ),
            "navigation": set(),
            "buttons": set(),
            "checkboxes": set(),
            "tabs": set(),
            "visible_text": set(),
            "features": set(),
            "actions": set()
        }

    screen = screens[screen_title]

    # visible text

    for item in data.get(
        "visible_text", []
    ):
        if item:
            screen["visible_text"].add(
                str(item)
            )

    # navigation

    for nav in data.get(
        "navigation_elements", []
    ):

        label = nav.get(
            "label", ""
        )

        if label:

            screen["navigation"].add(
                label
            )

            all_navigation.add(
                label
            )

    # buttons

    for btn in data.get(
        "buttons", []
    ):

        label = btn.get(
            "label", ""
        )

        if label:

            screen["buttons"].add(
                label
            )

            all_buttons.add(
                label
            )

    # tabs

    for tab in data.get(
        "tabs", []
    ):

        if isinstance(tab, str):

            screen["tabs"].add(tab)
            all_tabs.add(tab)

    # checkboxes

    for cb in data.get(
        "checkboxes",
        []
    ):

        label = cb.get(
            "label",
            ""
        )

        if label:

            screen["checkboxes"].add(
                label
            )

            all_checkboxes.add(
                label
            )

    # features

    for feat in data.get(
        "observed_features",
        []
    ):

        screen["features"].add(
            feat
        )

        all_features.add(
            feat
        )

    # user actions

    for act in data.get(
        "user_can_do",
        []
    ):

        screen["actions"].add(
            act
        )

        all_user_actions.add(
            act
        )


# =====================================================
# GENERATE MARKDOWN
# =====================================================

md = []

md.append("# Application Blueprint")
md.append("")
md.append(
    "Generated from video frame analysis."
)
md.append("")

md.append("---")
md.append("")

md.append("# Screen Catalog")
md.append("")

for name, screen in screens.items():

    md.append(
        f"## {name}"
    )

    md.append("")

    if screen["type"]:
        md.append(
            f"**Type:** {screen['type']}"
        )
        md.append("")

    if screen["description"]:
        md.append(
            f"**Description:** {screen['description']}"
        )
        md.append("")

    if screen["navigation"]:

        md.append(
            "### Navigation Elements"
        )

        for item in sorted(
            screen["navigation"]
        ):
            md.append(
                f"- {item}"
            )

        md.append("")

    if screen["buttons"]:

        md.append(
            "### Buttons"
        )

        for item in sorted(
            screen["buttons"]
        ):
            md.append(
                f"- {item}"
            )

        md.append("")

    if screen["checkboxes"]:

        md.append(
            "### Checkboxes"
        )

        for item in sorted(
            screen["checkboxes"]
        ):
            md.append(
                f"- {item}"
            )

        md.append("")

    if screen["tabs"]:

        md.append(
            "### Tabs"
        )

        for item in sorted(
            screen["tabs"]
        ):
            md.append(
                f"- {item}"
            )

        md.append("")

    if screen["visible_text"]:

        md.append(
            "### Visible Text"
        )

        for item in sorted(
            screen["visible_text"]
        ):
            md.append(
                f"- {item}"
            )

        md.append("")

    if screen["features"]:

        md.append(
            "### Observed Features"
        )

        for item in sorted(
            screen["features"]
        ):
            md.append(
                f"- {item}"
            )

        md.append("")

    if screen["actions"]:

        md.append(
            "### User Can Do"
        )

        for item in sorted(
            screen["actions"]
        ):
            md.append(
                f"- {item}"
            )

        md.append("")

    md.append("---")
    md.append("")


# =====================================================
# SUMMARY
# =====================================================

md.append("")
md.append("# Global Feature Inventory")
md.append("")

for item in sorted(
    all_features
):
    md.append(
        f"- {item}"
    )

md.append("")
md.append("# Navigation Inventory")
md.append("")

for item in sorted(
    all_navigation
):
    md.append(
        f"- {item}"
    )

md.append("")
md.append("# Button Inventory")
md.append("")

for item in sorted(
    all_buttons
):
    md.append(
        f"- {item}"
    )

md.append("")
md.append("# Checkbox Inventory")
md.append("")

for item in sorted(
    all_checkboxes
):
    md.append(
        f"- {item}"
    )

md.append("")
md.append("# User Actions")
md.append("")

for item in sorted(
    all_user_actions
):
    md.append(
        f"- {item}"
    )


# =====================================================
# SAVE
# =====================================================

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "\n".join(md)
    )

print()
print("=" * 40)
print("DONE")
print("=" * 40)
print(OUTPUT_FILE)
