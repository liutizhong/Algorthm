# coding:utf-8
import re
__author__ = 'root'

string = ''' <a href="/touch"> </a>
             <a href="http://mm.yougou.com/touch/mm/nn"'''
mm = "hellotest"
rl = re.compile(r"(?=test)")