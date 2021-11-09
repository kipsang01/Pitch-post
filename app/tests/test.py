import unittest
from flask_login import current_user
from models import User,Pitch,Comment




class Test_user(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(name= 'Tim',email = 'tim@gmail.com', username = 'timo', password = '1234')
        self.new_pitch = Pitch(category='interview', content='my work application', user_id = self.new_user.id)
        self.new_comment = Comment(content='Good work', pitch_id = self.new_pitch.id, user_id = self.new_user.id)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_password_setter(self):
    
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('1234'))
     
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch)) 
        self.assertTrue(isinstance(self.new_comment,Comment))   
        
    def test_user(self):
        pass
    
    def test_pitch(self):
        pass
    
    def test_comment(self):
        pass