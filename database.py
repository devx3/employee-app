from PyQt5 import QtSql
from PyQt5.QtSql import * 
from datetime import datetime

class Database: 
  is_intantiated = False

  def __init__(self): 
    if not Database.is_intantiated: 
      print( "Database has been instantiated!" )

      self.db = QSqlDatabase.addDatabase("QSQLITE")
      self.db.setDatabaseName("./Tests.db")
      self.db.open()
      Database.is_intantiated = True
    else: 
      print( "Has already instantiated!" )

  def get_salary_for_employee(self, id):
    query = QSqlQuery()
    queryString = """
      SELECT
        e.firstname as "Nome",
        e.lastname as "Sobrenome",
        e.department_name as "Setor",
        ls.salary as "Salário",
        ls.reason as "Razão",
        ls.date as "Data"
      FROM
        employees AS e
      INNER JOIN 
        log_salary AS ls
      ON ls.employee_id = e.id
      WHERE e.id = :id
    """
    query.prepare(queryString)
    query.bindValue(":id", id)
    query.exec()
    
    record = query.record()
    no_columns = record.count()
    
    # build the header
    header_list = []

    for i in range(no_columns):
      header_list.append(record.field(i).name())

    # get values
    result_list = []

    while query.next():
      sublist = []
      for i in range(no_columns):
        sublist.append(query.value(i))
      result_list.append(sublist)
    
    return [header_list, result_list]
  
  def get_position_for_employee(self, id):
    query = QSqlQuery()
    queryString = """
      SELECT
        e.firstname as "Nome",
        e.lastname as "Sobrenome",
        e.department_name as "Setor",
        lp.position as "Cargo",
        lp.date as "Data"
      FROM
        employees AS e
      INNER JOIN
        log_position AS lp
      ON lp.employee_id = e.id
      WHERE e.id = :id
    """
    query.prepare(queryString)
    query.bindValue(":id", id)
    query.exec()
    
    record = query.record()
    no_columns = record.count()
    
    # build the header
    header_list = []

    for i in range(no_columns):
      header_list.append(record.field(i).name())

    # get values
    result_list = []

    while query.next():
      sublist = []
      for i in range(no_columns):
        sublist.append(query.value(i))
      result_list.append(sublist)

    return [header_list, result_list]

  def get_employee_full_info(self, condition_list):
    query = QSqlQuery()

    len_condition_list = len(condition_list)
    condition = ""

    if len_condition_list != 0:
      for i in range(len_condition_list):
        if( i == 0 ):
          condition += "WHERE "
        else: 
          condition += "AND "
          
        condition += condition_list[i][0]
        condition += " LIKE "
        condition += f'{condition_list[i][1]} '
    
    condition += "GROUP BY e.id"
    
    sql = """
      SELECT 
        e.id as ID,
        e.firstname as "Nome",
        e.lastname as "Sobrenome",
        e.birthday as "Aniversário",
        e.department_name as "Setor",
        (SELECT salary FROM log_salary WHERE employee_id = e.id ORDER BY id DESC LIMIT 1) as "Salário",
        (SELECT reason FROM log_salary WHERE employee_id = e.id ORDER BY id DESC LIMIT 1) as "Razão",
        (SELECT position FROM log_position WHERE employee_id = e.id ORDER BY id DESC LIMIT 1) as "Cargo"
      FROM 
        employees as e	
      JOIN
        log_salary as ls
      ON 
        ls.employee_id = e.id
      JOIN 
        log_position as lp
      ON
        lp.employee_id = e.id
    """ + condition
    #print(sql)

    res = query.exec(sql)
    record = query.record()
    column_number = record.count()

    header_list = []

    for i in range(column_number):
      header_list.append(record.field(i).name()  )

    result_list = []

    while query.next():
      sublist = []

      for i in range(column_number):
        sublist.append(query.value(i))
      result_list.append(sublist)

    return [header_list, result_list]

  def insert_new_salary(self, id, new_salary, reason):
    query = QSqlQuery()
    query.prepare("""
      INSERT INTO log_salary (employee_id, salary, date, reason)
      VALUES ( :e_id, :salary, :date, :reason )
      """)

    query.bindValue(":e_id", id)
    query.bindValue(":salary", new_salary)
    query.bindValue(":date", datetime.today().strftime('%Y-%m-%d %H:%M:%S '))
    query.bindValue(":reason", reason)

    return query.exec()
  
  def insert_new_position(self, id, new_position):
    query = QSqlQuery()
    query.prepare("""
      INSERT INTO log_position (employee_id, position, date)
      VALUES ( :e_id, :position, :date )
    """)

    query.bindValue(":e_id", id)
    query.bindValue(":position", new_position)
    query.bindValue(":date", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

    return query.exec()

  def get_last_id(self):
    query = QSqlQuery()
    res = query.exec("SELECT MAX(id) FROM employees")
    
    if query.next():
      return query.value(0)
    return 0

  def insert_employee(self, employeeFullInfo ):
    query = QSqlQuery()

    # Insert in main table
    query.prepare("""
      INSERT INTO employees ( firstname, lastname, birthday, department_name )
      VALUES (:fname, :lname, :birthday, :department )
    """)

    query.bindValue( ":fname", employeeFullInfo.fname )
    query.bindValue( ":lname", employeeFullInfo.lname )
    query.bindValue( ":birthday", employeeFullInfo.birthday )
    query.bindValue( ":department", employeeFullInfo.department )

    query.exec()

    id = self.get_last_id()

    # Insert in Salary Log
    query.prepare("""
      INSERT INTO log_salary (employee_id, salary, date)
      VALUES ( :e_id, :salary, :date )
      """)

    query.bindValue(":e_id", id)
    query.bindValue(":salary", employeeFullInfo.salary)
    query.bindValue(":date", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    query.exec()

    # Insert in position Log
    query.prepare("""
      INSERT INTO log_position ( employee_id, position, date )
      VALUES (:id, :position, :date )
    """)
    query.bindValue( ":id", id )
    query.bindValue( ":position", employeeFullInfo.position )
    query.bindValue( ":date", datetime.today().strftime('%Y-%m-%d %H:%M:%S') )
    query.exec()

  def delete_employee(self, id):
    query = QSqlQuery()

    query.prepare("""
      DELETE FROM employees WHERE id = :id
    """)
    query.bindValue(':id', id)
    query.exec()

    query.prepare("""
      DELETE FROM log_salary WHERE employee_id = :id
    """)
    query.bindValue(':id', id)
    query.exec()

    query.prepare("""
      DELETE FROM log_position WHERE employee_id = :id
    """)
    query.bindValue(':id', id)
    query.exec()

  def get_salary_statistics(self):
    query = QSqlQuery()

    result_list = [0, 0, 0]
    query.exec("SELECT MAX(salary) FROM log_salary")    
    if query.next(): 
      result_list[2] = query.value(0)

    query.exec("SELECT AVG(salary) FROM log_salary")
    if query.next(): 
      result_list[1] = query.value(0)

    query.exec("SELECT MIN(salary) FROM log_salary")
    if query.next(): 
      result_list[0] = query.value(0)
    
    return result_list

  def get_total_department_salaries(self):
    query = QSqlQuery()

    query.exec("""
      SELECT e.department_name, sum(ls.salary)
      FROM employees as e
      INNER JOIN log_salary as ls
      ON e.id = ls.employee_id
      GROUP BY e.department_name
    """)

    rec = query.record()
    col_number = rec.count()
    the_list = []

    while query.next():
      sublist = []
      for i in range(col_number):
        sublist.append(query.value(i))
      the_list.append(sublist)
    
    return the_list

# if __name__ == "__main__":
#     db1=Database()
