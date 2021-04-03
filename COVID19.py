try:
    import core
except:
    print("Error! core.py file cannot be found! Please keep covid.py & core.py at the same directory & try again!")
    noc = input("Press Enter to Exit")
    quit()
core.clr()
print("""
---------------------------------------------------------------------------------------------------------


COVID - 19   WORLDOMETER

This Python Script retrieves the latest COVID-19 statistics from the web.

Following statistics/data is retrieved for all Countries/Regions of every date since the dawn of the COVID-19 pandemic :-
--> Total Cases (Confirmed Cases)
--> Active Cases
--> Recoveries
--> Deaths
--> New Cases in the last 24 hours
--> New Recoveries in the last 24 hours
--> New Deaths in the last 24 hours

---------------------------------------------------------------------------------------------------------

Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.
Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.

HOW IT SPREADS?

The virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, sneezes, or exhales.
These droplets are too heavy to hang in the air, and quickly fall on floors or surfaces.
You can be infected by breathing in the virus if you are within close proximity of someone who has COVID-19, or by touching a
contaminated surface and then your eyes, nose or mouth.

""")
noc = input("Press Enter to Continue")
core.clr()
try:
    print("\nFetching information from the web....")
    print("""Source: https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases""")
    core.obtain()
    print()
    print("Information successfully fetched.")
    noc = input("Press Enter to Proceed")
    core.clr()
    print("Current Date:", core.fdate())
    print()
    print("Current Worldwide COVID-19 Statistics:")
    print()
    core.loc_stat()
    print()
    print()
    noc = input("Press Enter to continue")
    r = True
    while r == True:
        core.clr()
        p = "0"
        while p not in ["1", '2', '3', '4']:
            print('''
Would you like to:
[1] Display the current COVID-19 status of all countries
[2] Display the COVID-19 status of all countries on a given date
[3] Display the COVID-19 status of a country/location
[4] Exit
        ''')
            p = input("Enter the corresponding number of your choice: ")
        core.clr()
        print()
        if p == "1":
            print("Please wait, since this may take a few seconds..")
            print()
            print("Current Date:", core.fdate())
            print()
            core.all_stat(core.fdate())
            print()
        elif p == "2":
            print("Note: Entered date must be between " +core.ldate() + " & " +
                    core.fdate()+", (Both included).\n")
            dte = dtes = core.dparse(input("Enter the date in DD-MM-YYYY format: "))
            if core.dvalid(dte) and core.dcheck(dte,True):
                dte,dtes=core.ldate(l=1),core.fdate()
            while dte!=core.fdate() and(not core.dvalid(dte) or not core.dcheck(dte)):
                core.clr()
                print("Invalid Date Entered! Try Again!")
                print()
                print("Note: Entered date must be between " +core.ldate() + " & " +
                core.fdate()+", (Both included).\n")
                dte = dtes = core.dparse(input("Enter the date in DD-MM-YYYY format: "))
                if core.dvalid(dte) and core.dcheck(dte,True):
                    dte,dtes=core.ldate(l=1),core.fdate()
            core.clr()
            print("Please wait, since this may take a few seconds..")
            print()
            print("\nDate Entered:", dtes)
            print()
            core.all_stat(dte)
            print()
        elif p == "3":
            print()
            for i in ["WORLD"]+core.locob():
                print("-->", i)
            cou = str(input("\nPlease Enter a valid Country/Region from the above list: ")).upper()
            while cou not in ["WORLD"]+core.locob():
                core.clr()
                print()
                print("Invalid Country/Region Entered! Please try again.")
                for i in ["WORLD"]+core.locob():
                    print(i)
                cou = str(input("\nPlease Enter a valid Country/Region from the above list: ")).upper()
            core.clr()
            print()
            print("Country/Region Selected: ", cou)
            q = "0"
            while q not in ["1", "2"]:
                print('''
Would you like to:
[1] Display statistics for current date
[2] Display statistics for a given date\n''')
                q = input("Enter the corresponding number of your choice: ")
            core.clr()
            if q == "1":
                print("Current Date:", core.fdate())
                print()
                core.loc_stat(cou, core.fdate())
                print()
            elif q == "2":
                print("Note: Entered date must be between " +core.ldate() + " & " +
                    core.fdate()+", (Both included).\n")
                dte = dtes = core.dparse(input("Enter the date in DD-MM-YYYY format: "))
                if core.dvalid(dte) and core.dcheck(dte,True):
                    dte,dtes=core.ldate(l=1),core.fdate()
                while dte!=core.fdate() and(not core.dvalid(dte) or not core.dcheck(dte)):
                    core.clr()
                    print("Invalid Date Entered! Try Again!")
                    print()
                    print("Note: Entered date must be between " +core.ldate() + " & " +
                    core.fdate()+", (Both included).\n")
                    dte = dtes = core.dparse(input("Enter the date in DD-MM-YYYY format: "))
                    if core.dvalid(dte) and core.dcheck(dte,True):
                        dte,dtes=core.ldate(l=1),core.fdate()
                core.clr()
                print("\nDate Entered: ", dtes)
                print()
                core.loc_stat(cou, dte)
                print()
        elif p == "4":
            r = False
        noc = input("Press Enter to Continue")
except IndexError:
    print()
    print("Proper Information cannot be obtained since the info hasn't been updated yet today, Please try again later")
    print()
    noc = input("Press enter to continue")
except:
    print()
    print("An unexpected error has occured! Please rerun the program & try again!\n")
    noc = input("Press Enter to Continue")
finally:
    core.clr()
    core.rve()
    print()
    print("Stay Safe & Healthy!\n")
    noc = input("Press Enter to exit\n")
    quit()