import json
import unittest
from time import sleep

import requests
service = 'um'

class MyTestCase(unittest.TestCase):

    def setUp(self):
        session = requests.session()
        self.host = 'http://192.168.5.25/user-management/'  # development server
        # self.host = 'https://192.168.5.30/esscom-um/'  # development server
        # self.host = 'http://localhost:8080/' # localhost
        login_data = {"inputEmail3": "admin@mail.com", "inputPassword3": "111111"}
        print("\n")
        # r = requests.head(self.host + "auth/login", json=login_data, allow_redirects=True)
        # r.headers.get('Location')
        r = session.post(self.host + "auth/login", data=login_data, verify=False)
        # r = requests.post(self.host + "auth/login", json=login_data, verify=False)
        # r = requests.post(self.host + "auth/login", data=login_data, verify=False, follow_redirects=False)
        # r = requests.head(self.host + "auth/login", data=login_data, verify=False, allow_redirects=True)

        # r = requests.post('http://github.com', allow_redirects=False)
        # print(r.status_code, r.headers)
        # self.assertEqual(r.status_code, 200)
        # self.assertEqual(r.headers['Content-Type'], "application/json")
        # # print(r.headers['Location'])
        # data = r.text
        result = r.text[423:455]
        # print(result)
        # print(data)
        # data['global_id'][0]
        # data = json.loads(r.text)
        print("API Login\n")
        # # # Assign data to variable
        self.userid = result
        # self.token = 'asf32rdfq234rq4rfew'

        print("\nlogin one time")

    def test_list_user(self):
        # print(self.host, " ", self.userid)
        r = requests.get((self.host + 'user/users/{"pagenum":1,"name":"a","email":"a","role":'
                                      '{"id":"41b6d48523634962ba9544fb06d3608f","name":"Normal User",'
                                      '"$$hashKey":"object:1039"},"position":{"id":"134a5ca0a27441638a146a801a5d8612",'
                                      '"name":"Staff","$$hashKey":"object:1042"},"pta":"na",'
                                      '"agency":"07f7f203a7404f1780eb5274db3f4ce7"}?iu=' + self.userid), verify=False)
        print(r.status_code, ' ', r.headers['Content-Type'])
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], "application/json")
        data2 = json.loads(r.text)
        print("API List User\n")
        print(data2)

    def test_view_user(self):
        # print(self.host, " ", self.userid)
        r = requests.get((self.host + 'user/api/' + self.userid + '?iu=' + self.userid), verify=False)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], "application/json")
        data2 = json.loads(r.text)
        print("API View User\n")
        print(data2)

    def test_register_user(self):
        # print(self.host, " ", self.userid)
        json_data = {"data": '{"name":"aideed","phone":"0163603554","email":"aideed@mail.com",'
                             '"role":"41b6d48523634962ba9544fb06d3608f","position":"134a5ca0a27441638a146a801a5d8612",'
                             '"pta":"na","agency":"07f7f203a7404f1780eb5274db3f4ce7"}'}
        r = requests.post(self.host + 'user/api?iu=' + self.userid, data=json_data, verify=False)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], "application/json")
        data2 = json.loads(r.text)
        # data2 = r.text
        # print(data2['taskId'])
        sleep(2)
        status_post = requests.get(self.host + 'user/status_add/' + data2['taskId'] + '?iu=' + self.userid,
                                   verify=False)
        status_post = json.loads(status_post.text)
        print(status_post)
        print("API Register User\n")
        print(data2)

    def test_user_update_profile(self):
        # print(self.host, " ", self.userid)
        json_data = {"data": '{"name":"wan aideed","phone":"0163603554","email":"aideed@mail.com",'
                             '"role":{"id":"41b6d48523634962ba9544fb06d3608f","name":"Normal User"},'
                             '"position":{"id":"134a5ca0a27441638a146a801a5d8612","name":"Staff"},'
                             '"pta":{"id":"na","name":"N/A"},"agency":{"id":"07f7f203a7404f1780eb5274db3f4ce7",'
                             '"name":"Majlis Perbandaran Kajang (MPKJ)"},"old_pic":null,"password":""}'}
        r = requests.patch(self.host + 'user/api/7315c482e3d94d1c9bc5620b59884e69?iu=' + self.userid, data=json_data,
                           verify=False)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], "application/json")
        # data2 = json.loads(r.text)
        data2 = r.text
        print("API Update Profile\n")
        print(data2)
    #
    # def test_user_forgot_password(self):
    #     print(self.host, " ", self.userid)
    #     json_data = {"email": "admin@mail.com"}
    #     r = requests.post(self.host + 'auth/forgot_password', json=json_data, verify=False)
    #     self.assertEqual(r.status_code, 200)
    #     self.assertEqual(r.headers['Content-Type'], "application/json")
    #     # data2 = json.loads(r.text)
    #     data2 = r.text
    #     print("API Forgot Password\n")
    #     print(data2)
    #
    # def test_user_change_password(self):
    #     print(self.host, " ", self.userid)
    #     json_data = {"password": "P@ssw0rd123"}
    #     r = requests.post(self.host + 'user/change_password/' + self.userid, json=json_data, verify=False)
    #     self.assertEqual(r.status_code, 200)
    #     self.assertEqual(r.headers['Content-Type'], "application/json")
    #     # data2 = json.loads(r.text)
    #     data2 = r.text
    #     print("API Forgot Password\n")
    #     print(data2)

    # def test_user_reset_password(self):
    #     print(self.host, " ", self.userid)
    #     json_data = {"token": "admin@mail.com"}
    #     r = requests.post(self.host + 'reset_password' + self.token, json=json_data, verify=False)
    #     self.assertEqual(r.status_code, 200)
    #     self.assertEqual(r.headers['Content-Type'], "application/json")
    #     # data2 = json.loads(r.text)
    #     data2 = r.text
    #     print("API Reset Password\n")
    #     print(data2)

    def test_list_roles(self):
        # print(self.host, " ", self.userid)
        r = requests.get((self.host + 'user/roles?iu=' + self.userid), verify=False)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], "application/json")
        data2 = json.loads(r.text)
        print("API List Roles\n")
        print(data2)

    def test_list_positions(self):
        # print(self.host, " ", self.userid)
        r = requests.get((self.host + 'user/positions?iu=' + self.userid), verify=False)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], "application/json")
        data2 = json.loads(r.text)
        print("API List Positions\n")
        print(data2)

    def test_list_agency(self):
        # print(self.host, " ", self.userid)
        r = requests.get((self.host + '../agency_be/report/list_agensi?iu=' + self.userid), verify=False)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], "application/json")
        data2 = json.loads(r.text)
        print("API List Agency/PTA\n")
        print(data2)

    # ------------------------------ Uncomment below script to test delete ------------------------------------------
    def test_delete_user(self):
        print(self.host, " ", self.userid)
        json_data = {"id": ["93b5ce40c72640828214ab72eb6e3326"]}
        task_id = "a598d0c3-519a-444e-a1e2-34fe178b3fd8"
        r = requests.delete(self.host + 'user/api?iu=' + self.userid, data=json_data, verify=False)
        self.assertEqual(r.status_code, 200)
        data2 = r.text

        sleep(2)
        status_post = requests.get(self.host + 'user/status_delete/' + task_id + '?iu=' + self.userid,
                                   verify=False)
        status_post = json.loads(status_post.text)
        print(status_post)
        print("API Delete Single User\n")
        # print(data2)
    #
    # def test_multiple_delete_user(self):
    #     print(self.host, " ", self.userid)
    #     json_data = {"data": ["4b9c18bb0d8e4633b268e813cb793f91", "8143e0ca72764c58977c154906a71116"]}
    #     r = requests.delete(self.host + 'user/delete_multiple/' + self.userid, json=json_data, verify=False)
    #     self.assertEqual(r.status_code, 200)
    #     data2 = r.text
    #     print("API Target Delete Multiple Dossier\n")
    #     print(data2)

    def tearDown(self):
        print('Done')

#
# if __name__ == '__main__':
#     unittest.main()


if __name__ == '__main__':
    import xmlrunner

    runner = xmlrunner.XMLTestRunner(output=service)
    unittest.main(testRunner=runner)
    unittest.main()
