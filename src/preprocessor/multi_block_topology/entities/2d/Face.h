// -*-c++-*-
//----------------------------------------------------------------------------
//  XC program; finite element analysis code
//  for structural analysis and design.
//
//  Copyright (C)  Luis Claudio Pérez Tato
//
//  This program derives from OpenSees <http://opensees.berkeley.edu>
//  developed by the  «Pacific earthquake engineering research center».
//
//  Except for the restrictions that may arise from the copyright
//  of the original program (see copyright_opensees.txt)
//  XC is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or 
//  (at your option) any later version.
//
//  This software is distributed in the hope that it will be useful, but 
//  WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details. 
//
//
// You should have received a copy of the GNU General Public License 
// along with this program.
// If not, see <http://www.gnu.org/licenses/>.
//----------------------------------------------------------------------------
//Face.h
//Face entities.

#ifndef FACE_H
#define FACE_H

#include "preprocessor/multi_block_topology/entities/1d/CmbEdge.h"

class Polygon3d;
namespace XC {
class Body;

//! @ingroup MultiBlockTopologyEnt
//!
//! @brief Surface.
class Face: public CmbEdge
  {
    friend class Edge;
    friend class Body;
    std::set<const Body *> bodies_surf; //!< Bodies that touch this surface (neighbors).

    void insert_body(Body *b);
    Node *getNode(const size_t &i);
    const Node *getNode(const size_t &i) const;
  protected:
    size_t ndivj; //!< number of divisions in the j axis.
    int get_index_opposite_side(const int &) const;
    virtual const Edge *get_opposite_side(const Edge *l) const;
    Edge *get_opposite_side(const Edge *l);
    size_t calc_ndiv_opposite_sides(const Edge *, const size_t &) const;
    void set_ndiv_opposite_sides(const size_t &, const size_t &);
    void set_ndiv_i(const size_t &);
    void set_ndiv_j(const size_t &);
  public:
    Face(void);
    Face(Preprocessor *m,const size_t &ndivI= 4, const size_t &ndivJ= 4);
    Face(const std::string &name,Preprocessor *m,const size_t &ndivI= 4, const size_t &ndivJ= 4);
    virtual bool operator==(const Face &) const;
     //! @brief Returns the dimension of the object.
    inline virtual unsigned short int GetDimension(void) const
      { return 2; }

    // Topology
    void update_topology(void);
    std::deque<std::pair<const Edge *, const Edge *> > getOppositeEdges(void) const;

    // Surface orientation.
    Vector3d getKVector(void) const;
    Matrix getLocalAxes(void) const;
    
    // Number of divisions
    inline size_t NDivI(void) const
      { return ndiv; }
    virtual void setNDivI(const size_t &);
    inline size_t NDivJ(void) const
      { return ndivj; }
    virtual void setNDivJ(const size_t &);
    virtual void ConciliaNDivIJ(void);
    virtual void SetElemSizeI(const double &sz);
    virtual void SetElemSizeJ(const double &sz);
    virtual void SetElemSizeIJ(const double &,const double &);
    virtual void SetElemSize(const double &sz, bool mustBeEven= true);
    
    //! @brief Returns the number of vertices.
    size_t getNumberOfVertices(void) const
      { return getNumberOfEdges(); }
    virtual const Pnt *getVertex(const size_t &i) const;
    Pos3d getCentroid(void) const;
    Polyline3d getContour(void) const;
    Polygon3d getPolygon(void) const;
    double getArea(void) const;
    //! @brief Return the bodies that touch this surface (neighbors).
    const std::set<const Body *> &getConnectedBodies(void) const
      { return bodies_surf; }
    size_t CommonEdge(const Face &other) const;
    int SenseOfEdge(const Edge *l,const Face &other) const;
    bool isConnectedTo(const Body &b) const;
    bool checkNDivs(const size_t &) const;
    virtual bool checkNDivs(void) const;

    virtual Node *getNode(const size_t &i1,const size_t &j,const size_t &k);
    virtual const Node *getNode(const size_t &i,const size_t &j,const size_t &k) const;
    virtual Node *getNode(const size_t &i,const size_t &j);
    virtual const Node *getNode(const size_t &i,const size_t &j) const;

    std::set<SetBase *> get_sets(void) const;
    void add_to_sets(std::set<SetBase *> &);
    virtual void reverse(void);

    int getVtkCellType(void) const;
  };

std::set<const Face *> getConnectedSurfaces(const Edge &l);
std::set<const Pnt *> getCommonVertex(const Face &,const Face &, const Face &);

} //end of XC namespace.

#endif
