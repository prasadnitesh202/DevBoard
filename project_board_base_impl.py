import json
import datetime
from project_board_base import ProjectBoardBase
import random


class ImplProjectBoardBase(ProjectBoardBase):
    # create a board
    def create_board(self, request):
        new_entry = json.loads(request)
        with open("db/names.json") as rf:
            nameData = json.load(rf)
            rf.close()
        names = nameData['names']
        # print(names)

        name = new_entry['name']
        description = new_entry['description']
        # print(name)
        if name not in names and len(name) <= 64 and len(description) <= 128:
            nameData['names'].append(name)
            with open("db/TeamBoard.json") as read_file:
                board_data = json.load(read_file)
                size = len(board_data['data'])
                new_entry['board_id'] = str(size+1)
                board_data['data'].append(new_entry)
                read_file.close()
            with open("db/TeamBoard.json", 'w') as read_file:
                json.dump(board_data, read_file, indent=4)
                read_file.close()

            with open("db/names.json", 'w') as rf:
                json.dump(nameData, rf, indent=4)
                rf.close()
            response = json.dumps({"id": new_entry['board_id']})
        else:
            response = json.dumps(
                {"error": "Request Failed, please check the constraints"})
        return response

        # close a board

    def close_board(self, request):
        data = json.loads(request)
        board_id = data['id']
        with open("db/TeamBoard.json") as readfile:
            boardData = json.load(readfile)
            readfile.close()
        # print(boardData)
        taskList = []
        constPassed = True
        for data in boardData['data']:
            # print(data)
            if data['board_id'] == board_id:
                # print(data['task'])
                if "task" in data:
                    for taskDict in data['task']:
                        if taskDict['status'] != "CLOSED":
                            constPassed = False
                            break

        if constPassed:
            # print("Constraints Passed")
            for data in boardData['data']:
                if data['board_id'] == board_id:
                    data['status'] = "CLOSED"
                    data['end_time'] = str(datetime.datetime.now())
            # print(boardData)
            with open("db/TeamBoard.json", 'w') as rf:
                json.dump(boardData, rf, indent=4)
                rf.close()
            response = {"message": "Successfully Executed"}

        else:
            # print("Constraints Failed")
            response = {
                "message": "Failed!! Please check the data and constraints"}
        return json.dumps(response)

    def add_task(self, request):
        data = json.loads(request)
        board_name = data['name']
        task_title = data['title']
        description = data['description']
        user_id = data['user_id']
        creation_time = data['creation_time']
        task_status = "OPEN"
        with open("db/TeamBoard.json") as readfile:
            boardData = json.load(readfile)
            readfile.close()
        with open("db/taskid.json") as readfile:
            taskidData = json.load(readfile)
            readfile.close()
        with open("db/tasktitles.json") as readfile:
            tasktitles = json.load(readfile)
            readfile.close()

        taskidList = list(map(int, taskidData['data']))
        nextId = max(taskidList)+1
        taskidData['data'].append(str(nextId))

        for data in boardData['data']:
            if data['name'] == board_name:
                print(data['name'])
                if "task" not in data and len(task_title) <= 64 and len(description) <= 128 and task_title not in tasktitles['data']:
                    print("Not in task")
                    data['task'] = [{"taskid": str(nextId),
                                     "title": task_title,
                                     "description": description,
                                     "userid": user_id,
                                     "creationtime": creation_time,
                                     "status": task_status
                                     }]
                    tasktitles['data'].append(task_title)
                    # print(tasktitles)
                    with open("db/taskTitles.json", 'w') as read_file:
                        json.dump(tasktitles, read_file, indent=4)
                        read_file.close()
                    with open("db/taskid.json", 'w') as read_file:
                        json.dump(taskidData, read_file, indent=4)
                        read_file.close()
                    break

                    # break
                elif "task" in data and len(task_title) <= 64 and len(description) <= 128 and task_title not in tasktitles['data']:
                    data['task'].append({
                        "taskid": str(nextId),
                        "title": task_title,
                        "description": description,
                        "userid": user_id,
                        "creationtime": creation_time,
                        "status": task_status

                    })
                    # break
                    tasktitles['data'].append(task_title)
                    print(tasktitles)
                    with open("db/taskTitles.json", 'w') as read_file:
                        json.dump(tasktitles, read_file, indent=4)
                        read_file.close()
                    with open("db/taskid.json", 'w') as read_file:
                        json.dump(taskidData, read_file, indent=4)
                        read_file.close()
                    break
        with open("db/TeamBoard.json", 'w') as read_file:
            json.dump(boardData, read_file, indent=4)
            read_file.close()

        # print(boardData)
    def update_task_status(self, request):
        data = json.loads(request)
        task_id = data['id']
        task_status = data['status']
        with open("db/TeamBoard.json") as readfile:
            boardData = json.load(readfile)
            readfile.close()
        for data in boardData['data']:
            if "task" in data:
                for dictTask in data['task']:
                    if dictTask['taskid'] == task_id:
                        dictTask['status'] = task_status
                        with open("db/TeamBoard.json", 'w') as read_file:
                            json.dump(boardData, read_file, indent=4)
                            read_file.close()
                        resonse = {"message": "Task Updated Succefully"}
                        return json.dumps(resonse)

        return json.dumps({"message": "Failed!! Task not updated successfully"})

    def list_boards(self, request):
        data = json.loads(request)
        team_id = data['id']
        result = []
        with open("db/TeamBoard.json") as readfile:
            boardData = json.load(readfile)
            readfile.close()
        for data in boardData['data']:
            if data['team_id'] == team_id:
                temp = {}
                temp['id'] = data['board_id']
                temp['name'] = data['name']
                result.append(temp)
        return json.dumps({"data": result})
