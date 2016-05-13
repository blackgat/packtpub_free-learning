# +-----------------------------------------------------------------------
# Required browser:
# Firefox
#
# Required python packages:
# pip install selenium
# +-----------------------------------------------------------------------
__author__ = 'Chia Chin Chang'
__version__ = '1.0'
__DEBUG__ = False
import signal
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def run(_user, _pass):
    try:
        driver = webdriver.Firefox()
        driver.get("https://www.packtpub.com/packt/offers/free-learning")
        pass
    except:
        print('There is no FireFox found at current system')
        return

    # Dump page for debug
    if __DEBUG__:
        free_learning_page = driver.page_source
        file = open('free_learning_page.html', 'wb')
        file.write(bytes(free_learning_page, encoding = "utf8"))
        file.close()
        pass

    try:
        login_style = driver.find_element_by_id('account-bar-logged-in').get_attribute('style')
        if login_style == 'display: block;':
            print('User already login\n')
            user_login = True
            pass
        else:
            print('User not login\n')
            user_login = False
            pass

        if user_login == False:
            driver.find_element_by_css_selector('#account-bar-login-register > a.login-popup > div').click()

            # ToDo: Try to not travel them all the time
            email_elements = driver.find_elements_by_id('email')
            for uid in email_elements:
                if uid.is_displayed():
                    uid.send_keys(_user)
                    pass
                pass

            pwd_elemets = driver.find_elements_by_id('password')
            for pwd_element in pwd_elemets:
                if pwd_element.is_displayed():
                    pwd_element.send_keys(_pass)
                    pass
                pass
        
            submit_elements = driver.find_elements_by_css_selector('#edit-submit-1')
            for submit_element in submit_elements:
                if submit_element.is_displayed():
                    submit_element.click()
                    pass
                pass
            pass

        # ToDo: Maybe we can using other way to find the target element and make it more readable.
        claim_eBook_element = driver.find_element_by_css_selector('#deal-of-the-day > div > div > div.dotd-main-book-summary.float-left > div.dotd-main-book-form.cf > div.float-left.free-ebook > a > div > input')
    
        actions = ActionChains(driver)
        actions.move_to_element(claim_eBook_element)
        actions.perform()
        claim_eBook_element.click()
        # Waiting web site responding for 30 seconds
        time.sleep(30)
        pass
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return
        pass

    # Whether bought or not bought, the final results are the same page
    # I think our action is finished, close browser.
    driver.close()
    pass

def banner():
    print ('''
Version     :   %s
Author      :   %s ''' % (__version__, __author__))
    print('')
    return

def main(argv):
    parser = argparse.ArgumentParser(description=banner())
    parser.add_argument("-u", '--user', dest='user', metavar='user', required=True,
                        help='[required] ' + 'user')
    parser.add_argument("-p", '--password', dest='password', metavar='pass', required=True,
                        help='[required] ' + 'password')

    args = parser.parse_args()
    _user = args.user
    _pass = args.password

    run(_ptc, _user, _pass)
    pass

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit)
    main(sys.argv)
    pass
