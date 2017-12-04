# -*- coding: utf-8 -*-

import xc_base
import geom
import xc

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2014, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

feProblem= xc.FEProblem()
preprocessor=  feProblem.getPreprocessor
# Definimos geometria

points= preprocessor.getCad.getPoints
pt1= points.newPntIDPos3d(1, geom.Pos3d(0.0,0.0,5.0) )
pt2= points.newPntIDPos3d(2, geom.Pos3d(0.0,0.0,10.0) )
pt3= points.newPntIDPos3d(3, geom.Pos3d(5.0,0.0,10.0) )
pt4= points.newPntIDPos3d(4, geom.Pos3d(0.0,5.0,10.0) )

lines= preprocessor.getCad.getLines
l1= lines.newLine(1,2)
l2= lines.newLine(1,3)
l3= lines.newLine(1,4)
l4= lines.newLine(2,4)
l5= lines.newLine(2,3)
l6= lines.newLine(4,3)

fName= "/tmp/dibuja_edges.tiff"
import os
pth= os.path.dirname(__file__)
if(not pth):
  pth= "."
fNameB= pth+"/dibuja_edges.verif.tiff"

from postprocess.xcVtk.CAD_model import vtk_CAD_graphic
defDisplay= vtk_grafico_cad.RecordDefDisplayCAD()
defDisplay.plotCadModel(preprocessor, "total",None,fName)

ratio1= xc_base.compare_images(fName,fNameB)

# os.system("rm -f " + fName)

#print "ratio1= ",(ratio1)

import os
from miscUtils import LogMessages as lmsg
fname= os.path.basename(__file__)
if  (abs(ratio1)<1e-10) :
  print "test ",fname,": ok."
else:
  lmsg.error(fname+' ERROR.')

