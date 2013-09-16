#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ©2013 Yordan Miladinov
# yordan[at]4web[dot]bg

import datetime
import random


multipliers = [
    2, 4, 8, 5, 10, 9, 7, 3, 6
]


def get_verif(base):
    numbers = [int(c) for c in base]
    s = sum(map(lambda t: t[0] * t[1], zip(numbers, multipliers)))
    verif = (s % 11) % 10
    return verif


def gen(birth=None, sex='m'):
    if birth is None:
        today = datetime.date.today()
        # Let's say EGN holder is between 18 and 28 years old
        y = today.year - (18 + random.randint(0, 10))
        birth = today.replace(year=y)
    base = '{date}{num:0>2}{sex}'.format_map({
        'date': birth.strftime('%y%m%d'),
        'num': random.randint(0, 99),
        'sex': 2 if sex == 'm' else 1,
    })
    verif = get_verif(base)
    return ''.join([base, str(verif)])


def main():
    print(gen())


if __name__ == '__main__':
    main()
