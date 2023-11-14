
speed = [0.01, 0.001, 0.0001, 0]

Berkeley_gps = [15.148509979248047, 1.8096516132354736, 0.27792859077453613, 0.014688253402709961]
Berkeley_gps_left = [1507.7745871543884, 196.727153301239, 29.248130083084106, 2.824681043624878]

SQLite_gps = [17.885916233062744, 4.198291540145874, 2.7613368034362793, 2.5079851150512695]
SQLite_gps_left = [1764.6701354980469, 441.307923078537, 303.5111207962036, 279.3373873233795]

gps =1467
gps_left = 144036

def small_calc(s, t1, t2):
    r1 = t1 - gps * s
    r2 = t2 - gps_left * s
    ret = (r1 / gps + r2 / gps_left) / 2
    return ret

# gps part
for i in range(len(speed)):
    print("Speed :", speed[i])
    print("SQLite:", small_calc(speed[i], SQLite_gps[i], SQLite_gps_left[i]))
    print("Berkeley:", small_calc(speed[i], Berkeley_gps[i], Berkeley_gps_left[i]))


print("*******************")
for i in range(len(speed)):
    print("Speed :", speed[i])
    print("SQLite:", SQLite_gps_left[i] - gps_left * speed[i])
    print("Berkeley:", Berkeley_gps_left[i] - gps_left * speed[i])


