from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
from google.cloud import translate
import six

def translate_text(text):
    """Translates text into the target language"""
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

        result = translate_client.translate(text, target_language='es')
        
        translator = Translator()
        txt = translator.translate(text, dest = 'es')
        return result['translatedText']

class Recipe(MethodView):
    def get(self):
        return render_template('recipes.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(translate_text((request.form['recipe'])), request.form['ingredients'], request.form['reviews'], request.form['time_to_cook'])
        return redirect(url_for('index'))
