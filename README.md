# fast-api-azure-template
Template app using Python 3.12 and FastAPI designed to be deployed in Ms Azure.

## Setup local machine
```
python -m venv .venv
pip install -r requirements.txt
```

## Running locally
run in the command line
```
./startup.sh
```

## Running the tests
`pytest`

# Deploy To Azure Cloud

## Create and configure App in App Service
```
export az_rg=<rg>
export az_plan=<plan_name>
export az_app=<app_name>

az group create --name $az_rg --location eastus
az appservice plan create --name $az_plan -g <rg> --sku B1 --is-linux
az webapp create -n $az_app -g $az_rg --plan $az_plan --runtime PYTHON:3.12
az webapp config set --startup-file "./startup.sh" -n $az_app -g $az_rg
az webapp config appsettings set -g $az_rg -n $az_app --settings SCM_DO_BUILD_DURING_DEPLOYMENT=true
```

## Deploy to app service

### Using CI/CD
// TO DO

### Using zip
```
zip -r deploy.zip . -x '.??*'
az webapp deploy -n $az_app -g $az_rg --src-path ./deploy.zip
az webapp restart -n $az_app -g $az_rg
```
