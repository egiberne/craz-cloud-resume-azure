# Changelog

## 0.7.1 - 2026-05-06
### Fixed
- Correct issue :  
    - client-side "detail": "Not Found" for endpoint http://127.0.0.1:8000/ 
    - server-side : Correct issue :127.0.0.1:56657 - "GET /info HTTP/1.1" 404 Not Found
    - Missing endpoint decorator "@app" instead of "app"


## 0.7.0 - 2026-05-06
### Added
- Implement the back-end 
    -  Receive the GET request via endpoints API :
        - GET request to say Hello ; endpoint /
        - GET request to check the server status ; endpoint /health
  
### Changed
-  Rename these javascript variables for understanding :
    - visit_count to visit_counter
    - visitCount to visitCounter 

## 0.6.1 - 2026-04-06
### Fixed
- Implement the back-end:
    - Correct issue : NameError: name 'FASTAPI' is not defined. Did you mean: 'FastAPI'? 
    - Python library is Case Sensitive
- Implement the front-end
    - Refine the html content to update the  final goal to address

## 0.6.0 - 2026-04-06
### Added
- Implement the back-end:
    - Install the python environment
    - Install the web server library (Uvicorn) and the api library (FastAPI)

## 0.5.0 - 2026-02-06
### Added
- Implement the front-end 
    - Define javascript visit counter
    - Define copyright
### Change
- Implement the front-end 
    - Modify the html to load the javascript
    - Modify the html to manipulate the DOM with javascript

## 0.4.0 - 2026-01-06
### Added
- Implement the front-end 
    - Define the flex layout
    - Define the media queries
    
### Change
- Implement the front-end 
    - Modify the html to load the styles
    - Remove the form
    - Update the content
   
## 0.3.0 - 2026-31-05
### Added
- Implement the front-end 
    - Reset the default CSS design
    - Define the typography
### Change
- Implement the front-end 
    - Refine html structure
    - Update the content

## 0.2.0 - 2026-29-05
### Added
- Implement the front-end 
    - Keep working on html
    - Create a form for contact
    - Include a avatar picture
### Change
- Implement the front-end 
    - Remove the id in the html file.
    - Modify the folder structure

## 0.1.0 - 2026-28-05
### Added
- Initiate resumer challenge project
- Implement the front-end:
    - Start with html
    - Create the resumer in html and include content