
def start():
    playable = False
    info_menu = ["Languages", "Settings", "Play"]
    while playable != True:
        for num,info in enumerate(info_menu,start=1):
            print(f"({num}){info}")
        o_que_fazer = int(input(".:"))
        if o_que_fazer not in range(1+ len(info_menu)):
            print(f"The number '{o_que_fazer}' is out of range!")
            playable = False
        elif o_que_fazer == "1" or o_que_fazer == "languages":
            language_selected = None
            while language_selected != True:
                try:
                    languages = ["Portugues BR", "English", "Español", "Français"]
                    for num, language in enumerate(languages, start=1):
                        print(f"\n{num}. {language}")
                    qual_lingua = int(input("Type the number of your language:"))
                    if qual_lingua not in range(1 + len(languages)):
                        print("Number out of range! please try again with another number or contact (Discord:LZ#9461)")
                        language_selected = False
                    for num, language in enumerate(languages, start=1):
                        if qual_lingua == num:
                            print(f"Language selected: {language}")
                            language_selected = True 
                except ValueError:
                    print("Number not found. Please try again with another number or contact (Discord:LZ#9461)")

        elif o_que_fazer == "2" or o_que_fazer == "settings":
            print("Esta funcao ainda esta em desenvolvimento!")
        elif o_que_fazer == "3" or o_que_fazer == "Play":
            print("Starting Game")

if __name__ == "__main__":
    start()