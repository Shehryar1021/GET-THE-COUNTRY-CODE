country_code = {'INDIA' : '0091' ,
                'AUSTRALIA' : '0025' ,
                'NEPAL' : '00977'}
             
print("COUNTRY CODE FOR INDIA -")            
print(country_code.get('INDIA', 'NOT FOUND'))
print("COUNTRY CODE FOR JAPAN -")            
print(country_code.get('JAPAN', 'NOT FOUND'))