import unittest
import os
import shutil
from subtitle_renamer import rename_and_move_subtitles  # Assuming your script is saved as subtitle_renamer.py

class TestSubtitleRenamer(unittest.TestCase):

    def setUp(self):
        # Create a mock directory structure
        self.test_dir = 'test_media'
        os.makedirs(self.test_dir, exist_ok=True)

        # Season folder with Subs folder and episode subfolders
        season_folder = os.path.join(self.test_dir, 'Season 1')
        os.makedirs(season_folder, exist_ok=True)
        
        subs_folder = os.path.join(season_folder, 'Subs')
        os.makedirs(subs_folder, exist_ok=True)
        
        # Create episode folders with subtitle files
        episode_folder_1 = os.path.join(subs_folder, 'Show.S01E01')
        os.makedirs(episode_folder_1, exist_ok=True)
        with open(os.path.join(episode_folder_1, '2_eng.srt'), 'w') as f:
            f.write("English Subtitle")

        episode_folder_2 = os.path.join(subs_folder, 'Show.S01E02')
        os.makedirs(episode_folder_2, exist_ok=True)
        with open(os.path.join(episode_folder_2, '2_fra.srt'), 'w') as f:
            f.write("French Subtitle")

        # Create an episode file to compare against
        with open(os.path.join(season_folder, 'Show.S01E01.mp4'), 'w') as f:
            f.write("Episode 1")
        with open(os.path.join(season_folder, 'Show.S01E02.mp4'), 'w') as f:
            f.write("Episode 2")

    def tearDown(self):
        # Clean up after tests
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_basic_renaming_and_moving(self):
        # Run the renaming and moving function
        rename_and_move_subtitles(self.test_dir)
        
        # Check if the subtitles were moved and renamed correctly
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Season 1', 'Show.S01E01.en.srt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Season 1', 'Show.S01E02.fr.srt')))

    def test_handling_no_subs_folder(self):
        # Remove the Subs folder
        shutil.rmtree(os.path.join(self.test_dir, 'Season 1', 'Subs'))
        
        # Run the function, it should handle this case gracefully
        rename_and_move_subtitles(self.test_dir)

        # Ensure no subtitles exist (because there were none to process)
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, 'Season 1', 'Show.S01E01.en.srt')))

    def test_handling_empty_subs_folder(self):
        # Clear the Subs folder content
        shutil.rmtree(os.path.join(self.test_dir, 'Season 1', 'Subs'))
        os.makedirs(os.path.join(self.test_dir, 'Season 1', 'Subs'))

        # Run the function, it should handle this case without errors
        rename_and_move_subtitles(self.test_dir)
        
        # Ensure no subtitles exist (because the Subs folder was empty)
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, 'Season 1', 'Show.S01E01.en.srt')))

    def test_incorrect_file_naming(self):
        # Rename the subtitle file to something unexpected
        incorrect_sub_path = os.path.join(self.test_dir, 'Season 1', 'Subs', 'Show.S01E01', 'wrongname.srt')
        os.rename(os.path.join(self.test_dir, 'Season 1', 'Subs', 'Show.S01E01', '2_eng.srt'), incorrect_sub_path)
        
        # Run the function
        rename_and_move_subtitles(self.test_dir)

        # Check that the incorrectly named subtitle file has been renamed to use the default 'en' language code
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Season 1', 'Show.S01E01.en.srt')))
        # Verify the original incorrect file no longer exists
        self.assertFalse(os.path.exists(incorrect_sub_path))

    def test_multiple_language_support(self):
        # Add more subtitles with different languages
        episode_folder_1 = os.path.join(self.test_dir, 'Season 1', 'Subs', 'Show.S01E01')
        with open(os.path.join(episode_folder_1, '2_spa.srt'), 'w') as f:
            f.write("Spanish Subtitle")
        with open(os.path.join(episode_folder_1, '2_deu.srt'), 'w') as f:
            f.write("German Subtitle")

        # Run the function
        rename_and_move_subtitles(self.test_dir)
        
        # Check if all subtitles were moved and renamed correctly
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Season 1', 'Show.S01E01.en.srt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Season 1', 'Show.S01E01.es.srt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Season 1', 'Show.S01E01.de.srt')))

if __name__ == '__main__':
    unittest.main()