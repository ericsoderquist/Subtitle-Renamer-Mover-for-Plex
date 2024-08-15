import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_and_move_subtitles(root_folder):
    # Map three-letter codes to two-letter ISO 639-1 codes
    language_mapping = {
        "eng": "en",  # English
        "fra": "fr",  # French
        "deu": "de",  # German
        "spa": "es",  # Spanish
        "ita": "it",  # Italian
        "por": "pt",  # Portuguese
        "rus": "ru",  # Russian
        "zho": "zh",  # Chinese
        "jpn": "ja",  # Japanese
        "kor": "ko",  # Korean
        "nld": "nl",  # Dutch
        "swe": "sv",  # Swedish
        "dan": "da",  # Danish
        "nor": "no",  # Norwegian
        "fin": "fi",  # Finnish
        "hun": "hu",  # Hungarian
        "pol": "pl",  # Polish
        "ces": "cs",  # Czech
        "tur": "tr",  # Turkish
        "ara": "ar",  # Arabic
        "heb": "he",  # Hebrew
        "tha": "th",  # Thai
        "ukr": "uk",  # Ukrainian
        "vie": "vi",  # Vietnamese
        "hin": "hi",  # Hindi
        "ben": "bn",  # Bengali
        "tam": "ta",  # Tamil
        "tel": "te",  # Telugu
        "ind": "id",  # Indonesian
        "msa": "ms",  # Malay
        "bul": "bg",  # Bulgarian
        "hrv": "hr",  # Croatian
        "srp": "sr",  # Serbian
        "slv": "sl",  # Slovenian
        "ell": "el",  # Greek
        "ron": "ro",  # Romanian
        "isl": "is",  # Icelandic
        "lav": "lv",  # Latvian
        "lit": "lt",  # Lithuanian
        "est": "et",  # Estonian
        "fil": "tl",  # Filipino
        "slk": "sk",  # Slovak
        "cat": "ca",  # Catalan
        "eus": "eu",  # Basque
        "glg": "gl",  # Galician
    }

    # Iterate over each season folder
    for season_folder in os.listdir(root_folder):
        season_path = os.path.join(root_folder, season_folder)
        if os.path.isdir(season_path):
            # Look inside the 'Subs' folder in the season folder
            subs_folder = os.path.join(season_path, 'Subs')
            if os.path.exists(subs_folder):
                # Iterate over each episode folder inside 'Subs'
                for episode_sub_folder in os.listdir(subs_folder):
                    episode_sub_path = os.path.join(subs_folder, episode_sub_folder)
                    if os.path.isdir(episode_sub_path):
                        # Iterate over each subtitle file inside the episode sub folder
                        for sub_file in os.listdir(episode_sub_path):
                            if sub_file.endswith('.srt'):
                                old_sub_path = os.path.join(episode_sub_path, sub_file)
                                # Extract language code from the subtitle file name
                                base_name = sub_file.split('_')[0]  # e.g., "2_eng" -> "eng"
                                language_code = base_name.split('.')[0]  # in case the base name has a period
                                # Convert three-letter code to two-letter code if necessary
                                language_code = language_mapping.get(language_code, language_code)
                                # Construct the new subtitle name based on the episode folder name and language code
                                new_sub_name = f"{episode_sub_folder}.{language_code}.srt"
                                new_sub_path = os.path.join(season_path, new_sub_name)
                                # Rename the subtitle file and move it to the season folder
                                shutil.move(old_sub_path, new_sub_path)
                                print(f"Moved and renamed '{old_sub_path}' to '{new_sub_path}'")
    messagebox.showinfo("Done", "Subtitle renaming and moving completed successfully!")

def select_folder():
    root_folder = filedialog.askdirectory()
    if root_folder:
        rename_and_move_subtitles(root_folder)

# Create the main window
root = tk.Tk()
root.title("Subtitle Renamer & Mover")

# Create and place the 'Select Folder' button
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

