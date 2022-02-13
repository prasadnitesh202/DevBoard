from project_board_base import ProjectBoardBase
from project_board_base_impl import ImplProjectBoardBase
import datetime
import json
from team_base_impl import ImplTeamBase

from user_base_impl import ImplUserBase

# x = {
#     "name": "Test3",
#     "description": "Developers of Automations in TOC",
#     "team_id": "12",
#     "creation_time": str(datetime.datetime.now())
# }

# x = {
#     "name": "PfXEBUa8ai57D6fsITzoJgQ37gu7tZciaW2FtHRoqdpyvw",
#     "displayname": "Nitesh Prasad",
#     "creation_time": str(datetime.datetime.now())

# }


# req = json.dumps(x)
obj1 = ImplProjectBoardBase()
# print(obj1.create_board(req))


obj2 = ImplUserBase()
# print(obj2.create_user(req))
# print(obj2.list_users())
# data = {
#     "id": "1"
# }
# print(obj2.describe_user(json.dumps(data)))

# data = {
#     "id": "10",
#     "user": {
#         "name": "jayesh",
#         "display_name": "Mishraji Jayesh"
#     }
# }
# print(obj2.update_user(json.dumps(data)))

obj3 = ImplTeamBase()
team = {
    "name": "IB-Tech",
    "description": "Team is responsible for application development in IB",
    "admin": ["8", "9"]
}
teamJson = json.dumps(team)
# print(obj3.create_team(teamJson))
# print(obj3.list_teams())
# print(obj3.describe_team(json.dumps({"id": "5"})))

updatedata = {
    "id": "5",
    "team": {
        "name": "IB-TECH-16",
        "description": "HANDLES TECH OPS IN IB",
        "admin": ["12"]
    }
}
# print(obj3.update_team(json.dumps(updatedata)))

addUsers = {
    "id": "5",
    "users": ["1", "2", "8", "9"]
}


# print(obj3.add_users_to_team(json.dumps(addUsers)))
# print(obj3.remove_users_from_team(json.dumps(addUsers)))

# print(obj3.list_team_users(json.dumps({"id": "5"})))

# print(obj2.get_user_teams(json.dumps({"id": "2"})))
# print(obj1.close_board(json.dumps({"id": "2"})))


taskadd = {
    "name": "TS-Automation-Enablement-1",
    "title": "Test7",
    "description": "<description>",
    "user_id": "<team id>",
    "creation_time": "<date:time when task was created>"
}
# obj1.add_task(json.dumps(taskadd))


# print(obj1.update_task_status(json.dumps(
#     {"id": "6", "status": "IN PROGRESS"})))

print(obj1.list_boards(json.dumps({"id": "141"})))
