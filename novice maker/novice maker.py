"""
solved by :
    Raghd Bashour - antony wassof - essa khaluf
"""
from datetime import date
bill_date = date.today()

total =0 
total_weight = 0
total_item=0
total_qty=0

name = []
qty=[]
wieght=[]
cost_per_kg=[]
item_cost=[]
coustmer = input('Enter customer name: ')
# تابع لحساب تكلفة كل غرض 
def calc_item_cost(w,cpkg,qty,counter) :
    item_cost = (w[counter] * cpkg[counter])
    return item_cost
# تابع طباعة معلومات الاغراض من الفاتورة
def print_nvoice(*list):
    for ele in zip(*list):
        print(*ele,sep=' | ')


def transport(cost_per_n,total_qty):
    return cost_per_n * total_qty

def porterage(lift_cost,total_qty):
    return lift_cost * total_qty

input_flag = True
counter =0
"""
 حلقة تتم ايقافها عن طريق 
علم تتغير قيمته تبعا لمدخلات امستخدم حيث عندا يشير المستدم لانتهائه
 ممن الادخال وتطبع الفاتورة وتتغير قيمة العلم للتوقف الحلقلة
 """
while input_flag == True:
    name.append(input('item name: '))
    qty.append(int(input('item quntity: ')))
    wieght.append(float(input('input item wieght: ')))
    cost_per_kg.append(int(input('cost per kg: ')))
    item_cost.append(calc_item_cost(wieght, cost_per_kg,qty,counter))
    commission =0
    commission_per = ''
      
    total += item_cost[counter]
    total_qty += qty[counter]
    total_weight += wieght[counter]
    flag = input('is there another item (y/n): ')
    if(flag =='n' or flag=="N"):
        cost_per_n = int(input('Enter the transport cost: '))
        lift_cost=int(input('Enter the porterage cost: '))
        if(total<= 1000000):
            commission_per = '10%'
            commission = total * 0.10
        elif(total <=3000000):
            commission_per = '9%'
            commission= total * 0.09
        elif(total <=5000000):
            commission_per = '8%'
            commission = total * 0.08
        print('----------------------------------------------------')  
        print('                Farmers Bill')
        print('----------------------------------------------------')
        print('phone:0940000000 ','   homs','  Farmers Market Alaman')
        print('----------------------------------------------------')
        print('date : ',bill_date ,'              Farmers name: ',coustmer)
        print('----------------------------------------------------')
        print('item:','| qyt: ','| wieght:' ,'| cost_per_kg:','| item cost:')
        print_nvoice(name,qty,wieght,cost_per_kg,item_cost)
        print('----------------------------------------------------')
        print('total: ',total , '| total qty:', total_qty,'| total wieght:',total_weight)
        print('----------------------------------------------------')
        print('transport' ,'| total qty:' ,total_qty,'        ','| t_cost: ',cost_per_n,'| value: ',transport(cost_per_n,total_qty))
        print('porterage' ,'| total qty:',total_qty,'        ','| p_cost: ',lift_cost,'| value: ',porterage(lift_cost,total_qty))
        print('commission' ,'| c_perctenge: ',commission_per,'| value: ',commission)
        print('******************************************************')
        print('GOOD LUCK!','                  ',"NET PAYMENT =",total - (commission + transport(cost_per_n,total_qty)+porterage(lift_cost,total_qty)))
        
        input_flag = False
    else:
        counter +=1
        

    
    






