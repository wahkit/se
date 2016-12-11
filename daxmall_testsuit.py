#coding=utf-8
import unittest, doctest
import normalorder
import cancel_order
import haiwaigou
import login_out
import shopManage

import HTMLTestRunner

suite=doctest._DocTestSuite()
suite.addTest(unittest.makeSuite(normalorder.Normalorder))
suite.addTest(unittest.makeSuite(cancel_order.Cancel_order))
suite.addTest(unittest.makeSuite(haiwaigou.Haiwaigou))
suite.addTest(unittest.makeSuite(login_out.Login_out))
suite.addTest(unittest.makeSuite(shopManage.ShopManage))



filename = ('D:\\daxmall.html')
fp = open(filename, 'wb')
runner=HTMLTestRunner.HTMLTestRunner(
                                    stream=fp,
                                    title='Report_title',
                                    description='Report_description')
runner.run(suite)
fp.close()
2012