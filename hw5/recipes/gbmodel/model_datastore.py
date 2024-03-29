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

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ recipe, ingredients, reviews, time_to_cook ]
    where recipe, ingredients, reviews, and time_to_cook are Python strings

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
        query = self.client.query(kind = 'datastore')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self,name,email,message):
        key = self.client.key('datastore')
        rev = datastore.Entity(key)
        rev.update( {
            'recipe': recipe,
            'ingredients' : ingredients,
            'reviews' : reviews,
            'time_to_cook' : time_to_cook
            })
        self.client.put(rev)
        return True
