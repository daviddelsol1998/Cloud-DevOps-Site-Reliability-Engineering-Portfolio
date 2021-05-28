
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
