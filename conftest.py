import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Ch_opt
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', 
                     help = "Specify the language for the browser (e.g., 'en', 'es')")

@pytest.fixture(scope="function")
def browser(request):
    
    user_language = request.config.getoption("language")
    chrome_opt = Ch_opt()
    chrome_opt.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    firefox_opt = Options()
    firefox_opt.set_preference("intl.accept_languages", user_language)

    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    browser = None
    
    if browser_name == 'chrome':
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_opt)

        print('\nLanguage assertion')
        browser_language = browser.execute_script("return navigator.language")
        assert browser_language == request.config.getoption("language"), "Browser language is not set correctly"
        print(f'\nlanguge is {browser_language}')
        
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=firefox_opt)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()