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

import itertools
import os.path

from django.conf import settings

from .api_base import APIBaseView


class APIMatchesView(APIBaseView):
    login_required = True

    def get_context_data(self, **kwargs):
        """Returns the matching words in a dictionary"""
        context = super().get_context_data(**kwargs)
        words = [''.join(word) for word
                 in set(itertools.permutations(iterable=kwargs['letters'],
                                               r=kwargs['length']))]
        dictionary_words = self.load_dictionary(kwargs['dictionary'])
        context['results'] = sorted(set(words) & set(dictionary_words))
        return context

    def load_dictionary(self, dictionary):
        """Load all the words in the dictionary"""
        dictionary_file = '{NAME}.dict'.format(NAME=dictionary)
        if os.path.isfile(os.path.join(settings.DICTIONARY_DIR,
                                       dictionary_file)):
            return [word.strip('\n') for word in open(
                os.path.join(settings.DICTIONARY_DIR, dictionary_file), 'r')]
        else:
            return []
