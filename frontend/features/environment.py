import os
import sys
from selenium import webdriver
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from util.utils import generate_report

def before_all(context):
    context.base_url = context.config.userdata['URL']
    context.driver = webdriver.Chrome('..\\drivers\\chromedriver.exe')
    context.driver.delete_all_cookies()
    context.driver.maximize_window()


def after_all(context):
    #generate_report(context.config.userdata['SYSTEM'])
    pass 