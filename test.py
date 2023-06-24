import speech_recognition as sr


t = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}

def offline(data):
    data = data.lower()
    current = 0
    total = 0
    count = 0
    arr = data.split(" ")
    i = 0
    while i < len(arr):
        print(str(arr[i])+" "+str(arr[i].isnumeric())+" "+str(i))
        if arr[i].isnumeric():
            current = float(arr[i])
            count = count + 1
        if total == 0:
            total = current
        if arr[i] == 'into' or arr[i] == '*':
            i = i + 1
            current = float(arr[i])
            total = total * current
        if arr[i] == 'plus' or arr[i] == '+':
            i = i + 1
            current = float(arr[i])
            total = total + current
        if arr[i] == 'minus' or arr[i] == '-':
            i = i + 1
            current = float(arr[i])
            total = total - current
        if arr[i] == 'divide':
            total = total / current
        if arr[i] == 'percentage':
            i = i + 1
            current = float(arr[i])
            total = total / count
        if arr[i] == 'power':
            i = i + 1
            current = float(arr[i])
            total = pow(total,current)
        if arr[i] == 'root':
            i = i + 1
            current = float(arr[i])
            total = total ** count
        if arr[i] == 'increase':
            i = i + 1
            current = float(arr[i])
            total = total + 1
        if arr[i] == 'decrease':
            i = i + 1
            current = float(arr[i])
            total = total - 1
        if arr[i] == 'table':
            i = i + 2
            current = int(arr[i])
            for k in range(1,10):
                print(str(current)+" * "+str(k)+" = "+str(current * k))
        i = i + 1    
    return total            
            
        
r = sr.Recognizer()
#temp = sr.Microphone.list_microphone_names()
#print(temp)
mic = sr.Microphone()
with mic as source:
#with sr.AudioFile('voice1.wav') as source:
    print("speak")
    r.adjust_for_ambient_noise(source)
    audio = r.record(source,duration=4)
    #try:
    data = r.recognize_google(audio)
    print("=="+data)
    total = offline(data)
    print(total)
    #except Exception as e:
    #    print(str(e))    
    

        
            
