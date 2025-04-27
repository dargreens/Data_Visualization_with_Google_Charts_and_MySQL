import json
from django.http import JsonResponse
import mysql.connector
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime


@csrf_exempt
def index(request):
    if request.method=='POST':
        try:
            okrr=request.POST['text_box']
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="spark",
            database="solar_site" )
                
            cursor = mydb.cursor()
            cursor.execute(f"select * from {okrr}")
            answer = cursor.fetchall()
            mydb.close()
            x=[]
            
            for k,v,a in answer: 
                #date_format = "%Y-%m-%d %H:%M:%S"               
                #y =datetime.datetime.strptime(k, date_format)
                x.append([v,a])
                
            return render(request, 'index.html', {'data':x })
        except:
            return render(request, 'index.html', {'invalid_request':'data does not exist'})
    
    else:
        return render(request, 'index.html')



def jsonurl(request):
    pass  
            
    

    

