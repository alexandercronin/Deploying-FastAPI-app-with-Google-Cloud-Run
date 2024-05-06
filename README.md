# Deploying-FastAPI-app-with-Google-Cloud-Run
Based on this tutorial: https://dev.to/0xnari/deploying-fastapi-app-with-google-cloud-run-13f3

# Additional Resource
- https://cloud.google.com/run?hl=en
- https://cloud.google.com/sdk/docs/install-sdk
- https://codelabs.developers.google.com/codelabs/cloud-run-deploy#0
- Cheat Sheet: https://cloud.google.com/sdk/docs/cheatsheet 

# Choosing a region 
- https://cloud.google.com/run/pricing#tables

Common reasons for errors
1. project has not been created on cloud
2. run/Region is not set correctly
3. run command is not executed in the folder in which the Dockerfile is located


# Useful command of gcloud cli 

- `gcloud info`
- `gcloud projects create PROJECT_ID`


# How to delete a project 
- https://cloud.google.com/sdk/gcloud/reference/projects/delete

List the billing options available for a project 
- https://cloud.google.com/sdk/gcloud/reference/billing/accounts/list

Link a project to a billing
- https://cloud.google.com/sdk/gcloud/reference/billing/projects/link

Adding poetry environment to the interpreter
ref: https://www.markhneedham.com/blog/2023/07/24/vscode-poetry-python-interpreter/

1. cd to the folder which contains the .toml lfile
2. execute `poetry env info` for general info
3. execute `poetry env info --path` to get the path to the virtual env
4. use `CMD+P` to open the command pallet and then use `> python` to open the interpretor selector
5. Then choose it  
6. 


# Mars Rover Photos Origin
- https://api.nasa.gov/ 



 # Fast API Responses References 
 - https://fastapi.tiangolo.com/advanced/custom-response/
