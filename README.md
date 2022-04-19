This repository has the Assesment mentioned below:
Tasks:
1. Create an API using your language/technology of choice that does the following:
o Given a U.S. State Code, return the full name of the state

o To help with the mapping of U.S. State code <-> full name, we provided some pre-
determined mappings below. You can also look up your own mappings online:

§ CSV: https://github.com/jasonong/List-of-US-States/blob/master/states.csv

2. Containerize the API above
3. Write the automation for the deployment of the container with a horizontally scalable
technology

Implemented FastAPI. 
Run Local:
uvicorn main:app --reload

Reference:
https://fastapi.tiangolo.com/tutorial/

CICD Pipeline:
Refer K8s_deployment.jpeg file.