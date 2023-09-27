import spacex_connectie


def geef_lanceringen_weer(api):
    missie_data = []

    for lancering in api:
        missie = {
            'mission_name': lancering['mission_name'],
            'flight_number': lancering['flight_number'],
            'launch_success': lancering['launch_success'],
            'video_link': lancering['links']['video_link'],
            'launch_site': lancering['launch_site']['site_name'],
            'launch_date': lancering['launch_date_utc']
        }
        missie_data.append(missie)

    return missie_data


def print_missie_info(missie):
    print(f"\nMissie: {missie['mission_name']}\n "
          f"Vluchtnummer: {missie['flight_number']}\n "
          f"Launch succes: {missie['launch_success']}\n "
          f"Video link: {missie['video_link']}\n"
          f"Lanceer locatie: {missie['launch_site']}\n"
          f"Lanceer datum: {missie['launch_date']}")


def zoek_specifieke_lancering(mission, api):
    x = geef_lanceringen_weer(api)
    for lancering in x:
        if lancering['mission_name'] == mission:
            return lancering


# TODO implement main menu
def geef_menu_weer():
    pass
def spacex():
    conn = spacex_connectie.spacex_connection()
    missies = geef_lanceringen_weer(conn)

    for missie in missies:
        print_missie_info(missie)

    waarde = input("Zoek missie : \n")
    gevonden_missie = zoek_specifieke_lancering(waarde, conn)

    if gevonden_missie:
        print_missie_info(gevonden_missie)
    else:
        print("Missie niet gevonden.")


if __name__ == "__main__":
    spacex()
