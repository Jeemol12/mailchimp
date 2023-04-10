import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

class Mailchimp_Marketing:
    def __init__(self,Apikey,server):
        self.Apikey = Apikey
        self.server = server

        
    def get_lists(self):
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.server
          })

          response = client.lists.get_all_lists()       
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))


    
    def create_lists_members(self,list_id,data):
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.server
          })
    
          response = client.lists.add_list_member(list_id,data)         
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))

    def get_lists_members(self,list_id):
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.server
          })

          response = client.lists.get_list_members_info(list_id)       
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))
          
          
          
    def update_lists_members(self,list_id,email_address):
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.Apikey
          })

          response = client.lists.update_list_member(list_id, email_address, {})
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))
          
    def delete_lists_members(self,list_id,email_address):
        
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.Apikey
          })
        
          response = client.lists.delete_list_member_permanent(list_id, email_address)
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))
          
    def create_list(self,data1):      
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.server
          })
    
          response = client.lists.create_list(data1)          
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))
        
    def update_list(self,list_id,data2):
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.server
          })

          response = client.lists.update_list(list_id,data2)         
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))
          
    def delete_list(self,list_id):
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.server
          })

          response = client.lists.delete_list(list_id)          
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))
          
          
    def get_campaigns(self):
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.server
          })
        
          response = client.campaigns.list()          
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))

    def send_test_email(self,campaign_id,send_type,test_emails):
        try:
          client = MailchimpMarketing.Client()
          client.set_config({
            "api_key": self.Apikey,
            "server": self.server
          })
        
          response = client.campaigns.send_test_email(campaign_id, {"test_emails": test_emails, "send_type": send_type})
          return response
        except ApiClientError as error:
          print("Error: {}".format(error.text))

             
class Mailchimp_Transactional:      
    def __init__(self,API_Key):
        self.API_Key = API_Key
        
    def send_email(self,message):
        try:
          client = MailchimpTransactional.Client(self.API_Key)
          response = client.messages.send({"message": message})
          return response
        except ApiClientError as error:
          print("An exception occurred: {}".format(error.text))
          
    def send_email_using_template(self,template_name,template_content,message):
      
        try:
          client = MailchimpTransactional.Client(self.API_Key)
          response = client.messages.send_template({"template_name": template_name, "template_content": [template_content], "message": message})
          return response
        except ApiClientError as error:
          print("An exception occurred: {}".format(error.text))
            
   
       

Apikey = "819b640543e2d573f80c21d686267f00-us21"    
server = "us21"
obj_M= Mailchimp_Marketing(Apikey,server)
# obj_M.get_lists()
# obj_M.create_lists_members(list_id,data)
# obj_M.get_lists_members(list_id)
# obj_M.update_lists_members(list_id,email_address)
# obj_M.delete_lists_members(list_id,email_address)
# obj_M.create_list(data1)
# obj_M.update_list(list_id,data2)
# obj_M.delete_list(list_id)
# obj_M.get_campaigns()
# obj_M.send_test_email(campaign_id,send_type,test_emails)

API_Key = "md-HJ01WiVYhBxJCyd5wjl0hQ"
obj_T= Mailchimp_Transactional(API_Key)
# message like a dictionary include from , to, subject etc..
# obj_T.send_email(message)
# obj_T.send_email_using_template(template_name,template_content,message)





