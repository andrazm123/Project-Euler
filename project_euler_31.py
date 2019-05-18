def st_nacinov_do(n):
    i = 0
    for a1 in range(n + 1):
        if a1 * 200 < n:
            for a2 in range(n + 1):
                if a1 * 200 + a2 * 100 < n:
                    for a3 in range(n + 1):
                        if a1 * 200 + a2 * 100 + a3 * 50 < n:
                            for a4 in range(n + 1):
                                if a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 < n:
                                    for a5 in range(n + 1):
                                        if a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 + a5 * 10 < n:
                                            for a6 in range(n + 1):
                                                if a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 + a5 * 10 + a6 * 5 < n:
                                                    for a7 in range(n + 1):
                                                        if a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 + a5 * 10 + a6 * 5 + a7 * 2 < n:
                                                            for a8 in range(1, n + 1):
                                                                if a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 +\
                                                                    a5 * 10 + a6 * 5 + a7 * 2 + a8 == n:
                                                                    i = i + 1
                                                        elif a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 + a5 * 10 + a6 * 5 + a7 * 2 == n:
                                                            i = i + 1
                                                elif a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 + a5 * 10 + a6 * 5 == n:
                                                    i = i + 1
                                        elif a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 + a5 * 10 == n:
                                            i = i + 1
                                elif a1 * 200 + a2 * 100 + a3 * 50 + a4 * 20 == n:
                                    i = i + 1
                        elif a1 * 200 + a2 * 100 + a3 * 50 == n:
                            i = i + 1
                elif a1 * 200 + a2 * 100 == n:
                    i = i + 1
        elif a1 * 200 == n:
            i = i + 1
    return i

print(st_nacinov_do(200))
