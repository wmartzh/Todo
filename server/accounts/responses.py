
from rest_framework.response import Response


class ResponseHelper():

    def emptyField(name):
        format = {
            'error':{ name : 'Please provide a '+name+'field' }
        }
        return Response(format,status=400);