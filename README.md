# Omega
Abra Home Assignment

There is a local DB with 3 users and messages between them.<br/>
Names: abra1, abra2, abra3 (their names are also the password)<br/>

### Endpoints -
#### GET 
`/users_messages/` - Retrieve all messages that current user (logged in) is the `owner`. <br/>

`/users_messages/<message_id: int>/ `<br/>
Retrieve a single message only for its `owner` or `receiver`.<br/>
If current user is the `receiver`, the message will be flagged as "read". <br/>


`/users_messages/inbox/[?is_read=[1/0/False/True]]` <br/>
Retrieve list of messages which was sent to current user, <br/>
with a possibility to view only those that wasn't watched before. (using `is_read` query parameter)

#### POST 
`/users_messages/` - Create a message (automatically associated with current user)<br/>
{<br/>
    "receiver": <some_id: int>,<br/>
    "subject": <char_field: char>,<br/>
    "body": <char_field: char><br/>
}<br/>


#### DELETE 
`/users_messages/<message_id: int>/ ` <br/>
Delete a message only if current user is its `owner` or `receiver`.<br/>


### Notes

1. There was an issue with Django5, so downgraded it to 4.2.7.
