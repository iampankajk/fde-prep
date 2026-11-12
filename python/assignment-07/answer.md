Q1. Using the restaurant analogy (see Setup), explain client, server, request, response and API. Then say
what "HTTP is stateless" means and one consequence of it

Ans:
Client
A client is an application or device that sends a request to a server to get some information or perform an operation.

Server
A server receives requests from clients, processes them, performs the required operations, interacts with databases, and sends back responses.

Request
A request is a message sent by a client to a server asking it to perform an operation or provide some information.

Response
A response is the message sent by the server back to the client after processing a request.

API (Application Programming Interface)
An API defines the available operations that a client can request from a server and how to communicate with it.

HTTP is stateless
HTTP is a stateless protocol, which means: The server does not automatically remember previous requests made by a client. Each request is treated independently.

The server needs an additional mechanism to maintain user identity and session information across multiple requests.

Q2. Name every part of this URL and say which part is never sent to the server:
https://api.neurapath.in:443/v1/students/7?course=Data%20Science&limit=5#top
Ans:

URL components
Component Value Meaning
Scheme / Protocol https Defines how to communicate securely
Host / Domain api.neurapath.in Identifies the server
Port 443 Port through which the connection is made
Path /v1/students/7 Identifies the requested resource
Path segment v1 API version
Path segment students Resource type
Path segment 7 Student ID
Query parameter course=Data%20Science Filters by course
Query parameter limit=5 Limits results to 5
Fragment top Identifies a section or location within the resource

The fragment identifier (#top) is handled by the browser/client and is not included in the HTTP request sent to the server.

Q3. Give the meaning of 200, 201, 400, 401, 403, 404, 409, 429, 500 and 503 in one line each. Which of them
should a client retry automatically, and why only those?

Code Meaning
200 OK Request succeeded, and the server returned the requested result.
201 Created Request succeeded, and a new resource was created.
400 Bad Request The request contains invalid data or incorrect syntax.
401 Unauthorized Authentication is missing or invalid; the client needs valid credentials.
403 Forbidden The client is authenticated (or otherwise identified), but does not have permission to access the resource.
404 Not Found The requested resource does not exist or cannot be found.
409 Conflict The request conflicts with the current state of the resource, such as creating a duplicate record.
429 Too Many Requests The client has exceeded the allowed request rate (rate limit).
500 Internal Server Error Something unexpected went wrong on the server.
503 Service Unavailable The server is temporarily unable to handle requests, often due to maintenance or overload.

429, 500 and 503 are the main candidates for automatic retries.

Q4. Give three differences between a Python dict and JSON. What happens when you run json.loads("
{'a': None}") and why?

Ans:
A Python dictionary is a native Python data structure used to store key-value pairs, whereas JSON (JavaScript Object Notation) is a language-independent text format used to exchange data between applications.

Key differences
Feature Python dict JSON
Key types Keys can be strings, numbers, tuples, etc. (must be hashable). Object keys must always be strings.
Null values Uses None. Uses null.
Boolean values Uses True and False. Uses true and false.
String quotes Supports single and double quotes. Requires double quotes.
Data types Supports Python-specific objects like tuples, sets, and custom objects. Supports strings, numbers, booleans, null, arrays, and objects.
json.loads("{'a': None}")
Python raises a json.decoder.JSONDecodeError.

Q5. What do "safe" and "idempotent" mean for HTTP methods? Classify GET, POST, PUT and DELETE.

Ans:

1. Safe
   An HTTP method is called safe if it does not modify the server's data or state.
2. Idempotent
   An HTTP method is called idempotent if performing the same request multiple times produces the same intended effect on the server as performing it once.

3. Classification of HTTP methods
   HTTP Method Safe? Idempotent? Reason
   GET Yes Yes Retrieves data without modifying server state.
   POST No No (generally) Usually creates a new resource or performs an operation.
   PUT No Yes Replaces or creates a resource with the specified representation.
   DELETE No Yes Deletes a resource; repeating the deletion has the same intended effect.
