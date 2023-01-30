def fee(min, distance):
             
    def charge_fee():               # 시간에 따른 대여 요금
        result_min = min//10
        charge_min = 1200 * result_min 
        return charge_min


    def insure_fee():               # 보험료
        result_insure = min// 30
        if min % 60 >= 50:
            result_insure = result_insure+1
                 
        charge_insure = result_insure * 525
        return charge_insure

    
                
    def distance_fee():             # 거리에 따른 대여 요금
        if distance >=100:
            charge_distance = 170 * 100 + 85*(distance-100)
        else:
            charge_distance = 170 * distance
            
        return charge_distance
    
    return charge_fee() + insure_fee() + distance_fee()


print(fee(600,50))