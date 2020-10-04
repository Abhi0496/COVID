from django.shortcuts import render
from covid import Covid

covid = Covid()
data0 = covid.get_data()
print(len(data0))

confirmed = covid.get_total_confirmed_cases()
recovered = covid.get_total_recovered()
deaths = covid.get_total_deaths()
active = covid.get_total_active_cases()

data0.append(confirmed)
data0.append(recovered)
data0.append(deaths)
data0.append(active)

#data1 = {"conf":confirmed,"reco":recovered,"death":deaths,"active":active}


def showData(req):
    return render(req,"index.html",{"data":data0})

def searchCountry(req):
    entry = req.POST.get('t1')
    #print(entry)

    for x in data0:
        if x['country'] == entry:
            output = x
            return render(req, "index.html", {"out": output})
            break
    else:
        return render(req, "index.html", {"data":data0,"total":data1})

    #print(output)


