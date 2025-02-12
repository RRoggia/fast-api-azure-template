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

## Environment variables
We are using pydantic to load the Environment variables. We use the pydantic's default priority list to determine the envs.
The `.env-example` shows an example of the values expected.

## CORS
The CORS middleware is enabled, the allowed urls can be configured in the .env file using the `cors` attribute.

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

## Scaling the App Service in Azure
```
az webapp scale -g $az_rg -n $az_app --instance-count 2
```

## Configure Health Probe
```
az webapp config set -n $az_app -g $az_rg --health-check-enabled true --health-check-path "/"
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

# App Service Configuration
The App service is configured in the following way:
- App Service Plan is configure to use Pricing plan P0v3, it allows 1 CPU and 4GB of RAM. And up to 30 instances.
- The Production pricing such as, P0v3, enables us to use the deployment slots. Which enables advanced deploy strategies.
- The App Service uses linux as OS
- We choose the runtime stack as Python:3.12
