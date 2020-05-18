from termcolor import colored


def evaluate_warn (headers):
    warn = 0
    try:


        if(headers['x-frame-options'] != "SAMEORIGIN"):
            warn += 1
            output = colored("WARNING\n Incorrect value for <x-frame-option> header", 'red')
            print(output)

        try:
            headers['strict-transport-security']
        except:
            warn += 1
            output = colored("WARNING\n Incorrect value for <strict-transport-security>", 'red')
            print(output)

        try:
            headers['access-control-allow-origin']
        except:
            warn +=1
            output = colored("WARNING\n Incorrect value for <access-control-allow-origin>", 'red')
            print(output)


        if (headers['content-security-policy'] == '*'):
            warn += 1
            output = colored("WARNING\n Incorrect value for <content-security-policy>", 'red')
            print(output)

        if headers['x-xss-protection']:
            if headers['x-xss-protection'].lower() not in ['1', '1; mode=block']:
                warn += 1
                output = colored("WARNING\n Incorrect value for <x-xss-protection>", 'red')
                print((output))

        if header['x-content-type-options'].lower() != 'nosniff':
                warn += 1
                output = colored("WARNING\n Incorrect value for <x-content-type-options>", 'red')
                print((output))

        if headers['x-powered-by']['server']:
            warn += 1
            output = colored("WARNING\n Server version is disclosed", 'red')
            print((output))

    except:
        if (warn > 0):
            print(colored("Execution ended with some errors", 'red'))

    finally:
        return warn
