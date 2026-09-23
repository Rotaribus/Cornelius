from CORNIBU import CORNIBU_v2

dist_func = 'gausshyper'
loc = -7.67
scale = 97.67
args = [1.52,0.79,0.51,1.16]

CORNIBU_v2.CORNIBU(T = 1000, To = 0, DTc = 50, DTs = 1200, S_max = 0.6, N_max = 16, H_max = 2.5, inter_rang = 0.6, density = 9, incli_top = 15, incli_base = 45, l = 0.5, delta = 115, phyllotactic_angle = 180, phyllotactic_deviation = 25, loc = loc, scale = scale, arg = args, dist = dist_func, Caribu = True, vizu = True, mode = 'direct', norm = False, DOY = 175, latitude = 43, mode_AgriPV = True)