import unittest
from APISpotifyEx import get_access_token, get_playlist

class TestFileName(unittest.TestCase):
    def test_get_access_token(self):
        myCID = '2b1a105e0bf94d69924ed5789171693f'
        mySID = '487346bb76a54e05b308947a10a96ebe'
    
        #Empty string tests
        self.assertEqual(get_access_token('',''), None)
        self.assertEqual(get_access_token(myCID, ''), None)
        self.assertEqual(get_access_token('',mySID), None)
        
        #Random string
        self.assertEqual(get_access_token('adsgfasf','rh4y5yh4eu63uu'),
                         None)
        self.assertEqual(get_access_token(myCID,'4hjb231yr3yb25'), 
                         None)
        self.assertEqual(get_access_token('43qtqxdgfcfq3',mySID), 
                         None)
        
        #Success Test Length
        self.assertEqual(len(get_access_token(myCID,mySID)), 83)
        
    def test_get_playlist(self):
        myPID = '37i9dQZF1DXcBWIGoYBM5M' 
        myOtherPID = '1KNl4AYfgZtOVm9KHkhPTF'
        
        #Get valid access token for tests
        myCID = '2b1a105e0bf94d69924ed5789171693f'
        mySID = '487346bb76a54e05b308947a10a96ebe'
        access_token = get_access_token(myCID,mySID)
        
        #Empty string tests
        self.assertEqual(get_playlist('',''), None)
        self.assertEqual(get_playlist(myPID, ''), None)
        self.assertEqual(get_playlist('',access_token), None)
        
        #Random string
        self.assertEqual(get_playlist('raq4tctcfheagvsa','rh4y5yh4eu63uu'),
                         None)
        self.assertEqual(get_playlist(myOtherPID,'4hjb231yr3yb25'), 
                         None)
        self.assertEqual(get_playlist('43qtqxdgfcfq3',access_token), 
                         None)
        
        #Success Test Length
        # self.assertEqual()


if __name__ == '__main__':
    unittest.main()
