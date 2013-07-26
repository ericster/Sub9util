'''
Created on Jul 1, 2013

@author: me.jung
'''

import xlrd
import re
from tcPattern import TMO_TV
from schema import TMOTV_Schema as S 
# from test.test_iterlen import len
# from data2Xml import Data2Xml
from testsuite2LXml import Testsuite2LXml
from xlsData_AFM import XlsData
from cellParser_AFM import CellParser
from testSuite import TestSuite, TestCase, Step


# Conversion Flow
## 1
## 
## XlsData()

## CellExl()

## 1-2
## CellParser()

## 2
## TestSuite()/TestCase()/Steps()        

## 3
## Data2Xml(testsuite)



def main():

    ## 1st stage to create cell data from a xls spreadsheet
    xlsData = XlsData()
#     xlsData.readXls()
    xlsData.readCsv()
     
    ## 2nd stage to parse xlsData and create testsuites

    cellParser = CellParser(xlsData)

    print '-------------------------------------'
    print '2nd stage'
    print '-------------------------------------'
    
    
    """  @var no_rows: no of rows to parse
    """ 
    if True:
        no_rows = xlsData.getRowLength() 
        print 'number of rows is ', no_rows
        testsuites = cellParser.parseRows(no_rows)
        print '-------------------------------------'
        print 'printing testsuites'
        print '-------------------------------------'
        cellParser.printTestSuites(testsuites)

    ## 3rd stage to create xml compatible with TestLink
    print '-------------------------------------'
    print ' ### 3rd stage '
    print '-------------------------------------'
    
    """  @ test lxml
    """ 
    ts2xml = Testsuite2LXml(testsuites[0])
    ts2xml.createTSElement()
    ts2xml.printPrettyForm()
    filename = 'Attfamilymapsample2.xml'
    ts2xml.saveTestsuiteTag(filename)


if __name__ == '__main__':
    main()



