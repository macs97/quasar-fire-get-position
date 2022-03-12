def handler(event, context):
    print("APP**************************")
    print(event)
    try:
        K = (-500, -200)  # Kenobi
        SK = (100, -100)  # Skywalker
        S = (500, 100)  # Sato

        kenobi_distance = event[0]
        skywalker_distance = event[1]
        sato_distance = event[2]

        A = K[0] ** 2 + K[1] ** 2 - kenobi_distance ** 2
        B = SK[0] ** 2 + SK[1] ** 2 - skywalker_distance ** 2
        C = S[0] ** 2 + S[1] ** 2 - sato_distance ** 2
        X32 = S[0] - SK[0]
        X13 = K[0] - S[0]
        X21 = SK[0] - K[0]

        Y32 = S[1] - SK[1]
        Y13 = K[1] - S[1]
        Y21 = SK[1] - K[1]

        x = (A * Y32 + B * Y13 + C * Y21) / (2.0 * (K[0] * Y32 + SK[0] * Y13 + S[0] * Y21))
        y = (A * X32 + B * X13 + C * X21) / (2.0 * (K[1] * X32 + SK[1] * X13 + S[1] * X21))

        print(x, y)

        return x, y
    
    except:
        return 0, 0
