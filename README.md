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

- ## ImplProjBoardBase
  - Create an object of this class and call the api methods,
  - example:  
    obj1=ImplProjBoardBase()
  - obj1.api_methods() will calL the api methods
    <br> <br>
- ### Below are the API Methods implented by this class

<br>

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

  - add_task(request)

        :param request: A json string with the task details. Task is assigned to a user_id who works on the task
        {
            "title" : "<board_name>",
            "description" : "<description>",
            "user_id" : "<team id>"
            "creation_time" : "<date:time when task was created>"
        }
        :return: A json string with the response {"id" : "<task_id>"}

        Constraint:
         * task title must be unique for a board
         * title name can be max 64 characters
         * description can be max 128 characters

        Constraints:
        * Can only add task to an OPEN board
        """

  - update_task_status(request)
    :param request: A json string with the user details
    {
    "id" : "<task_id>",
    "status" : "OPEN | IN_PROGRESS | COMPLETE"
    }
  - list_boards(request)

            :param request: A json string with the team identifier
            {
              "id" : "<team_id>"
            }

            :return:
            [
              {
                "id" : "<board_id>",
                "name" : "<board_name>"
              }
            ]

    <br> <br>

- ## ImplUserBase

  - Create an object of this class and call the api methods,
  - example:  
    obj1=ImplUserBase()
  - obj1.api_methods() will calL the api methods
    <br> <br>

- ### Below are the API Methods implented by this class

<br>

- create_user(request)

        :param request: A json string with the user details
        {
          "name" : "<user_name>",
          "display_name" : "<display name>"
        }
        :return: A json string with the response {"id" : "<user_id>"}

        Constraint:
            * user name must be unique
            * name can be max 64 characters
            * display name can be max 64 characters

- list_users(request)
  :return: A json list with the response
  [
  {
  "name" : "<user_name>",
  "display_name" : "<display name>",
  "creation_time" : "<some date:time format>"
  }
  ]
- describe_user(request)

        :param request: A json string with the user details
        {
          "id" : "<user_id>"
        }

        :return: A json string with the response

        {
          "name" : "<user_name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>"
        }

- update_user(request)

        :param request: A json string with the user details
        {
          "id" : "<user_id>",
          "user" : {
            "name" : "<user_name>",
            "display_name" : "<display name>"
          }
        }

        Constraint:
            * user name cannot be updated
            * name can be max 64 characters
            * display name can be max 128 characters

- get_user_teams(request)

        :param request:
        {
          "id" : "<user_id>"
        }

        :return: A json list with the response.
        [
          {
            "name" : "<team_name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>"
          }
        ]
        <br><br>

<br><br>

- ## ImplTeamBase

  - Create an object of this class and call the api methods,
  - example:  
    obj1=ImplTeamBase()
  - obj1.api_methods() will calL the api methods
    <br> <br>

- ### Below are the API Methods implented by this class

<br>

- create_team(request)

        :param request: A json string with the team details
        {
          "name" : "<team_name>",
          "description" : "<some description>",
          "admin": "<id of a user>"
        }
        :return: A json string with the response {"id" : "<team_id>"}

        Constraint:
            * Team name must be unique
            * Name can be max 64 characters
            * Description can be max 128 characters


- list_teams()
        :return: A json list with the response.
        [
          {
            "name" : "<team_name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>",
            "admin": "<id of a user>"
          }
        ]
- describe_team(request)

        :param request: A json string with the team details
        {
          "id" : "<team_id>"
        }

        :return: A json string with the response

        {
          "name" : "<team_name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>",
          "admin": "<id of a user>"
        }

- update_team(request)

        :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "team" : {
            "name" : "<team_name>",
            "description" : "<team_description>",
            "admin": "<id of a user>"
          }
        }

        :return:

        Constraint:
            * Team name must be unique
            * Name can be max 64 characters
            * Description can be max 128 characters


- add_users_to_team(request)

        :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "users" : ["user_id 1", "user_id2"]
        }

        :return:

        Constraint:
        * Cap the max users that can be added to 50


- remove_users_from_team(request)

        :param request: A json string with the team details
        {
          "id" : "<team_id>",
          "users" : ["user_id 1", "user_id2"]
        }

        :return:

        Constraint:
        * Cap the max users that can be added to 50


- list_team_users(request)

        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<user_id>",
            "name" : "<user_name>",
            "display_name" : "<display name>"
          }
        ]
