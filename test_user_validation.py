
import unittest
from user_validation import UserValidation

class TestEmailValidation(unittest.TestCase):
    def test_valid_email_returns_true(self):
        # Arrange
        email = 'user@example.com'
        # Act
        result = UserValidation.validate_email(email)
        # Assert
        self.assertTrue(result)

    def test_missing_at_symbol_returns_false(self):
        self.assertFalse(UserValidation.validate_email('userexample.com'))

    def test_missing_domain_returns_false(self):
        self.assertFalse(UserValidation.validate_email('user@'))

    def test_invalid_tld_returns_false(self):
        self.assertFalse(UserValidation.validate_email('user@mail.c'))

    def test_email_with_subdomain_returns_true(self):
        self.assertTrue(UserValidation.validate_email('user@mail.company.com'))

    def test_email_with_special_characters_returns_true(self):
        self.assertTrue(UserValidation.validate_email('ramy.gomaa_21@mail.co'))

    def test_uppercase_email_returns_true(self):
        self.assertTrue(UserValidation.validate_email('USER@MAIL.COM'))

    def test_email_with_space_returns_false(self):
        self.assertFalse(UserValidation.validate_email('user name@mail.com'))

    def test_empty_email_returns_false(self):
        self.assertFalse(UserValidation.validate_email(''))

    def test_null_email_returns_false(self):
        self.assertFalse(UserValidation.validate_email(None))


class TestUsernameValidation(unittest.TestCase):
    def test_valid_username_returns_true(self):
        self.assertTrue(UserValidation.validate_username('ramy_gomaa'))

    def test_username_too_short_returns_false(self):
        self.assertFalse(UserValidation.validate_username('ab'))

    def test_username_too_long_returns_false(self):
        self.assertFalse(UserValidation.validate_username('ramygomaaisaverylongusername'))

    def test_username_with_spaces_returns_false(self):
        self.assertFalse(UserValidation.validate_username('ramy gomaa'))

    def test_username_with_symbols_returns_false(self):
        self.assertFalse(UserValidation.validate_username('ramy@123'))

    def test_username_with_digits_returns_true(self):
        self.assertTrue(UserValidation.validate_username('ramy123'))

    def test_empty_username_returns_false(self):
        self.assertFalse(UserValidation.validate_username(''))

    def test_null_username_returns_false(self):
        self.assertFalse(UserValidation.validate_username(None))


class TestPhoneNumberValidation(unittest.TestCase):
    def test_valid_vodafone_number_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number('01012345678'))

    def test_valid_orange_number_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number('01234567890'))

    def test_valid_etisalat_number_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number('01198765432'))

    def test_valid_we_number_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number('01555555555'))

    def test_valid_vodafone_with_country_code_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number('201012345678'))

    def test_valid_orange_with_country_code_returns_true(self):
        self.assertTrue(UserValidation.validate_phone_number('201234567890'))

    def test_invalid_prefix_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number('01812345678'))

    def test_too_short_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number('0101234567'))

    def test_too_long_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number('010123456789'))

    def test_contains_characters_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number('01012abc678'))

    def test_empty_phone_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number(''))

    def test_null_phone_returns_false(self):
        self.assertFalse(UserValidation.validate_phone_number(None))


class TestNationalIDValidation(unittest.TestCase):
    def test_valid_national_id_returns_true(self):
        self.assertTrue(UserValidation.validate_national_id('29812251234567'))

    def test_too_short_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id('2981225123456'))

    def test_too_long_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id('298122512345678'))

    def test_contains_letters_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id('2981225AB34567'))

    def test_invalid_century_code_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id('19812251234567'))

    def test_invalid_month_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id('29813251234567'))

    def test_invalid_day_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id('29812323234567'))

    def test_invalid_governorate_code_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id('29812380034567'))

    def test_empty_national_id_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id(''))

    def test_null_national_id_returns_false(self):
        self.assertFalse(UserValidation.validate_national_id(None))


if __name__ == '__main__':
    unittest.main()
