#choix de la couche sur laquel on applique la selection
layer=QgsProject.instance().mapLayersByName('cables')[0]
layer_provider=layer.dataProvider()
for f in layer.getFeatures():
    id=f.id()
    longueur=f.geometry().length()
    attr_value={5:longueur}
    layer_provider.changeAttributeValues({id:attr_value})
layer.commitChanges()