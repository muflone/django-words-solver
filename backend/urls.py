##
#     Project: Django Words Solver Backend
# Description: Django backend for Words Solver Android app
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2019 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

from django.urls import path

from . import views


urlpatterns = []

# Version page
urlpatterns.append(path('versions/',
                        views.APIVersionsView.as_view(),
                   name='api/versions'))

# Status page
urlpatterns.append(path('status/',
                        views.APIStatusView.as_view(),
                   name='api/status'))

# Permutations page
urlpatterns.append(path('permutations/'
                        '<int:device>/'
                        '<int:password>/'
                        '<slug:letters>/'
                        '<int:length>/',
                        views.APIPermutationsView.as_view(),
                   name='api/permutations'))

# Default route
urlpatterns.append(path('',
                        views.APIVersionsView.as_view(),
                   name='api/default'))
