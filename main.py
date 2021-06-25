def list_benefits() :
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
def buildsentence(benefit) :
    return "%s is a benefits of function" %benefit
def name_the_benefits_of_function() :
    list_bene = list_benefits()
    for benefit in list_bene :
        print(buildsentence(benefit))
name_the_benefits_of_function()