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

import sqlite3
import sys

import django

import json_views

import project

from .api_base import APIBaseView


class APIVersionsView(APIBaseView):
    login_required = False

    def get_context_data(self, **kwargs):
        """Returns the versions"""
        context = super().get_context_data(**kwargs)
        context['version'] = project.VERSION
        context['python version'] = sys.version
        context['python version info'] = sys.version_info
        context['sqlite version'] = sqlite3.sqlite_version
        context['sqlite version info'] = sqlite3.sqlite_version_info
        context['sqlite3 version'] = sqlite3.version
        context['sqlite3 version info'] = sqlite3.version_info
        context['django version'] = django.__version__
        context['django version info'] = django.VERSION
        context['json_views version'] = json_views.__version__
        context['json_views version info'] = json_views.__version_info__
        return context
