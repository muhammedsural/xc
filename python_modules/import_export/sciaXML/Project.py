# -*- coding: utf-8 -*-

#Based on sXML-master projet on gitHub

import Definition as df
import Object as obj
import Container as ctr
import xml.etree.cElementTree as ET

class Project:    
    
  xmlns= ''
  defn= df.Definition('')
  containers= []
  fileName= ''
  comprimentoX= 0.0
  comprimentoY= 0.0
  comprimentoZ= 0.0
  uuid= ''

  def __init__(self,xmlns, defn, containers):
    self.xmlns= xmlns
    self.defn= defn
    self.containers= containers

  # def __init__(self, sumarioDados, fileName):
  #   if(sumarioDados != None):
  #     self.uuid= sumarioDados.getSiglaProjeto()
  #     self.xmlns= SciaXMLConstantes.XMLNS
  #     self.defn= df.Definition(fileName+SciaXMLConstantes.DEF)
  #     self.containers= []
  #     self.containers.append(getContainerNos(sumarioDados))
  #     self.containers.append(getContainerPecas(sumarioDados))
  #     self.containers.append(getContainerCamadas(sumarioDados))

  def getContainerNos(self, sumarioDados):
    nos= sumarioDados.getListaDeNos()
    containerNos= None
    if(len(nos) > 0):
      objects= []
      for coordenada in nos:
        o= obj.Object()
        o.setId(coordenada.getId() + self.uuid)
        o.setNm(coordenada.getName()  + self.uuid)
        o.setP0(ObjectItem(String.valueOf(coordenada.getName()  + self.uuid), None, None, None, None, None))
        o.setP1(ObjectItem(String.valueOf(coordenada.getX()), None, None, None, None, None))
        o.setP2(ObjectItem(String.valueOf(coordenada.getY()), None, None, None, None, None))
        o.setP3(ObjectItem(String.valueOf(coordenada.getZ()), None, None, None, None, None))
        objects.append(o)


      header= getDefaultStructNodeHeader()
      tabelaNos=TableNode(SciaXMLConstantes.STRUCT_NODE_TABLE_ID,SciaXMLConstantes.STRUCT_NODE_TABLE, SciaXMLConstantes.STRUCT_NODE_TABLE_NAME, header, objects)
      containerNos= Container(SciaXMLConstantes.STRUCT_NODE_ID, SciaXMLConstantes.STRUCT_NODE_TITLE, tabelaNos)
      return containerNos


  def getContainerPecas(self, sumarioDados):
    containerPecas= None
    objects= []
    objects.appendAll(getPecas(sumarioDados.getPecasFinais()))

    header= getDefaultBeamHeader()
    tabelaPecas= TableNode(SciaXMLConstantes.BEAM_TABLE_ID, SciaXMLConstantes.BEAM_TABLE, SciaXMLConstantes.BEAM_TABLE_NAME, header, objects)

    containerPecas= ctr.Container(SciaXMLConstantes.BEAM_ID, SciaXMLConstantes.BEAM_TITLE, tabelaPecas)

    return containerPecas


  def getContainerCamadas(self, sumarioDados):
    containerPecas= None

    objects= []
    objects.appendAll(getCamadas(sumarioDados.getPecasFinais()))

    header= getDefaultDataLayerNodeHeader()
    tabelaPecas= TableNode(SciaXMLConstantes.DATA_LAYER_TABLE_ID,SciaXMLConstantes.DATA_LAYER_TABLE, SciaXMLConstantes.DATA_LAYER_TABLE_NAME, header, objects)
    containerPecas= Container(SciaXMLConstantes.DATA_LAYER_ID, SciaXMLConstantes.DATA_LAYER_TITLE, tabelaPecas)
    return containerPecas


  def getCamadas(pecas):
    retorno= []

    pecasUnicas= set()

    # Removendo os itens repetidos
    for peca in pecas:
      pecasUnicas.append(peca.getTipo())


    if(len(pecasUnicas) > 0):
      counterID= 1
      for peca in pecasUnicas:
        pecaOrigem= RepositorioPecas.pecas.get(peca)
        o= Object()                
        containerOrigem= None
        listaContainer= pecaOrigem.getContainers()

        for container in listaContainer:
          if(container.getT().contains(SciaXMLConstantes.DATA_LAYER)):
            containerOrigem= container
            break


      # Um arquivo de peça só possui um object/peça no container Beam
      objectOrigem= containerOrigem.getTable().getObjects().get(0)

      o.setId(String.valueOf(counterID))
      o.setNm(peca)
      o.setP0(ObjectItem(peca, None, None, None, None, None))
      o.setP1(objectOrigem.getP1())
      retorno.append(o)
      counterID+= 1
 
    return retorno


  def getPecas(self, pecas):
    retorno= []
    for peca in pecas:
      o= Object()
      pecaOrigem= RepositorioPecas.pecas.get(peca.getTipo())

      containerOrigem= None
      listaContainer= pecaOrigem.getContainers()
      for container in listaContainer:
        if(container.getT().contains(SciaXMLConstantes.BEAM)):
          containerOrigem= container
          break

      # Um arquivo de peça só possui um object/peça no container Beam
      objectOrigem= containerOrigem.getTable().getObjects().get(0)

      o.setId(peca.getId() + self.uuid)
      o.setNm(peca.getName() + self.uuid)
      o.setP0(ObjectItem(peca.getId()  + self.uuid, None, None, None, None, None))
      o.setP1(ObjectItem(None,String.valueOf(peca.getNoInicial().getId()  + self.uuid),String.valueOf(peca.getNoInicial().getId() + self.uuid),None,None,None))
      o.setP2(ObjectItem(None,String.valueOf(peca.getNoFinal().getId() + self.uuid),String.valueOf(peca.getNoFinal().getId() + self.uuid),None,None,None))

      item= ObjectItem()
      item.setV(peca.getId())
      if(objectOrigem.getP3() != None):
        valor= objectOrigem.getP3().getN().substring(0, objectOrigem.getP3().getN().indexOf("-")-1)
        item.setN(valor)

      o.setP3(item)            
      o.setP4(objectOrigem.getP4())
      o.setP5(objectOrigem.getP5())
      o.setP6(objectOrigem.getP6())
      o.setP7(objectOrigem.getP7())
      o.setP8(objectOrigem.getP8())
      o.setP9(objectOrigem.getP9())
      o.setP10(objectOrigem.getP10())
      o.setP11(objectOrigem.getP11())
      o.setP12(objectOrigem.getP12())

    # TODO: Se necessário atualizar os valores da tabela de geometria
    # o.getXX().setT(String())
    retorno.append(o)
    return retorno

  def getDefaultBeamHeader(self):
    retorno= hdr.Header()
    retorno.setH0(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H0))
    retorno.setH1(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H1))
    retorno.setH2(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H2))
    retorno.setH3(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H3))
    retorno.setH4(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H4))
    retorno.setH5(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H5))
    retorno.setH6(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H6))
    retorno.setH7(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H7))
    retorno.setH8(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H8))
    retorno.setH9(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H9))
    retorno.setH10(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H10))
    retorno.setH11(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H11))
    retorno.setH12(HeaderItem(SciaXMLConstantes.BEAM_HEADER_H12))
    return retorno

  def getDefaultStructNodeHeader(self):
    retorno= Header()
    retorno.setH0(HeaderItem(SciaXMLConstantes.STRUCT_NODE_HEADER_H0))
    retorno.setH1(HeaderItem(SciaXMLConstantes.STRUCT_NODE_HEADER_H1))
    retorno.setH2(HeaderItem(SciaXMLConstantes.STRUCT_NODE_HEADER_H2))
    retorno.setH3(HeaderItem(SciaXMLConstantes.STRUCT_NODE_HEADER_H3))
    return retorno

  def getDefaultDataLayerNodeHeader(self):
    retorno= Header()
    retorno.setH0(HeaderItem(SciaXMLConstantes.DATA_LAYER_HEADER_H0))
    retorno.setH1(HeaderItem(SciaXMLConstantes.DATA_LAYER_HEADER_H1))
    return retorno

  def getDef(self):
    return self.defn
  def setDef(defn):
    self.defn= defn


  def getContainers(self):
    return containers
  def setContainers(containers):
    self.containers= containers


  def getXmlns(self):
    return self.xmlns
  def setXmlns(self, xmlns):
    self.xmlns= xmlns

  def toString(self):
    return "Project [xmlns=" + xmlns + ", def=" + self.defn + ", container=" + containers + "]"


  def getFileName(self):
    return self.fileName
  def setFileName(self, fileName):
    self.fileName= fileName


  def getComprimentoX(self):
    return self.comprimentoX
  def setComprimentoX(self, comprimentoX):
    self.comprimentoX= comprimentoX
  def getComprimentoY(self):
    return self.comprimentoY
  def setComprimentoY(self, comprimentoY):
    self.comprimentoY= comprimentoY
  def getComprimentoZ(self):
    return self.comprimentoZ
  def setComprimentoZ(self, comprimentoZ):
    self.comprimentoZ= comprimentoZ

  def getXMLElement(self,defFileName):
    project= ET.Element("project")
    project.set("xmlns",self.xmlns)
    df= ET.SubElement(project,"def")
    df.set("uri",defFileName)
    for c in self.containers:
      elem= c.getXMLElement(project)
    return project

  def getXMLTree(self,defFileName):
    project= self.getXMLElement(defFileName)
    tree = ET.ElementTree(project)
    return tree

  def getDefFileName(self):
    return self.fileName + ".def"

  def writeXMLFile(self): 
    tree= self.getXMLTree(getDefFileName())
    tree.write(self.fileName,encoding="UTF-8", xml_declaration=None, default_namespace=None, method="xml")
