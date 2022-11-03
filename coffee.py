def buy_coffee(x,n,precio):
    gratis = x // n
    pagos = x - gratis
    # print("cafe gratis",gratis,"cafes pagos",pagos)
    return pagos* precio

assert(buy_coffee(20,8,150)==2700)
assert(buy_coffee(8,8,120)==840)