H,M = map(int,input().split())
print(f'{H} {M-45}') if M >= 45 else print(f'{H-1} {M+15}') if H > 0 else print(f'23 {M+15}')
