# from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# import io
from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
from restapp.serializer import ClientSerializer
# import json
from django.http import JsonResponse
from restapp.models import Student

@csrf_exempt
def clients(request):
    if request.method == "POST":
        # s = request.body
        # print(s)
        # print(type(s)) #bytes
        # sdata = io.BytesIO(s) #byte to string
        # # print(sdata)
        # print(type(sdata)) #io.BytesIO
        # print(sdata)
        # dict1 = JSONParser().parse(sdata)
        # # print(dict1)
        # print(type(dict1)) #dict
        # serializer = StudentSerializer(data = dict1)

        data = JSONParser().parse(request)
        # print(type(data)) # dict
        # print(data)
        serializer = ClientSerializer(data = data) 
        # print(type(serializer)) # studentserializer
        if serializer.is_valid():
            serializer.save() #stu.is_valid() must be called before this
            # resp = { 'response':'Student added !!!'}
            # json_resp = json.dumps(resp)
            # return HttpResponse(json_resp)
            return JsonResponse(serializer.data, status = 201)
        else:
            # print('within else')
            return JsonResponse(serializer.errors,status=400)
    else: #GET request
        students = Student.objects.all()
        #print(dict(students))
        ser = ClientSerializer(students,many=True)
        # print(type(ser.data))
        return JsonResponse(ser.data,status=200,safe=False)
    
@csrf_exempt    
def clientDetails(request,sid):
    stu = clients.objects.get(id = sid)
    if stu:
        if request.method == "GET":
            serialiser = ClientSerializer(stu)
            # print("ser data ------>\n",serialiser.data) # gives dict
            data = serialiser.data
            return JsonResponse(data,status=200)
        elif request.method == "DELETE":
            stu.delete()
            success = {'success':'Client deleted !!'}
            return JsonResponse(success,status = 204)
        elif request.method == "PUT":
            data = JSONParser().parse(request)
            # print(data) here id is string
            data['id'] = sid
            data['id'] = int(data['id'])
            # print('updated',data)
            serializer = ClientSerializer(stu,data = data) 
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
    else:
        error = {'error':'Invalid client id, user not found'}
        return JsonResponse(error,status=404)
    



'''

in order to convert json iobyte  data to dict 
we have 
JSONPasrer.parse(iodata)

dict to Json byte data
JSONrenderer.render(dict)

'''
