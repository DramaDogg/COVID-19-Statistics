from csv import DictReader as fmat
try:
    from requests import get
except ModuleNotFoundError:
    print()
    print("Your python install doesn't have 'requests' module installed. Please wait while 'requests' is being installed via pip.")
    print("NOTE: If in case the installation fails, kindly run 'pip3 install requests' in your command line")
    print()
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    print()
    print("Installation was successful!")
    print("Kindly rerun this program to load 'requests' module into the intrepreter for proper functioning.")
    noc=input("Press Enter to Exit")
    quit()
def tablemaker(x):
    '''prints a table out of a dictionary(taken as parameter), whose keys are columns and the
    values of each row are as list indices of a list, which are values of each column in the dictionary.'''
    def maxlen(d):
        k,m=[],0
        for i in d:
            mx=List(i)
            for j in d[i]:
                j=str(j)
                if len(List(j))>len(mx):
                    mx=List(j)
            k.append(len(mx)+2)
        return k
    def values(d):
        k=[]
        for i in d.values():
            k.append(i)
        return k
    def colcount(x):
        c,r=0,[]
        for i in x:
            for j in i:
                c+=1
            r.append(c)
            c=0
        r.sort()
        return r[len(r)-1]
    def List(x):
        k=[]
        for i in x:
            k.append(i)
        return k
    def keys(d):
        k=[]
        for i in d.keys():
            k.append(i)
        return k
    d=x
    lo=maxlen(x)
    ky=keys(x)
    vl=values(x)
    print("+",end="")
    for i in range(len(ky)):
        print("-"*lo[i],end="")
        print("+",end="")
    print()
    print("|",end="")
    for i in range(len(ky)):
        print(" ",end="")
        print(ky[i],end="")
        print(" "*(lo[i]-len(List(ky[i]))-1),end="")
        print("|",end="")
    print()
    print("+",end="")
    for i in range(len(ky)):
        print("-"*lo[i],end="")
        print("+",end="")
    print()
    g=colcount(vl)
    for i in range(g):
        print("|",end="")
        p=0
        for j in vl:
            print(" ",end="")
            print(j[i],end="")
            print(" "*(lo[p]-len(List(str(j[i])))-1),end="")
            print("|",end="")
            p+=1
        print()
    print("+",end="")
    for i in range(len(ky)):
        print("-"*lo[i],end="")
        print("+",end="")
    print()
def clr():
    """Clears the terminal screen wherever required(called)"""
    def plt():
        from platform import system
        from platform import release
        return system(),release()
    from os import system
    if plt()[0]=="Linux":
        system("clear")
    elif plt()[0]=="Windows":
        system("cls")
def download(url, fname):
    '''fetches and downloads required files using requests module.'''
    dobj = get(url, allow_redirects=True)
    s = dobj.content.decode("utf-8")
    with open(fname, "w") as f:
        f.write(s)
def obtain():
    '''initiates the download of the required files'''
    tot_cases = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"
    tot_deaths = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv"
    tot_recov= "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv"
    download(tot_cases, "tc.csv")
    download(tot_recov, "tr.csv")
    download(tot_deaths, "td.csv")
def dparse(date):
    """corrects date into DD-MM-YYYY"""
    k,x="",date.split("-")
    for i in x:
        if len(i)==1:
            k+="0"
        elif len(i)==2 and i==x[len(x)-1]:
            k+="20"+i
            continue
        k+=i+"-"
    return k.rstrip("-")
def fdate():
    '''fetches & returns current date in DD-MM-YYYY format.'''
    from datetime import datetime
    return str(datetime.today().strftime('%d-%m-%Y'))
def pdate(n=1,date=fdate()):
    '''Returns the date n days(taken as parameter) before given date(taken as parameter) in DD-MM-YYYY format'''
    from datetime import timedelta,datetime
    return str((datetime.strptime(date, '%d-%m-%Y') - timedelta(days=n)).strftime('%d-%m-%Y'))
def dfmat(date):
    '''converts date to and from DD-MM-YYYY and MM/DD/YY formats'''
    if "-" in date:
        t=[i.lstrip("0") for i in (date[:6]+date[8:]).split("-")]
        return t[1]+"/"+t[0]+"/"+t[2]
    elif "/" in date:
        t=[]
        for i in date.split("/"):
            if len(i)==1:
                t.append("0"+i)
            else:
                t.append(i)
        return t[1]+"-"+t[0]+"-"+"20"+t[2]
def dvalid(date):
    """checks whether a date(taken as paramater) is valid"""
    from datetime import datetime
    try :
        d,m,y=date.split("-")
        datetime(int(y),int(m),int(d))
    except:
        return False
    return True
def com(n):
    '''Adds commas to a number after every 3 digits from the right end'''
    try:
        return str(format(int(n), ",d"))
    except ValueError:
        return "-"    
