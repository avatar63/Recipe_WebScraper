#This program is gonna be ambitious. But hey, when did that ever stop a cs student from pursuing a project of such calibre :)





from bs4 import BeautifulSoup as bs     #Used to scrape through html data and only pull out required data
import requests                         #Needed to pull html data from URL
import os

url = input("Enter the URL you would like to scrape from budgetbytes for comparative analysis: ")


database = requests.get(url).text

soup=bs(database,'lxml')

block = soup.find_all("article")        #Every article tag consists of the name of each recipe which is how the URLs in this website are formed as well.
temp=[]
dish_list=[]
url_list=[]
d_name=[]
for k in block:
    dishes = k.find('h2').text.split()  #this takes each recipe's name to break them down into lists of strings.\
    dish_name=(" ").join(dishes)
    d_name.append(dish_name)
    temp.append(dishes)
for j in range(len(temp)):
    name = ('-').join(temp[j])          #since each url on budget bytes is made with name of recipe seperated with - instead of spaces.
    dish_list.append(name.lower())

for m in range(len(temp)):
    url_list_temp=('https://www.budgetbytes.com/'+dish_list[m]+'/')     #this is to reconstruct the final url from the link provided above
    url_list.append(url_list_temp)

print(d_name)
ing_list=[]
temp=[]     #temporary list for ingredients to create contents of list ing_list
broken=[]   #broken links
fixed=[]    # working links
data_dict={}

#CREATING THE DICTIONARY.
dict_list=[]
for i in range(len(url_list)):
    dict_list.append(url_list[i])
    dict_list.append(d_name[i]) 
    data_dict.update({i+1:dict_list})
    dict_list=[]


count=0
for i in url_list:
    count=count+1
    print(i)                                                             #used to extract individual url links of each recipe in the provided link
    datasource=requests.get(i).text
    soup = bs(datasource,'lxml')
    try:                                                                        #The try except error handling is necessary in case of broken links in the website
        data = soup.find('div', class_="wprm-recipe-container")
        hmm=data.find('ul')
        final = hmm.find_all("span", class_="wprm-recipe-ingredient-name")
        print(final)
        for p in final:
            print(p.text)
            temp.append(p.text)
        ing_list.append(temp)
        temp=[]
        fixed.append(int(count))
        print('')
        print('')
        print('')
    except:
        print("The link "+ i +" is invalid.")
        broken.append(int(count))
        print('')
        print('')
        print('')

os.system('clear')
for i in broken:        #This is to remove all items in the dictionary with broken URLs.
    data_dict.pop(i)





print(data_dict)


key_list=[]
same_ing_list_n=[]
for d in range(len(ing_list)):                                                      
    print("Base Length: "+ str(len(ing_list[d])))
    print("RECIPE NUMBER:",fixed[d])
    print(data_dict[int(fixed[d])])
    for j in range (len(ing_list)):
        print(list(set(ing_list[d]) & set(ing_list[j])))      #These set & set tags make it easy to compare lists to check for similar items even if there is an uneven distribuition of ingredients 
        
        same_ing = (list(set(ing_list[d]) & set(ing_list[j])))
        same_ing_list_n.append(int((len(same_ing))))
    same_ing=[]
    print("List of number of similar items: "+ str(same_ing_list_n))
    sort_same=sorted(same_ing_list_n)
    print("YOU ARE LOOKING FOR THIS",sort_same)
    imp=sort_same[-2]
    print(imp)
    recipe_key = same_ing_list_n.index(imp) 
    print(recipe_key)           #This is the index we need.
    key_list.append(recipe_key)
    for k in key_list:
        print(data_dict[list(data_dict)[k]])
    key_list=[]


    print("Recommended Recipe: ", data_dict[fixed[same_ing_list_n.index(imp)]])
    print('')
    print('')
    print('')
    print('')
    same_ing_list_n=[]
    temp_sort=[]


# CHANGE LOG:
# At the moment there are a few more things that need to be brought into this project. A dictionary that allows the user to choose which recipe to select. here the key will be number of similarities and string will be the url to the dish.


#The dictionary here will be a 1 D dictionary such that a single recipe will allow the user to gain access to URL, along with a given recipe's ingredients and name.

#The keys of each dictionary must be a unique number so we can form preferences.
#Create a dictionary where a key opens up a list. The contents of the list will be recipe names along with URLs.