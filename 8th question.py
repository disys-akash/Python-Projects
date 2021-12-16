def age_fun():
    for k, v in di.items():
        if type(v) is dict:
            for t, c in v.items():
                if type(c) is dict:
                    for x,y in c.items():
                        if x=="Age" and int(y) >=25:
                            print(c)

age_fun()
