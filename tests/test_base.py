from flask import current_app, url_for
from flask_testing import TestCase
from todoapp import create_app

class BaseTest(TestCase):

    def create_app(self):
        """ disable cross site request for testing
            This property avoids injected scripts
        """    
        app = create_app()
        app.config['TESTING'] = True

        
        app.config['WTF_CSFR_ENABLED'] = False
        
        return app
    
    
    def test_app_exists(self):
        """ Validate our app exists """
        self.assertIsNotNone(current_app)


    
    def test_app_in_test_mode(self):
        """ Validate is in test mode """
        self.assertTrue( current_app.config['TESTING'] )


    def test_root_redirects(self):
        """ Validate redirection to home with todo.index """
        response = self.client.get( url_for('go_home') )
        self.assertRedirects(  response,  url_for('todo.index')  )



    def test_auth_login_get(self):
        """ Validate to redirecting to login page """
        self.client.get( url_for('auth.login') )
        self.assertTemplateUsed( '/auth/login.html' )



    def test_auth_login_fail_post(self):
        """ Validate you can not enter with a invalid user """
        dummy_form = {
            "username": "dummyUser",
            "password": "bla"
        }

        response = self.client.post( url_for('auth.login') , data=dummy_form  )
        self.assertTemplateUsed('/auth/login.html')
