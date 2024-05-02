a = int(input('Digite o numero que se deseja transformar base: '));
b = int(a);
c = int();
lista = [];
d = int(input('Digite para qual base se deseja transformar: 1 - Binaria, 2 - octal, 3 - Hexadecimal'));

if d==1:
    while b>0:
        b = a//2;
        c = a%2;
        a = b;
        lista.insert(0, c);

    print(" ".join(map(str, lista)));
elif d==2:
    while b>0:
        b = a//8;
        c = a%8;
        a = b;
        lista.insert(0, c);

    print(" ".join(map(str, lista)));
elif d==3:
    while b>0:
        b = a//16;
        c = a%16;
        if c>9:
            if c==10:
                c = 'A'
            elif c==11:
                c = 'B'
            elif c==12:
                c = 'C'
            elif c==13:
                c = 'D'
            elif c==14:
                c = 'E'
            elif c==15:
                c = 'F'
        a = b;
        lista.insert(0, c);

    print(" ".join(map(str, lista)));