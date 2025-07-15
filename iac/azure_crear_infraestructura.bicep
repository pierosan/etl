targetScope = 'subscription'
param rgName string = 'grupo_recursos_etl'
param rgLocation string = 'Brazil South'
param tags object = {}

resource rg 'Microsoft.Resources/resourceGroups@2018-05-01' = {
  location: rgLocation
  name: rgName
  properties: {}
  tags: tags
}
