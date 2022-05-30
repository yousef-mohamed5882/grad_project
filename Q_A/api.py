import Q_A
import joblib
import os
from .models import questions,answers
from .serializers import questionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination


@api_view(['GET',])

def questionlistapi(request):
    all_questions = questions.objects.all()
    serializer = questionSerializer(all_questions, many=True)
    questions1 = serializer.data
    context = {}
    i = 0
    for i in range(0,len(questions1)-5,5):
        context[(i//5)+1] = questions1[i:i+5]
    if len(questions1) > i:
        context[(i//5)+2] = questions1[i+5:]
    return Response(data=context)
@api_view(['POST',])
def results_api(request):
    if request.method == 'POST':
        from django.db.models import Q
        from django.db import connection
        model_path = os.path.join(os.getcwd()+r'/model/personalityPredictor.pk1')
        all_answers = answers.objects.all()

        f_answers = []
        counter = 0

        print(request.data)
        for answer in request.data:
            if counter <=34:
                f_answers.append(answer)
            counter+=1

        print(f_answers)
        print(request.data[35])
        print(request.data[40])

        char_list = []
        for answer1 in f_answers:
            x = answers.objects.filter(Q(answer = answer1)).first()
            if x:
                char_list.append(x.Char_ID_id)
            else: print(answer1)

        new_record = [0,int(request.data[40]),int(request.data[35]),int(request.data[36]),int(request.data[37]),int(request.data[38]),int(request.data[39]),0]
        print(new_record)
        model = joblib.load(open(model_path,"rb"))
        result = model.predict(new_record)
        if result == 0 :
            result = '3'
        elif result == 1:
            result = '9'
        elif result == 2:
            result = '7'
        elif result == 3:
            result = '2'
        elif result == 4:
            result = '4'
        print('the result = ', result)
        char_list.append(int(result[0]))
        print(char_list)
        print("Length of char list:",len(char_list))
    #################################################################
        c1=c2=c3=c4=c5=c6=c7=c8=c9=0
        for char in char_list:
            if char == 1:
                c1+=1
            if char == 2:
                c2+=1
            if char == 3:
                c3+=1
            if char == 4:
                c4+=1
            if char == 5:
                c5+=1
            if char == 6:
                c6+=1
            if char == 7:
                c7+=1
            if char == 8:
                c8+=1
            if char == 9:
                c9+=1
    ####################################################################
        final_list = [0]
        if c1 > 10:
            final_list.append(1)
        if c2 >= 3:
            final_list.append(2)
        if c3 >= 3:
            final_list.append(3)
        if c4 >= 5:
            final_list.append(4)
        if c5 >= 4:
            final_list.append(5)
        if c6 >= 5:
            final_list.append(6)
        if c7 >= 5:
            final_list.append(7)
        if c8 >= 5:
            final_list.append(8)
        if c9 >= 6:
            final_list.append(9)
        print(final_list)
        final_result = max(final_list)
        print('final result is:',final_result)
        return Response(data=final_result)
        
        
