import unittest
import os

from powertab import *

class TestPowerTabReading(unittest.TestCase):
  def assert_song_info_field(self, field, expected):
    self.assertEqual(self.power_tab.song_info[field], expected)

  def setUp(self):
    self.resource_folder = f"{os.path.dirname(__file__)}/resource"
    
  def test_version(self):
    self.assertEqual(self.power_tab.get_version(), 'ptab-4')

  def test_get_song_info_public_release(self):
    self.power_tab = PowerTab(os.path.abspath(f"{self.resource_folder}/test-song-public-release.ptb"))

    self.assert_song_info_field('name', 'Test Title')
    self.assert_song_info_field('artist', 'Test Artist')
    self.assert_song_info_field('release_type', 0) # Public Release
    self.assert_song_info_field('album_type', 0) # single

    self.assert_song_info_field('album', 'Test Album')
    self.assert_song_info_field('year', 2021)
    self.assert_song_info_field('is_live_recording', True)

    self.assert_song_info_field('music_by', 'Test Music By')
    self.assert_song_info_field('guitar_transcriber', 'Test Transcribed By')
    self.assert_song_info_field('bass_transcriber', 'Test Bass Transcribed By')
    self.assert_song_info_field('copyright', 'Test Copyright')
    self.assert_song_info_field('lyrics', 'Test Lyrics')
    self.assert_song_info_field('guitar_instructions', 'Test Guitar Notes')
    self.assert_song_info_field('bass_instructions', 'Test Bass Notes')

  def test_get_song_info_bootleg(self):
    pass

if __name__ == '__main__':
  unittest.main()