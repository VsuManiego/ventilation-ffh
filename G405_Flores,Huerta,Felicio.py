
import requests, json


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Ormoc, PH"
API_KEY = "c3dcdb0204f115dc5394ff1f1f06d3ff"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)

if response.status_code == 200:
   data = response.json()
   main = data['main']

   temperature = main['temp']
   humidity = main['humidity']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature - 273.15}")
   print(f"Humidity: {humidity}")

Outside_temp = temperature - 273.15
outside_Hum = humidity




    
print('''
>establishment walls are concrete
''')
print('''
>dining room temperature: 22.22 degrees Celsius
''')
number_person = int(input('''
number of person inside? '''))
    
heat_person = 730
room_temp = 22.22
k = 2.25
wall_thickness = 0.254
wall_area = 140
temp_diff = (Outside_temp - room_temp)
Q = (((k * wall_area * temp_diff) / 0.254) + (heat_person * number_person))

if 4655 < Q <= 5000:
   print('''
   >30% Make-up air system was turned on''')
elif 6000 >= Q > 5000:
   print('''
   >60% Make-up air system was turned on''')
elif Q > 6000:
   print('''
   >100% Make-up air system was turned on''')
else:
   print('''
   >Make-up air system was turned off''')
       
import math
T1 = Outside_temp
T2 = room_temp
RH1 = outside_Hum


absMoisture1 = (RH1*0.42*math.exp(T1*10*0.006235398)/10)
RH2 = (absMoisture1*10/(0.42*math.exp(T2*10*0.006235398)))

if RH2 > 50:
   print('''
   >Exhaust fans was turned on''')
else:
   print('''
   >Exhaust fans was turned off''')
   


def menu():
   print('''
   ------------------------
   where do you want to go?
   ------------------------''')

   print('press 1: stay in the dining room ')
   print('press 2: go to the main kitchen ')
   print('press 3: exit ')
   return(int(input('''
Select: ''')))
      
run = menu()


while True:
   if run == 1:
      print('''
      >Welcome customer!''')
      run = menu()  
   elif run == 2:
      print('''
      >kitchen temperature: 21 degrees Celsius''')
      number_person2 = int(input('''
      >number of personnel inside? '''))
      ref = 430
      room_temp2 = 21
      wall_area2 = 120
      temp_diff2 = (Outside_temp - room_temp2)
      Q2 = ((k * wall_area2 * temp_diff2) / 0.254) + (heat_person * number_person2) + ref
      print('''
      >refrigerator was turned on everyday''')
      if 5952 < Q2 <= 6000:
         print('''
         >30% Make-up air system was turned on''')
      elif 7000 >= Q2 > 6000:
         print('''
         >60% Make-up air system was turned on''')
      elif Q2 > 7000:
         print('''
         >100% Make-up air system was turned on''')
      else:
         print('''
         >Make-up air system was turned off''')
      import math
      T1 = Outside_temp
      T3 = room_temp2
      RH1 = outside_Hum
      absMoisture1 = (RH1*0.42*math.exp(T1*10*0.006235398)/10)
      RH3 = (absMoisture1*10/(0.42*math.exp(T3*10*0.006235398)))

      if RH3 > 30:
         print('''
         >Exhaust fans was turned on''')
      else:
         print('''
         >Exhaust fans was turned off''')
         
         
         
      def menu2():
            
         print('''
         ------------
         MAIN KITCHEN
         ------------''')
         print('press 1: turn on restaurant range ')
         print('press 2: turn off restaurant range ')
         print('press 3: turn on oven ')
         print('press 4: turn off oven ')
         print('press 5: go back to the dining room ')
         return(int(input('''
Select: ''')))
      run2 = menu2()
      while True:
         if run2 == 1:
            print('''
            >restaurant range was turned on''')
            print('''
            >100% Ventilation hoods was turned on''')

            run2 = menu2()

         elif run2 == 2:
            print('''
            >restaurant range was turned off''')
            print('''
            >Ventilation hoods was turned off''')

            run2 = menu2()

         elif run2 == 3:
               
            print('''
            >oven was turned on''')
               
            room_temp2 = 21
            oven = 284
            wall_area2 = 120
            temp_diff2 = (Outside_temp - room_temp2)

            Q3 = Q2 + oven
               
               
            if 5952 < Q2 <= 6000:
               print('''
               >30% Make-up air system was turned on''')
            elif 7000 >= Q2 > 6000:
               print('''
               >60% Make-up air system was turned on''')
            elif Q2 > 7000:
               print('''
               >100% Make-up air system was turned on''')
            else:
               print('''
               >Make-up air system was turned off''')

            import math
            T1 = Outside_temp

            T4 = room_temp2
            RH1 = outside_Hum


            absMoisture1 = (RH1*0.42*math.exp(T1*10*0.006235398)/10)
            RH3 = (absMoisture1*10/(0.42*math.exp(T4*10*0.006235398)))

            if RH3 > 30:
               print('''
               >Exhaust fans was turned on''')
               
            else:
               print('''
               >Exhaust fans was turned off''')
            run2 = menu2()
         elif run2 == 4:
               
            print('''
            >Oven was turned off''')

               
            room_temp2 = 21
            oven = 284
            wall_area2 = 120
            temp_diff2 = (Outside_temp - room_temp2)
            Q3 = Q2 - oven
            if 5952 < Q3 <= 6000:
               print('''
               >30% Make-up air system was turned on''')
            elif 7000 >= Q3 > 6000:
               print('''
               >60% Make-up air system was turned on''')
            elif Q3 > 7000:
               print('''
               >100% Make-up air system was turned on''')
            else:
               print('''
               >Make-up air system was turned off''')
            import math
            T1 = Outside_temp
            T4 = room_temp2
            RH1 = outside_Hum

            absMoisture1 = (RH1*0.42*math.exp(T1*10*0.006235398)/10)
            RH3 = (absMoisture1*10/(0.42*math.exp(T4*10*0.006235398)))

            if RH3 > 30:
               print('''
               >Exhaust fans was turned on''')
               
            else:
               print('''
               >Exhaust fans was turned off''')
            run2 = menu2()

         elif run2 == 5:
            run = menu()
            break
          
   elif run == 3:
      print('''
      thank you for visiting FHF restaurant''')
      break
