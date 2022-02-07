from qgis.utils import iface
from PyQt5.QtCore import QVariant
Vlayer = iface.addVectorLayer("D:\\Master_2_G2M\\Python_pour_Qgis\\projet\\Evaluation_PyQGIS_2021\\data\\","","ogr")
if not Vlayer:
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(Vlayer)
