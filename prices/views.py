from django.shortcuts import render
import pandas as pd
from datetime import datetime
from datetime import timedelta 
import pickle
with open('model/model_final', 'rb') as f:
    modelf = pickle.load(f)

def tryout(request):
    return render(request, 'home.html')

def predict(request):
    if request.method =='POST':
        print(request.POST.dict())
        val = {}
        val['destination']=request.POST.get('destination')
        val['compagnie']=request.POST.get('compagnie')
        val['date_depart']=request.POST.get('date_depart')
        val['date_arivee']=request.POST.get('date_arivee')

        datearivee  = request.POST.get('date_arivee')
        datepart = request.POST.get('date_depart')

        val['escale']=request.POST.get('escale')
        escale  = request.POST.get('escale')
        val['lheure_darivee']=request.POST.get('lheure_darivee')
        for key, value in val.items():
            if key== 'destination':
                if value == 'Paris':
                    destination_paris = 1
                    destination_rome = 0
                    destination_madrid = 0
                    destination_istanbul = 0
                elif value == 'Rome':
                    destination_paris = 0
                    destination_rome = 1
                    destination_madrid = 0
                    destination_istanbul = 0
                elif value == 'Istanbul':
                    destination_paris = 0
                    destination_rome = 0
                    destination_madrid = 0
                    destination_istanbul = 1
                elif value == 'Madrid':
                    destination_paris = 0
                    destination_rome = 0
                    destination_madrid = 1
                    destination_istanbul = 0
                else:
                    destination_paris = 0
                    destination_rome = 0
                    destination_madrid = 0
                    destination_istanbul = 0

            if key== 'compagnie':

                if value == 'Air france':
                    compagnie_air_france = 1
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 0
                    compagnie_emirates = 0
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 0
                    compagnie_vueling = 0 
                    compagnie_iberia = 0
                    print(compagnie_air_france)
                elif value == 'Aliitalia':
                    compagnie_air_france = 0
                    compagnie_aliitalia = 1
                    compagnie_egyptair = 0
                    compagnie_emirates = 0
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 0
                    compagnie_vueling = 0 
                    compagnie_iberia = 0

                elif value == 'Egyptair':
                    compagnie_air_france = 0
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 1
                    compagnie_emirates = 0
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 0
                    compagnie_vueling = 0 
                    compagnie_iberia = 0

                elif value == 'Emirates':
                    compagnie_air_france = 0
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 0
                    compagnie_emirates = 1
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 0
                    compagnie_vueling = 0 
                    compagnie_iberia = 0
                
                elif value == 'Ryan air':
                    compagnie_air_france = 0
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 0
                    compagnie_emirates = 0
                    compagnie_ryan_air = 1
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 0
                    compagnie_vueling = 0 
                    compagnie_iberia = 0
                
                elif value == 'Turkish airlines':
                    compagnie_air_france = 0
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 0
                    compagnie_emirates = 0
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 1
                    compagnie_transavia_France = 0
                    compagnie_vueling = 0 
                    compagnie_iberia = 0


                elif value == 'Transavia france':
                    compagnie_air_france = 0
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 0
                    compagnie_emirates = 0
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 1
                    compagnie_vueling = 0 
                    compagnie_iberia = 0

                elif value == 'Vueling':
                    compagnie_air_france = 0
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 0
                    compagnie_emirates = 0
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 0
                    compagnie_vueling = 1
                    compagnie_iberia = 0

                elif value == 'Iberia':
                    compagnie_air_france = 0
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 0
                    compagnie_emirates = 0
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 0
                    compagnie_vueling = 0
                    compagnie_iberia = 1
                else:
                    compagnie_air_france = 0
                    compagnie_aliitalia = 0
                    compagnie_egyptair = 0
                    compagnie_emirates = 0
                    compagnie_ryan_air = 0
                    compagnie_turkish_airlines = 0
                    compagnie_transavia_France = 0
                    compagnie_vueling = 0
                    compagnie_iberia = 0

            if key == 'escale':
                if (value=='Sans escale'):
                    escale = 0
                elif (value=='1 escale'):
                    escale = 1
                elif (value=='2 escale'):
                    escale = 2
                elif (value=='3 escale'):
                    escale = 3

            if key == 'date_depart':
                jour_depart  = int(pd.to_datetime(value, format="%Y-%m-%dT%H:%M").day)
                mois_depart = int(pd.to_datetime(value, format="%Y-%m-%dT%H:%M").month)
                heure_depart = int(pd.to_datetime(value, format="%Y-%m-%dT%H:%M").hour)
                min_depart = int(pd.to_datetime(value, format="%Y-%m-%dT%H:%M").minute)

            if key == 'date_arivee':
                jour_retour = int(pd.to_datetime(value, format="%Y-%m-%d").day)
                mois_retour = int(pd.to_datetime(value, format="%Y-%m-%d").month)

            if key == 'lheure_darivee':
                
                heure_arivee = int(pd.to_datetime(value, format="%H:%M").hour)
                min_arivee = int(pd.to_datetime(value, format="%H:%M").minute)
                duree_heure = abs(heure_arivee - heure_depart)
                duree_min = abs(min_arivee - min_depart)

            
        
        time1 = datetime.strptime(datepart , '%Y-%m-%dT%H:%M') 
        time2 = datetime.strptime(datearivee , '%Y-%m-%d')  
        duree_sejour = int(str(time2 - time1).split(' ')[0]) + 1
        
    
        a = modelf.predict([[ 
            escale,
            duree_sejour,
            jour_depart,
            mois_depart,
            jour_retour,
            mois_retour,
            duree_heure,
            duree_min,
            heure_depart,
            min_depart, 
            heure_arivee,
            min_arivee,
            destination_istanbul, 
            destination_madrid, 
            destination_paris,
            destination_rome,
            compagnie_air_france, 
            compagnie_aliitalia,
            compagnie_egyptair,
            compagnie_emirates,
            compagnie_iberia, 
            compagnie_ryan_air,
            compagnie_transavia_France,
            compagnie_turkish_airlines, 
            compagnie_vueling
    ]])

        output=round(a[0], 2)

        context = {'output': output}
    return render(request, 'home.html', context)