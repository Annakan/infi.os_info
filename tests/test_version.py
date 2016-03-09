# coding=utf8
from infi import unittest
from os import path
from infi.os_info import get_version_from_git, get_version_from_file, shorten_version_string


class VersionTestCase(unittest.TestCase):

    def test_git(self):
        git_version = shorten_version_string(get_version_from_git())
        git_versionlist = git_version.split('.')
        self.assertEquals(len(git_versionlist), 4)
        self.assertGreater(int(git_versionlist[0]), 0)

    def test_file(self):
        current_path = path.dirname(path.realpath(__file__))
        filepath = path.abspath(path.join(current_path, '..', 'src', 'infi', 'os_info', '__version__.py'))
        file_version = shorten_version_string(get_version_from_file(filepath))
        file_version_list = file_version.split('.')
        self.assertEquals(len(file_version_list), 3)

    def test_shortening(self):
        self.assertEquals(shorten_version_string("1.2.3"), "1.2.3")
        self.assertEquals(shorten_version_string("1.2.3.post1.g1234567"), "1.2.3.1")
        self.assertEquals(shorten_version_string("1.2.3.post1+g1234567"), "1.2.3.1")
        self.assertEquals(shorten_version_string("1.2.2.post1+g1234567"), "1.2.2.1")
