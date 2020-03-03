import sys, os
sys.path.append(os.getcwd())
import time
from Base.Init_driver import init_driver
from Page.Page_Obj import Page_O
import pytest
class Test_Search:

    def setup_class(self):
        # 实例化driver
        self.driver = init_driver()
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        self.driver.keyevent(4)
        # 统一页面对象管理类
        self.po = Page_O(self.driver).login_page()

    # def teardown_class(self):
    #     time.sleep(10)
    #     self.driver.quit()
    # @pytest.fixture(scope="class")
    @pytest.mark.parametrize("email,pws", [("88888888@qq.com", 123123)])
    def test_login(self,email,pws):
        self.po.login(email,pws)
        self.driver.save_screenshot("rxall2.png")
        time.sleep(20)
        self.driver.tap([(946, 1998), (1080, 2232)], 500)
        # self.po.sercher()

    @pytest.mark.parametrize("text", ['Art'])
    def test_shuru(self,text):
        self.po.sercher(text)
        self.driver.save_screenshot("rxall3.png")