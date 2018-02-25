import math

def task1(text="Count stuff in this random sentence."):
    print(text)
    vowels=['a','e','i','o','u','y']
    consonants=list('bcdfghjklmnpqrstvwxyz')
    sumofv=0
    sumofc=0
    for i in vowels:
        print(str(i)+': '+str(text.count(i,0,-1)))
        sumofv=sumofv+text.count(i,0,-1)
    print('Sum of vowels:' +str(sumofv))
    for a in consonants:
        sumofc=sumofc+text.count(a,0,-1)
    print('Sum of consonants:' + str(sumofc))
    print('Number of words: ' + str(len(text.split(' '))))

def task2(minval=1,maxval=100):
    even_numbers = []
    for i in range(1,100):
        if i%2==0:
            even_numbers.append(i)
    print (even_numbers)

def task3(maxval=100):
    uneven_no=[]
    num_table=list(range(0,maxval+1))
    for i in range(2,int(math.sqrt(maxval))):
        if num_table[i] != 0:
            for j in range (i**2,maxval+1,i):
                num_table[j]=0
    for i in num_table:
        if i != 0 and i>1:
            uneven_no.append(i)
    print(uneven_no)

def task4(text='long text to revert'):
    to_revert=list(text)
    print(text)
    reverted=[]
    for i in range(len(to_revert),0,-1):
        reverted.append(to_revert[i-1])
    print(''.join(reverted))

# def task5(a=4,b=3,c=-5):


if __name__ == '__main__':
    task1()
    # task2()
    task3()
    task4()
