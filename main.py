import pytest


if __name__ == "__main__":
    '''It start code marketplace. no password'''
    pytest.main(["-v", "--junitxml=save_search_data_test.xml", "test/marketplace_one_page_test_no_password.py"])



