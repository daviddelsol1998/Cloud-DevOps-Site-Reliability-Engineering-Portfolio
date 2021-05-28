import requests

""" CREATE A USER """
# Call create user API (from postman)
# :)
# specify the function to be carried out
signupURL = "api/account/sign-up?otp_check=true"

# set a variable to equal the URL
pitch59_URL = f"https://api.p59.dev/{signupURL}"


# fake user info
emailId = "lakeramn21@gmail.com"
password = "BetterThanCap10"
body = {
    "firstName": "Test23",
    "lastName": "Test23",
    "isTesterUser": True,
    "contactNumber": "(999) 999-9457",
    "emailId": emailId,
    "password": password,
    "zipCode": "84440",
    "otpCode": 9865
}
# request information from endpoint according to listed arguments
response = requests.post(pitch59_URL, json=body)
# check for successful request
if response.status_code == 200:
    # convert data to a python dictionary
    print(response.status_code, "- Create User Success!", "\n")
    data_dict = response.json()["data"]
    userId = data_dict["userId"]
    userToken = data_dict["token"]
    print(response.json())
else:
    # The request failed- print the status code:
    print("Failure with status code:", response.status_code)
    print(response.json())

""" DELETE A USER"""
# Call Delete user API (from postman)
deleteURL = f"api/users/{userId}/deleteTestUser"
pitch59_URL = f"https://api.p59.dev/{deleteURL}"
body = {}
head = {
    "content-type": "application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Authorization": f"bearer {userToken}"
}
# request information from endpoint according to listed arguments

response = requests.post(pitch59_URL, data=body, headers=head)

# check for successful request
# print(response.status_code)
if response.status_code == 200:
    # convert data to a python dictionary

    print(response.status_code, "- Successfully deleted! :D")


else:
    # The request failed- print the status code:
    print("Failure with status code:", response.status_code)
    print(response.json())
