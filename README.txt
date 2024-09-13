# Circl API PRD

## Project Description
Circl project aims to develop a real-time messaging API that enables users to communicate instantly. The API will support **user registration**, **friend management**, **one-on-one messaging**, and **group chats**. This API will serve as the foundation for chat applications, providing essential features for seamless and interactive communication.

### Detailed Description
In today's digital age, real-time communication is crucial for both personal and professional interactions. This project will create an API that supports all necessary functionalities for a robust chat application. Here’s a detailed look at how users will interact with the app:

#### User Registration and Authentication:
* **Sign Up:** New users can create an account by providing a **username**, **email**, and **password**. A confirmation email will be sent to verify the account.

* **Login:** Registered users can log in using their **email** and **password**. For added security, **multi-factor authentication (MFA)** will be supported.

#### Friend Management:
* **Add Friends:** Users can send friend requests to other users. Once accepted, they can see each other’s online status and initiate chats.

* **Remove Friends:** Users can remove friends from their list, which will also end any ongoing chats with them.

#### One-on-One Messaging:
* **Send and Receive Messages:** Users can send text messages, images, and files to their friends in real-time. The API will **support delivery receipts and read receipts**.

* **View Chat History:** Users can view the history of their conversations, including sent and received messages.

#### Group Chats:
* **Create Group Chats:** Users can create group chats by adding multiple friends to a single conversation. They can name the group and set a group picture.

* **Manage Group Chats:** Users can add or remove members, change the group name, and update the group picture. All members will see the updated information.

* **Send and Receive Messages in Groups:** Users can send messages in group chats, with the ability to reply to specific messages and mention other users.

#### Real-Time Notifications:
* **Message Notifications:** Users will receive notifications for new messages, both in one-on-one chats and group chats.

* **Friend Request Notifications:** Users will receive notifications for incoming friend requests and when their friend requests are accepted.

## Real-World Example
Consider Emma, who uses Circl to stay in touch with her friends and coordinate group projects. Emma signs up for an account using her email and a secure password. After logging in, she adds her friends by sending them friend requests.

Emma starts a conversation with her friend John, sharing updates and exchanging images. They both see each other’s messages instantly, thanks to real-time messaging. Emma also creates a group chat for her study group, adding multiple friends. They use the group chat to share resources, discuss assignments, and plan meetings.

Whenever Emma receives a new message or a friend request, she gets a real-time notification, ensuring she stays updated on all interactions.

---
1. ### Introduction
    The Circl project aims to develop a comprehensive real-time messaging API that supports **user registration**, **friend management**, **one-on-one messaging**, and **group chats**. Users will be able to communicate instantly and manage their contacts and conversations effectively.

2. ### Objectives
    * Allow users to sign up, log in, and manage their accounts
    * Enable users to add and remove friends.
    * Support real-time one-on-one messaging.
    * Provide features for creating and managing group chats.
    * Ensure users receive real-time notifications for messages and friend requests.

3. ### Functional Requirements
    #### User Management
    * **Sign Up:** Users can create an account by providing a username, email, and password.
    * **Login:** Users can log in using their email and password.
    * **Profile Management:** Users can update their profile information.

    #### Friend Management
    * **Add Friends:** Users can send friend requests to other users.
    * **Remove Friends:** Users can remove friends from their list.

    #### Messaging
    * **Send and Receive Messages:** Users can send and receive text messages, images, and files.
    * **View Chat History:** Users can view their chat history.

    #### Group Chats
    * **Create Group Chats:** Users can create group chats and add friends.
    * **Manage Group Chats:** Users can add or remove members and update group details.
    * **Send and Receive Messages in Groups:** Users can communicate within group chats.

    #### Notifications
    * **Message Notifications:** Users receive notifications for new messages.
    * **Friend Request Notifications:** Users receive notifications for friend requests.

4. ### Non-Functional Requirements
    * **Scalability:** The API should handle a growing number of users and messages.
    * **Performance:** The API should have a fast response time and handle concurrent requests efficiently.
    * **Security:** Implement authentication and authorization mechanisms to protect user data.
    * **Reliability:** The API should be highly available and handle failures gracefully.
    * **Usability:** The API should be easy to use and well-documented.

5. ### Use Cases
    * User Sign Up and Login: New users sign up and existing users log in.
    * Friend Management: Users add and remove friends.
    * One-on-One Messaging: Users send and receive messages in private chats.
    * Group Chat Management: Users create and manage group chats.
    * Receive Notifications: Users receive notifications for new messages and friend requests.

6. ### User Stories
    * As a user, I want to sign up for an account so that I can chat with others.
    * As a user, I want to log in to my account so that I can access my chats.
    * As a user, I want to add friends so that I can chat with them.
    * As a user, I want to remove friends so that I can manage my contacts.
    * As a user, I want to send messages so that I can communicate in real-time.
    * As a user, I want to receive messages instantly so that I can stay updated.
    * As a user, I want to create group chats so that I can chat with multiple friends.
    * As a user, I want to manage group chats so that I can add or remove members.
    * As a user, I want to receive notifications for new messages so that I stay informed.
    * As a user, I want to receive notifications for friend requests so that I can manage my contacts.

