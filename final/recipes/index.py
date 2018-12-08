from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(recipe=row[0], ingredients=row[1], reviews=row[2],time_to_cook=row[3] ) for row in model.select()]
        return render_template('index.html',entries=entries)
