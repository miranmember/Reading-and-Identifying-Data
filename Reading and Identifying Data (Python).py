######################################################
# Project: Project 3
# Student Name: Member, Miran
# UIN: 654424039
# URL to repl.it: https://repl.it/@mmembe2/Fall2019-Project-3-starter
######################################################
data_by_region = {}
data_by_country = {} 
answers = []

def load_dictionaries():#created dictionary from cvs file
  f = open("dph_SYB60_T03_Population Growth, Fertility and Mortality Indicators.csv")
  countries = f.readlines()
  f.close()#opens the file and puts its content in countires
  

  for i in countries:#for the regional dictionry
    s = i.split(',')
    country=str(s[1])
    year=str(s[2])
    stat=str(s[3])
    value=str(s[4])
    if country == 'Afghanistan':
      break
    else:
      if country in data_by_region:
        if '"Maternal mortality ratio (deaths per 100' == stat:
          value1=str(s[5])
          data_by_region[country][year][stat]=value1
        elif year in data_by_region[country]:
          data_by_region[country][year][stat]=value
        else:
          data_by_region[country][year]={}
      else:
        data_by_region[country]={}
        data_by_region[country][year]={}
        data_by_region[country][year][stat]=value


  pass_afghan=0
  for i in countries:#for countires
    s = i.split(',')
    country=str(s[1])
    year=str(s[2])
    stat=str(s[3])
    value=str(s[4])
    if country == 'Afghanistan':
      pass_afghan+=1
    elif pass_afghan>1:
      if country in data_by_country:
        if '"Maternal mortality ratio (deaths per 100' == stat or '"Infant mortality for both sexes (per 1'== stat:
          try:
            value1=str(s[5])
            data_by_country[country][year][stat]=value1
          except:
            continue
        elif year in data_by_country[country]:
          data_by_country[country][year][stat]=value
        else:
          data_by_country[country][year]={}
      else:
        data_by_country[country]={}
        data_by_country[country][year]={}
        data_by_country[country][year][stat]=value
    
    
 

#"Maternal mortality ratio (deaths per 100

def write_answers():#calls the fucntion that writes all the asnwers and puts them in a file
  answer_1_8()
  f= open("654424039_answers.txt","x")  
  ''' IMPORTANT Note'''#the file is on x, which means it creates the file so if it alread exists it will give an error
  for i in answers:
    an=str(i[0])+': '+str(i[1])+', '+str(i[2])+'\n'
    f.write(an)
  f.close()






def answer_1_8():#writes all the answeres in the list answers
  result = 0
  percent=0
  country= ''
  for i in data_by_region:
    for x in data_by_region[i]:
      if '"Maternal mortality ratio (deaths per 100' in (data_by_region[i][x]):
        sub_total= int(data_by_region[i]['2005']['"Maternal mortality ratio (deaths per 100'])-int(data_by_region[i]['2015']['"Maternal mortality ratio (deaths per 100'])
        percent+=abs(sub_total)
        if sub_total>result:
          result=sub_total
          country = i
  q1='1',str(country),'%0.2f'%(result)
  answers.append(q1)
 
  result=0
  country=''
  for i in data_by_region:
    for x in data_by_region[i]:
      if '"Maternal mortality ratio (deaths per 100' in (data_by_region[i][x]):
        sub_total= int(data_by_region[i]['2005']['"Maternal mortality ratio (deaths per 100'])-int(data_by_region[i]['2015']['"Maternal mortality ratio (deaths per 100'])
        percentage=sub_total/int(data_by_region[i]['2005']['"Maternal mortality ratio (deaths per 100'])
        if result<percentage:
          result=percentage
          country=i
        break
  q2='2',str(country),'%0.2f'%(result*100)
  answers.append(q2)

  result = 0
  country= ''
  for i in data_by_region:
    for x in data_by_region[i]:
      if 'Life expectancy at birth for both sexes (years)' in (data_by_region[i][x]):
        sub_total= float(data_by_region[i]['2005']['Life expectancy at birth for both sexes (years)'])-float(data_by_region[i]['2015']['Life expectancy at birth for both sexes (years)'])
        if abs(sub_total)>result:
          result=abs(sub_total)
          country = i
  q3='3',str(country),'%0.2f'%(result)
  answers.append(q3)

  result = 0
  country= ''
  for i in data_by_country:
    for x in data_by_country[i]:
      try:
        if 'Life expectancy at birth for females (years)' in (data_by_country[i][x]) or 'Lifeexpectancy at birth for females' in (data_by_country[i][x]):
          sub_total= float(data_by_country[i]['2005']['Life expectancy at birth for females (years)'])-float(data_by_country[i]['2015']['Life expectancy at birth for females (years)'])
          if abs(sub_total)>result:
            result=abs(sub_total)
            country = i
            break
      except:
        break
  q4='4',str(country),'%0.2f'%(result)
  answers.append(q4)

  result = 0
  country= ''  
  for i in data_by_country:
    for x in data_by_country[i]:
      try:
        if '"Infant mortality for both sexes (per 1' in (data_by_country[i][x]):
          sub_total= float(data_by_country[i]['2005']['"Infant mortality for both sexes (per 1'])-float(data_by_country[i]['2015']['"Infant mortality for both sexes (per 1'])
          if abs(sub_total)>result:
            result=abs(sub_total)
            country = i
            break
      except:
        break
  q5='5',str(country),'%0.2f'%(result)
  answers.append(q5) 

  minimum=0
  country= ''  
  for i in data_by_country:
    for x in data_by_country[i]:
      try:
        if '"Infant mortality for both sexes (per 1' in (data_by_country[i][x]):
          sub_total= float(data_by_country[i]['2005']['"Infant mortality for both sexes (per 1'])-float(data_by_country[i]['2015']['"Infant mortality for both sexes (per 1'])
          if abs(sub_total)<result:
              result=abs(sub_total)
              minimum=abs(sub_total)
              country = i
              break
      except:
        break
  q6='6',str(country),'%0.2f'%(minimum)
  answers.append(q6) 

  result = 0
  country=''
  for i in data_by_country:
    for x in data_by_country[i]:
      try:
        if 'Total fertility rate (children per women)' in data_by_country[i]['2015']:
          if float(data_by_country[i]['2015']['Total fertility rate (children per women)']) > result:
            result= float(data_by_country[i]['2015']['Total fertility rate (children per women)'])
            country=i
            break
      except:
        break
  q7='7',str(country),'%0.2f'%(result)
  answers.append(q7)

  country=''
  for i in data_by_country:
    for x in data_by_country[i]:
      try:
        if 'Total fertility rate (children per women)' in data_by_country[i]['2015']:
          if float(data_by_country[i]['2015']['Total fertility rate (children per women)']) < result:
            result= float(data_by_country[i]['2015']['Total fertility rate (children per women)'])
            country=i
            break
      except:
        break
  q8='8',str(country),'%0.2f'%(result)
  answers.append(q8)

def main():#loads the dictionaries and writes the asnwers in the answer file
  load_dictionaries()
  write_answers()

main()
print(answers)#printed the answeres for any instructor to see




