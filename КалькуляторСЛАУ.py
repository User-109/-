import copy
import time
import os
os.system('cls')
def getInput():
    unknownVariablesAmount = input("Введите количество переменных: ")
    expressionAmount = input("ВВедите количество уравнений: ")
    os.system("cls")
    if (unknownVariablesAmount != expressionAmount):
        print("Ваша матрица должна быть квадратной.")
        os.system('cls')
        if(input("Вы хотите повторить попытку? y/n ") == "y"):
            os.system('cls')
            getInput()

        else:
            print("Программа закончила работу")
            time.sleep(0.5)
            exit()
    else:
        return expressionAmount

def det(matr):
    n =len(matr)
    if n == 2:
        return matr[0][0]*matr[1][1]-matr[0][1]*matr[1][0]
    else:
        s=0
        z=1
        for i in range(n):
            s = s+matr[0][i]*z*det(minor(matr,i))
            z=-z
        return s
        
def minor(matr,k):
    n=len(matr)
    r=[]
    for i in range(1,n):
        row=[]
        for j in range(n):
            if (j != k):
                row.append(matr[i][j])
        r.append(row)
    return r    
 
def Kramer(matr,b):
    
    detg=det(matr)  # рассчитали главный определитель
    
    n=len(b)        # количество переменных
    
    d=[0 for _ in range(n)] # место для определителей
    
    for i in range(n): 
        
        cmatr=copy.deepcopy(matr) # создали копию матрицы
        for k in range(n):   # замена i-го столбца на b[i]
            cmatr[k][i]=b[k]
    
        d[i]=det(cmatr)
        os.system('cls')
        displayMatrix(n)
        print(str(i/n * 100) + "%")
    os.system('cls')
    displayMatrix(n)
    print("100%")
    if abs(detg)>1.0e-15:  # решение единственно
    
       for i in range(n):
           d[i]=d[i]/detg
           
       return d
       
    else:
        
        q=0
        
        for a in d:
            if abs(a)>1.0e-15:
                q+=1
        
        if q==0:
            return ()
        else:
            return

n = int(getInput())
matrix = [[None for j in range(n)] for i in range(n)]
resultMatrix = [None for j in range(n)]

def displayMatrix(n):
    for i in range(n):
        line = str(i+1) + ": "
        for j in range(n):
            if (matrix[i][j] != None):
                if (j == 0):
                    line += str(matrix[i][j]) +  "x" + str(j+1)
                elif (j < n):
                    line += " + " + str(matrix[i][j]) + "x" + str(j + 1)
        if (resultMatrix[i] != None):
            line += " = " + str(resultMatrix[i])
        print(line)

def evaluate_expression(expression):

    try:
        result = eval(expression)
        return result
    except Exception as e:
        return 0

def insertNumberInmatrix(n, i = 0,j = 0):
    try:
        os.system('cls')
        displayMatrix(n)
        input_text = input("Введите коэфицент в ячейку " + "a" + str(i + 1) + str(j + 1) + " = ")
        num = int(evaluate_expression(input_text))
        matrix[i][j] = num

    except:
        os.system('cls')
        displayMatrix(n)
        matrix[i][j] = 0
        print('Вы ввели некорректное число. Поробуйтей снова или нажмите  "ctrl + c" ')
    if (j+1 != n):
        insertNumberInmatrix(n,i,j+1)
    else:
        os.system('cls')
        try:
            os.system('cls')
            displayMatrix(n)
            resultMatrix[i] = int(evaluate_expression((input("Введите константу для линейного уравнения под номером " + str(i+1) + " : "))))

        except:
            os.system('cls')
            displayMatrix(n)
            print('Вы ввели некорректное число. Поробуйтей снова или нажмите  "ctrl + c" ')
        if (i+1 != n):
            os.system('cls')
            insertNumberInmatrix(n,i+1,0)

os.system('cls')
insertNumberInmatrix(n,0,0)
os.system('cls')
displayMatrix(n)

while True:
    os.system("cls")
    displayMatrix(n)
    pos = ''
    pos = input('Вы хоитите внести правки в матрицу?\nЕсли ДА, то введите индекс ячейки, иначе просто нажмите ENTER. \nПример: "1,1" или "1,2"\n')
    if len(pos) > 0:
        temp = pos.replace(" ","")
        temp = temp.split(",")
        j = int(temp[1])
        i = int(temp[0])
        if (j >= 1 and j <= (n+1)  and i >= 1 and i <= n):
            while True:
                try:
                    newnum = int(input("Введите новое число для этой ячейки: "))
                    break    
                except:
                    os.system("cls")
                    displayMatrix(n)
                    print("Вы ввели некорректное число. ")
                    print("Попробуйте снова")
            i-=1
            j-=1
            if (j == (n)):
                resultMatrix[i] = newnum
                continue
            else:
                matrix[i][j] = newnum
                continue
        else:
            while True:
                os.system('cls')
                displayMatrix(n)
                pos = input("Вы указали несуществующую ячейку. Пробуйте снова.\n Пример адреса '1,2'")
                temp = pos.replace(" ","")
                temp = temp.split(",")

                if (len(temp) != 2):
                    continue
                i = int(temp[0])
                j = int(temp[1])
                if (j >= 1 and j <= (n)  and i >= 0 and i <= n):
                    i-=1
                    j-=1
                    while True:
                        try:
                            newnum = int(input("Введите новое число для этой ячейки: "))
                            break    
                        except:
                            os.system("cls")
                            displayMatrix(n)
                            print("Вы ввели некорректное число. ")
                            print("Попробуйте снова")
                    if (j == (n+2)):
                        resultMatrix[i] = newnum
                        continue
                    else:
                        matrix[i][j] = newnum
                        continue
    else:
        break
print(Kramer(matrix,resultMatrix))
