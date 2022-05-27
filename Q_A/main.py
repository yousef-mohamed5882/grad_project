import joblib
import os

model_path = os.path.join(os.getcwd()+r'\personalityPredictor.pk1')

def modelPredictor(listOfValues:list):
    model = joblib.load(open(model_path,"rb"))
    result = model.predict(listOfValues)
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
    '''
    note 1 
        you must install requirment.txt
        
    note 2
        ### Gender ### 
        Female = 0
        Male = 1
        
    note 3 
        the input must be in list same >> 
        new_record = [0,19,2,4,7,1,3,0]
        u must do it in backend
        
    note 4 
        function return personality type in string >> don't need any thing 
        in arabic >> "متبعبصش في حاجه " 
    '''
    return result


new_record = [0,19,9,2,2,2,2,0]
result = modelPredictor(new_record)
print(int(result[0]))