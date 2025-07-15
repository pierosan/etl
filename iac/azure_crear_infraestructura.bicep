@description('Nombre de usuario administrador del servidor.')
param administratorLogin string

@secure()
@description('Contraseña del administrador del servidor.')
param administratorLoginPassword string


resource mysqlServer 'Microsoft.DBforMySQL/flexibleServers@2021-05-01' = {
  name: 'dbfobguard'
  location: 'mexicocentral'
  sku: {
    name: 'Standard_B1ms'
    tier: 'Burstable'
  }
  properties: {
    createMode: 'Default'
    version: '8.0.21'
    administratorLogin: administratorLogin
    administratorLoginPassword: administratorLoginPassword
    storage: {
      storageSizeGB: 20
      autoGrow: 'Enabled'
      iops: 360
    }
    backup: {
      backupRetentionDays: 1
      geoRedundantBackup: 'Disabled'
    }
    highAvailability: {
      mode: 'Disabled'
    }
  }
}

// Reglas de firewall (solo se crean si la lista contiene elementos)
resource firewallRulesRes 'Microsoft.DBforMySQL/flexibleServers/firewallRules@2022-01-01' = {
  parent: mysqlServer
  name: 'TodasLasIps'
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress:   '255.255.255.255'
}
}
