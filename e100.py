def run(n, m):
    t = m + 100
    n = (n * t / m if m != 0 else n) + 1
    m = t

    return n, m

if __name__ == '__main__':
    epoch, progress, total = 0, 0, 0;

    while progress <= total:
        progress, total = run(progress, total)
        epoch += 1

    print('Final Epoch: {}', epoch)
