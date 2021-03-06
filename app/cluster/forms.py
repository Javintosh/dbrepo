# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright (C) 2018 Toni Mas <antoni.mas@gmail.com>
#
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


from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import DataRequired


class ClusterForm(FlaskForm):
    cluname = StringField(u'Cluster Name', validators=[DataRequired()])
    business = SelectField(
        label=u'Business',
        coerce=int,
        validators=[DataRequired()]
    )
    domainprefix = StringField(u'Domain Prefix', validators=[DataRequired()])
    active = BooleanField(u'Active', validators=[DataRequired()])
