#-*- coding:gbk-*-
import time
from selenium import webdriver
import pytest
from pages.register import Registerpage
from common.db_connect import *

conf = {'host': '49.235.92.12',
        'port': '3309',
        'user': 'root',
        'password': '123456',
        'db': 'online'}


@pytest.fixture(scope='session', name='driver')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addini("url", type=None, default='http://124.70.221.221:8201', help='ceshi')


@pytest.fixture(scope='session')
def baseurl(pytestconfig):
    url = pytestconfig.getini('url')
    return url


@pytest.fixture(scope='session')
def get_ini(pytestconfig):
    log_cli = pytestconfig.getini('log_cli')
    print('获取到的marks:%s' % log_cli)


@pytest.fixture(scope='session')
def register(driver, baseurl):
    register1 = Registerpage(driver, baseurl)
    return register1


@pytest.fixture(scope='session')
def db1():
    _db = Dbcon('online', conf)
    yield _db
    _db.close()


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("gbk").decode('unicode_escape')
        item._nodeid = item.nodeid.encode("gbk").decode('unicode_escape')