7. ### Technical Requirements
    * Programming Language: Python.
    * Database: PostgreSQL, MongoDB.
    * Authentication: JWT for secure user authentication.
    * Real-Time Communication: WebSockets or a similar technology for real-time messaging.
    * API Documentation: Swagger or similar tools for API documentation.

8. ### API Endpoints
    * **User Management:**
        * POST /signup: Register a new user.
        * POST /login: Authenticate a user.
        * GET /profile: Get user profile details.
        * PUT /profile: Update user profile.

Friend Management
POST /friends/add: Send a friend request.
POST /friends/remove: Remove a friend.

Messaging
POST /messages: Send a new message.
GET /messages/{user_id}: Retrieve messages in a one-on-one chat.
GET /messages/group/{group_id}: Retrieve messages in a group chat.

Group Chats
POST /groups: Create a new group chat.
PUT /groups/{group_id}: Update group chat details.
POST /groups/{group_id}/add: Add a member to a group chat.
POST /groups/{group_id}/remove: Remove a member from a group chat.

Notifications
GET /notifications: Retrieve the user's notifications.

9. Security
Use HTTPS to encrypt data in transit.
Implement input validation and sanitization to prevent SQL injection and XSS attacks.
Use strong password hashing algorithms like bcrypt.

10. Performance
Implement caching strategies to improve response times.
Optimize database queries to handle large datasets efficiently.
Use load balancing to distribute traffic evenly across servers.

11. Documentation
Provide comprehensive API documentation using tools like Swagger.
Create user guides and developer documentation to assist with integration and usage.

12. Glossary
API: Application Programming Interface.
JWT: JSON Web Token.
CRUD: Create, Read, Update, Delete.
MFA: Multi-Factor Authentication.

13. Appendix
Include any relevant diagrams, data models, and additional references.



# Understanding the Requirements
Core entities and their relationships are:
* User: Has properties like ID, username, email, password, etc
* Friend: Represents a relationship between two users.
* Message: Can be a text, image, or file, associated with a sender, recipient(s), and a timestamp.
* Chat: A container for messages, can be one-on-one or a group.
* Group: A collection of users, with properties like name, description, etc.
* Notification: Represents a message sent to a user, indicating a new message, friend request, etc.

## Schemas
* **User**
```JSON
{
  "id": "uuid", // Unique identifier
  "username": "string",
  "email": "string",
  "password_hash": "string", // Hashed password
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

* **Friend**
```JSON
{
  "user_id": "uuid", // Foreign key to User
  "friend_id": "uuid", // Foreign key to User
  "status": "enum(pending, accepted, rejected)",
  "created_at": "datetime"
}
```

* **Message**
```JSON
{
  "id": "uuid",
  "sender_id": "uuid", // Foreign key to User
  "content": "string", // Text, image URL, or file reference
  "type": "enum(text, image, file)",
  "created_at": "datetime"
}
```

* **Chat**
```JSON
{
  "id": "uuid",
  "type": "enum(one_on_one, group)",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

* **Group**
```JSON
{
  "id": "uuid", // Same as chat_id for group chats
  "name": "string",
  "description": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

* **GroupMember**
```JSON
{
  "group_id": "uuid", // Foreign key to Group
  "user_id": "uuid", // Foreign key to User
  "joined_at": "datetime"
}
```

* **MessageRecipient**
```JSON
{
  "message_id": "uuid", // Foreign key to Message
  "recipient_id": "uuid", // Foreign key to User
  "read_at": "datetime" // Optional, for read receipts
}
```

* **ChatParticipant**
```JSON
{
  "chat_id": "uuid", // Foreign key to Chat
  "user_id": "uuid", // Foreign key to User
  "joined_at": "datetime"
}
```

* **Notification**
```JSON
{
  "id": "uuid",
  "user_id": "uuid", // Foreign key to User
  "type": "enum(message, friend_request, group_invite, etc.)",
  "message": "string", // Notification content
  "read": "boolean",
  "created_at": "datetime"
}
```

Additional Considerations
* Indexes: Create appropriate indexes for frequently queried fields (e.g., sender_id, recipient_id, created_at in Message, user_id in Friend, etc.) for performance optimization.
* Message Content: For images and files, consider storing references (URLs or paths) instead of the actual data in the Message table.
* Relationships: Define relationships between tables using foreign keys to establish data integrity.
* Data Types: Choose appropriate data types for fields (e.g., UUID for unique identifiers, datetime for timestamps).
* Normalization: Ensure data normalization to avoid redundancy and improve data integrity.
* Scalability: Consider partitioning or sharding strategies for handling large amounts of data.
