from flask import Flask,render_template,request
import pybuster as pb

app = Flask(__name__)


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        #print(form_data)
        #print(request.form)
        a=form_data
        if a['Field1_name']=='' or a['Field2_name']=='':
            return 'You need to fill every textbox.<br><a href="/form"><em><font font color="#D2738A">Go Back</a> </font>'
        '''
        for e in a:
            print(e)
            print(a[e])
        '''
        #print(a)
        if 'direct' in a and 'subd' in a:
            url=a['Field1_name']
            wl=a['Field2_name']
            lista=(pb.sdir(url, wl))
            stringa=''
            if lista==None:
                pass
            else:
                for e in range(len(lista)):
                    stringa+='<p>'+lista[e]+'</p><br>'

            lista=[]
            lista=(pb.sub(url, wl))
            if lista==None:
                pass
            else:
                stringa=''
                for e in range(len(lista)):
                    stringa+='<p>'+lista[e]+'</p><br>'
            with open('logs.txt', mode='w', encoding='UTF-8') as f:
                f.write(stringa)
            if stringa=='':
                return 'Nothing was found.<br><a href="/form"><em><font font color="#D2738A">Go Back</a> </font>'
            else:
                with open('logs.txt', mode='w', encoding='UTF-8') as f:
                    f.write(stringa)
                return stringa
        elif 'direct' in a:
            url=a['Field1_name']
            wl=a['Field2_name']
            lista=(pb.sdir(url, wl))
            stringa=''
            for e in range(len(lista)):
                stringa+='<p>'+lista[e]+'</p><br>'
            if stringa=='':
                return 'Nothing was found.<br><a href="/form"><em><font font color="#D2738A">Go Back</a> </font>'
            else:
                with open('logs.txt', mode='w', encoding='UTF-8') as f:
                    f.write(stringa)
                return stringa

        elif 'subd' in a:
            url=a['Field1_name']
            wl=a['Field2_name']
            stringa=''
            lista=(pb.sub(url, wl))
            if lista==None:
                pass
            else:
                for e in range(len(lista)):
                    stringa+='<p>'+lista[e]+'</p><br>'
            if stringa=='' or stringa==Null:
                return 'Nothing was found.<br><a href="/form"><em><font font color="#D2738A">Go Back</a> </font>'
            else:
                with open('logs.txt', mode='w', encoding='UTF-8') as f:
                    f.write(stringa)
                return stringa

        elif 'direct' and 'subd' not in a:
            return 'You need to pick at least one of the two checkboxes.<br><a href="/form"><em><font font color="#D2738A">Go Back</a> </font>'







app.run(host='localhost', port=5000, debug=True)
