import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongorest import MongoRest
from flask.ext.mongorest.views import ResourceView
from flask.ext.mongorest.resources import Resource
from flask.ext.mongorest import operators as ops
from flask.ext.mongorest import methods  
from ga4ghmongo.schema import *
from flask.ext.mongorest.operators import Exact
from flask.ext.mongorest.operators import Gte
from flask.ext.mongorest.operators import Operator

class Boolean(Operator):
    op = 'exact'

    def prepare_queryset_kwargs(self, field, value, negate):
        print value
        if value == 'false':
            bool_value = False
        else:
            bool_value = True

        if negate:
            bool_value = not bool_value

        return {field: bool_value}

class In(Operator):
    op = 'in'

app = Flask(__name__)

MONGOLAB_URI =  os.environ.get("MONGOLAB_URI")
if MONGOLAB_URI is None:
	app.config.update(
	    MONGODB_HOST = 'localhost',
	    MONGODB_PORT = '27017',
	    MONGODB_DB = 'atlas-tb',
	)
else:
	app.config.update(MONGODB_HOST=MONGOLAB_URI)

db = MongoEngine(app)
api = MongoRest(app)


class ReferenceSetResource(Resource):
    document = ReferenceSet

class ReferenceResource(Resource):
    document = Reference
    related_resources = {
        'reference_sets': ReferenceSetResource,
    }

class VariantSetResource(Resource):
    document = VariantSet

class VariantResource(Resource):
    max_limit = 250
    document = Variant
    # related_resources = {
        # 'variant_sets': VariantSetResource,
        # 'reference' : ReferenceResource
    # }
    filters = {
        'is_snp': [Boolean],
        "variant_sets" : [ops.Exact, In]
    }
    allowed_ordering = ["start"]

class CallSetResource(Resource):
    document = CallSet

class VariantCallSetResource(Resource):
    document = VariantCallSet

class VariantCallResource(Resource):
    max_limit = 250
    document = VariantCall
    child_document_resources = {
        "call_set" : VariantCallSet,
        'variant': Variant,
    }
#    allowed_ordering = ["start"]


@api.register(name='variant_sets', url='/variant_sets/')
class VariantSetView(ResourceView):
    resource = VariantSetResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]

@api.register(name='variants', url='/variants/')
class VariantView(ResourceView):
    resource = VariantResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]

@api.register(name='call_sets', url='/call_sets/')
class VariantCallView(ResourceView):
    resource = CallSetResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]

@api.register(name='variant_call_sets', url='/variant_call_sets/')
class VariantCallView(ResourceView):
    resource = VariantCallSetResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]

@api.register(name='variant_calls', url='/variant_calls/')
class VariantCallView(ResourceView):
    resource = VariantCallResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]


  