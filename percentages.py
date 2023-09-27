
# TODO bereken succespercentage
def bereken_succes_percentage(api):
    missies = len(api)
    succesvolle_missies = sum(1 for missie in api if missie['launch_success'])

    if missies > 0:
        success_percentage = (succesvolle_missies / missies) * 100
    else:
        success_percentage = 0

    return success_percentage