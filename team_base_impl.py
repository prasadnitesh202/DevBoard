import datetime
import json
from team_base import TeamBase


class ImplTeamBase(TeamBase):
    def create_team(self, request):
        new_entry = json.loads(request)
        # with open("db/userNames.json") as rf:
        #     usernameData = json.load(rf)
        # rf.close()
        # usernames = usernameData['usernames']
        # username = new_entry['name']
        # displayName = new_entry['displayname']
        new_entry['creation_time'] = str(datetime.datetime.now())
        # print(new_entry)
        with open("db/teamNames.json") as rf:
            teamnameData = json.load(rf)
            rf.close()
        teamnames = teamnameData['names']
        # print(teamnames)
        teamname = new_entry['name']
        description = new_entry['description']
        if teamname not in teamnames and len(teamname) <= 64 and len(description) <= 128:
            teamnameData['names'].append(teamname)
            with open("db/Team.json",) as read_file:
                team_data = json.load(read_file)
                # print(user_data)
                size = len(team_data['data'])
                # print(size)
                new_entry['team_id'] = str(size+1)
                # print(new_entry)
                team_data['data'].append(new_entry)
                read_file.close()
            with open("db/Team.json", 'w') as read_file:
                json.dump(team_data, read_file, indent=4)
                read_file.close()
            with open("db/teamNames.json", 'w') as rf:
                json.dump(teamnameData, rf, indent=4)
                rf.close()
            response = json.dumps({"id": new_entry['team_id']})
        else:
            response = json.dumps(
                {"error": "Request Failed, please check the constraints"})
        return response

    def list_teams(self):
        with open("db/Team.json") as rf:
            teamData = json.load(rf)
            rf.close()
        filter_fields = ['name', 'description', 'creation_time', 'admin']
        result = {"data": []}
        for dictUser in teamData['data']:
            dict_result = {key: dictUser[key]
                           for key in dictUser if key in filter_fields}
            result['data'].append(dict_result)
        # print(result)
        # print(userData)
        return json.dumps(result)

    def describe_team(self, request):
        data = json.loads(request)
        teamid = data['id']
        with open("db/Team.json") as rf:
            teamData = json.load(rf)
            rf.close()
        result = {}
        for data in teamData['data']:
            if data['team_id'] == teamid:
                result['name'] = data['name']
                result['creation_time'] = data['creation_time']
                result['description'] = data['description']
                result['admin'] = data['admin']
                break

        return json.dumps(result)

    def update_team(self, request):
        data = json.loads(request)
        with open("db/teamNames.json") as rf:
            teamnameData = json.load(rf)
            rf.close()
        teamnames = teamnameData['names']
        teamid = data['id']
        oldData = {}
        new_team_name = data['team']['name']
        new_description = data['team']['description']
        new_admin = data['team']['admin']
        with open('db/Team.json') as rf:
            td = json.load(rf)
            rf.close()
        for data in td['data']:
            if data['team_id'] == teamid:
                old_team_name = data['name']
                break

        if new_team_name not in teamnames and len(new_team_name) <= 64 and len(new_description) <= 128:

            with open("db/Team.json") as readfile:
                teamData = json.load(readfile)
                readfile.close()
            for entry in teamData['data']:
                if entry['team_id'] == teamid:
                    oldData['data'] = entry
                    oldData['data']['name'] = new_team_name
                    oldData['data']['description'] = new_description
                    oldData['data']['admin'] = new_admin
                    oldName = entry['name']
                    teamData['data'].remove(entry)
                    teamData['data'].append(oldData['data'])
                    with open("db/Team.json", 'w') as rf:
                        json.dump(teamData, rf, indent=4)
                        rf.close()
                    teamnameData['names'].append(new_team_name)
                    teamnameData['names'].remove(old_team_name)
                    with open("db/teamNames.json", 'w') as wf:
                        json.dump(teamnameData, wf, indent=4)
                        rf.close()
                    break

            response = json.dumps(
                {"message": "Success"})
        else:
            response = json.dumps(
                {"message": "Request Failed, please check the constraints"})
        return response

    def add_users_to_team(self, request):
        data = json.loads(request)
        teamid = data['id']
        users = data['users']
        with open("db/Team.json") as readfile:
            teamData = json.load(readfile)
            readfile.close()
        with open("db/teamNames.json") as rf:
            teamnameData = json.load(rf)
            rf.close()
        for data in teamData['data']:
            if data['team_id'] == teamid:
                for val in users:
                    if val not in data['admin'] and len(data['admin']) <= 49:
                        data['admin'].append(val)
                # print(data)
        with open("db/Team.json", 'w') as rf:
            json.dump(teamData, rf, indent=4)
            rf.close()
        return json.dumps({"message": "Succesfully Executed"})

    def remove_users_from_team(self, request):
        data = json.loads(request)
        teamid = data['id']
        users = data['users']
        with open("db/Team.json") as readfile:
            teamData = json.load(readfile)
            readfile.close()
        with open("db/teamNames.json") as rf:
            teamnameData = json.load(rf)
            rf.close()
        for data in teamData['data']:
            if data['team_id'] == teamid:
                for val in users:
                    if val in data['admin']:
                        data['admin'].remove(val)
                # print(data)
        # print(teamData)
        with open("db/Team.json", 'w') as rf:
            json.dump(teamData, rf, indent=4)
            rf.close()
        return json.dumps({"message": "Succesfully Executed"})

    def list_team_users(self, request):
        data = json.loads(request)
        teamid = data['id']
        userids = []
        result = {"data": []}
        result2 = []
        with open("db/Team.json") as readfile:
            teamData = json.load(readfile)
            readfile.close()
        for data in teamData['data']:
            if data['team_id'] == teamid:
                userids = data['admin']
        # print(userids)
        with open("db/User.json") as readfile:
            userData = json.load(readfile)
            readfile.close()
        for data in userData['data']:
            for uid in userids:
                if data['userid'] == uid:
                    result['data'].append(data)
        # print(result)
        temp = {}
        resJson = {"data": []}
        for resdict in result['data']:
            # print(resdict)
            temp['name'] = resdict['name']
            temp['displayname'] = resdict['displayname']
            temp['userid'] = resdict['userid']
            resJson['data'].append(temp)
        return json.dumps(resJson)