def rcom(n):
    '''Removes the commas'''
    if n=="":
        return ""
    return "".join(n.split(","))
def ldate(l=0):
    """returns the last date of the archives"""
    if l==1:
        with open("tc.csv","r") as f:
            k=fmat(f).fieldnames
            return dfmat(k[len(k)-1])
    with open("tc.csv","r") as f:
        return dfmat(fmat(f).fieldnames[5])
def dcheck(date,c=None):
    '''Checks if the date is vaild'''
    if c==True:
        from datetime import datetime
        if datetime.strptime(date, '%d-%m-%Y') >= datetime.today():
            return True
        return False
    with open("tc.csv","r") as f:
        if dfmat(date) in fmat(f).fieldnames:
            return True
        return False
def locob():
    '''obtains a list of all countries from loc.csv'''
    with open("tc.csv","r") as f:
        return list(dict.fromkeys([i["Country/Region"].upper() for i in fmat(f)]))
def infob(date,fname,location="WORLD"):
    """returns the statistics of a given location and date(taken as parameter)"""
    s=0
    with open(fname,"r") as f:
        if location=="WORLD":
            return sum([int(i[date]) for i in fmat(f)])
        else:
            for i in fmat(f):
                if i["Country/Region"]=="UNITED KINGDOM":
                    s+=int(i[date])
                elif i["Country/Region"].upper()==location:
                    if i["Province/State"]=="":
                        return int(i[date])
                    else:
                        s+=int(i[date])
            return s
def tsort(d):
    '''Sorts the table in decreasing order of number of total cases by Country/Region'''
    l=[]
    for i in range(len(d["Country/Region"])):
        l.append([d["Country/Region"][i],d["Total Cases"][i],d["Active Cases"][i],d["Recoveries"][i],d["Deaths"][i],d["New Cases"][i],d["New Recoveries"][i],d["New Deaths"][i]])
    t=[]
    for i in l:
        if i[1]!="-":
            t.append(i)
    l=t
    l.sort(key = lambda x: int(rcom(x[1])))
    l.reverse()
    d={"Country/Region":[],"Total Cases":[],"Active Cases":[],"Recoveries":[],"Deaths":[],"New Cases":[],"New Recoveries":[],"New Deaths":[]}
    for i in l:
        d["Country/Region"].append(i[0])
        d["Total Cases"].append(i[1])
        d["Active Cases"].append(i[2])
        d["Recoveries"].append(i[3])
        d["Deaths"].append(i[4])
        d["New Cases"].append(i[5])
        d["New Recoveries"].append(i[6])
        d["New Deaths"].append(i[7])
    return d
def loc_stat(location="WORLD",date=fdate()):
    """displays the statstics of a given Country/Region at a given date(taken as parameters)"""
    d,f,l,m = {},1,[location],[location]
    if date==fdate() or date==pdate():
        while not dcheck(date):
            date=pdate(f)
            f+=1
    for i in ["tc.csv","tr.csv","td.csv"]:
        l.append(infob(dfmat(date),i,location))
        m.append(infob(dfmat(pdate(1,date)),i,location))
    tablemaker({"Country/Region":[l[0]],
    "Total Cases":[com(l[1])],
    "Active Cases":[com(l[1]-l[2]-l[3])],
    "Recoveries":[com(l[2])],
    "Deaths":[com(l[3])],
    "New Cases":[com(l[1]-m[1])],
    "New Recoveries":[com(l[2]-m[2])],
    "New Deaths":[com(l[3]-m[3])]})
def all_stat(date=fdate()):
    """Displays the statistics of all Countries/Region for a given date(taken as parameter)"""
    d,f = {"Country/Region":["WORLD"]+locob(),"Total Cases":[],"Active Cases":[],"Recoveries":[],"Deaths":[],"New Cases":[],"New Recoveries":[],"New Deaths":[]},1
    if date==fdate() or date==pdate():
        while not dcheck(date):
            date=pdate(f)
            f+=1
    for i in d["Country/Region"]:
        l,m=[],[]
        for j in ["tc.csv","tr.csv","td.csv"]:
            l.append(infob(dfmat(date),j,i))
            m.append(infob(dfmat(pdate(1,date)),j,i))
        d["Total Cases"].append(com(l[0]))
        d["Active Cases"].append(com(l[0]-l[1]-l[2]))
        d["Recoveries"].append(com(l[1]))
        d["Deaths"].append(com(l[2]))
        d["New Cases"].append(com(l[0]-m[0]))
        d["New Recoveries"].append(com(l[1]-m[1]))
        d["New Deaths"].append(com(l[2]-m[2]))
    tablemaker(tsort(d))
def rve():
    """Removes unwanted files before termination of the script"""
    from os import remove as rm
    try:
        rm("tr.csv")
        rm("tc.csv")
        rm("td.csv")
    except:
        pass