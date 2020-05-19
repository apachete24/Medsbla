from termcolor import colored


def evaluate_warn (headers):
    warn: int = 0


    try:
        if (headers['x-frame-options'] != "SAMEORIGIN"):
            warn += 1
            output = colored("WARNING\n Incorrect value for <x-frame-option> header", 'red')
            print(output)
        else:
            print(colored("<x-frame-option>", 'green'))
    except:
        warn += 1
        print(colored("WARNING\n <x-frame-option> header is empty", 'red'))


    try:
        if (headers['strict-transport-security']):
            print(colored("strict-transport-security", "green"))
    except:
        warn += 1
        print(colored("WARNING\n Incorrect value for <strict-transport-security>", 'red'))


    try:
        if (headers['access-control-allow-origin']):
            print(colored("\naccess-control-allow-origin", "green"))
    except:
        warn += 1
        print(colored("WARNING\n Incorrect value for <access-control-allow-origin>", 'red'))


    try:
        if (headers['content-security-policy']):
            print(colored("content-security-policy", 'green'))
    except:
        warn += 1
        print(colored("WARNING\n Incorrect value for <content-security-policy>", 'red'))


    try:
        if (headers['x-xss-protection']):
            if headers['x-xss-protection'].lower() in ['1', '1; mode=block']:
                print(colored("x-xss-protection", 'green'))
            else:
                warn += 1
                print(colored("WARNING\n Incorrect value for <x-xss-protection>", 'red'))
    except:
        warn += 1
        print(colored("WARNING\n Incorrect value for <x-xss-protection>", 'red'))


    try:
        if headers['x-content-type-options'].lower() == 'nosniff':
            print(colored("x-content-type-options", 'green'))
        else:
            warn += 1
            print(colored("WARNING\n Incorrect value for <x-content-type-options>", 'red'))
    except:
        warn += 1
        print(colored("WARNING\n Incorrect value for <x-content-type-options>", 'red'))

    try:
        if headers['x-powered-by']['server']:
            warn += 1
            print(colored("WARNING\n Server version is disclosed", 'red'))
    except:
        print(colored("x-powered-by", 'green'))

    if (warn > 0):
        print(colored("Execution ended with some errors", 'red'))

    return warn
