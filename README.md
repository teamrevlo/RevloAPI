# Revlo API Specification

**Version 1**

https://api.revlo.co/1/

Welcome to the *Revlo API* Documentation. Here you can find everything needed to extend & build applications on top of Revlo's Rewards system. 

## Terms of Service
Usage of the Revlo API is bound by our [Terms of Service](https://www.revlo.co/p/legal/api-terms-of-service)

## Libraries

You can find our [Python client](http://github.com/teamrevlo/revlo-python-client) and [example](https://github.com/teamrevlo/revlo-python-client/tree/master/examples/) to help you get started!

If you wrote your own client and would like to share it with the community, feel free to reach out via email: scott@revlo.co, or any Staff member on [Discord](https://discord.gg/0gGuQOPSxJCe5xjd).

Community contributions:

* [NodeJS (Author: dbkynd)](https://www.npmjs.com/package/node-revlobot-api)

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
completed:
  type: Boolean (true or false)
refunded:
  type: Boolean (true or false)
```

*Example Request*

```
GET /1/redemptions?page=1&refunded=false HTTP/1.1
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

### /redemptions/`redemption_id`

**GET**

Get a specific redemption record.

*Example Request*
```
GET /1/redemptions/1337 HTTP/1.1
x-api-key: MyApiToken
Accept: application/json
Host: api.revlo.co:443
Connection: close
```

*Response*
```
HTTP/1.1 200 OK
Content-Type: application/json
X-Content-Type-Options: nosniff
Connection: close
Content-Length: 215

{"redemption":{"reward_id":2,"redemption_id":1337,"created_at":"2016-11-17T21:24:17.069Z","refunded":false,"completed":false,"user_input":{"song":"https://www.youtube.com/watch?v=mRt0d1O4tiE"},"username":"pokemaniac"}}
```

**PATCH**

Update the redemption record. Modifiable fields include: completed.

*Example Request*
```
PATCH /1/redemptions/1337 HTTP/1.1
x-api-key: MyApiToken
Accept: application/json
Host: api.revlo.co:443
Connection: close

{"completed": true}
```

*Response*
```
HTTP/1.1 200 OK
Content-Type: application/json
X-Content-Type-Options: nosniff
Connection: close
Content-Length: 215

{"redemption":{"reward_id":2,"redemption_id":1337,"created_at":"2016-11-17T21:24:17.069Z","refunded":false,"completed":true,"user_input":{"song":"https://www.youtube.com/watch?v=mRt0d1O4tiE"},"username":"pokemaniac"}}
```

### /fans/`username`/points

**GET**

Returns a loyalty object related to the broadcaster's account containing `current_points` earned through the broadcaster and `total_points` earned through the broadcaster.

*Example Request*

```
GET /1/fans/pokemaniac HTTPS/1.1
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

{"loyalty":{"fan":"pokemaniac","total_points":0,"current_points":0,"updated_at":"2016-09-14T16:02:00.000Z"}}
```


### /fans/`username`/points/bonus

**POST**

Bonus or subtract points to a fan. If subtracting more points than what a user currently has, the user's points is set to 0. Bonus points are restricted to +/- 1,000,000 points per call. 

*Required Parameters*

```
amount:
  type: Integer between -1000000 and 1000000
```

*Example Request*

```
POST /1/fans/pokemaniac HTTPS/1.1
x-api-key: MyApiToken
Accept: application/json
Host: api.revlo.co:443
Connection: close

{"amount": 100}
```

*Response*

```
HTTPS/1.1 200 OK
Content-Type: application/json
X-Content-Type-Options: nosniff
Connection: close
Content-Length: 492

{"loyalty":{"fan":"pokemaniac","total_points":0,"current_points":100,"updated_at":"2016-09-14T16:02:00.000Z"}}
```
