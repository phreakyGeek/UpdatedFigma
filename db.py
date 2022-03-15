import sqlite3  
import time    


class dbs():

    
    def __init__(self):
        self.conn = sqlite3.connect('maindb.db') 
        self.conn.row_factory = self.dict_factory 

    def dict_factory(self,cursor, row):

        d = {}

        for idx, col in enumerate(cursor.description):

            d[col[0]] = row[idx]

        return d


    # user functions ---- start
    def get_userlogin(self,username):
        cursor = self.conn.execute("SELECT username, password, usertype from UserLogin")
        data = cursor.fetchall()
        for i in data:
            if i['username'] == username:
                return i
        return {}

    def create_userlogin(self,username,password,type):
        if self.get_userlogin(username)=={}:
            self.conn.execute("INSERT INTO UserLogin (username, password, usertype) VALUES ('{}','{}','{}')".format(username,password,type))
            self.conn.commit()
            return "success user added successfully"
        else:
            return "error user already exists"

    # user functions ---- end

    # masterdata functions ---- start

    def get_masterdata(self,partno):
        cursor = self.conn.execute("SELECT PartNo, LearnData, PINNames from Masterdata")
        data = cursor.fetchall()
        for i in data:
            if i['PartNo'] == partno:
                return i
        return {}

    def get_allpnos(self):
        cursor = self.conn.execute("SELECT PartNo from Masterdata")
        data = cursor.fetchall()
        return data

    def create_masterdata(self,partno,learndata,pinnanmes):
        if self.get_masterdata(partno)=={}:
            self.conn.execute("INSERT INTO Masterdata (PartNo, LearnData, PINNames) VALUES ('{}','{}','{}')".format(partno,learndata,pinnanmes))
            self.conn.commit()
            return "success masterdata added successfully"
        else:
            return "error masterdata already exists"

    def update_masterdata(self,partno,learndata,pinnanmes):
        if self.get_masterdata(partno)!={}:
            self.conn.execute("UPDATE Masterdata set learndata='{}',pinnames='{}' where PartNo='{}'".format(learndata,pinnanmes,partno))
            self.conn.commit()
            return "success masterdata updated successfully"
        else:
            return "error masterdata does not exists"
    # masterdata functions ---- end

    # TestLogs functions ---- start

    def get_testlogs(self,partno):
        cursor = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}'".format(partno,))
        data = cursor.fetchall()
        return data

    def create_testlogs(self,partno,masterresult,continuityresult,orientationresult,hipotresult):
        t = time.strftime('%Y-%m-%d %H:%M:%S')
        if self.get_masterdata(partno)!={}:
            self.conn.execute("INSERT INTO TestLogs (PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult) VALUES ('{}','{}','{}','{}','{}','{}')".format(partno,t,masterresult,continuityresult,orientationresult,hipotresult))
            self.conn.commit()
            return "success masterdata added successfully"
        else:
            return "error masterdata does not exists"

    def get_testlogs_stats(self,partno):
        mpassdata = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}' and MasterResult='pass'".format(partno,)).fetchall()
        mfaildata = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}' and MasterResult='fail'".format(partno,)).fetchall()
        cpassdata = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}' and ContinuityResult='pass'".format(partno,)).fetchall()
        cfaildata = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}' and ContinuityResult='fail'".format(partno,)).fetchall()
        opassdata = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}' and OrientationResult='pass'".format(partno,)).fetchall()
        ofaildata = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}' and OrientationResult='fail'".format(partno,)).fetchall()
        hpassdata = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}' and HipotResult='pass'".format(partno,)).fetchall()
        hfaildata = self.conn.execute("SELECT PartNo, Date, MasterResult,ContinuityResult,OrientationResult,HipotResult from TestLogs where PartNo='{}' and HipotResult='fail'".format(partno,)).fetchall()

        retval = {}
        retval['partno']=partno
        retval['masterresult']={'pass':len(mpassdata),'fail':len(mfaildata)}
        retval['continuityresult']={'pass':len(cpassdata),'fail':len(cfaildata)}
        retval['orientationresult']={'pass':len(opassdata),'fail':len(ofaildata)}
        retval['hipotresult']={'pass':len(hpassdata),'fail':len(hfaildata)}
        return retval

    # testlogs functions ---- end
s = '''
pin 51 - 52,
pin 52 - 51,

'''
names='''
pin 51 - test1
pin 52 - test point 2

'''
if __name__ == "__main__":
    db = dbs()
    # print("Opened database successfully");  
    # print(db.get_userlogin("admin"))
    # print(db.create_userlogin("test1","test1","user"))
    # print(db.get_masterdata("987654321"))
    # print(db.create_masterdata("987654321","pin1 2 3","abc def gh"))
    #db.update_masterdata("987654321","879879","hjhgjkhg jhgjhgjh jhgjgj")
    #print(db.get_masterdata("987654321"))
    # print(db.get_testlogs("123456"))
    # print(db.create_testlogs("123456","fail","fail","pass","pass"))
    # print(db.get_testlogs("123456"))
    # print(db.get_testlogs_stats("123456"))
    # db.update_masterdata("987654321",s,names)
    # db.update_masterdata("987654321",s,names)
    # print(db.get_masterdata("987654321"))
    print(db.get_allpnos())
