### README: Subtitle Renamer & Mover for Plex

---

### Introduction

Welcome to the **Subtitle Renamer & Mover** tool! This handy tool is designed to help you organize your media files, especially when you're adding content to Plex Media Server. Plex requires subtitles to be in a specific format: the subtitle files must be in the same folder as the video files, and they need to be named exactly like the corresponding episode file, with the addition of a language code (e.g., `.en.srt` for English subtitles).

If you have a collection of media files where the subtitles are located in a separate subfolder and are not named correctly, this tool will make your life much easier by automatically renaming and moving the subtitle files to the correct location.

---

### What Does This Tool Do?

- **Renames Subtitles**: It renames subtitle files so they match the corresponding episode file name, followed by the correct language code.
- **Moves Subtitles**: It moves the renamed subtitle files from their subfolder to the main folder where the video files are located.
- **Supports Multiple Languages**: It automatically detects and renames subtitles in many different languages.

---

### System Requirements

- **Python**: You’ll need to have Python installed on your computer to run this tool. You can download it from the official [Python website](https://www.python.org/downloads/).

---

### How to Use This Tool

1. **Download the Script**: Save the script file as `subtitle_renamer.py` on your computer.

2. **Prepare Your Files**:
   - Make sure your media files are organized by seasons in separate folders (e.g., `Season 1`, `Season 2`, etc.).
   - Inside each season folder, you should have a `Subs` folder where the subtitle files are stored, with separate folders for each episode's subtitles.

3. **Install Python**:
   - If you don’t already have Python installed, download and install it from [here](https://www.python.org/downloads/).
   - Ensure Python is added to your system’s PATH during installation.

4. **Run the Script**:
   - Open a terminal (Command Prompt on Windows, Terminal on Mac, or Linux).
   - Navigate to the directory where you saved the script using the `cd` command. For example:
     ```
     cd path\to\your\script
     ```
   - Run the script by typing:
     ```
     python subtitle_renamer.py
     ```
   - A small window will open with a "Select Folder" button.

5. **Select Your Media Folder**:
   - Click the "Select Folder" button.
   - Navigate to the main folder where your media files are stored (the one containing all the season folders).
   - Click "OK" to start the process.

6. **Let the Tool Work**:
   - The tool will automatically rename and move the subtitle files for you.
   - Once it’s done, you’ll see a confirmation message.

7. **Check Your Files**:
   - Verify that the subtitles have been moved and renamed correctly in each season folder.
   - Your media files are now ready to be added to Plex with correctly formatted subtitles!

---

### Example

Let’s say you have the following structure:

```
Show Name
│
├── Season 1
│   ├── Show.S01E01.mp4
│   ├── Show.S01E02.mp4
│   └── Subs
│       ├── Show.S01E01
│       │   └── 2_eng.srt
│       └── Show.S01E02
│           └── 2_fra.srt
```

After running the script, it will be reorganized to:

```
Show Name
│
├── Season 1
│   ├── Show.S01E01.mp4
│   ├── Show.S01E01.en.srt
│   ├── Show.S01E02.mp4
│   ├── Show.S01E02.fr.srt
│   └── Subs (optional: this can be deleted after processing)
```

---

### Language Support

This tool supports a wide range of languages. Here are some examples of the supported language codes:

- **English**: `.en.srt`
- **French**: `.fr.srt`
- **Spanish**: `.es.srt`
- **German**: `.de.srt`
- **Chinese**: `.zh.srt`
- **Japanese**: `.ja.srt`
- **Korean**: `.ko.srt`
- **Russian**: `.ru.srt`
- **Arabic**: `.ar.srt`
- **Portuguese**: `.pt.srt`

And many more! The script automatically detects the language based on the file name and renames it accordingly.

---

### Troubleshooting

- **Python Not Found**: If you get an error that Python isn’t recognized, make sure it’s properly installed and added to your PATH.
- **Incorrect File Names**: Ensure your subtitles follow the expected naming convention with a three-letter language code (e.g., `2_eng.srt`). If the naming convention is different, the script might need adjustments.
- **Folders Not Selected**: If nothing happens after you select the folder, make sure you selected the correct main folder that contains all the season folders.

---

### Contributing

If you’re comfortable with coding and want to contribute to this project, feel free to make improvements or add new features! You can edit the Python script directly and add additional language support or new functionalities.

---

### License

This tool is provided as-is without any warranties. Use it at your own risk. (MIT License)

---

Thank you for using the **Subtitle Renamer & Mover** tool! We hope it makes managing your media library with Plex a little easier. Enjoy your well-organized subtitles! 😊
