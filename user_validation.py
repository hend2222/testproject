
import re
from datetime import date

class UserValidation:
    @staticmethod
    def validate_email(email: str) -> bool:
        if email is None:
            return False
        email = email.strip()
        if not email:
            return False
        # Basic email regex: allow subdomains and common special characters in local part
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_username(username: str) -> bool:
        if username is None:
            return False
        username = username.strip()
        if not username:
            return False
        pattern = r'^[A-Za-z0-9_]{3,20}$'
        return re.match(pattern, username) is not None

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        if phone is None:
            return False
        phone = phone.strip()
        if not phone:
            return False
        if not phone.isdigit():
            return False
        # Local format: 11 digits starting with 010,011,012,015
        if re.match(r'^(010|011|012|015)\d{8}$', phone):
            return True
        # With country code (no plus): 12 digits starting with 20 then 10/11/12/15 then 8 digits
        if re.match(r'^20(10|11|12|15)\d{8}$', phone):
            return True
        return False

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        if national_id is None:
            return False
        national_id = national_id.strip()
        if not national_id:
            return False
        if not national_id.isdigit() or len(national_id) != 14:
            return False
        # First digit must be 2 or 3
        if national_id[0] not in ('2', '3'):
            return False
        # Extract year, month, day, governorate
        century = int(national_id[0])
        yy = int(national_id[1:3])
        mm = int(national_id[3:5])
        dd = int(national_id[5:7])
        gov = int(national_id[7:9])
        # month/day basic ranges
        if mm < 1 or mm > 12:
            return False
        if dd < 1 or dd > 31:
            return False
        # Governorate code 01..88
        if gov < 1 or gov > 88:
            return False
        # Validate actual calendar date (handle month lengths and leap years)
        full_year = (1900 if century == 2 else 2000) + yy
        try:
            date(full_year, mm, dd)
        except Exception:
            return False
        return True
