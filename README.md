# Revlo API Specification

**Version 1**

https://api.revlo.co/1/

Welcome to the *Revlo API* Documentation. <PR STUFF HERE>


## Protocols Supported

* HTTPS

## Media Types Supported

* application/json


## Endpoints

### /rewards

**GET**

Rewards on your broadcaster account

*Optional Query Parameters*

```
page:
  type: Integer
  default: 1
```

*Example Request*

```
GET /1/rewards?page=1 HTTPS/1.1
x-api-key: MyApiToken
Accept: application/json
Host: api.revlo.co:443
Connection: close
```

*Response*

```
HTTPS/1.1 200 OK
Content-Type: application/json
X-Content-Type-Options: nosniff
Connection: close
Content-Length: 492

{"rewards":[{"reward_id":3,"created_at":"2016-11-17T21:07:47.762Z","title":"Display Random giphy","bot_command":"giphy","enabled":true,"points":300,"sub_only":false,"input_fields":[]},{"reward_id":2,"created_at":"2016-11-17T21:07:35.615Z","title":"Song Requests","bot_command":"song","enabled":true,"points":100,"sub_only":false,"input_fields":[]},{"reward_id":1,"created_at":"2016-11-17T21:07:24.924Z","title":"Reward Suggestions","bot_command":"suggestions","enabled":true,"points":1,"sub_only":false,"input_fields":[]}],"total":3,"page_size":25}
```

### /redemptions

**GET**

Reward redemptions on your broadcaster account.

*Optional Query Parameters*

```
page:
  type: Integer
  default: 1
```

*Example Request*

```
GET /1/redemptions?page=1 HTTP/1.1
x-api-key: MyApiToken
Accept: application/json
Host: api.revlo.co:443
Connection: close
```

*Response*

```
HTTPS/1.1 200 OK
Content-Type: application/json
X-Content-Type-Options: nosniff
Connection: close
Content-Length: 3385

{"redemptions":[{"reward_id":2,"redemption_id":26,"created_at":"2016-11-17T21:24:20.703Z","refunded":false,"completed":false,"user_input":{"song":
"https://www.youtube.com/watch?v=VN8GXJBJpr0"},"username":"youngster"},{"reward_id":2,"redemption_id":25,"created_at":"2016-11-17T21:24:17.069Z","refunded":false,"completed":false,"user_input":{"song":"https://www.youtube.com/watch?v=i25zLvU_xcs"},"username":"cooltrainer"},{"reward_id":2,"redemption_id":24,"created_at":"2016-11-17T21:24:15.802Z","refunded":false,"completed":false,"user_input":{"song":"https://www.youtube.com/watch?v=xMk8wuw7nek","username":"pokemaniac"},{"reward_id":2,"redemption_id":22,"created_at":"2016-11-17T21:24:12.621Z","refunded":false,"completed":false,"user_input":{"song":"https://www.youtube.com/watch?v=mRt0d1O4tiE"},"username":"bugcatcher"},..],"total":26,"page_size":25}
```

