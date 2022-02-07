#choix de la couche à modiffiier
layer=QgsProject.instance().mapLayersByName('cables')[0]

layer_provider=layer.dataProvider()
layer_provider.addAttributes([QgsField("Longueur",QVariant.Double)])
layer.updateFields()
