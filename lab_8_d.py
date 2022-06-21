def TOH(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TOH(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk ", n, "from rod", from_rod, "to rod", to_rod)
    TOH(n - 1, aux_rod, to_rod, from_rod)


a = int(input("Enter number of disks: "))
TOH(a, 'A', 'C', 'B')
