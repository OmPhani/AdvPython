from database_connection import MysqlDatabaseConnection
class HclPythonTransaction(MysqlDatabaseConnection):
    def execute_transaction_query(self):
        cust_id = 2
        sql = "delete from customer where cust_id=%s"

        try:
            self.cursor.execute(sql,(cust_id,))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("Something goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connect_obj = HclPythonTransaction()
connect_obj.connect("localhost","root","12345678","hcl_vij")
connect_obj.execute_transaction_query()