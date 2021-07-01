import unittest
from APISpotifyEx import (get_access_token, 
                          get_playlist, 
                          parse_playlist_to_dataframe)


class TestFileName(unittest.TestCase):
    def test_get_access_token(self):
        # Constants
        myCID = '2b1a105e0bf94d69924ed5789171693f'
        mySID = '487346bb76a54e05b308947a10a96ebe'

        # TEST Empty string 
        self.assertEqual(get_access_token('', ''), None)
        self.assertEqual(get_access_token(myCID, ''), None)
        self.assertEqual(get_access_token('', mySID), None)

        # TEST Random string
        self.assertEqual(get_access_token('adsgfasf', 'rh4y5yh4eu63uu'),
                         None)
        self.assertEqual(get_access_token(myCID, '4hjb231yr3yb25'), 
                         None)
        self.assertEqual(get_access_token('43qtqxdgfcfq3', mySID), 
                         None)

        # TEST Success Check Length
        self.assertEqual(len(get_access_token(myCID, mySID)), 83)

    def test_get_playlist(self):
        # Get valid access token for tests
        myCID = '2b1a105e0bf94d69924ed5789171693f'
        mySID = '487346bb76a54e05b308947a10a96ebe'
        access_token = get_access_token(myCID, mySID)
        
        # Constants
        playlist = None
        myPID = '37i9dQZF1DXcBWIGoYBM5M' 
        myOtherPID = '1KNl4AYfgZtOVm9KHkhPTF'

        # TEST Empty string 
        self.assertEqual(get_playlist('', ''), None)
        self.assertEqual(get_playlist(myPID, ''), None)
        self.assertEqual(get_playlist('', access_token), None)
        
        # TEST Random string
        self.assertEqual(get_playlist('raq4tctcfheagvsa', 'rh4y5yh4eu63uu'),
                         None)
        self.assertEqual(get_playlist(myOtherPID, '4hjb231yr3yb25'), 
                         None)
        self.assertEqual(get_playlist('43qtqxdgfcfq3', access_token), 
                         None)

        # TEST Success 1
        playlist = get_playlist(myPID, access_token)
        self.assertIs(type(playlist), dict,
                      msg="Json() value should be returned which is dict")
        self.assertNotEqual(playlist["id"], None,
                            msg="Playlist should have id parameter")
        self.assertEqual(playlist["id"], myPID,
                         msg="Playlist should have correct PID")

        # TEST Success 2
        playlist = get_playlist(myOtherPID, access_token)
        self.assertIs(type(playlist), dict,
                      msg="Json() value should be returned which is dict")
        self.assertNotEqual(playlist["id"], None,
                            msg="Playlist should have id parameter")
        self.assertEqual(playlist["id"], myOtherPID,
                         msg="Playlist should have correct PID")

    def test_parse_playlist_to_dataframe(self):
        myPID = '37i9dQZF1DXcBWIGoYBM5M' 


if __name__ == '__main__':
    unittest.main()
