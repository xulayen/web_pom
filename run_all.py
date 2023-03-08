#-*- coding:gbk-*-

import os
import time

import pytest
import allure
import os

if __name__=='__main__':
    case_path=os.path.dirname(os.path.abspath(__file__))
    rel_path=os.path.join(case_path,r'cases\test_register.py')
    report_dir=os.path.join(case_path, r'cases\report')
    print(report_dir)
    pytest.main(['--alluredir',report_dir,rel_path,'--clean-alluredir'])
    time.sleep(2)
    os.system('allure serve cases/report')