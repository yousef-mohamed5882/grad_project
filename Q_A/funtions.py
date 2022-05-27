# from .models import answers
def function2(front_list):
    list = front_list
    for i in list:
        if i[0] in ('2','4'):
            print('well-done',i[1])

frontlist = [('2','very good2'),('3','very good3'),('4','very good4'),('5','very good5')]
function2(frontlist)

# def function2(requist,front_list):
#     list = front_list
#     list_stat_Q = []
#     result2 = []
#     for i in list:
#         if i[0] in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35):
#             list_stat_Q.append(i)
#     for i in list_stat_Q:
#         raw = answers.objects.extra(where=['answer=%s'], params=[i[1]])
#         # result2.append(raw.Char_ID_id)
#         print(raw)

# frontlist = [('2','No, you prefer to stay away from danger.'),('3','You back off and take a long time to solve it.'),('50','You depend on yourself.')]
# function2(frontlist)