#coding=utf-8
import unittest
import HTMLTestRunner
import os,time


"""
suite=doctest._DocTestSuite()
suite.addTest(unittest.makeSuite(normalorder.Normalorder))
suite.addTest(unittest.makeSuite(cancel_order.Cancel_order))"""

listaa='D:\\selenium_python\\test_case'
def creatsuitel():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,
                                                 pattern ='start_*.py',
                                                 top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print (testunit)
    return testunit
alltestnames = creatsuitel()

now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
filename = ('D:\\selenium_python\\report\\'+now+'result.html')
fp = open(filename, 'wb')

runner=HTMLTestRunner.HTMLTestRunner(
                                    stream=fp,
                                    title='Report_title',
                                    description='Report_description')
runner.run(alltestnames)

