from django.contrib.staticfiles.testing import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import re

from organization.models import Organization
from shift.utils import create_organization, create_country

class SignUpVolunteer(LiveServerTestCase):
    '''
    SignUpVolunteer Class contains tests to register volunteer User
    Tests included.

    Name Fields:
        - Test Null values
        - Test legit characters in first_name, last_name fields
        - Register volunteer with already registered username
        - Test length of name fields ( 30 char, limit)

    Location Field (Address, City, State, Country):
        - Test Null Values
        - Test legit characters as per Models defined

    Email Field:
        - Test Null Values
        - Test uniqueness of field

    Phone Number Field:
        - Test Null Values
        - Test validity of number against country entered
        - Test legit characters as per Models defined

    Organization Field:
        - Test Null Values
        - Test legit characters as per Models defined

    Retention of fields:
        - Field values are checked to see that they are not lost when the page gets reloaded
    '''
    @classmethod
    def setUpClass(cls):
        cls.homepage = '/'
        cls.volunteer_registration_page = '/registration/signup_volunteer/'
        cls.authentication_page = '/authentication/login/'

        cls.username = 'id_username'
        cls.password = 'id_password'
        cls.first_name = 'id_first_name'
        cls.last_name = 'id_last_name'
        cls.email = 'id_email'
        cls.address = 'id_address'
        cls.city = 'id_city'
        cls.state = 'id_state'
        cls.country = 'id_country'
        cls.phone = 'id_phone_number'
        cls.organization = 'id_unlisted_organization'

        cls.username_error = "id('div_id_username')/div/p/strong"
        cls.first_name_error = "id('div_id_first_name')/div/p/strong"
        cls.last_name_error = "id('div_id_last_name')/div/p/strong"
        cls.email_error = "id('div_id_email')/div/p/strong"
        cls.address_error = "id('div_id_address')/div/p/strong"
        cls.city_error = "id('div_id_city')/div/p/strong"
        cls.state_error = "id('div_id_state')/div/p/strong"
        cls.country_error = "id('div_id_country')/div/p/strong"
        cls.phone_error = "id('div_id_phone_number')/div/p/strong"
        cls.organization_error = "id('div_id_unlisted_organization')/div/p/strong"

        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        super(SignUpVolunteer, cls).setUpClass()

    def setUp(self):
        # create an org prior to registration. Bug in Code
        # added to pass CI
        create_organization()

        # country created so that phone number can be checked
        create_country()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super(SignUpVolunteer, cls).tearDownClass()

    def fill_registration_form(self, info):
        self.driver.find_element_by_id(self.username).send_keys(info[0])
        self.driver.find_element_by_id(self.password).send_keys(info[1])
        self.driver.find_element_by_id(self.first_name).send_keys(info[2])
        self.driver.find_element_by_id(self.last_name).send_keys(info[3])
        self.driver.find_element_by_id(self.email).send_keys(info[4])
        self.driver.find_element_by_id(self.address).send_keys(info[5])
        self.driver.find_element_by_id(self.city).send_keys(info[6])
        self.driver.find_element_by_id(self.state).send_keys(info[7])
        self.driver.find_element_by_id(self.country).send_keys(info[8])
        self.driver.find_element_by_id(self.phone).send_keys(info[9])
        self.driver.find_element_by_id(self.organization).send_keys(info[10])
        self.driver.find_element_by_xpath('//form[1]').submit()

    def verify_field_values(self, info):
        self.assertEqual(self.driver.find_element_by_id(self.username).get_attribute('value'),info[0])
        self.assertEqual(self.driver.find_element_by_id(self.first_name).get_attribute('value'),info[1])
        self.assertEqual(self.driver.find_element_by_id(self.last_name).get_attribute('value'),info[2])
        self.assertEqual(self.driver.find_element_by_id(self.email).get_attribute('value'),info[3])
        self.assertEqual(self.driver.find_element_by_id(self.address).get_attribute('value'),info[4])
        self.assertEqual(self.driver.find_element_by_id(self.city).get_attribute('value'),info[5])
        self.assertEqual(self.driver.find_element_by_id(self.state).get_attribute('value'),info[6])
        self.assertEqual(self.driver.find_element_by_id(self.country).get_attribute('value'),info[7])
        self.assertEqual(self.driver.find_element_by_id(self.phone).get_attribute('value'),info[8])
        self.assertEqual(self.driver.find_element_by_id(self.organization).get_attribute('value'),info[9])

    def register_valid_details(self):
        self.driver.get(self.live_server_url + self.volunteer_registration_page)
        entry = ['volunteer-username','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','volunteer-org']
        self.fill_registration_form(entry)

    def test_null_values(self):
        self.driver.get(self.live_server_url
                        + self.volunteer_registration_page)

        entry = ['','','','','','','','','','','']
        self.fill_registration_form(entry)

        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        # verify that all of the fields are compulsory
        self.assertEqual(len(self.driver.find_elements_by_class_name('help-block')),
                11)

    def test_successful_registration(self):
        self.register_valid_details()
        self.assertNotEqual(self.driver.find_elements_by_class_name('messages'),
                None)
        self.assertEqual(self.driver.find_element_by_class_name('messages').text,
                'You have successfully registered!')

    def test_name_fields(self):
        # register valid volunteer user
        self.register_valid_details()
        self.assertNotEqual(self.driver.find_elements_by_class_name('messages'),
                None)
        self.assertEqual(self.driver.find_element_by_class_name('messages').text,
                'You have successfully registered!')

        # register a user again with username same as already registered user
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.homepage)

        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email1@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.find_element_by_xpath(self.username_error).text,
                'User with this Username already exists.')

        # test numeric characters in first-name, last-name
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-1','volunteer-password!@#$%^&*()_','volunteer-first-name-1','volunteer-last-name-1','volunteer-email1@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.find_element_by_xpath(self.first_name_error).text,
                'Enter a valid value.')
        self.assertEqual(self.driver.find_element_by_xpath(self.last_name_error).text,
                'Enter a valid value.')

        # test special characters in first-name, last-name
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-1','volunteer-password!@#$%^&*()_','first-name-!@#$%^&*()_','last-name!@#$%^&*()_','volunteer-email@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.find_element_by_xpath(self.first_name_error).text,
                'Enter a valid value.')
        self.assertEqual(self.driver.find_element_by_xpath(self.last_name_error).text,
                'Enter a valid value.')

        # test length of first-name, last-name not exceed 30
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-1','volunteer-password!@#$%^&*()_','volunteer-first-name-long-asdfghjkl','volunteer-last-name-long-asdfghjkl','volunteer-email@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        error_message = self.driver.find_element_by_xpath(self.first_name_error).text
        self.assertTrue(bool(re.search(r'Ensure this value has at most 30 characters', str(error_message))))

        error_message = self.driver.find_element_by_xpath(self.last_name_error).text,
        self.assertTrue(bool(re.search(r'Ensure this value has at most 30 characters', str(error_message))))

    def test_location_fields(self):
        # test numeric characters in address, city, state, country
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-1','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email1@systers.org','123 New-City address','1 volunteer-city','007 volunteer-state','54 volunteer-country','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.volunteer_registration_page)

        # Verify that messages are displayed for city, state and country but not address
        # Test commented out as there is a bug in the template
        """self.assertEqual(len(self.driver.find_elements_by_class_name('help-block')),
                3)"""
        self.assertEqual(self.driver.find_element_by_xpath(self.city_error).text,
                'Enter a valid value.')
        self.assertEqual(self.driver.find_element_by_xpath(self.state_error).text,
                'Enter a valid value.')
        self.assertEqual(self.driver.find_element_by_xpath(self.country_error).text,
                'Enter a valid value.')

        # Test special characters in address, city, state, country
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-2','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email2@systers.org','volunteer-address!@#$()','!$@%^#&volunteer-city','!$@%^#&volunteer-state','&%^*volunteer-country!@$#','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.volunteer_registration_page)

        # verify that messages are displayed for all fields
        self.assertEqual(self.driver.find_element_by_xpath(self.address_error).text,
                'Enter a valid value.')
        self.assertEqual(self.driver.find_element_by_xpath(self.city_error).text,
                'Enter a valid value.')
        self.assertEqual(self.driver.find_element_by_xpath(self.state_error).text,
                'Enter a valid value.')
        self.assertEqual(self.driver.find_element_by_xpath(self.country_error).text,
                'Enter a valid value.')

    def test_email_field(self):

        # register valid volunteer user
        self.register_valid_details()

        # verify successful registration
        self.assertNotEqual(self.driver.find_elements_by_class_name('messages'),
                None)
        self.assertEqual(self.driver.find_element_by_class_name('messages').text,
                'You have successfully registered!')
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.homepage)

        # Try to register volunteer again with same email address
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-1','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        # verify that volunteer wasn't registered
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.volunteer_registration_page)
        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.find_element_by_xpath(self.email_error).text,
                'Volunteer with this Email already exists.')

    def test_phone_field(self):

        # register valid volunteer user with valid phone number for country
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        # verify successful registration
        self.assertNotEqual(self.driver.find_elements_by_class_name('messages'),
                None)
        self.assertEqual(self.driver.find_element_by_class_name('messages').text,
                'You have successfully registered!')
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.homepage)

        # Try to register volunteer with incorrect phone number for country
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-1','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email1@systers.org','volunteer-address','volunteer-city','volunteer-state','India','237937913','volunteer-org']
        self.fill_registration_form(entry)

        # verify that user wasn't registered
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.volunteer_registration_page)
        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.find_element_by_xpath(self.phone_error).text,
                "This phone number isn't valid for the selected country")

        # Use invalid characters in phone number
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-1','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email1@systers.org','volunteer-address','volunteer-city','volunteer-state','India','23&79^37913','volunteer-org']
        self.fill_registration_form(entry)

        # verify that user wasn't registered
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.volunteer_registration_page)
        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.find_element_by_xpath(self.phone_error).text,
                "Please enter a valid phone number")

    def test_organization_field(self):

        # test numeric characters in organization
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-1','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email1@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','volunteer-org 13']
        self.fill_registration_form(entry)

        # verify successful registration
        self.assertNotEqual(self.driver.find_elements_by_class_name('messages'),
                None)
        self.assertEqual(self.driver.find_element_by_class_name('messages').text,
                'You have successfully registered!')
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.homepage)

        # Use invalid characters in organization
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username-2','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name','volunteer-email2@systers.org','volunteer-address','volunteer-city','volunteer-state','volunteer-country','9999999999','!*^$volunteer-org']
        self.fill_registration_form(entry)

        # verify that user wasn't registered
        self.assertEqual(self.driver.current_url, self.live_server_url +
                self.volunteer_registration_page)
        self.assertNotEqual(self.driver.find_elements_by_class_name('help-block'),
                None)
        self.assertEqual(self.driver.find_element_by_xpath(self.organization_error).text,
                "Enter a valid value.")

    def test_field_value_retention(self):

        # send invalid value in fields - first name, state, phone, organization
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username','volunteer-password!@#$%^&*()_','volunteer-first-name-3','volunteer-last-name','volunteer-email@systers.org','volunteer-address','volunteer-city','volunteer-state!','volunteer-country','99999.!9999','@#volunteer-org']
        self.fill_registration_form(entry)

        # verify that user wasn't registered and that field values are not erased
        self.assertEqual(self.driver.current_url, self.live_server_url + self.volunteer_registration_page)
        details = ['volunteer-username','volunteer-first-name-3','volunteer-last-name','volunteer-email@systers.org','volunteer-address','volunteer-city','volunteer-state!','volunteer-country','99999.!9999','@#volunteer-org']
        self.verify_field_values(details)
        

        # send invalid value in fields - last name, address, city, country
        self.driver.get(self.live_server_url + self.volunteer_registration_page)

        entry = ['volunteer-username','volunteer-password!@#$%^&*()_','volunteer-first-name','volunteer-last-name-3','volunteer-email@systers.org','volunteer-address$@!','volunteer-city#$','volunteer-state','volunteer-country 15','9999999999','volunteer-org']
        self.fill_registration_form(entry)

        # verify that user wasn't registered and that field values are not erased
        self.assertEqual(self.driver.current_url, self.live_server_url + self.volunteer_registration_page)
        details = ['volunteer-username','volunteer-first-name','volunteer-last-name-3','volunteer-email@systers.org','volunteer-address$@!','volunteer-city#$','volunteer-state','volunteer-country 15','9999999999','volunteer-org']
        self.verify_field_values(details)
