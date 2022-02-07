# -*- coding: utf-8 -*-

"""
***************************************************************************
                                                                         
   Traité de la question 3 de l'evaluation Python Pour Qgis Prof :(DOUMBIA) 
    Etudiant: DOUNOH Mohamed Karifa Master G2M
                                                                         
***************************************************************************
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterField,
                       QgsProcessingParameterString,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterFile,
                       QgsField,
                       QgsExpression,
                       QgsExpressionContext,
                       QgsExpressionContextUtils,
                       QgsSymbol,
                       QgsRendererRange,
                       QgsGraduatedSymbolRenderer,
                       QgsProcessingAlgorithm,
                        QgsProcessingParameterNumber,
                        QgsProcessingParameterEnum,
                        QgsVectorLayer
                       
                       )
from qgis import processing


class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT_1 = 'INPUT_1'
    INPUT_2 = 'INPUT_2'
    # REGION ='REGION'
    
    INPUT_BUFFERDIST = 'BUFFERDIST'
    OUTPUT_BUFFER = 'OUTPUT_BUFFER'
    # INPUT_VECTOR = 'INPUT_VECTOR'
        
    CHAMP_1= 'CHAMP_1'
    CHAMP_2= 'CHAMP_2'
    OUTPUT_CENTROIDE = 'OUTPUT_CENTROIDE'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ExampleProcessingAlgorithm()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Exo3 MKD'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Exo3 MKD')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('Example scripts')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'examplescripts'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Algorithm qui permet de faire un buffer autour d'une couche boite selectionnée et creer une classification de la couche cable en foction du mode de pose specifier et de la capcité fait par DOUNOH Mohamed Karifa")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.INPUT_1,
                self.tr('couche boite'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
      
        """self.addParameter(QgsProcessingParameterString
            (self.REGION, 
            'BUFFER', 
            optional=False,
             defaultValue=None))
             
        self.addParameter(QgsProcessingParameterFeatureSource(
            self.INPUT_VECTOR, "Input vector"))"""
            
        self.addParameter(QgsProcessingParameterNumber(
            self.INPUT_BUFFERDIST, "distance de buffer",
            QgsProcessingParameterNumber.Double,
            10.0))
            
        """self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT_BUFFER, "Output buffer"))"""
            
        
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.INPUT_2,
                self.tr('Couche 2'),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        
        """self.addParameter(QgsProcessingParameterField(
            self.CHAMP_1, 
            self.tr('Champ de fusion 1'),
            optional=False, 
            type=QgsProcessingParameterField.Any,
            parentLayerParameterName=self.INPUT_1,
            allowMultiple=False,
            defaultValue=None))"""
            
        self.addParameter(QgsProcessingParameterNumber(
            self.CHAMP_1, "Capacité choisit",
            QgsProcessingParameterNumber.Integer))
        
        
            
        """self.addParameter(QgsProcessingParameterField(
            self.CHAMP_2, 
            self.tr('Champ de fusion 2'),
            optional=False, 
            type=QgsProcessingParameterField.Any,
            parentLayerParameterName=self.INPUT_2,
            allowMultiple=False,
            defaultValue=None))"""
            
        self.addParameter(QgsProcessingParameterString
            (self.CHAMP_2, 
            'Mode de pose', 
            optional=False,
             defaultValue='FACADE'))

        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT_CENTROIDE,
                self.tr('Couche boite en sortie')
            )
        )
        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Couche cable en sortie')
            )
        )
        
        
        """self.addParameter(
            QgsProcessingParameterEnum(
            self.OUTPUT_BUFFER,
            self.tr('Valeur possible du mode de pose'),
            options=[self.tr('Lat,Lon (Y,X) - Google map order'),self.tr('Lon,Lat (X,Y) order')],
            defaultValue=0,
            optional=True)
        )"""
        
        """self.addParameter(
            QgsProcessingParameterEnum(
            self.OUTPUT_BUFFER,
            self.tr('Valeur possible du mode de pose'),
            options=['FACADE', 'AERIEN', 'IMMEUBLE', 'SOUTERRAIN'],
            defaultValue=0,
            optional=True)
        )"""
        

    def processAlgorithm(self, parameters, context, feedback):
        
        # Traitement du Buffer
        
        bufferresult = processing.run('native:buffer',
            {'INPUT': parameters[self.INPUT_2],
            'DISTANCE': parameters[self.INPUT_BUFFERDIST],
            'SEGMENTS': 5,
            'END_CAP_STYLE': 0,
            'JOIN_STYLE': 0,
            'MITER_LIMIT': 10,
            'DISSOLVE': True,
            'OUTPUT': parameters[self.OUTPUT]},
            context=context, feedback=feedback, is_child_algorithm=True)
            
        buffered = bufferresult['OUTPUT']
        feedback.pushInfo('sink output number of features is')
        #return {self.OUTPUT_BUFFER: buffered}
        return {self.OUTPUT_CENTROIDE: buffered}
        
        
        
        #----------SELECTION DE LA region 
        """select = self.parameterAsVectorLayer(
            parameters,
            self.INPUT_1,
            context
        )
        select.selectByExpression(" \"capacite\" > {} and \"mode_pose\" = '{}'".format(parameters[self.CHAMP_1], parameters[self.CHAMP_2]))
        
        
        cable_select=processing.run('qgis:saveselectedfeatures',
        {'INPUT':select,
       'OUTPUT':parameters[self.OUTPUT]},
        context=context, feedback=feedback, is_child_algorithm=True)
        feedback.pushInfo('sink output number of features is')
        return {self.OUTPUT_CENTROIDE: cable_select}"""
        
        """region_select=processing.run('qgis:saveselectedfeatures',
        {'INPUT':select,
        'OUTPUT':'memory:'},
        context=context, feedback=feedback, is_child_algorithm=True)"""
        




#---------------------------------- Symbole gradué----------------------------------------------------------------
        niveau_densite = (
            ('Faible', 1, 9, 'green'),
            ('Moyen_1', 10, 25, 'yellow'),
            ('Moyen_2', 26, 100, 'orange'),
            ('Elevé', 101, 10000000, 'red'),
            
        )

        # creation 
        ranges = []
        for label, lower, upper, color in niveau_densite:
            symbol = QgsSymbol.defaultSymbol(commune.geometryType())
            symbol.setColor(QColor(color))
            rng = QgsRendererRange(lower, upper, symbol, label)
            ranges.append(rng)

        # create the renderer and assign it to a layer
        expression = 'densite' # field name
        renderer = QgsGraduatedSymbolRenderer(expression, ranges)
        commune.setRenderer(renderer)


       