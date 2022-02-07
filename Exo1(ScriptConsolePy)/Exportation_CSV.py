folder=r'D:\\Master_2_G2M\\Python_pour_Qgis\\projet\\Evaluation_PyQGIS_2021\\data\\'
# Selectionner, sauvegarder et importer
layer=QgsProject.instance().mapLayersByName('cables')[0]

QgsVectorFileWriter.writeAsVectorFormat(layer,folder+"\\cables",
"UTF-8",driverName="csv", onlySelected=False)

