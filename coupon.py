import random

def AddCouponNumber():
    try:
        couponSet=set()
        condition=True

        while condition==True:
            userCoupon=int(input('enter distinct numbers: '))


            couponSet.add(userCoupon)
            print('Number added: ')
            print(userCoupon)
            anotherNumber=input('to add another number enter a, or enter other key to stop: ')
            if anotherNumber == 'a' or anotherNumber == 'a':
                condition=True
            
            else:
                
                condition=False

        sortedUserCoupon=sorted(couponSet)
        firstElement=sortedUserCoupon[0]
        lastElement=sortedUserCoupon[len(sortedUserCoupon)-1]
        Coupons=set()
        condition2=True
        while condition2==True:
            randomCoupan= random.randint(firstElement,lastElement)
            print('generated coupon: ')
            print(randomCoupan)
            Coupons.add(randomCoupan)
            print('Coupon set is:')
            generateAnotherCoupon=input('enter x to generate another coupon, or press any other key to see all generated coupons: ')
            if generateAnotherCoupon=='x' or generateAnotherCoupon=='x':
                condition2=True
            else:
                condition2=False
        
        print(Coupons)
    except Exception as e:
        print("Invlid Input",e)       

AddCouponNumber()