from django.shortcuts import render
from matplotlib.style import context
from .models import questions,answers
frontlist = [('2','No, you prefer to stay away from danger.'),('3','You back off and take a long time to solve it.'),('50','You depend on yourself.')]

def function2(requist):
    list = [('2','No, you prefer to stay away from danger.'),('3','You back off and take a long time to solve it.'),('50','You depend on yourself.')]
    list_stat_Q = []
    result2 = []
    for i in list:
        if i[0] in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35):
            list_stat_Q.append(i)
    for i in list_stat_Q:
    
        # result2.append(raw.Char_ID_id)
        pass
    result = list[0][1]
    result2 = list[1][1]
    raw = answers.objects.extra(where=['answer=%s'], params=[result])
    raw1 = answers.objects.extra(where=['answer=%s'], params=[result2])
    print(raw)
    print(raw1)

    context = {'raw': raw}
    return render(requist,'main.html',context)