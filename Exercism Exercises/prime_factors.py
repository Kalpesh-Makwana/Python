def factors(natural_number):
    pfs = []
    factor = 2
    while natural_number > 1:
        if natural_number%factor==0:
            pfs.append(factor)
            natural_number /= factor
        else:
            if factor>2:
                factor += 2
            else:
                factor += 1
    return pfs