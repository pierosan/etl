param llave string


resource name_resource 'Microsoft.App/jobs@2024-08-02-preview' = {
  name: 'contenedoretl'
  location: 'brazilsouth'
  properties: {
    environmentId: '${subscription().id}/resourceGroups/${resourceGroup().name}/providers/Microsoft.App/managedEnvironments/managedEnvironment-gruporecursoset'
    configuration: {
      secrets: []
      registries: []
      replicaTimeout: 1800
      replicaRetryLimit: 0
      triggerType: 'Schedule'
      scheduleTriggerConfig: {
        replicaCompletionCount: 1
        parallelism: 1
        cronExpression: '*/5 * * * *'
      }
    }
    template: {
  containers: [
    {
      name: 'contenedoretl'
      image: 'docker.io/pierosan/etl_fob_guard:latest'
      command: []
      args: []
      resources: {
        cpu: 4
        memory: '8Gi'
      }
      env: [
        {
          name: 'LLAVE'
          value: llave
        }
      ]
    }
  ]
}
    workloadProfileName: 'Consumption'
  }
  dependsOn: [
    environment
  ]
}

resource environment 'Microsoft.App/managedEnvironments@2024-08-02-preview' = {
  name: 'managedEnvironment-gruporecursoset'
  location: 'brazilsouth'
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: reference('Microsoft.OperationalInsights/workspaces/workspacegruporecursosetl', '2020-08-01').customerId
        sharedKey: listKeys('Microsoft.OperationalInsights/workspaces/workspacegruporecursosetl', '2020-08-01').primarySharedKey
      }
    }
    workloadProfiles: [
      {
        name: 'Consumption'
        workloadProfileType: 'Consumption'
      }
    ]
  }
  dependsOn: [
    workspace
  ]
}

resource workspace 'Microsoft.OperationalInsights/workspaces@2020-08-01' = {
  name: 'workspacegruporecursosetl'
  location: 'brazilsouth'
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
    workspaceCapping: {}
  }
  dependsOn: []
}

