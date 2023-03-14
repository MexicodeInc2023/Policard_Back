from rest_framework.response import Response
from apps.credential.models import *
from apps.credential.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet

# Create your views here.

class studentView(GenericViewSet):
    serializer_class = studentSerializer
    update_serializer_class = studentUpdateSerializer
    model = student
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, user=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.exclude(status='eliminado')
        return self.queryset

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            'msg': 'OK',
            'data': data.data
        }
        return Response(data)

    # Obtenemos el registro de students por id de user 
    def retrieve(self, reques, pk):
        print(pk,"Hola")
        print(self.get_object(pk),"Hola")
        student = self.get_object(pk)
        student_serializer = self.serializer_class(student)
        data = {
            'msg': 'OK',
            'data': student_serializer.data
        }
        return Response(data, status=200)

    def create(self, request):
        student_serializer = self.serializer_class(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            data = {
                'status': 201,
                'message': 'Registro creado correctamente',
                'data': student_serializer.data
            }
            return Response(data, status=201)
        data = {
            'status': 400,
            'message': 'Se produjo un error al crear el registro',
            'erros': student_serializer.errors,
            'data': None
        }
        return Response(data, status=400)

    def update(self, request, pk):
        student = self.get_object(pk=pk)
        student_serializer = self.update_serializer_class(student, data=request.data)

        if student_serializer.is_valid():
            student_serializer.save()
            return Response({
                'status': 200,
                'message': 'Informacion actualizada correctamente',
                'data': student_serializer.data
            }, status=200)

        return Response({
            'status': 400,
            'message': 'Se produjo un error al actualizar los datos',
            'data': None
        }, status=400)

    def destroy(self, request, pk):
        student = self.get_object(pk=pk)
        student.status = 'inactivo'
        student.save()
        return Response({
            'message': 'Informacion eliminada correctamente'
        })
class request_reasonView(GenericViewSet):
    serializer_class = request_reasonSerializer
    update_serializer_class = request_reasonUpdateSerializer
    model = request_reason
    queryset = None
    
    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if  self.queryset is None:
            self.queryset = self.model.objects.exclude(status='eliminado')
        return self.queryset

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            'msg': 'OK',
            'data': data.data
        }
        return Response(data)

    def retrieve(self, reques, pk):
        request_reason = self.get_object(pk)
        request_reason_serializer = self.serializer_class(request_reason)
        data = {
            'msg': 'OK',
            'data': request_reason_serializer.data
        }
        return Response(data, status=200)

    def create(self, request):
        request_reason_serializer = self.serializer_class(data=request.data)
        if  request_reason_serializer.is_valid():
            request_reason_serializer.save()
            data = {
                'status': 201,
                'message': 'Registro creado correctamente',
                'data': {
                'id': request_reason.id,
                **request_reason_serializer.data,
            },
            }
            return Response(data, status=201)
        data = {
            'status': 400,
            'message': 'Se produjo un error al crear el registro',
            'erros': request_reason_serializer.errors,
            'data': None
        }
        return Response(data, status=400)
    
    def update(self, request, pk):
        request_reason_serializer = self.get_object(pk=pk)
        request_reason_serializer = self.update_serializer_class(request_reason, data=request.data)

        if  request_reason_serializer.is_valid():
            request_reason_serializer.save()
            return Response({
                'status': 200,
                'message': 'Informacion actualizada correctamente',
                'data': request_reason_serializer.data
            }, status=200)

        return Response({
            'status': 400,
            'message': 'Se produjo un error al actualizar los datos',
            'data': None
        }, status=400)

    def destroy(self, request, pk):
        request_reason_serializer = self.get_object(pk=pk)
        request_reason_serializer.status = 'eliminado'
        request_reason_serializer.save()
        return Response({
            'message': 'Informacion eliminada correctamente'
        })
        
class careersView(GenericViewSet):
    serializer_class = careersSerializer
    update_serializer_class = careersUpdateSerializer
    model = careers
    queryset = None
    
    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if  self.queryset is None:
            self.queryset = self.model.objects.exclude(status='inactiva')
        return self.queryset

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            'msg': 'OK',
            'data': data.data
        }
        return Response(data)

    def retrieve(self, reques, pk):
        careers = self.get_object(pk)
        careers_serializer = self.serializer_class(careers)
        data = {
            'msg': 'OK',
            'data': careers_serializer.data
        }
        return Response(data, status=200)

    def create(self, request):
        careers_serializer = self.serializer_class(data=request.data)
        if  careers_serializer.is_valid():
            careers_serializer.save()
            data = {
                'status': 201,
                'message': 'Registro creado correctamente',
                'data': careers_serializer.data
            }
            return Response(data, status=201)
        data = {
            'status': 400,
            'message': 'Se produjo un error al crear el registro',
            'erros': careers_serializer.errors,
            'data': None
        }
        return Response(data, status=400)
    
    def update(self, request, pk):
        careers_serializer = self.get_object(pk=pk)
        careers_serializer = self.update_serializer_class(careers, data=request.data)

        if  careers_serializer.is_valid():
            careers_serializer.save()
            return Response({
                'status': 200,
                'message': 'Informacion actualizada correctamente',
                'data': careers_serializer.data
            }, status=200)

        return Response({
            'status': 400,
            'message': 'Se produjo un error al actualizar los datos',
            'data': None
        }, status=400)

    def destroy(self, request, pk):
        careers_serializer = self.get_object(pk=pk)
        careers_serializer.status = 'inactiva'
        careers_serializer.save()
        return Response({
            'message': 'Informacion eliminada correctamente'
        })

class emergency_infoView(GenericViewSet):
    serializer_class = emergency_infoSerializer
    update_serializer_class = emergency_infoUpdateSerializer
    model = emergency_info
    queryset = None
    
    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if  self.queryset is None:
            self.queryset = self.model.objects.exclude(status='eliminado')
        return self.queryset

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            'msg': 'OK',
            'data': data.data
        }
        return Response(data)

    def retrieve(self, reques, pk):
        emergency_info = self.get_object(pk)
        emergency_info_serializer = self.serializer_class(emergency_info)
        data = {
            'msg': 'OK',
            'data': emergency_info_serializer.data
        }
        return Response(data, status=200)

    def create(self, request):
        emergency_info_serializer = self.serializer_class(data=request.data)
        if  emergency_info_serializer.is_valid():
            emergency_info_serializer.save()
            data = {
                'status': 201,
                'message': 'Registro creado correctamente',
                'data': emergency_info_serializer.data
            }
            return Response(data, status=201)
        data = {
            'status': 400,
            'message': 'Se produjo un error al crear el registro',
            'erros': emergency_info_serializer.errors,
            'data': None
        }
        return Response(data, status=400)
    
    def update(self, request, pk):
        emergency_info_serializer = self.get_object(pk=pk)
        emergency_info_serializer = self.update_serializer_class(emergency_info, data=request.data)

        if  emergency_info_serializer.is_valid():
            emergency_info_serializer.save()
            return Response({
                'status': 200,
                'message': 'Informacion actualizada correctamente',
                'data': emergency_info_serializer.data
            }, status=200)

        return Response({
            'status': 400,
            'message': 'Se produjo un error al actualizar los datos',
            'data': None
        }, status=400)

    def destroy(self, request, pk):
        emergency_info_serializer = self.get_object(pk=pk)
        emergency_info_serializer.status = 'eliminado'
        emergency_info_serializer.save()
        return Response({
            'message': 'Informacion eliminada correctamente'
        })