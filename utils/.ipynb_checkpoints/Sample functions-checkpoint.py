# Recode function
for i in df['instant_bookable']:
    if i == 'f': 
        df['instant_bookable'] = df['instant_bookable'].replace('f', 0)
    else:
        df['instant_bookable'] = df['instant_bookable'].replace('t', 1)