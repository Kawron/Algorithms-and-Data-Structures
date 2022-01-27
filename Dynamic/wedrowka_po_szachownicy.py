# Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (0, 0) na pole (n, n) korzystając jedynie z ruchów “w dół”
# oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# znajdujący trasę o minimalnym koszcie.

# f(i,j) - najmniejszy koszt wejścia na pole (i,j)
# f(i,j) = min(f(i-1,j)+A[i][j], f(i, j-1)+A[i][j])
# warunek początkowy pierwsza kolumna i pierwszy wiersz (można iśc
# tylko w dół lub tylko w prawo)

def main(A):
    n = len(A)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]
    # warunek początkowy
    F[0][0] = 0
    for i in range(1, n):
        F[0][i] = F[0][i-1] + A[0][i]
        F[i][0] = F[i-1][0] + A[i][0]
    # main loop
    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = min(F[i-1][j]+A[i][j], F[i][j-1]+A[i][j])
    for row in F:
        print(row)