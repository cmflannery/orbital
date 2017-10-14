if ST4:
    t_st4.delay(4000)

if ST2:
    t_st2.delay(4000)

if (ST1 or (ST4 and t_st2_DN) and (not(ST1 or S1) or S2)) or first_scan:
    ST1X = True

if ST2 or (ST1 and S1 and not(S2)) and not(ST2 or t_st4_DN):
    ST2X = True

if ST3 or (ST2 and t_st4_DN) and (not(ST3) or S1 or not(S2)):
    ST3X = True

if ST4 or (ST3 and not(S1) and S2) and not(ST4 or t_st2_DN):
    ST4X = True
