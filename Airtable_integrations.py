# from pyairtable import Api, Base, Table
# from operator import itemgetter
# import operator, functools
import json
# from json import dumps
import requests
class Airtable:

    def __init__(self, token):
        self.token = token
    
    def get_bases(self):
        
        URL = "https://api.airtable.com/v0/meta/bases"
        headers = {'Authorization':"Bearer "+self.token}
        r = requests.get(url = URL, headers  = headers)
        self.data_base = r.json()
       
   
              

    def get_tables(self, base_id):
        
        URL = "https://api.airtable.com/v0/meta/bases/{0}/tables".format(base_id)
        headers = {'Authorization':"Bearer "+self.token}
        r = requests.get(url = URL, headers  = headers)
        self.data_tables = r.json()
        return  self.data_tables          
          
    def get_datas(self,base_id,table_id):
         URL = "https://api.airtable.com/v0/{0}/{1}".format(base_id,table_id)
         headers = {'Authorization':"Bearer "+self.token}
         r = requests.get(url = URL, headers  = headers)
         self.datas = r.json()
         return self.datas
         
    def create_records(self,base_id,table_id,data):
     
        URL= "https://api.airtable.com/v0/{0}/{1}".format(base_id,table_id)
        headers = {'Authorization':"Bearer "+self.token,"Content-Type":"application/json"}
        
        data1 = {
             "records": [
               {
                 "fields": 
                  data
               
                }
             ]
           }
        
        # resposnse = requests.post(url=URL , data=json.dumps(data1) , headers=headers)
        # print(resposnse.json())
        return data1

    def update_record(self,base_id,table_id,record_id,data):
        try:
            
            headers = {'Authorization':"Bearer "+token , "Content-Type":"application/json"}
            
            data={
            "fields": 
            data
                  
                }
           
            URL="https://api.airtable.com/v0/{0}/{1}/{2}".format(base_id,table_id,record_id)
            
            # resposnse = requests.put(url=URL , data=json.dumps(data) , headers=headers)
            # updated_record = resposnse.json()
            # return updated_record
        except Exception as e:
            import sys
            print(' Error on line {0} {1}'.format(sys.exc_info()[-1].tb_lineno,str(e)))
         
            
    def update_multiple_records(self,base_id,table_id,data1,data2,record_id1, record_id2):
        try:
            URL= "https://api.airtable.com/v0/{0}/{1}".format(base_id,table_id)
            headers = {'Authorization':"Bearer "+token ,"Content-Type":"application/json"}
           
            data = {
            "records": [
                  {
                    "fields": data1,
                    "id": record_id1
                  },
                  {
                    "fields": 
                      data2,                    
                    "id": record_id2
                  }
                ]
              }
              
        
            resposnse = requests.put(url=URL , data=json.dumps(data) , headers=headers)
            updated_multiple_records = resposnse.json()
            return updated_multiple_records
        
        except Exception as e:
            print(str(e))
        
    
    def delete_record(self,base_id,table_id,record_id):
        try:
        
            URL = "https://api.airtable.com/v0/{0}/{1}/{2}".format(base_id,table_id,record_id)
            headers = {'Authorization':"Bearer "+self.token ,"Content-Type":"application/json"}
            
            # resposnse = requests.delete(url=URL , headers=headers)
            # deleted_record = resposnse.json()
            # return deleted_record
       
        except Exception as e:
            print(str(e))
                 
    def delete_multiple_records(self,base_id,table_id,record_id1,record_id2):
        try:
            URL = "https://api.airtable.com/v0/{0}/{1}?records={2}&records={3}".format(base_id,table_id,record_id1,record_id2)
            headers = {'Authorization':"Bearer "+token , "Content-Type":"application/json"}
            
            # resposnse = requests.delete(url=URL , headers=headers)
            # deleted_multiple_records = resposnse.json()
            # return deleted_multiple_records
              
        except Exception as e:
            print(str(e))
                     
token = "patJxPje68ruB2IVs.febd8bfd5601685f7b0be0dab1583301b379c34914383eee2b6edde50e65c070"
obj= Airtable(token)
obj.get_bases()
obj.get_bases()
# obj.get_tables(base_id)
# obj.create_records(base_id,table_id,data)
# obj.update_record(base_id,table_id,record_id,data)
# obj.delete_record(base_id,table_id,record_id)
# obj.update_multiple_records(base_id,table_id,data1,data2,record_id1,record_id2)
# obj.delete_multiple_records(base_id,table_id,record_id1,record_id2)




