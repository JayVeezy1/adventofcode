# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:35:54 2020

@author: Jakob
"""
## part 1 hatte geklappt. 2 krieg ich leider nicht hin. 
## komme wohl mit global/local variablen durcheinander. position 307 sollte noch nicht
## history drin sein. programm stoppt zu frueh. Aber guter Versuch. 
    
ACC = 0

def nop_to_jmp(history, pos, commands):
    print('nop2jmp testing position: ', pos, 'for: ', commands[pos])
    commands[pos][0] = 'jmp'
    global ACC
    
    temp = history
    temp.remove(pos)
    
    while pos <= len(commands):
        if pos in temp:
            print('no ending possible')
            return False
        else:
            if(commands[pos][0] == 'nop'):
                temp.append(pos)
                pos += 1
            elif(commands[pos][0] == 'jmp'):
                temp.append(pos)
                pos = pos + int(commands[pos][1])
            elif (commands[pos][0] == 'acc'):
                temp.append(pos)
                ACC += int(commands[pos][1])
                pos += 1
            else:
                print("command not valid.")
                return False
    commands[pos][0] = 'nop'
    return True
    
def jmp_to_nop(history, pos, commands):
    print('jmp2nop testing position: ', pos, 'for: ', commands[pos])
    commands[pos][0] = 'nop'
    global ACC
    
    temp = history
    temp.remove(pos)
    
    while pos <= len(commands):
        if pos in temp:
            print('no ending possible')
            return False
        else:
            if(commands[pos][0] == 'nop'):
                temp.append(pos)
                pos += 1
            elif(commands[pos][0] == 'jmp'):
                temp.append(pos)
                pos = pos + int(commands[pos][1])
            elif (commands[pos][0] == 'acc'):
                temp.append(pos)
                ACC += int(commands[pos][1])
                pos += 1
            else:
                print("command not valid.")
                return False
    print('position finally ran through all commands')
    commands[pos][0] = 'jmp'
    return True
    

def main():
    global ACC
    
    with open(r'C:\Users\vanek\Desktop\AdventOfCode\data\data_8.txt') as file:
        lines = file.read().splitlines()
    
    for field in range(0, len(lines)):
        lines[field] = list(lines[field].split(' '))
    commands = lines
    
    history = []
    pos = 0
    while pos < len(commands):
        if pos in history:
            print("position", pos, "was called twice. Last ACC value: ", ACC)
            break
        else:
            if(commands[pos][0] == 'nop'):
                history.append(pos)
                if nop_to_jmp(history, pos, commands):
                    print('nop at: ', pos, 'should be jmp for the program to end.')
                    print('ACC should probably be: ', ACC)
                    break
                else:
                    pos += 1
            elif(commands[pos][0] == 'jmp'):
                history.append(pos)
                if jmp_to_nop(history, pos, commands):
                    print('jmp at: ', pos, 'should be nop for the program to end.')
                    print('ACC should probably be: ', ACC)
                    break
                else:
                    pos = pos + int(commands[pos][1])
                    print('jmp to: ', pos)
            elif (commands[pos][0] == 'acc'):
                print('acc at', pos, 'is: ', ACC)
                history.append(pos)
                ACC += int(commands[pos][1])
                print('acc is:', ACC)
                pos += 1
            else:
                print("command not valid.")
   
                
main()                