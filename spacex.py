import percentages
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



def geef_menu_weer():
    api = spacex_connectie.spacex_connection()
    missies = geef_lanceringen_weer(api)
    x = int(input("Welkom bij SpaceX! Maak uw keuze:"
                  "\n [1] Alle lanceringen bekekijk"
                  "\n [2] Een specifieke lancering bekijken"
                  "\n [3] Succes percentage berekenen"
                  "\n [4] Applicatie afsluiten "
                  "\n Type hier: "))
    is_aan = True
    while is_aan:
        match x:
            case 1:
                for missie in missies:
                    print_missie_info(missie)
                _continue = input("Wilt u doorgaan?: j/n").lower()
                if _continue == 'j':
                    geef_menu_weer()
                else:
                    is_aan = False

            case 2:
                waarde = input("Zoek missie : \n")
                gevonden_missie = zoek_specifieke_lancering(waarde, api)

                if gevonden_missie:
                    print_missie_info(gevonden_missie)
                    _continue = input("Wilt u doorgaan?: j/n").lower()
                    if _continue == 'j':
                        geef_menu_weer()
                    elif _continue == 'n':
                        is_aan = False
                else:
                    print("Missie niet gevonden.")
                _continue = input("Wilt u opnieuw zoeken? j/n").lower()
                if _continue == 'j':
                    break
                else:
                    is_aan = False
            case 3:
                print(f"Success Percentage: {percentages.bereken_succes_percentage(api):.2f}%")
                _continue = input("Wilt u doorgaan?: j/n").lower()
                if _continue == 'j':
                    geef_menu_weer()
                elif _continue == 'n':
                    is_aan = False
            case 4:
                print("Tot ziens!")
                is_aan = False


def spacex():
    geef_menu_weer()


if __name__ == "__main__":
    spacex()
