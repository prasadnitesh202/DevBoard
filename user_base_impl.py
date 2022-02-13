import json
from user_base import UserBase


class ImplUserBase(UserBase):
    # create a user
    def create_user(self, request):
        new_entry = json.loads(request)
        with open("db/userNames.json") as rf:
            usernameData = json.load(rf)
            rf.close()
        usernames = usernameData['usernames']
        username = new_entry['name']
        displayName = new_entry['displayname']

        if username not in usernames and len(username) <= 64 and len(displayName) <= 64:
            usernameData['usernames'].append(username)
            with open("db/User.json",) as read_file:
                user_data = json.load(read_file)
                # print(user_data)
                size = len(user_data['data'])
                # print(size)
                new_entry['userid'] = str(size+1)
                # print(new_entry)
                user_data['data'].append(new_entry)
                read_file.close()
            with open("db/User.json", 'w') as read_file:
                json.dump(user_data, read_file, indent=4)
                read_file.close()
            with open("db/usernames.json", 'w') as rf:
                json.dump(usernameData, rf, indent=4)
                rf.close()
            response = json.dumps({"id": new_entry['userid']})
        else:
            response = json.dumps(
                {"error": "Request Failed, please check the constraints"})
        return response

        # list all users
    def list_users(self):
        with open("db/User.json") as rf:
            userData = json.load(rf)
            rf.close()
        filter_fields = ['name', 'displayname', 'creation_time']
        result = {"data": []}
        for dictUser in userData['data']:
            dict_result = {key: dictUser[key]
                           for key in dictUser if key in filter_fields}
            result['data'].append(dict_result)
        # print(result)
        # print(userData)
        return json.dumps(result)

        # userData['data'])
    def describe_user(self, request):
        data = json.loads(request)
        userid = data['id']
        with open("db/User.json") as rf:
            userData = json.load(rf)
            rf.close()
        result = {}
        for data in userData['data']:
            if data['userid'] == userid:
                result['name'] = data['name']
                result['creation_time'] = data['creation_time']
                break

        return json.dumps(result)

    def update_user(self, request):
        data = json.loads(request)
        userid = data['id']
        oldData = {}
        new_display_name = data['user']['display_name']
        if len(new_display_name) <= 128:
            with open("db/User.json") as rf:
                userData = json.load(rf)
                rf.close()
            for entry in userData['data']:
                if entry['userid'] == userid:
                    oldData['data'] = entry
                    oldData['data']['displayname'] = new_display_name
                    userData['data'].remove(entry)
                    userData['data'].append(oldData['data'])
                    with open("db/User.json", 'w') as rf:
                        json.dump(userData, rf, indent=4)
                        rf.close()
                    break

            response = json.dumps(
                {"message": "Success"})
        else:
            response = json.dumps(
                {"message": "Request Failed, please check the constraints"})
        return response

    def get_user_teams(self, request):
        data = json.loads(request)
        userid = data['id']
        listTeams = []
        with open("db/User.json") as rf:
            userData = json.load(rf)
            rf.close()
        with open("db/Team.json") as rf:
            teamData = json.load(rf)
            rf.close()
        for data in teamData['data']:
            for uid in data['admin']:
                if uid == userid:
                    listTeams.append(data)
        # print(listTeams)
        result = {"data": []}
        temp = {}
        for resDict in listTeams:
            temp['name'] = resDict['name']
            temp['description'] = resDict['description']
            temp['creation_time'] = resDict['creation_time']
            result['data'].append(temp)
        # print(result)
        return result
