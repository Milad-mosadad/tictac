#starting game coding:
table=['x',2,'x',4,5,6,'x',8,9]
table2=[' '] *9
# making table by function:
def print_table(table) :
    print(f'{table[0]} | {table[1]} | {table[2]}')
    print('---------')
    print(f'{table[3]} | {table[4]} | {table[5]}')
    print('---------')
    print(f'{table[6]} | {table[7]} | {table[8]}')
# making table marks by user:
def table_mark(table, mark, index):
    if table[index]==' ':
        table[index]=mark
    else:
        print('this cell is already filled!')
# making functio to check the winer:
def table_winner (table):
    if(
        (table[0]=='x' and table[1]=='x' and table[2]=='x')or
        (table[3]=='x' and table[4]=='x' and table[5]=='x')or
        (table[6]=='x' and table[7]=='x' and table[8]=='x')or
        (table[1]=='x' and table[4]=='x' and table[7]=='x')or
        (table[2]=='x' and table[5]=='x' and table[8]=='x')or
        (table[0]=='x' and table[4]=='x' and table[8]=='x')or
        (table[2]=='x' and table[4]=='x' and table[6]=='x')
    ):
        return 'x is winner'
    elif(
        (table[0]=='o' and table[1]=='o' and table[2]=='o')or
        (table[3]=='o' and table[4]=='o' and table[5]=='o')or
        (table[6]=='o' and table[7]=='o' and table[8]=='o')or
        (table[0]=='o' and table[3]=='o' and table[6]=='o')or
        (table[1]=='o' and table[4]=='o' and table[7]=='o')or
        (table[2]=='o' and table[5]=='o' and table[8]=='o')or
        (table[0]=='o' and table[4]=='o' and table[8]=='o')or
       (table[2]=='o' and table[4]=='o' and table[6]=='o')
    ):
        return 'o is winner'
    else:
        return 'no one is winner...!'

while True:
    
    x_index=int(input('enter the x potion between(0-8):'))
    table_mark(table2, 'x', x_index)
    print_table(table2)
    
    result_x=table_winner(table2)
    if result_x=='x is winner' :
        print(result_x)
        break

    
    o_index=int(input('enter the o potion between(0-8):'))
    table_mark(table2, 'o', o_index)
    print_table(table2)
    
    result_o=table_winner(table2)
    if result_o== 'o is winner':
        print(result_o)
        break



