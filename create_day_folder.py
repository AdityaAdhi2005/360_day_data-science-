import os
from datetime import datetime

# Your repo folder path
base_path = "360_day_data-science-"

# Count how many DayXXX folders already exist
existing_days = [
    d for d in os.listdir(base_path) if d.startswith("Day") and os.path.isdir(os.path.join(base_path, d))
]

next_day = len(existing_days) + 1
day_folder = f"Day{next_day:03d}"
folder_path = os.path.join(base_path, day_folder)

# Create the new Day folder
os.makedirs(folder_path, exist_ok=True)

# Create a README.md inside it
with open(os.path.join(folder_path, "README.md"), "w") as f:
    f.write(f"# Day {next_day:03d}\n\nWork done on {datetime.now().strftime('%Y-%m-%d')}.")

print(f"✅ Created: {day_folder}")
