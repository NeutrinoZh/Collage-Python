while True:
    text = input('Введите символ(ы):').lower()
    for ch in text:
        if ch in 'aeiou':
            print(ch, '- голосна!')
        elif ch == 'y':
            print(ch, ' може бути і голосною, і приголосную')
        else:
            if ch in 'qwertyuiopasdfghjklzxcvbnm':
                print(ch, '- приголосна!')
            else:
                print(ch, '- не латинська літера!')