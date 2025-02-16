section .data
    align 32
    ; x_vals dd 1.0, 1.0, 1.1
    ; x_vals dd 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0
    ; x_vals dd 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0
    ; x_vals dd 3.0, 9.0, 5.0, 3.0
    x_vals dd 4.0, 7.0, 3.0, 1.0
    x_len equ ($ - x_vals) / 4
    ; y_vals dd 3.0, 3.0, 2.0
    ; y_vals dd 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0
    ; y_vals dd 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.1, 1.23123
    ; y_vals dd 8.0, 6.0, 4.0, 2.0
    y_vals dd 6.0, 5.0, 8.0, 3.0
    y_len equ ($ - y_vals) / 4
    fmt_x db "Sum X: %f", 10, 0
    fmt_y db "Sum Y: %f", 10, 0
    fmt_x2 db "Sum X^2: %f", 10, 0
    fmt_xy db "Sum X*Y: %f", 10, 0
    fmt_slope db "Slope: %f", 10, 0
    fmt_intercept db "Intercept: %f", 10, 0

section .bss
    align 32
    sum_x resq 1
    sum_y resq 1
    sum_x_times_y resq 1
    sum_x_squared resq 1
    m resq 1
    b resq 1 

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp
    and rsp, -32

init:
    vxorps ymm0, ymm0, ymm0 ; sum(x)
    vxorps ymm1, ymm1, ymm1
    vxorps ymm2, ymm2, ymm2 ; sum(y)
    vxorps ymm3, ymm3, ymm3 
    vxorps ymm4, ymm4, ymm4 ; sum(x^2)
    vxorps ymm5, ymm5, ymm5
    vxorps ymm6, ymm6, ymm6 ; sum(x*y)
    vxorps ymm7, ymm7, ymm7

    mov ecx, x_len
    mov eax, ecx        
    shr ecx, 3               
    mov rsi, x_vals
    mov rdi, y_vals
    cmp ecx, 0
    jz process_sum

ymm_load:
    vxorps ymm7, ymm7, ymm7
    vxorps ymm5, ymm5, ymm5
    vaddps ymm0, ymm0, [rsi]
    vaddps ymm2, ymm2, [rdi]
    vaddps ymm5, ymm5, [rsi]
    vaddps ymm7, ymm7, [rdi]
    vmulps ymm7, ymm7, ymm5
    vmulps ymm5, ymm5, ymm5
    vaddps ymm4, ymm4, ymm5
    vaddps ymm6, ymm6, ymm7
    add rsi, 32
    add rdi, 32
    dec ecx
    jnz ymm_load 
    jz process_sum

sisd_sum:                       
    vxorps xmm5, xmm5, xmm5
    vxorps xmm7, xmm7, xmm7
    vaddss xmm0, xmm0, [rsi]
    vaddss xmm2, xmm2, [rdi]
    movss xmm5, [rsi]
    movss xmm7, [rdi]
    mulss xmm7, xmm5 
    mulss xmm5, xmm5
    vaddss xmm4, xmm4, xmm5
    vaddss xmm6, xmm6, xmm7
    add rsi, 4
    add rdi, 4
    dec eax
    jnz sisd_sum
    jmp calculate_slope

process_sum:
    vxorps ymm1, ymm1, ymm1
    vxorps ymm3, ymm3, ymm3
    vxorps ymm5, ymm5, ymm5
    vxorps ymm7, ymm7, ymm7

    vextractf128 xmm1, ymm0, 1      ; sum(x)
    vaddps xmm0, xmm0, xmm1
    vhaddps xmm0, xmm0, xmm0
    vhaddps xmm0, xmm0, xmm0
    vmovss xmm0, xmm0, xmm0

    vextractf128 xmm3, ymm2, 1      ; sum(y)
    vaddps xmm2, xmm2, xmm3
    vhaddps xmm2, xmm2, xmm2
    vhaddps xmm2, xmm2, xmm2
    vmovss xmm2, xmm2, xmm2

    vextractf128 xmm5, ymm4, 1      ; sum (x^2)
    vaddps xmm4, xmm4, xmm5
    vhaddps xmm4, xmm4, xmm4
    vhaddps xmm4, xmm4, xmm4
    vmovss xmm4, xmm4, xmm4
    
    vextractf128 xmm7, ymm6, 1      ; sum(x*y)
    vaddps xmm6, xmm6, xmm7
    vhaddps xmm6, xmm6, xmm6
    vhaddps xmm6, xmm6, xmm6
    vmovss xmm6, xmm6, xmm6

    and eax, 7
    jnz sisd_sum
    
calculate_slope:
    vxorps xmm9, xmm9   ; n
    vxorps xmm10, xmm10 ; sum(x) * sum(y)
    vxorps xmm11, xmm11 ; (sum(x) ^ 2)
    addss xmm10, xmm0
    mulss xmm10, xmm2
    addss xmm11, xmm0
    mulss xmm11, xmm11
    mov ecx, x_len
    cvtsi2ss xmm9, ecx 
    mulss xmm6, xmm9    ; n * sum(x*y)
    mulss xmm4, xmm9    ; n * sum(x^2)
    subss xmm6, xmm10
    subss xmm4, xmm11
    divss xmm6, xmm4    ; slope

    mulss xmm0, xmm6    ; m * sum(x)
    subss xmm2, xmm0 
    divss xmm2, xmm9    ; intercept

    vmovss dword [b], xmm2
    vmovss dword [m], xmm6

print_result:
    ; vmovss dword [sum_x], xmm0 ; to debug this, comment out overwrite in calc_slope
    ; vmovss dword [sum_y], xmm2
    ; vmovss dword [sum_x_squared], xmm4
    ; vmovss dword [sum_x_times_y], xmm6

    ; vzeroupper
    ; lea rdi, [fmt_x]
    ; movss xmm0, dword [sum_x]
    ; cvtss2sd xmm0, xmm0
    ; mov rax, 1
    ; call printf

    ; lea rdi, [fmt_y]
    ; movss xmm0, dword [sum_y]
    ; cvtss2sd xmm0, xmm0
    ; mov rax, 1
    ; call printf

    ; lea rdi, [fmt_x2]
    ; movss xmm0, dword [sum_x_squared]
    ; cvtss2sd xmm0, xmm0
    ; mov rax, 1
    ; call printf
    
    ; lea rdi, [fmt_xy]
    ; movss xmm0, dword [sum_x_times_y]
    ; cvtss2sd xmm0, xmm0
    ; mov rax, 1
    ; call printf

    lea rdi, [fmt_slope]
    movss xmm0, dword [m]
    cvtss2sd xmm0, xmm0
    mov rax, 1
    call printf
    
    lea rdi, [fmt_intercept]
    movss xmm0, dword [b]
    cvtss2sd xmm0, xmm0
    mov rax, 1
    call printf

    mov rsp, rbp
    pop rbp
    xor eax, eax
    ret