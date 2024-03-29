# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .Model import Model
from datetime import datetime
from google.cloud import datastore
from google.cloud import translate
import six

def translate_text(text):
    """Translates text into the target language"""
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

        result = translate_client.translate(text, target_language='es')
        return result['translatedText']

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ name, email, date, message ]
    where name, email, and message are Python strings
    and where date is a Python datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['recipe'],entity['ingredients'],entity['reviews'],entity['time_to_cook']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cs410c-tim-pugh2')

    def select(self):
        query = self.client.query(kind = 'recipe')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self, recipe, ingredients, reviews,time_to_cook):
        key = self.client.key('recipe')
        rev = datastore.Entity(key)
        rev.update( {
            'recipe': recipe,
            'ingredients' : ingredients,
            'reviews' : reviews,
            'time_to_cook' : time_to_cook
            })
        self.client.put(rev)
        return True
