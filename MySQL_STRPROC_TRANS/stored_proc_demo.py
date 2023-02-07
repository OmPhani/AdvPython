from mysql.connector import Error
from database_connection import MysqlDatabaseConnection
class StoredProcedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            mydata = ('Pizza',)
            self.cursor.callproc("get_cust_details",args=mydata)
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()

connect_obj = StoredProcedure();
connect_obj.connect("localhost","root","12345678","hcl_vij")
connect_obj.execute_str_procedure()