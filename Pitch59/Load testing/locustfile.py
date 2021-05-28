from locust import HttpUser, task, between


class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # initialize user data
        self.data = """{"firstName": "Tony", 
                     "lastName": "Stark",
                     "isTesterUser": true,
                     "contactNumber": "(999) 999-9986",
                     "emailId": "ironman99@gmail.com",
                     "profilePictureThumbnailId": "",
                     "profilePictureThumbnailUrl": "",
                     "profilePictureFileId": "",
                     "password": "BetterThanCap10",
                     "zipCode": "84440",
                     "userReferralModel": {
                         "userName": "",
                         "referralEmail": "help@pitch59.com",
                         "referralPhone": "",
                         "senderEmail": ""
                     },
                     "otpCode": 9865}"""

    @task(1)
    def post(self):
        response = self.client.post(url='https://api.p59.dev/api/account/sign-up?otp_check=true',
                                    headers={"content-type": "application/json"}, data=self.data)  # create user
        json_response_dict = response.json()
        userid = json_response_dict["data"]["userId"]
        token = json_response_dict["data"]["token"]
        self.client.post(url=f'https://api.p59.dev/api/users/{userid}/deleteTestUser',
                         headers={"Authorization": "bearer " + token})  # delete user
