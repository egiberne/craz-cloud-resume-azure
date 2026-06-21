# Changelog

## 0.11.0 - 2026-06-21
### Changed
- Modify the path of the different endpoint to visits as more conventional 
- Modify the database schema to include a simple database identify for each row (unique visit)
        
### Fixed
- Error message on the server side :
` 
"GET /v2/visits?userId=702fca00-a4bd-4b57-9ac2-44f30ab72e2b HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
 return {"dbID": row["dbID"], "userId": userId, "visitCount": row["visitCount"]}
`
    - Updated the SQL query to response with all the information for the query string with the userId :
        ```sql
        "SELECT visitCount, dbID FROM visits WHERE userId = ?", (userId,)
        ```

### Added 
- GET request find the user info based on is user identifier (userId)
- GET request find the user info based on is db identifier (dbID) but failing with error
    - {"detail":[{"type":"missing","loc":["query","userId"],"msg":"Field required","input":null}]}


## 0.10.0 - 2026-06-18
### Added
POST Request
### Changed
Modify the path of the different endpoint versions 


## 0.9.1 - 2026-06-11
### Added
Implement database.py module to create sqlite database and function for connection and initialization
### Changed
- Keep it simple with sqlite3 python module instead of using additional modules like sqlalchemy, pydantic
### Fixed
- Troubleshoot errors :
`from database import init_db
ModuleNotFoundError: No module named 'database'
`
    - Fix: as I create the module
        ```Python
        from .database ...
        `
        
## 0.9.0 - 2026-06-10
### Added
- Implement SQLite database 
- Implement endpoint health for GET request
- Implement endpoint visit for POST request; But there is issue with the counter

## 0.8.3 - 2026-06-09
### Changed
- Updated LICENSE with missing terms and content.
- Updated README.md with a cleared roadmap and table
- Update index.html with minor but relevant content.

## 0.8.2 - 2026-06-07
### Fixed
- Troubleshoot errors :
   - `Access to fetch at 'http://127.0.0.1:8000/counter' from origin 'http://127.0.0.1:3000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
    script.js:38  POST http://127.0.0.1:8000/counter net::ERR_FAILED 500 (Internal Server Error)
    `
    - `AttributeError: 'function' object has no attribute 'get'`
        - Must use an function .json() on `request` instead of attribute
            ```python
            request.json() 
            ```
    - `AttributeError: 'coroutine' object has no attribute 'get'`
        - Endpoint function must be asynchronous for the POST to collect `data` from `request` :   
            ```python 
                    async def update_counter(request:Request):
                    data = await request.json() 
            ```
        - Front-end must send json data :
            ```javascript
                 body:JSON.stringify({userId:userId})
            ``` 


## 0.8.1 - 2026-06-06
### Fixed
- Troubleshoot issues :
    - client-side in the browser page: `"detail":"Method Not Allowed"` ; Browser submit GET request by default.
    - client-side in the browser dev tool : no error :It works as Cross-origin enabled with CORS protocol (cors) is enabled by default
    - server-side terminal console tool  : `"GET /visit HTTP/1.1" 405 Method Not Allowed`
        - Correct with specify the method POST in the command:
        ```powershell
         Invoke-WebRequest -uri  http://127.0.0.1:8000/health -Method POST 
        `
        
    - client side javascript console:
        - Correct this CORS error, with enabling the CORS protocol on the backend
        `Access to fetch at 'http://127.0.0.1:8000/health' from origin 'http://127.0.0.1:3000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
        script.js:30  GET http://127.0.0.1:8000/health net::ERR_FAILED 200 (OK)
        `
       ```python
        origins =['*']
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins
        )
        ```
        - Correct this CORS error, with enabling CORS protocol in the back-end :
        `Access to fetch at 'http://127.0.0.1:8000/echo' from origin 'http://127.0.0.1:3000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
        script.js:34  POST http://127.0.0.1:8000/echo net::ERR_FAILED 200 (OK)
        `
        
        ```python
        origins =['*']
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins
        )
        ```
        - and specify the method in the front-end
        ```javascript
        {method:"POST"}
        ```
        



## 0.8.0 - 2026-06-06
### Added 
- Implement Front-end:
    - code to send the visit counter 
    - code to send GET and POST request to endpoint API /health and /echo
- Implement Back-end:
    - code to receive the visit counter
    - code to receive POST request via endpoint API /health and /echo

## 0.7.1 - 2026-06-05
### Fixed
- Correct issue :  
    - client-side "detail": "Not Found" for endpoint http://127.0.0.1:8000/ 
    - server-side : Correct issue : "GET /info HTTP/1.1" 404 Not Found because of :
        - Missing endpoint decorator "@app" instead of "app" : Meaning no endpoint instance
        - Or Mistyping the name of the endpoint


## 0.7.0 - 2026-06-05
### Added
- Implement the back-end 
    -  Code to receive the GET request via endpoints API :
        - GET request to say Hello ; endpoint /
        - GET request to check the server status ; endpoint /health
  
### Changed
-  Rename these javascript variables for understanding :
    - visit_count to visit_counter
    - visitCount to visitCounter 

## 0.6.1 - 2026-06-04
### Fixed
- Implement the back-end:
    - Correct issue : NameError: name 'FASTAPI' is not defined. Did you mean: 'FastAPI'? 
    - Python library is Case Sensitive
- Implement the front-end
    - Refine the html content to update the  final goal to address

## 0.6.0 - 2026-06-04
### Added
- Implement the back-end:
    - Install the python environment
    - Install the web server library (Uvicorn) and the api library (FastAPI)

## 0.5.0 - 2026-06-02
### Added
- Implement the front-end 
    - Define javascript visit counter
    - Define copyright
### Change
- Implement the front-end 
    - Modify the html to load the javascript
    - Modify the html to manipulate the DOM with javascript

## 0.4.0 - 2026-06-01
### Added
- Implement the front-end 
    - Define the flex layout
    - Define the media queries
    
### Change
- Implement the front-end 
    - Modify the html to load the styles
    - Remove the form
    - Update the content
   
## 0.3.0 - 2026-05-31
### Added
- Implement the front-end 
    - Reset the default CSS design
    - Define the typography
### Change
- Implement the front-end 
    - Refine html structure
    - Update the content

## 0.2.0 - 2026-05-29
### Added
- Implement the front-end 
    - Keep working on html
    - Create a form for contact
    - Include a avatar picture
### Change
- Implement the front-end 
    - Remove the id in the html file.
    - Modify the folder structure

## 0.1.0 - 2026-05-28
### Added
- Initiate resumer challenge project
- Implement the front-end:
    - Start with html
    - Create the resumer in html and include content