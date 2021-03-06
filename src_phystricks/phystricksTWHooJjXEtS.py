# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def TWHooJjXEtS():
    pspict,fig = SinglePicture("TWHooJjXEtS")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction(sin(x)).graph(-5/2*pi,5/2*pi)

    pspict.DrawGraphs(f)
    pspict.axes.single_axeX.axes_unit=AxesUnit(pi/2,'')

    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

