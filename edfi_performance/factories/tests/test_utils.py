from pytest import mark, fixture

from ..utils import *

class Test_utils(object):
    def test_given_no_year_when_formatting_date_then_use_current_year(self):        

        month = 12
        day = 1
        expected = str(date.today().year) + "-12-01"

        actual = formatted_date(month, day)

        assert actual == expected

        
    def test_given_year_is_supplied_when_formatting_date_then_use_supplied_year(self):        

        year = 1999
        month = 12
        day = 1
        expected = "1999-12-01"

        actual = formatted_date(month, day, year)

        assert actual == expected