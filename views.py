"""
Process requests
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.http import Http404

from medibot.serializers import ResultSerializer

class MedibotView(APIView):

	def post(self, request, format=None):
		# print 'REQUEST.DATA'
		# print request.data
		data = request.data.copy()
		serializer = ResultSerializer(data=data)

		if serializer.is_valid(raise_exception=True):
			return Response(serializer.data)
