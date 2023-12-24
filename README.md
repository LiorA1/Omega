# Omega
Abra Home Assignment

There is a local DB with 3 users and messages between them.

### Endpoints -
GET /users_messages/ - Retrieve all messages that current user (logged in) is the `owner`.
POST /users_messages/ - Create a message (automatically associated with current user)
{
    "receiver": <some_id: int>,
    "subject": <char_field: char>,
    "body": <char_field: char>
}

DELETE /users_messages/<message_id: int>/ 
Delete a message only if current user is its `owner` or `receiver`.


GET /users_messages/<message_id: int>/ 
Retrieve a single message only for its `owner` or `receiver`.
If current user is the `receiver`, the message will be flagged as "read".


GET /users_messages/inbox/[?is_read=[1/0/False/True]]
Retrieve list of messages which was sent to current user, with a possibility to view only those that wasn't watched before. 


Note: there was an issue with Django5, so downgraded it to 4.2.7.
