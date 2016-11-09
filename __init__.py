# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AQGeocodage
                                 A QGIS plugin
 Localiser une adresse contenue dans Adresse Quebec
                             -------------------
        begin                : 2016-11-09
        copyright            : (C) 2016 by Steve Toutant/INSPQ
        email                : steve.toutant@inspq.qc.ca
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AQGeocodage class from file AQGeocodage.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .msp_glo import AQGeocodage
    return AQGeocodage(iface)
