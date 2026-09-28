19. PUT is use for replace/update whole document/data and PATCH is use to update partial data.

20. API should return 404 status code, 404 status is use for when data not found inside DB or url is wrong.

21. {"message": "id is already exist."}, status = 409

22. answer in code

23. URL will give the /students route info, headers will give content-type info and body will give student json data.

24. method: PATCH
    route: /student/id
    body: {"course": "Data Science"}

25. method: PUT
    route: /student/1
    body: {"name": "Pankaj", "age":24, "course":"Python"}

26. It is standard to transfer data through API in form of JSON and accepted by all major programming, and appropriate status code also represent the meaning of the response.

27. @app.route("/students")
    def get_students():
    name = request.args.get("name")
    result = []
    for student in students:
    if student["name"].lower() == name.lower()
    result.append(student)
    return jsonify(result)

28. /students/2 : passing path param as 2
    /students?id=2 : passing query key id with

29. /students?search=
    I would use query param not path param

30. I would retrieve the api_key from request header and compare it with db api key if it matches then I will allow user to perform delete operation else reject the request with Unauthorized msg

31. because PATCH updates data partially and it doesn't need to have full json to update

32. {"message":"student doesn't exist"}, 404

33. PUT request needs all data of json which required to change and validation will be on each field to update

34. answer in code and , i would read query as
    request.args.get("course")
    request.args.get("age")
