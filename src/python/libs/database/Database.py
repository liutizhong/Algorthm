#encoding=utf-8

from hive_service import ThriftHive
from hive_service.ttypes import HiveServerException
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import sys
sys.path.append("/usr/local/python/lib/python2.7/site-packages/py")
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class HiveDB:
    def __init__(self):
        self.hiveHost="192.168.212.20"
        self.hivePort=10000
        transport = TSocket.TSocket(self.hiveHost, self.hivePort)
        self.transport = TTransport.TBufferedTransport(transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = ThriftHive.Client(self.protocol)

    def exists(self,selectSQL):
        try:
            self.transport.open()
            self.client.execute(selectSQL)
            results=self.client.fetchAll()
            if len(results)==0:
                return False
            else:
                return True
        except Thrift.TException, tx:
            print '%s' % (tx.message)
        finally:
            self.transport.close()

    def execute(self,insertSQL):
        try:
            self.transport.open()
            self.client.execute(insertSQL)
        except Thrift.TException, tx:
            print '%s' % (tx.message)
        finally:
            self.transport.close()

    def select(self,selectSQL):
        try:
            self.transport.open()
            self.client.execute(selectSQL)
            results=self.client.fetchAll()
            return  results
        except Thrift.TException, tx:
            print '%s' % (tx.message)
        finally:
            self.transport.close()

    def console(self, sql):
        sql = sql.lower()[:len(sql)-1]
        if sql.startswith("select") or sql.startswith("desc") or sql.startswith("show"):
            results = self.select(sql)
            for row in results:
                print row
        else:
            self.execute(sql)
if __name__=='__main__':
    console("select * from tbl_analytics limit 10;")