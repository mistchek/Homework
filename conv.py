# Homework
# Задоянная Анастасия, Дубина Александра БИ-252
from get_rate import getrates

def main():
    rates = getrates()
    if not rates:
        print('ERROR: No rates found')
        return
    while True:
        print(f"CURRENCIES: {','.join(rates.keys())}")
        try:
            summa=float(input('Enter summa: '))
            fromcur=(input('Enter from: ').upper())
            tocur=(input('Enter to: ').upper())
            if fromcur not in rates:
                print(f'ERROR: {fromcur} not in rates')
                continue
            if tocur not in rates:
                print(f'ERROR: {tocur} not in rates')
                continue
            res=summa*rates[fromcur]/rates[tocur]
            print(f'RES: {summa}{fromcur} = {res}{tocur}')
        except ValueError:
            print(f'ERROR: try number')
            continue

        con=input('Do you want to continue (y/n)? ').lower()
        if con not in ['y','yes','да']:
            print('SEE YOU LATER!')
            break
if __name__ == '__main__':
    main()
