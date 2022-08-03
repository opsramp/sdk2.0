# Overview

- [Setup](#setup)
- [Prepare Domain model json](#prepare-domain-model-json)
- [Generate code from domain json](#generate-code-from-domain-json)
- [Fill target stubs](#fill-target-stubs)
- [Building project](#building-project)
- [Publishing app](#publishing-app)
- [Installing app](#installing-app)


###### Setup

**Setup pycharam** <br>

1. Make sure python is installed
2. Download **pycharam** community version from this link https://www.jetbrains.com/pycharm/download/#section=linux <br>
3. The file pycharm*.tar.gz will be downloaded, extract this file <br>
4. Go to bin folder in the extracted folder and run **sh pycharam.sh** <br>
5. pycharam editor will be open and ready to use <br>

**Install virtual environment** <br>

```shell
python3 -m pip install --user virtualenv
```

###### Prepare Domain model json

```json
{
  "appName": "dell-brightclustermanager",
  "appVersion": "1.0.0",
  "discoveryConfiguration": [
    {
      "propertyName": "dellBCMIP",
      "label": "Dell BCM Manager IP Address",
      "dataType": "string"
    },
    {
      "propertyName": "managerCredentials",
      "label": "Dell BCM Manager Credentials",
      "dataType": "string",
      "credentialType": "SSH",
      "placeholder": "Select Credentials"
    },
    {
      "propertyName": "appFailureNotifications",
      "label": "App Failure Notifications",
      "dataType": "boolean"
    }
  ],
  "required": [
    "dellBCMIP",
    "managerCredentials"
  ],
  "data": {
    "appFailureNotifications": false
  },
  "nativeTypeMapping": [
    {
      "nativeType": "Dell BrightCluster Manager",
      "opsrampResourceType": "Cluster"
    },
    {
      "nativeType": "Dell BCM Head Node",
      "opsrampResourceType": "Server"
    },
    {
      "nativeType": "Dell BCM Virtual Node",
      "opsrampResourceType": "Server"
    },
    {
      "nativeType": "Dell BCM Physical Node",
      "opsrampResourceType": "Server"
    },
    {
      "nativeType": "Dell BCM Switch",
      "opsrampResourceType": "Switch"
    },
    {
      "nativeType": "Dell BCM PDU",
      "opsrampResourceType": "Power"
    }
  ],
  "nativeType": [
    {
      "name": "Dell BrightCluster Manager",
      "metric": [],
      "monitors": [
        {
          "title": "Dell BrightCluster Manager Monitor",
          "frequency": 30,
          "metric": []
        }
      ]
    },
    {
      "name": "Dell BCM Head Node",
      "metric": [
        {
          "name": "dell_bcm_headNode_healthStatus",
          "units": "",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${component.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Component: ${component.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": "NONE",
            "value": "0",
            "repeat": 1
          },
          "critical": {
            "operator": "NOT_EQUAL",
            "value": "0",
            "repeat": 1
          },
          "availability": true,
          "graphPoint": true,
          "raiseAlert": true,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false,
          "dataPointConverisonOptions": [
            {
              "pass": "0"
            },
            {
              "fail": "1"
            }
          ]
        },
        {
          "name": "dell_bcm_headNode_blockedProcesses",
          "units": "count",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_headNode_systemCpuTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_headNode_cpuWaitTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        }
      ],
      "monitors": [
        {
          "title": "Dell BCM HeadNode Health Status Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_headNode_healthStatus"
          ]
        },
        {
          "title": "Dell BCM HeadNode Performance Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_headNode_blockedProcesses",
            "dell_bcm_headNode_systemCpuTime",
            "dell_bcm_headNode_cpuWaitTime"
          ]
        }
      ]
    },
    {
      "name": "Dell BCM Virtual Node",
      "metric": [
        {
          "name": "dell_bcm_virtualNode_healthStatus",
          "units": "",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${component.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Component: ${component.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": "NONE",
            "value": "0",
            "repeat": 1
          },
          "critical": {
            "operator": "NOT_EQUAL",
            "value": "0",
            "repeat": 1
          },
          "availability": true,
          "graphPoint": true,
          "raiseAlert": true,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false,
          "dataPointConverisonOptions": [
            {
              "pass": "0"
            },
            {
              "fail": "1"
            }
          ]
        },
        {
          "name": "dell_bcm_virtualNode_blockedProcesses",
          "units": "count",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_virtualNode_systemCpuTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_virtualNode_cpuWaitTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        }
      ],
      "monitors": [
        {
          "title": "Dell BCM VirtualNode Health Status Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_virtualNode_healthStatus"
          ]
        },
        {
          "title": "Dell BCM VirtualNode Performance Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_virtualNode_blockedProcesses",
            "dell_bcm_virtualNode_systemCpuTime",
            "dell_bcm_virtualNode_cpuWaitTime"
          ]
        }
      ]
    },
    {
      "name": "Dell BCM Physical Node",
      "metric": [
        {
          "name": "dell_bcm_physicalNode_healthStatus",
          "units": "",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${component.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Component: ${component.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": "NONE",
            "value": "0",
            "repeat": 1
          },
          "critical": {
            "operator": "NOT_EQUAL",
            "value": "0",
            "repeat": 1
          },
          "availability": true,
          "graphPoint": true,
          "raiseAlert": true,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false,
          "dataPointConverisonOptions": [
            {
              "pass": "0"
            },
            {
              "fail": "1"
            }
          ]
        },
        {
          "name": "dell_bcm_physicalNode_blockedProcesses",
          "units": "count",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_physicalNode_systemCpuTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_physicalNode_cpuWaitTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        }
      ],
      "monitors": [
        {
          "title": "Dell BCM PhysicalNode Health Status Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_physicalNode_healthStatus"
          ]
        },
        {
          "title": "Dell BCM PhysicalNode Performance Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_physicalNode_blockedProcesses",
            "dell_bcm_physicalNode_systemCpuTime",
            "dell_bcm_physicalNode_cpuWaitTime"
          ]
        }
      ]
    },
    {
      "name": "Dell BCM Switch",
      "metric": [],
      "monitors": [
        {
          "title": "Dell BCM Switch Monitor",
          "frequency": 30,
          "metric": []
        }
      ]
    },
    {
      "name": "Dell BCM PDU",
      "metric": [],
      "monitors": [
        {
          "title": "Dell BCM PDU Monitor",
          "frequency": 30,
          "metric": []
        }
      ]
    }
  ]
}

```

###### Generate code from domain json

Once the domain.json file is done, than we need to generate code to build the App, follow the below steps

- Clone the sdk-app-starter project in local environment[https://github.com/opsramp/sdk2.0/tree/main/projects/sdk-app-starter/python]
- Replace the above domain.json file into the above project
- Execute this command coming to sdk-app-starter project: **python3 app.py destination-folder-path python**
- An App will be created with the destination-folder-path
- Once app created successfully, than open the project in pycharm
- Open a terminal pointing app folder
- create virtual environment python3 -m venv env
- source env/bin/activate
- Run **python3 app.py** make sure App is running

Code generator generates below artifacts

- App skeleton code
- Manifest
- Helm chart
- Docker file
- Make file


###### Fill target stubs

App developer need to fill the stubs by following below steps

1. Talking to target
2. Process target data
3. Return data back with opsramp domain model


###### Building project

Run the below make file from the project folder

```shell
sh make.sh
```

Running this command will run the following steps in sequence
- Building python code
- Building docker image
- Pushing docker image to repo
- Pushing helm chart to repo

###### Publishing app

Publishing App requries following data

1. Client id
2. Client OAuth2.0 token
3. Manifest.json  

Follow the APIs in the [link](https://github.com/opsramp/sdk2.0/blob/41574c5f5a0edad7000054950e6b0372842dd37b/documentation/app_publish_rest_calls.md) 
to publish the App

###### Installing app

Once app is published, login to cloud portal and check whether app is available in the manage apps list

Login to cloud portal
1. Select -->Partner-->Client
2. Go to Setup-->Integrations and Apps
3. Click on Manage Apps button to see list of Apps
4. The published App should be seen here

6. 



















