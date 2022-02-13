# Implementation of Team Project Planner Tool

## Base classes are implemented in:

- project_board_base_impl.py
- team_base_impl.py
- user_base_impl.py

- client.py is used to create objects of the abover classes and utilise the api methods

- ### db folder containes JSON files which are used for local file storage persistence

## JSON File Structures

- TeamBoard.json

```json
  - {
    "data": [
        {
            "board_id": "",
            "name": "",
            "description": "",
            "team_id": "",
            "creation_time": "",
            "status": "",
            "task": [
                {
                    "taskid": "",
                    "title": "",
                    "description": "",
                    "userId": "",
                    "creationtime": "",
                    "status": "",
                }
            ],
            "end_time": "",
        }
    ]
}
```

- Team.json

```json
{
  "data": [
    {
      "team_id": "",
      "name": "",
      "description": "",
      "admin": [],
      "creation_time": ""
    }
  ]
}
```

- User.json

```json
{
  "data": [
    {
      "userid": "",
      "name": "",
      "displayname": "",
      "creation_time": ""
    }
  ]
}
```

- names.json, taskid.json, taskTitles.json,teamNames.json and userNames.json were created for utility purposes in order to enable api methods to follow the provided constraints

### API Methods:

- ImplProjBoardBase

  - create_board(request)

        :param request: A json string with the board details.
        {
            "name" : "<board_name>",
            "description" : "<description>",
            "team_id" : "<team id>"
            "creation_time" : "<date:time when board was created>"
        }
        :return: A json string with the response {"id" : "<board_id>"}

        Constraint:
         * board name must be unique for a team
         * board name can be max 64 characters
         * description can be max 128 characters

  - close_board(request)

         :param request: A json string with the user details
        {
          "id" : "<board_id>"
        }

        :return:

        Constraint:
          * Set the board status to CLOSED and record the end_time date:time
          * You can only close boards with all tasks marked as COMPLETE
        """
