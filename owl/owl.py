from datetime import datetime


def print_owl():
    print(r"""
    
    #      _____   _   _   _____    ____ __          __ _                ___   _  _   
    #     |  __ \ | \ | | / ____|  / __ \\ \        / /| |              / _ \ | || |  
    #     | |  | ||  \| || (___   | |  | |\ \  /\  / / | |      __   __| | | || || |_ 
    #     | |  | || . ` | \___ \  | |  | | \ \/  \/ /  | |      \ \ / /| | | ||__   _|
    #     | |__| || |\  | ____) | | |__| |  \  /\  /   | |____   \ V / | |_| |_  | |  
    #     |_____/ |_| \_||_____/   \____/    \/  \/    |______|   \_/   \___/(_) |_|  
                                                                       
                                                                                  


    __________-------____                 ____-------__________
          \------____-------___--__---------__--___-------____------/
           \//////// / / / / / \   _-------_   / \ \ \ \ \ \\\\\\\\/
             \////-/-/------/_/_| /___   ___\ |_\_\------\-\-\\\\/
               --//// / /  /  //|| (O)\ /(O) ||\\  \  \ \ \\\\--
                    ---__/  // /| \_  /V\  _/ |\ \\  \__---
                         -//  / /\_ ------- _/\ \  \\-
                           \_/_/ /\---------/\ \_\_/
                               ----\   |   /----
                                    | -|- |
                                   /   |   \
                                   ---- \___|

      # by Simon169    
    """)


def starting_message():
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    print(f"""
    \t Starting DNS-Owl...
    \t Time/Date: {current_time}
    """)
    print_owl()


if __name__ == "__main__":

    starting_message()


# ASCII Art created with https://patorjk.com/software/taag
# Settings: font big, width fitted
